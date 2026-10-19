"""Document ownership, cross-source decisions and unchanged review gates."""
import copy
import json
from pathlib import Path
import subprocess
import sys
import unittest
import test_review_work as fixtures
STAMP = fixtures.STAMP

SHARDS = fixtures.load('review_shards_test', 'review-shards.py')

class ReviewShardTests(unittest.TestCase):
    def setUp(self):
        self.fixture=fixtures.ReviewWorkTests();self.fixture.setUp();self.addCleanup(self.fixture.doCleanups)
        self.work=self.fixture.work;self.facts=self.fixture.facts
        self.plan=SHARDS.split(self.work,self.facts)
    def parts(self, plan=None, work=None):
        plan=plan or self.plan;work=work or self.work
        batches={b['source_id']:b['review_fact_ids'] for b in work['source_batches']}
        return [dict(schema_version=1,format='review-source-part-v1',
            **{k:work[k] for k in ('run_id','company','as_of','phase')},job_id=job['id'],
            review_work_fingerprint=work['fingerprint'],plan_fingerprint=plan['fingerprint'],
            documents=[dict(source_id=sid,original_read=True,note='SIMULATED original reading',
                findings=[dict(claim_id=cid,depth='A',status='geprüft',note='SIMULATED source-specific finding') for cid in batches[sid]]) for sid in job['source_ids']]) for job in plan['jobs']]
    def lead(self, plan=None, work=None, parts=None):
        plan=plan or self.plan;work=work or self.work
        report=SHARDS.collect(plan,work,self.facts,self.parts(plan,work) if parts is None else parts)
        draft=self.fixture.draft(work=work);draft.pop('source_checks')
        draft.update(plan_fingerprint=plan['fingerprint'],source_collection_fingerprint=report['fingerprint'])
        return draft
    def test_document_owner_unique_and_same_model(self):
        self.assertEqual(len(self.plan['jobs']),2)
        owned=[sid for j in self.plan['jobs'] for sid in j['source_ids']]
        self.assertEqual(len(owned),len(set(owned)));self.assertEqual(len(owned),2)
        self.assertTrue(all(j['model']=='inherit' for j in self.plan['jobs']))
        self.assertEqual(self.plan,SHARDS.split(self.work,self.facts))
        for n in (0,4,True):
            with self.assertRaises(ValueError):SHARDS.split(self.work,self.facts,n)
    def test_job_shows_only_assigned_facts_once(self):
        for job in self.plan['jobs']:
            view=SHARDS.show(self.plan,self.work,self.facts,job['id'])
            expected={c for b in self.work['source_batches'] if b['source_id'] in job['source_ids'] for c in b['review_fact_ids']}
            self.assertEqual({c['id'] for c in view['facts']},expected)
            self.assertEqual(len(view['facts']),len(expected))
            self.assertNotIn('module_views',view)
    def test_success_preserves_explicit_lead_and_existing_stamp(self):
        parts=self.parts();lead=self.lead(parts=parts)
        merged=SHARDS.merge(self.plan,self.work,self.facts,parts,lead,self.fixture.report)
        result=STAMP.stamp(merged,self.fixture.report,self.work)
        self.assertEqual(result['status'],'freigegeben')
        self.assertEqual(len(result['source_checks']),2)
        self.assertEqual({r['id'] for r in result['claims']},{'P1','P2','P3'})
    def test_missing_duplicate_or_wrong_owned_results_fail(self):
        mutations=[lambda p:p.pop(),lambda p:p.append(copy.deepcopy(p[0])),
            lambda p:p[0]['documents'].clear(),lambda p:p[0]['documents'][0]['findings'].pop(),
            lambda p:p[0]['documents'][0].update(source_id='unknown'),
            lambda p:p[0].update(plan_fingerprint='stale')]
        for mutation in mutations:
            parts=self.parts();mutation(parts)
            with self.assertRaises(ValueError):SHARDS.collect(self.plan,self.work,self.facts,parts)
    def test_changed_plan_or_packet_rejected(self):
        plan=copy.deepcopy(self.plan);plan['jobs'][0]['source_ids'].append('other')
        with self.assertRaises(ValueError):SHARDS.collect(plan,self.work,self.facts,self.parts())
        facts=copy.deepcopy(self.facts);facts['claims'][0]['statement']='changed'
        with self.assertRaises(ValueError):SHARDS.split(self.work,facts)
    def test_each_source_of_multisource_claim_must_support_it(self):
        parts=self.parts()
        finding=next(f for p in parts for d in p['documents'] for f in d['findings'] if f['claim_id']=='P2')
        finding.update(status='Korrektur',reason='Contradiction',action='Correct claim',owner='portfolio')
        lead=self.lead(parts=parts)
        with self.assertRaisesRegex(ValueError,'unresolved source'):SHARDS.merge(self.plan,self.work,self.facts,parts,lead,self.fixture.report)
    def test_no_upgrade_no_unread_original_and_no_stale_lead(self):
        parts=self.parts();parts[0]['documents'][0]['original_read']=False
        with self.assertRaisesRegex(ValueError,'original reading'):SHARDS.collect(self.plan,self.work,self.facts,parts)
        parts=self.parts();parts[0]['documents'][0]['findings'][0]['depth']='B'
        with self.assertRaisesRegex(ValueError,'insufficient depth'):SHARDS.merge(self.plan,self.work,self.facts,parts,self.lead(parts=parts),self.fixture.report)
        parts=self.parts();lead=self.lead();lead['source_collection_fingerprint']='old'
        with self.assertRaisesRegex(ValueError,'acknowledge'):SHARDS.merge(self.plan,self.work,self.facts,parts,lead,self.fixture.report)
    def test_global_scope_and_required_claim_gates_remain(self):
        lead=self.lead();lead['scope_and_mappings_checked']=False
        with self.assertRaisesRegex(ValueError,'scope/module mapping'):SHARDS.merge(self.plan,self.work,self.facts,self.parts(),lead,self.fixture.report)
        lead=self.lead();lead['review_groups'][0]['claim_ids']=['P1']
        with self.assertRaisesRegex(ValueError,'required full check'):SHARDS.merge(self.plan,self.work,self.facts,self.parts(),lead,self.fixture.report)
    def test_final_reuses_facts_without_starting_document_workers(self):
        basis,pc,po,sc,so,validation,rows,work=self.fixture.final()
        plan=SHARDS.split(work,self.facts)
        self.assertEqual(plan['jobs'],[])
        lead=self.lead(plan,work,[]);lead['reuse_fact_ids']=sorted(work['fact_reuse_candidates'])
        merged=SHARDS.merge(plan,work,self.facts,[],lead,validation)
        self.assertEqual(STAMP.stamp(merged,validation,work)['status'],'freigegeben')
    def test_cli_split_show_collect_merge_and_stamp(self):
        root=self.fixture.root
        files={'work':self.work,'facts':self.facts,'plan':self.plan,'validation':self.fixture.report,'lead':self.lead()}
        for name,value in files.items():(root/(name+'.json')).write_text(json.dumps(value))
        part_paths=[]
        for i,part in enumerate(self.parts()):
            path=root/('part'+str(i)+'.json');path.write_text(json.dumps(part));part_paths.append(str(path))
        common=['--work',str(root/'work.json'),'--facts',str(root/'facts.json')]
        script=str(Path(SHARDS.__file__))
        commands=[['split',*common,'--out',str(root/'fresh-plan.json')],
            ['show',*common,'--plan',str(root/'plan.json'),'--job',self.plan['jobs'][0]['id']],
            ['collect',*common,'--plan',str(root/'plan.json'),'--parts',*part_paths,'--out',str(root/'collection.json')],
            ['merge',*common,'--plan',str(root/'plan.json'),'--parts',*part_paths,'--lead',str(root/'lead.json'),'--validation',str(root/'validation.json'),'--out',str(root/'merged.json')]]
        for command in commands:
            result=subprocess.run([sys.executable,script,*command],capture_output=True,text=True)
            self.assertEqual(result.returncode,0,result.stdout+result.stderr)
        self.assertEqual(STAMP.stamp(json.loads((root/'merged.json').read_text()),self.fixture.report,self.work)['status'],'freigegeben')

    def test_three_documents_create_three_disjoint_jobs(self):
        third={**self.fixture.sources[0], 'id':fixtures.FACTS.source_id('https://example.org/third'), 'url':'https://example.org/third'}
        self.fixture.module['source_proposals'].append(third)
        self.fixture.module['claims'][2]['source_ids']=[third['id']]
        self.fixture.store(third,'Third synthetic original')
        validation,facts=fixtures.FACTS.build(self.fixture.manifest,[self.fixture.module])
        self.assertEqual(validation['errors'],[])
        work=fixtures.WORK.prepare(self.fixture.manifest,facts,validation,cache=self.fixture.cache)
        plan=SHARDS.split(work,facts)
        self.assertEqual(len(plan['jobs']),3)
        self.assertTrue(all(len(j['source_ids'])==1 for j in plan['jobs']))

    def test_changed_original_invalidates_plan_and_worker_results(self):
        parts=self.parts()
        self.fixture.store(self.fixture.sources[0],'Changed original text')
        with self.assertRaisesRegex(ValueError,'source snapshot changed'):
            SHARDS.collect(self.plan,self.work,self.facts,parts)

    def test_final_changed_sources_are_checked_by_jobs(self):
        basis,pc,po,sc,so,validation,rows,first=self.fixture.final()
        draft=self.fixture.draft(first);draft['reuse_fact_ids']=['P1','P2']
        previous=STAMP.stamp(draft,validation,first)
        self.fixture.store(self.fixture.sources[0],'Changed original for final phase')
        work=fixtures.WORK.prepare(self.fixture.manifest,self.facts,validation,rows,self.fixture.cache,basis,self.work,first,previous)
        plan=SHARDS.split(work,self.facts);parts=self.parts(plan,work)
        lead=self.lead(plan,work,parts)
        lead['fact_groups']=[dict(claim_ids=work['facts_to_verify'],depth='A',status='geprüft',note='SIMULATED lead cross-source review')]
        lead['reuse_fact_ids']=sorted(work['fact_reuse_candidates'])
        merged=SHARDS.merge(plan,work,self.facts,parts,lead,validation)
        result=STAMP.stamp(merged,validation,work)
        self.assertEqual(result['status'],'freigegeben')
        self.assertEqual(set(result['fact_review']),{'P1','P2'})

if __name__=='__main__':unittest.main()
