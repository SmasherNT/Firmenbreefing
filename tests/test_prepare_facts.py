import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("facts", ROOT / "scripts/prepare-facts.py")
FACTS = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(FACTS)

class FactsTests(unittest.TestCase):
    def setUp(self):
        self.source = {"id": FACTS.source_id("https://example.org/product"),
                       "url": "https://example.org/product", "name": "Example",
                       "title": "Product sheet", "published_date": None,
                       "accessed_date": "2026-10-09", "source_kind": "Herstellerangabe"}
        self.manifest = {"schema_version": 1, "mode": "facts-v2", "run_id": "fixture",
                         "company": "Example", "as_of": "2026-10-09",
                         "scope": "Inspection systems", "selected_roles": ["portfolio"]}
        self.claim = {"id": "P001", "statement": "Manufacturer reports a test",
                      "kind": "Herstellerangabe", "source_ids": [self.source["id"]],
                      "evidence": "Paraphrase: laboratory test reported",
                      "location": "Testing section", "uncertainty": "Manufacturer report"}
        self.module = {k: v for k, v in self.manifest.items() if k != "selected_roles"}
        self.module.update(role="portfolio", status="vollständig", claims=[self.claim],
                           source_proposals=[self.source], gaps=[], coverage=[])
        self.plan = {"run_id": "fixture", "company": "Example", "as_of": "2026-10-09",
                     "comparison_unit": "Inspection systems", "purpose": "Compare accuracy",
                     "peer_groups": ["Direct peers"], "version": 1,
                     "criteria": [{"id": "accuracy", "label": "Measurement accuracy",
                                   "question": "What accuracy was reported?",
                                   "evidence_required": "Result and test conditions",
                                   "display_type": "Kennzahl", "unit": "mm",
                                   "conditions": "same distance", "applicability": "Sensors",
                                   "rationale": "User asks for inspection capability"}]}

    def result(self, module=None, manifest=None, plan=None):
        return FACTS.build(manifest or self.manifest, [module or self.module], plan)[0]

    def market(self):
        manifest = {**self.manifest, "selected_roles": ["market"],
                    "comparison_plan_path": "comparison-plan.json"}
        module = copy.deepcopy(self.module)
        module.update(role="market", comparison_plan_version=1,
                      peers=[{"id": "peer", "label": "Example"}],
                      observations=[{"peer_id": "peer", "criterion_id": "accuracy",
                                     "claim_ids": ["M001"], "factual_description": "Test reported"}])
        module["claims"][0]["id"] = "M001"
        return manifest, module

    def test_valid_packet_and_fingerprint_changes(self):
        result = self.result()
        self.assertEqual(result["errors"], [])
        self.assertEqual(result["run_id"], self.manifest["run_id"])
        self.assertEqual(result["phase"], "basis")
        changed = copy.deepcopy(self.module)
        changed["claims"][0]["statement"] += " changed"
        self.assertNotEqual(result["fingerprints"], self.result(changed)["fingerprints"])

    def test_source_identity_preserves_queries(self):
        self.assertEqual(FACTS.source_id("https://example.org/product#page=4"), self.source["id"])
        self.assertNotEqual(FACTS.source_id("https://example.org/product?lang=de"), self.source["id"])

    def test_foreign_company_or_run_rejected(self):
        for key in ("company", "run_id", "as_of"):
            changed = copy.deepcopy(self.module)
            changed[key] = "other"
            self.assertTrue(self.result(changed)["errors"])

    def test_missing_and_duplicate_modules_rejected(self):
        self.assertTrue(FACTS.build(self.manifest, [])[0]["errors"])
        self.assertTrue(FACTS.build(self.manifest, [self.module, self.module])[0]["errors"])

    def test_interpretation_and_user_input_rejected(self):
        for field in ("score", "interpretation"):
            changed = copy.deepcopy(self.module)
            changed["claims"][0][field] = 5
            self.assertTrue(self.result(changed)["errors"])
        for kind in ("Interpretation", "Nutzerangabe"):
            changed = copy.deepcopy(self.module)
            changed["claims"][0]["kind"] = kind
            self.assertTrue(self.result(changed)["errors"])

    def test_unknown_references_and_invalid_dates_rejected(self):
        for mutate in (
            lambda m: m["claims"][0].update(source_ids=["missing"]),
            lambda m: m["claims"][0].update(depends_on=["missing"]),
            lambda m: m["source_proposals"][0].update(published_date="2026-02-30"),
            lambda m: m.update(reuse_claim_ids=["missing"]),
        ):
            changed = copy.deepcopy(self.module)
            mutate(changed)
            self.assertTrue(self.result(changed)["errors"])

    def test_two_sources_need_mapped_evidence(self):
        changed = copy.deepcopy(self.module)
        other = {**self.source, "url": "https://example.org/second",
                 "id": FACTS.source_id("https://example.org/second")}
        changed["source_proposals"].append(other)
        changed["claims"][0]["source_ids"].append(other["id"])
        self.assertTrue(self.result(changed)["errors"])
        changed["claims"][0]["evidence_items"] = [
            {"source_id": s["id"], "text": "Test report", "mode": "Paraphrase",
             "location": "Testing section"} for s in changed["source_proposals"]]
        self.assertEqual(self.result(changed)["errors"], [])

    def test_dynamic_criteria_without_autonomy_defaults(self):
        manifest, module = self.market()
        self.assertEqual(self.result(module, manifest, self.plan)["errors"], [])
        module["observations"][0]["criterion_id"] = "autonomy"
        self.assertTrue(self.result(module, manifest, self.plan)["errors"])

    def test_missing_plan_or_version_or_metric_conditions_rejected(self):
        manifest, module = self.market()
        self.assertTrue(self.result(module, manifest)["errors"])
        module["comparison_plan_version"] = 2
        self.assertTrue(self.result(module, manifest, self.plan)["errors"])
        plan = copy.deepcopy(self.plan)
        del plan["criteria"][0]["conditions"]
        self.assertTrue(FACTS.validate_plan(plan, manifest))

    def test_market_observations_must_not_score(self):
        manifest, module = self.market()
        module["observations"][0]["score"] = 4
        self.assertTrue(self.result(module, manifest, self.plan)["errors"])

    def test_cluster_identity_and_interpretation(self):
        manifest = {**self.manifest, "selected_roles": ["cluster"]}
        module = copy.deepcopy(self.module)
        module["role"] = "cluster"
        module["claims"][0]["id"] = "C001"
        module["network"] = {"company": "Example", "as_of": "2026-10-09", "target_id": "n1",
                             "nodes": [{"id": "n1", "kind": "target"}, {"id": "n2", "kind": "partner"}],
                             "sources": [copy.deepcopy(self.source)], "products": [],
                             "edges": [{"id": "e1", "from": "n1", "to": "n2",
                                        "source_ids": [self.source["id"]], "claim_ids": ["C001"], "product_ids": []}]}
        self.assertEqual(self.result(module, manifest)["errors"], [])
        self.assertEqual(self.result(module, manifest)["required_full_review_ids"], ["C001"])
        module["network"]["edges"][0]["interpretation"] = "Strategic advantage"
        self.assertTrue(self.result(module, manifest)["errors"])

    def test_cli_writes_only_valid_packets(self):
        with tempfile.TemporaryDirectory() as path:
            root = Path(path)
            for name, data in (("manifest.json", self.manifest), ("module.json", self.module)):
                (root / name).write_text(json.dumps(data), encoding="utf-8")
            args = [sys.executable, str(ROOT / "scripts/prepare-facts.py"),
                    "--manifest", str(root / "manifest.json"), "--modules",
                    str(root / "module.json"), "--out", str(root / "work")]
            result = subprocess.run(args, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stdout)
            self.assertTrue((root / "work/sources.json").exists())
            bad = copy.deepcopy(self.module)
            bad["claims"][0]["score"] = 5
            (root / "module.json").write_text(json.dumps(bad), encoding="utf-8")
            args[-1] = str(root / "invalid-work")
            result = subprocess.run(args, capture_output=True, text=True)
            self.assertEqual(result.returncode, 1)
            self.assertFalse((root / "invalid-work").exists())

if __name__ == "__main__":
    unittest.main()
