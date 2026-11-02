"""Render six figures solely from the supplied public aggregates; never run models.

Python 3.12, matplotlib 3.11.2 and Pillow 12.3.0 were used for the reviewed bytes.
Repeatability means identical bytes in the same renderer/font environment.
"""
from pathlib import Path
import argparse,json,math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import TwoSlopeNorm,LinearSegmentedColormap
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch
ROOT=Path(__file__).resolve().parent
COLORS=['#e5aa64','#83b9ea','#9bdcca','#cfb3e8']
NAMES={'zero':'No change','ar1':'AR(1)','ar20_ridge':'AR(20) Ridge','chronos_grouped':'Chronos-2 grouped','chronos_ungrouped':'Chronos-2 ungrouped','train_quantiles':'Static training quantiles'}
def theme():
 plt.rcParams.update({'font.family':['DejaVu Sans','Arial','sans-serif'],'font.size':10,'figure.facecolor':'#0b171c','axes.facecolor':'#0b171c','axes.edgecolor':'#52636b','axes.labelcolor':'#e4efea','text.color':'#e4efea','xtick.color':'#c1cec9','ytick.color':'#c1cec9','grid.color':'#31434a','grid.alpha':.6,'axes.spines.top':False,'axes.spines.right':False,'svg.fonttype':'none','svg.hashsalt':'quant-fx-development-public-v2','savefig.facecolor':'#0b171c','axes.titleweight':'bold'})
def save(fig,out,name,title,note):
 fig.suptitle(title,x=.055,ha='left',fontsize=18,fontweight='bold',y=.985)
 fig.text(.055,.025,note,fontsize=9,color='#b0c1b9',va='bottom')
 fig.savefig(out/(name+'.svg'),metadata={'Date':None,'Creator':'Quant Research Lab public aggregate renderer'},bbox_inches=None)
 fig.savefig(out/(name+'.png'),dpi=160,metadata={'Software':'Quant Research Lab public aggregate renderer'},bbox_inches=None)
 plt.close(fig)
