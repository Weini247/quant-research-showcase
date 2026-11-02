/* Present stored aggregates only; no inference, resampling or model selection. */
(()=>{'use strict';const d=window.FX_PUBLIC;if(!d||!document.querySelector('#performance-table'))return;
const names={zero:'No change',ar1:'AR(1)',ar20_ridge:'AR(20) Ridge',chronos_grouped:'Chronos-2 grouped',chronos_ungrouped:'Chronos-2 ungrouped'};
const colors=['#e5aa64','#83b9ea','#9bdcca','#cfb3e8'];const signed=x=>(x>=0?'+':'')+x.toFixed(6);
function render(h){const rows=d.performance.filter(r=>r.horizon===h);const body=document.querySelector('#performance-table tbody');body.replaceChildren();
for(const r of rows){const p=d.paired.find(x=>x.horizon===h&&x.contrast===r.variant+'-minus-zero');const ci=p?.intervals['60'];const tr=document.createElement('tr');for(const [i,value]of [names[r.variant],r.scaled_mae.toFixed(6),p?signed(p.mean):'Reference',p?'['+signed(ci.low)+', '+signed(ci.high)+']':'—',String(r.n)].entries()){const td=document.createElement('td');td.textContent=value;if(i)td.className='number';tr.append(td);}body.append(tr);}
document.querySelectorAll('[data-horizon]').forEach(b=>b.setAttribute('aria-pressed',String(Number(b.dataset.horizon)===h)));
const label='H'+h+' / '+(h===1?'primary':'secondary');document.querySelector('#horizon-status').textContent=label+' — 98 origins × 8 currencies; stored 95% block intervals.';document.querySelector('#performance-table caption').textContent=label+' performance and paired differences. Negative differences indicate lower loss.';
const svg=document.querySelector('#effect-chart');svg.replaceChildren();const ns='http://www.w3.org/2000/svg';const add=(tag,attrs,text)=>{const e=document.createElementNS(ns,tag);for(const[k,v]of Object.entries(attrs))e.setAttribute(k,v);if(text)e.textContent=text;svg.append(e);return e;};const x=v=>260+(v+.0045)/.009*550;
add('title',{},label+': paired scaled MAE differences with stored intervals');add('line',{x1:x(0),x2:x(0),y1:15,y2:215,stroke:'#e4efea','stroke-dasharray':'4 4'});
for(const[k,v]of d.study.variants.slice(1).entries()){const p=d.paired.find(r=>r.horizon===h&&r.contrast===v+'-minus-zero');const y=45+k*48;add('text',{x:8,y:y+5,fill:'#c6d7ce','font-size':15},names[v]);add('line',{x1:x(p.intervals['60'].low),x2:x(p.intervals['60'].high),y1:y,y2:y,stroke:colors[k],'stroke-width':3});add('circle',{cx:x(p.mean),cy:y,r:5,fill:colors[k]});}
for(const t of [-.004,-.002,0,.002,.004])add('text',{x:x(t),y:238,fill:'#b0c1b9','font-size':13,'text-anchor':'middle'},t.toFixed(3));add('text',{x:535,y:264,fill:'#b0c1b9','font-size':13,'text-anchor':'middle'},'Model minus no change / negative = lower loss');}
document.querySelectorAll('[data-horizon]').forEach(b=>b.addEventListener('click',()=>render(Number(b.dataset.horizon))));render(1);
})();
