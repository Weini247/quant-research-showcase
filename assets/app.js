/* Public roadmap presentation; not connected to private experiments. */
const stages = {
foundation:['MILESTONE 01 / DESIGNED','Research foundation','A documented architecture for quantitative-finance research, statistical validation, experiment tracking and reproducible analysis.','Public research principles and high-level roadmap. Internal specifications remain private.','Proceed to a narrowly scoped historical-data diagnostic.'],
contract:['MILESTONE 02 / CONDITIONAL','First diagnostic contract','A small historical measurement and accounting pilot using AAPL and MSFT has been designed. No actual market-data pilot has run.','Proposed data fields, test scenarios and open provider requirements.','Resolve applicable data-access and retention questions before processing licensed data.'],
data:['MILESTONE 03 / NEXT','Data & accounting core','Develop a standalone Python data-checking and accounting core, initially using synthetic fixtures.','A separate public synthetic ledger demonstration is included; it is not the private P1 implementation.','Run correctness tests and establish an authorized data source.'],
ennead:['MILESTONE 04 / PLANNED','ENNEAD research workbench','A GUI for datasets, experiment configurations, logs, model selection and validation graphics.','This describes planned trading integration only.','Connect a independently testable Python engine to a small end-to-end UI workflow.'],
ml:['MILESTONE 05 / PLANNED','ML research','Compare simple statistical baselines against appropriately justified machine-learning methods.','No trading models have been trained in this project.','Define the prediction task and temporally separated evaluation.'],
strategies:['MILESTONE 06 / PLANNED','Strategy research','Translate economic mechanisms into testable signals, portfolio decisions and research hypotheses.','No profitable strategy is claimed.','Record candidate hypotheses and non-ML baselines.'],
validation:['MILESTONE 07 / PLANNED','Independent validation','Evaluate independent data, multiple-testing uncertainty, robustness and transaction costs.','These are planned research requirements rather than completed backtest results.','Apply independent holdouts and explicit failure criteria.'],
paper:['MILESTONE 08 / CONDITIONAL','Paper operations','Simulate operational decisions using current market information without real orders, if validation justifies the cost.','No paper operations are underway.','Demonstrate data, execution and monitoring readiness.'],
northstar:['NORTHSTAR / VISION','Continuously evaluated research system','An extensible platform for defensible quantitative research that could support controlled trading only if evidence warrants it.','Long-term research aspiration, not profitability evidence.','Maintain reproducibility, falsifiability and clear uncertainty throughout development.']
};
function selectStage(id){
 const x=stages[id]; if(!x)return;
 const values={'detail-label':x[0],'detail-title':x[1],'detail-body':x[2],'detail-evidence':x[3],'detail-next':x[4]};
 Object.entries(values).forEach(([name,value])=>{const el=document.getElementById(name);if(el)el.textContent=value;});
 document.querySelectorAll('.stage').forEach(b=>{const yes=b.dataset.stage===id;b.classList.toggle('is-selected',yes);b.setAttribute('aria-pressed',String(yes));});
}
document.querySelectorAll('.stage').forEach(b=>b.addEventListener('click',()=>selectStage(b.dataset.stage)));
selectStage('foundation');
