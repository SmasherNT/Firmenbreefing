(()=>{
 const root=document.getElementById('briefing-regional-presence');if(!root)return;
 const links=[...root.querySelectorAll('.rp-row')],profiles=[...root.querySelectorAll('.rp-profile')];
 root.addEventListener('click',event=>{
  const link=event.target.closest('.rp-row');if(!link||!root.contains(link))return;
  const target=document.getElementById(link.getAttribute('href').slice(1));if(!target)return;
  event.preventDefault();event.stopPropagation();profiles.forEach(profile=>profile.open=profile===target);
  links.forEach(row=>{if(row===link)row.setAttribute('aria-current','true');else row.removeAttribute('aria-current');});
  target.scrollIntoView({block:'start',behavior:'smooth'});
 });
})();