def render(data,out):
 theme();out.mkdir(parents=True,exist_ok=True);models=data['study']['variants'][1:]
 pair={(r['contrast'],r['horizon']):r for r in data['paired']}
 fig,axes=plt.subplots(1,2,figsize=(13,4.7));fig.subplots_adjust(left=.20,right=.96,bottom=.23,top=.77,wspace=.35)
 for ax,h in zip(axes,(1,20)):
  for k,v in enumerate(models):
   r=pair[(v+'-minus-zero',h)];lo,hi=[r['intervals']['60'][x] for x in ('low','high')]
   ax.plot([lo,hi],[k,k],color=COLORS[k],lw=2);ax.scatter(r['mean'],k,s=55,color=COLORS[k],zorder=3)
  ax.axvline(0,color='white',lw=1,ls='--');ax.set_yticks(range(4),[NAMES[v] for v in models]);ax.invert_yaxis();ax.set_xlim(-.004,.0045);ax.set_title(f'H{h}'+(' / primary' if h==1 else ' / secondary'));ax.set_xlabel('Paired scaled MAE difference');ax.grid(axis='x')
  if h==20:ax.set_yticklabels([])
  ax.set_xticks([-.004,-.002,0,.002,.004])
 save(fig,out,'F1-model-performance','01 / Point forecasts: no clear improvement','Model minus no change; negative is lower loss. Stored 95% percentile intervals, 60-day blocks; 98 origins x 8 currencies.\nDevelopment evidence only. Intervals do not establish equivalence or independent validation.')
 assets=data['study']['assets'];quarters=sorted({r['quarter'] for r in data['quarterly_landscape']});lookup={(r['variant'],r['horizon'],r['asset'],r['quarter']):r for r in data['quarterly_landscape']}
 limit=max(abs(r['mean']) for r in lookup.values());limit=math.ceil(limit*100)/100
 cmap=LinearSegmentedColormap.from_list('loss_difference',['#428fa4','#eef1e7','#a25424'])
 fig,axes=plt.subplots(2,4,figsize=(17,9));fig.subplots_adjust(left=.055,right=.91,bottom=.18,top=.84,wspace=.34,hspace=.60)
 for row,h in enumerate((1,20)):
  for col,v in enumerate(models):
   ax=axes[row,col];values=[[lookup[v,h,a,q]['mean'] for q in quarters] for a in assets];im=ax.imshow(values,cmap=cmap,norm=TwoSlopeNorm(vmin=-limit,vcenter=0,vmax=limit),aspect='auto')
   labels=[q.replace('2018 ','18 ').replace('2019 ','19 ')+'\nn='+str(lookup[v,h,assets[0],q]['n']) for q in quarters]
   ax.set_xticks(range(8),labels,rotation=60,ha='right',fontsize=8);ax.set_yticks(range(8),assets,fontsize=9);ax.set_title(NAMES[v]+f' / H{h}',fontsize=11)
 cax=fig.add_axes([.935,.28,.012,.43]);fig.colorbar(im,cax=cax,label='Mean paired scaled absolute-loss difference')
 save(fig,out,'F2-failure-landscape','02 / Failure landscape across the complete development calendar','All eight origin-calendar quarters, all currencies and all four nonzero models; n denotes origins per currency/cell.\nShared symmetric colour scale; blue = lower loss than no change, brown = higher. Descriptive aggregation, no event selection.')
 prob={(r['variant'],r['horizon']):r for r in data['calibration']};vlist=['train_quantiles','chronos_grouped','chronos_ungrouped'];pc=['#afbbb7','#9bdcca','#cfb3e8']
 fig,axes=plt.subplots(2,3,figsize=(14,8));fig.subplots_adjust(left=.14,right=.96,bottom=.17,top=.83,wspace=.42,hspace=.48)
 for row,h in enumerate((1,20)):
  ax=axes[row,0];ax.barh(range(3),[prob[v,h]['wis'] for v in vlist],color=pc);ax.set_yticks(range(3),['Static quantiles','Grouped','Ungrouped']);ax.invert_yaxis();ax.set_xlim(0,.62);ax.set_title(f'H{h} / scaled WIS');ax.grid(axis='x');ax.set_xlabel('Lower is better')
  for k,v in enumerate(vlist):ax.text(prob[v,h]['wis']+.005,k,f"{prob[v,h]['wis']:.4f}",va='center',fontsize=9)
  for k,v in enumerate(vlist):
   intervals=sorted(prob[v,h]['intervals'],key=lambda r:r['nominal_coverage']);nom=[r['nominal_coverage'] for r in intervals]
   axes[row,1].plot(nom,[r['coverage'] for r in intervals],'o-',color=pc[k],label=['Static quantiles','Grouped','Ungrouped'][k])
   axes[row,2].plot(nom,[r['scaled_width'] for r in intervals],'o-',color=pc[k])
  axes[row,1].plot([.35,.95],[.35,.95],color='#ffffff',ls='--',lw=1,label='Nominal' if row==0 else None);axes[row,1].set_ylim(.3,.98);axes[row,1].set_title(f'H{h} / empirical coverage');axes[row,2].set_title(f'H{h} / scaled interval width')
  for ax in axes[row,1:]:ax.set_xticks([.4,.6,.8],['40%','60%','80%']);ax.set_xlabel('Nominal interval coverage');ax.grid()
 axes[0,1].legend(loc='upper left',fontsize=8,frameon=False)
 save(fig,out,'F3-probabilistic-quality','03 / Sharper distributions against a limited static reference','784 valid cells per model/horizon. WIS and width use training-only absolute-change scales. Native quantiles; no repair.\nStatic training quantiles are not an adaptive volatility baseline. No WIS significance claim; dependence limits calibration inference.')
 fig,ax=plt.subplots(figsize=(11,4.1));fig.subplots_adjust(left=.20,right=.94,bottom=.31,top=.73)
 for k,h in enumerate((1,20)):
  r=pair[('chronos_grouped-minus-chronos_ungrouped',h)];lo,hi=[r['intervals']['60'][x] for x in ('low','high')]
  ax.plot([lo,hi],[k,k],lw=3,color=COLORS[k*2]);ax.scatter(r['mean'],k,color=COLORS[k*2],s=70,zorder=3)
 ax.axvline(0,color='white',ls='--');ax.set_yticks([0,1],['H1 / primary','H20 / secondary']);ax.invert_yaxis();ax.set_xlim(-.0035,.0025);ax.set_xlabel('Grouped minus ungrouped scaled MAE');ax.grid(axis='x')
 save(fig,out,'F4-grouping-ablation','04 / Grouping does not show a consistent advantage','Identical origins, checkpoint and inputs; attention grouping differs. Negative favours grouping.\nStored 95% percentile intervals, 60-day blocks; both intervals include zero. Marginal quantiles are not a joint asset distribution.')
 resources=data['resources'];fig,axes=plt.subplots(1,3,figsize=(14,5));fig.subplots_adjust(left=.19,right=.96,bottom=.25,top=.78,wspace=.34)
 for ax,field,div,title in [(axes[0],'wall_seconds',60,'Fit + run walltime / min'),(axes[1],'peak_rss_bytes',2**20,'Observed worker peak / MiB'),(axes[2],'origin_count',1,'Completed origin jobs')]:
  values=[r[field]/div for r in resources];ax.barh(range(5),values,color=['#afbbb7']+COLORS);ax.set_yticks(range(5),[NAMES[r['variant_id']] for r in resources] if ax is axes[0] else []);ax.invert_yaxis();ax.set_title(title,fontsize=11);ax.set_xlim(0,max(values)*1.30);ax.grid(axis='x')
  for k,value in enumerate(values):ax.text(value+max(values)*.02,k,f'{value:.2f}' if field!='origin_count' else str(int(value)),va='center',fontsize=9)
 save(fig,out,'F5-computational-profile','05 / Measured execution cost, not a hardware benchmark','Five primary variants only; 98/98 jobs each, no failures. Complete component walltime includes loading, fit and I/O.\nRSS is an observed sampled peak. Shared-host serial CPU execution; no GPU measurements or estimated CPU-time conversion.')
 fig,ax=plt.subplots(figsize=(14,6.6));fig.subplots_adjust(left=.03,right=.97,bottom=.19,top=.83);ax.set_xlim(0,14);ax.set_ylim(0,5);ax.axis('off')
 nodes=[('01  SOURCE','ECB reference rates','Units, attribution and scope'),('02  SNAPSHOT','Preserved source bytes','Observation != availability'),('03  PROTOCOL','Registered comparisons','Train-only transformations'),('04  MODEL VERSIONS','Frozen model artifacts','No performance-based tuning'),('05  INFERENCE','Causal contexts -> targets','Recorded failures and resources'),('06  CROSS-CHECK','Independent recalculation','Inputs, losses and intervals'),('07  EVIDENCE ATLAS','Linked measurements','Sources -> runs -> claims'),('08  INTERPRETATION','Proportional conclusions','Development != confirmation')]
 positions=[(.15,2.9),(3.65,2.9),(7.15,2.9),(10.65,2.9),(10.65,.45),(7.15,.45),(3.65,.45),(.15,.45)]
 for i,((x,y),(label,title,sub)) in enumerate(zip(positions,nodes)):
  ax.add_patch(FancyBboxPatch((x,y),3.1,1.6,boxstyle='round,pad=.08,rounding_size=.13',edgecolor='#4b7d73',facecolor='#132b2e'))
  ax.text(x+.16,y+1.25,label,fontsize=9,color='#9bdcca',weight='bold');ax.text(x+.16,y+.80,title,fontsize=11,weight='bold');ax.text(x+.16,y+.36,sub,fontsize=8.5,color='#bdcec5')
  if i<7:
   nx,ny=positions[i+1];start=(x+3.15,y+.8) if i<3 else (x+1.55,y-.1) if i==3 else (x-.1,y+.8);end=(nx-.1,ny+.8) if i<3 else (nx+1.55,ny+1.7) if i==3 else (nx+3.2,ny+.8)
   ax.add_patch(FancyArrowPatch(start,end,arrowstyle='-|>',mutation_scale=15,color='#9bdcca',lw=1.6))
 save(fig,out,'F6-reproducibility-pipeline','06 / From source integrity to a bounded scientific claim','Privately audited chain shown conceptually; no private source, topology or forecast series distributed.\nPublic reproduction starts from curated aggregates and regenerates figures. It does not reproduce model inference or independent validation.')
if __name__=='__main__':
 parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--output',type=Path,default=ROOT/'figures');args=parser.parse_args()
 render(json.loads((ROOT/'aggregates.json').read_text(encoding='utf-8')),args.output)
 print('Rendered F1-F6 as SVG and PNG from public aggregates only.')
