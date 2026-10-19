/* BED-CAR — nawigacja mobilna, cień nagłówka, reveal, formularz demo */
(function(){
  var d=document, b=d.body, hdr=d.getElementById('hdr'), burger=d.getElementById('burger');
  if(burger){burger.addEventListener('click',function(){var o=b.classList.toggle('nav-open');burger.setAttribute('aria-expanded',o?'true':'false');});
    d.querySelectorAll('#nav a').forEach(function(a){a.addEventListener('click',function(){b.classList.remove('nav-open');burger.setAttribute('aria-expanded','false');});});}
  function sc(){if(hdr)hdr.classList.toggle('scrolled',window.scrollY>8);}
  sc();window.addEventListener('scroll',sc,{passive:true});
  var rv=d.querySelectorAll('.rv');
  if('IntersectionObserver' in window){var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target);}});},{rootMargin:'0px 0px -8% 0px'});rv.forEach(function(el){io.observe(el);});}
  else rv.forEach(function(el){el.classList.add('in');});
  d.querySelectorAll('.js-form').forEach(function(f){f.addEventListener('submit',function(e){e.preventDefault();
    var bad=null;f.querySelectorAll('[required]').forEach(function(i){var ok=i.value.trim().length>1;i.style.borderColor=ok?'':'#d64545';if(!ok&&!bad)bad=i;});
    if(bad){bad.focus();return;} f.classList.add('sent');});});
})();

/* === licznik otwarć demo (buy-signal) + geo === */
(function(){try{if(String(location.protocol).indexOf('http')!==0)return;try{if(/[?&#]team=1/.test(location.search+location.hash)){localStorage.setItem('nb_team','1');}}catch(e){}try{if(localStorage.getItem('nb_team')==='1')return;}catch(e){}if((document.referrer||'').indexOf('crm-newbeginning')>-1)return;try{if(navigator.webdriver)return;}catch(e){}try{if(/^https?:\/\/(kris20032|impulseo-pl)\.github\.io\/?$/i.test(document.referrer||''))return;}catch(e){}if(sessionStorage.getItem('_dv'))return;sessionStorage.setItem('_dv','1');var seg=(location.pathname.split('/').filter(Boolean)[0])||'';var base=location.origin+(seg?('/'+seg):'');var ua='';try{ua=(navigator.userAgent||'').slice(0,300);}catch(e){}var EP='https://zngfubfinbojfgaxdrbf.supabase.co/rest/v1/demo_views';var KEY='sb_publishable_MWwoyGlSCWnJ4awtOPF0ow_ZVS0Y8qK';function send(g){try{fetch(EP,{method:'POST',keepalive:true,headers:{'Content-Type':'application/json','apikey':KEY,'Authorization':'Bearer '+KEY,'Prefer':'return=minimal'},body:JSON.stringify({demo_url:base,page:location.pathname,referrer:(document.referrer||null),user_agent:(ua||null),ip:(g&&g.ip)||null,country:(g&&g.cc)||null,city:(g&&g.city)||null})}).catch(function(){});}catch(e){}}var done=false;function once(g){if(done)return;done=true;send(g);}try{var t=setTimeout(function(){once(null);},1500);fetch('https://ipwho.is/?fields=ip,success,country_code,city',{cache:'no-store'}).then(function(r){return r.json();}).then(function(d){clearTimeout(t);once(d&&d.success!==false?{ip:d.ip,cc:d.country_code,city:d.city}:null);}).catch(function(){clearTimeout(t);once(null);});}catch(e){once(null);}}catch(e){}})();
