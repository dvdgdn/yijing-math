'use strict';
const D = JSON.parse(document.getElementById('research-data').textContent);
const view = document.getElementById('view');
const recordIndex = new Map([...D.assignments,...D.claims,...D.investigations].map(r=>[r.id,r]));
const local = path => '../' + String(path).replace(/^\/+/, '');
const esc = value => String(value ?? '').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const attr = esc;
const count = (object,key) => object?.[key] || 0;
const titleCase = s => String(s).replace(/-/g,' ').replace(/^./,c=>c.toUpperCase());
const safeHref = url => { try { const u=new URL(url,document.baseURI); return ['http:','https:','file:'].includes(u.protocol)?u.href:'#'; } catch { return '#'; } };
const href = path => esc(safeHref(local(path)));
const statusStyles = {'ready':'positive','verified':'positive','registered':'positive','draft':'warm','reported':'warm','in-verification':'blue','running':'blue','launched':'blue','completed':'blue','missing-output':'alert','disputed':'alert','refuted':'alert','withdrawn':'neutral','superseded':'neutral','reproduced':'neutral','prepared':'neutral'};
const statusLabel = status => ({'completed':'Awaiting registration','missing-output':'Output missing','in-verification':'Being checked'}[status] || titleCase(status));
function pill(status,label) { return `<span class="pill ${statusStyles[status]||'neutral'}">${esc(label||statusLabel(status))}</span>`; }
function chip(id) { const r=recordIndex.get(id); return `<button class="record-chip" data-record="${attr(id)}"><span class="chip-dot ${r?.status==='draft'?'draft':''}"></span>${esc(id)}</button>`; }
function heading(eyebrow,title,description) { return `<section class="hero"><div class="view-intro"><span class="eyebrow">${esc(eyebrow)}</span><h1>${esc(title)}</h1><p>${esc(description)}</p></div></section>`; }
function empty(title,body) {return `<div class="empty"><strong>${esc(title)}</strong>${esc(body)}</div>`;}
function block(title,value) {return `<div><dt>${esc(title)}</dt><dd>${esc(value||'unknown')}</dd></div>`;}
function link(path,label,cls='text-link') {return `<a class="${cls}" href="${href(path)}">${esc(label)} ↗</a>`;}
let currentView='overview';
let filters={assignmentSearch:'',assignmentStatus:'all',assignmentRole:'all',claudeOnly:false,claimSearch:'',claimStatus:'all',claimDomain:'all',paperSearch:'',paperReviewed:false,paperLimit:24,territoryUnassigned:false};
try { Object.assign(filters,JSON.parse(sessionStorage.getItem('yijing-dashboard-filters')||'{}')); } catch {}
function remember() {try {sessionStorage.setItem('yijing-dashboard-filters',JSON.stringify(filters));}catch{}}
function overview() {
 const s=D.summary;
 const ready=count(s.assignment_statuses,'ready'), drafts=count(s.assignment_statuses,'draft');
 const reports=D.investigations.filter(i=>!['missing-output','prepared','running','abandoned'].includes(i.status)).length;
 const stats=[['Registered claims',s.claims,'Assertions preserved in the ledger',''],['Independently verified',s.verified,`Of ${s.claims} registered claims`,''],['Investigations running',s.running,`${ready} assignments ready · ${drafts} draft`,''],['Awaiting registration',s.pending_registration,'Completed reports to reconcile','warm']];
 const pending=D.investigations.filter(i=>i.status==='completed');
 const missing=D.investigations.filter(i=>i.status==='missing-output');
 const waiting=D.assignments.filter(a=>a.waiting_for.length);
 const undeclared=D.overlaps.filter(o=>!o.declared);
 const attention=[...pending.map(i=>({icon:'↗',title:'Reconcile a completed report',text:i.title,id:i.id})),...missing.map(i=>({icon:'?',title:'Recover a missing output',text:'Its covered territory and independence remain unknown until the report is located.',id:i.id})),...waiting.map(a=>({icon:'⌁',title:'A draft is waiting on inputs',text:`${a.title}. Waiting for ${a.waiting_for.join(', ')}.`,id:a.id})),...undeclared.map(o=>({icon:'!',title:'Review an undeclared overlap',text:`${o.a} and ${o.b} share work without a recorded division.`,id:o.a}))].slice(0,5);
 const tracks=(D.notes.tracks||[]).map(t=>`<article class="track"><div class="track-top"><span class="rank">${esc(t.rank)}</span><span class="track-kind">${esc(t.kind)}</span></div><h3>${esc(t.title)}</h3><p>${esc(t.description)}</p><div class="track-actions">${t.assignments.map(chip).join('')}</div><div class="track-foot">${esc(t.label)}</div></article>`).join('');
 const availableLabel=reports===1?'1 available report':`${reports} available reports`;
 return `<section class="hero"><div><span class="eyebrow">A COLLABORATIVE MATHEMATICAL INVESTIGATION</span><h1>Yijing, in progress.</h1><p>One shared view of the evidence, the open territory,<br class="desktop-break"> and the next questions worth asking.</p></div><div class="hero-right">${pill(s.running?'running':'prepared',s.running?`${s.running} investigation${s.running===1?'':'s'} running`:'No investigations running')}<div class="tiny">${availableLabel} · ${s.missing} missing output${s.missing===1?'':'s'}</div></div></section>
 <section class="stats" aria-label="Research status">${stats.map(([label,n,note,tone])=>`<div class="stat"><div class="stat-label">${esc(label)}<span class="stat-marker ${tone}"></span></div><div class="stat-value"><span class="stat-number">${n}</span></div><div class="stat-note">${esc(note)}</div></div>`).join('')}</section>
 <div class="section-head"><h2>Where to go next</h2><a class="section-link" href="#assignments">Explore all assignments ↗</a></div><section class="tracks" aria-label="Proposed priorities">${tracks||empty('No priority slate recorded','Choose work from the assignment queue and current roadmap.')}</section><p class="below-note">${esc(D.notes.note||'Proposed priorities from the current roadmap. A suggestion does not launch an investigation.')}</p>
 <section class="overview-grid"><div><div class="panel"><div class="panel-head"><h2>Needs a coordinator</h2><span class="pill pill-outline">${attention.length} item${attention.length===1?'':'s'}</span></div>${attention.length?attention.map(a=>`<div class="attention-row"><span class="attention-icon" aria-hidden="true">${a.icon}</span><div><h4>${esc(a.title)}</h4><p>${esc(a.text)}</p>${chip(a.id)}</div></div>`).join(''):empty('The handoffs are clear','No missing outputs, pending registrations, blocked inputs or undeclared overlaps are recorded.')}</div>
 <div class="collaboration">${familyCard('claude','Claude')}${familyCard('gpt','GPT / Codex')}</div></div>
 <div><div class="panel evidence-panel"><div class="panel-head"><h2>Evidence, honestly</h2><a class="text-link" href="#evidence">View ledger ↗</a></div><div class="big-fraction">${s.verified}<small>of ${s.claims} claims verified</small></div><div class="evidence-stack" aria-label="Verified fraction"><span style="width:${s.claims?100*s.verified/s.claims:0}%;background:#72916c"></span></div><div class="evidence-legend"><span class="legend-dot"></span>${count(s.claim_statuses,'reported')} reported</div><div class="evidence-legend"><span class="legend-dot green"></span>${s.verified} independently verified</div><p>A result can be precise and promising while its independent check is still ahead. Completed reports enter the ledger through reconciliation.</p>${link('methods/ledger-conventions.md','How verification is recorded')}</div>
 <div class="callout" style="margin-bottom:0"><div><span class="overline">WORKING WITH CLAUDE</span><h3 style="margin-top:8px">Start with a clear handoff.</h3><p>Choose a task, preserve its context boundary, and return a traceable report.</p><a class="text-link" style="display:inline-block;margin-top:14px" href="#guide">Open the collaboration guide ↗</a></div></div></div></section>
 <div class="section-head" style="margin-top:32px"><h2>The library behind the next questions</h2><a class="section-link" href="#library">Browse manuscripts ↗</a></div><div class="panel" style="display:flex;gap:25px;align-items:center;flex-wrap:wrap"><span style="font-family:var(--serif);font-size:36px">${D.corpus.papers.length}</span><span style="font-size:12px;color:var(--muted)">manuscripts indexed · ${D.corpus.families} result families<br>${D.corpus.inspected} theorem statements inspected. Full proof audits remain separate.</span>${link('roadmap/literature/openai-math/transfers.md','Read the transfer review')}</div>`;
}
function familyCard(family,label) {
 const rows=D.investigations.filter(i=>i.model_family===family),running=rows.filter(i=>i.status==='running').length;
 const registered=rows.filter(i=>i.status==='registered').length,pending=rows.filter(i=>i.status==='completed').length,missing=rows.filter(i=>i.status==='missing-output').length;
 return `<div class="family-card"><div class="family-head"><span class="family-name">${label}</span><span class="family-icon ${family==='gpt'?'gpt':''}" aria-hidden="true">${family==='claude'?'✳':'◈'}</span></div><p>${running} running · ${registered} registered report${registered===1?'':'s'}<br>${pending} awaiting registration${missing?` · ${missing} output missing`:''}</p>${family==='claude'?'<button class="text-link" data-action="claude-opportunities">Find a suitable assignment ↗</button>':'<a class="text-link" href="#evidence">Inspect sources and verifiers ↗</a>'}</div>`;
}
function searchField(id,value,placeholder) {return `<label class="search-field"><span aria-hidden="true">⌕</span><input id="${id}" type="search" value="${attr(value)}" placeholder="${attr(placeholder)}" aria-label="${attr(placeholder)}"></label>`;}
function selectField(id,label,value,options) {return `<select id="${id}" aria-label="${attr(label)}">${options.map(([v,l])=>`<option value="${attr(v)}" ${value===v?'selected':''}>${esc(l)}</option>`).join('')}</select>`;}
function assignments() {
 const s=D.summary;
 return heading('THE WORK QUEUE','A question for every investigation.','Review status, context and model-family fit before launching. A draft is a proposal; a running investigation has its own linked record.')+
 `<div class="toolbar">${searchField('assignment-search',filters.assignmentSearch,'Search questions, titles or assignment IDs')}${selectField('assignment-status','Assignment status',filters.assignmentStatus,[['all','Every status'],...['ready','draft','launched','completed','withdrawn'].map(v=>[v,titleCase(v)])])}${selectField('assignment-role','Investigator role',filters.assignmentRole,[['all','Every role'],...['explorer','specialist','verifier','paradigm-breaker','synthesis','coordinator'].map(v=>[v,titleCase(v)])])}<button class="filter-button ${filters.claudeOnly?'active':''}" data-action="claude-filter" aria-pressed="${filters.claudeOnly}">Claude opportunities</button></div>
 <div id="assignment-results"></div><div class="callout"><div><h3>One record, many independent minds.</h3><p>Reserve work with the coordinator, then give an investigator only its assembled package. Use the record to distinguish a suggested model from the model that actually ran.</p></div><a class="button secondary" href="#guide">Prepare a handoff ↗</a></div>`;
}
function assignmentResults() {
 const q=filters.assignmentSearch.toLowerCase();
 const rows=D.assignments.filter(a=>(filters.assignmentStatus==='all'||a.status===filters.assignmentStatus)&&(filters.assignmentRole==='all'||a.role===filters.assignmentRole)&&(!filters.claudeOnly||(a.claude_fit==='eligible'&&['ready','draft'].includes(a.status)))&&[a.id,a.title,a.role,a.purpose,...a.work_items,...a.directions,...a.questions].join(' ').toLowerCase().includes(q));
 document.getElementById('assignment-results').innerHTML=`<div class="result-count">${rows.length} of ${D.assignments.length} assignments${filters.claudeOnly?' · Includes drafts that need coordinator review':''}</div><div class="table-wrap"><table><thead><tr><th scope="col">Question / assignment</th><th scope="col">Status</th><th scope="col">Role / context</th><th scope="col">Model & handoff</th></tr></thead><tbody>${rows.map(a=>`<tr><td><span class="row-id">${esc(a.id)}</span><button class="row-title" data-record="${attr(a.id)}">${esc(a.title)}</button><div class="row-sub">${esc(titleCase(a.purpose))}${a.waiting_for.length?' · Waiting for '+esc(a.waiting_for.join(', ')):''}</div></td><td class="status-cell">${pill(a.status,a.status==='completed'?'Completed':undefined)}${a.waiting_for.length?'<div class="fit-note">Inputs incomplete</div>':''}</td><td>${esc(titleCase(a.role))}<div class="row-sub">${esc(a.context_mode)} context</div></td><td>${esc(a.recommended_model)}<div class="fit-note">${a.runs.length?'Linked runs: '+esc(a.runs.join(', ')):a.claude_fit==='reproduction-only'?'Claude: same-family reproduction':a.claude_fit==='check-provenance'?'Verifier family needs a provenance check':a.claude_fit==='excluded'?'Claude is excluded from this assignment':'Claude can contribute within the stated scope'}</div></td></tr>`).join('')}</tbody></table>${rows.length?'':empty('No matching assignments','Try a broader search or clear the filters.')}</div>`;
}
function evidence() {
 return heading('THE EVIDENCE BASE','Keep certainty visible.','Every registered statement retains its provenance, assumptions and verification state. Independent checks and source correspondence are recorded separately.')+
 `<div class="toolbar">${searchField('claim-search',filters.claimSearch,'Search claims, sources or claim IDs')}${selectField('claim-status','Claim status',filters.claimStatus,[['all','Every status'],...Object.keys(D.summary.claim_statuses).sort().map(v=>[v,titleCase(v)])])}${selectField('claim-domain','Claim domain',filters.claimDomain,[['all','Every domain'],...['formal','source-dependent','historical','interpretive'].map(v=>[v,titleCase(v)])])}</div><div id="claim-results"></div>
 <div class="two-col"><div class="panel"><div class="panel-head"><h2>Investigation records</h2></div>${D.investigations.map(i=>`<div class="attention-row"><div style="flex:1"><span class="row-id">${esc(i.id)} · ${esc(i.model_family||'unknown')}</span><button class="row-title" data-record="${attr(i.id)}">${esc(i.title)}</button><div class="row-sub">${esc(i.model)} · ${esc(i.context_mode)} context · ${esc(i.independence)}</div><div style="margin-top:9px">${pill(i.status)}</div></div></div>`).join('')}</div><div class="panel"><div class="panel-head"><h2>Live disputes</h2></div>${D.disputes.map(d=>`<div class="attention-row"><div><span class="row-id">${esc(d.id)}</span><h4>${esc(d.title)}</h4><p>${esc(d.status)}</p><div style="margin-top:8px">${link(d.path,'Open the positions and tests')}</div></div></div>`).join('')||empty('None recorded','No dispute entries are present.')}</div></div>`;
}
function claimResults() {
 const q=filters.claimSearch.toLowerCase();
 const rows=D.claims.filter(c=>(filters.claimStatus==='all'||c.status===filters.claimStatus)&&(filters.claimDomain==='all'||c.domain===filters.claimDomain)&&[c.id,c.title,c.evidence,...c.sources].join(' ').toLowerCase().includes(q));
 document.getElementById('claim-results').innerHTML=`<div class="result-count">${rows.length} of ${D.claims.length} registered claims · report-local results awaiting registration are listed separately below.</div><div class="table-wrap"><table><thead><tr><th scope="col">Statement</th><th scope="col">Evidence status</th><th scope="col">Domain</th><th scope="col">Dependencies</th></tr></thead><tbody>${rows.map(c=>`<tr><td><span class="row-id">${esc(c.id)}</span><button class="row-title" data-record="${attr(c.id)}">${esc(c.title)}</button><div class="row-sub">${esc(titleCase(c.type))}</div></td><td class="status-cell">${pill(c.status)}<div class="fit-note">${c.verifiers.length} verifier record${c.verifiers.length===1?'':'s'}</div></td><td>${esc(titleCase(c.domain))}<div class="row-sub">${esc(c.contingency)}</div></td><td>${c.dependents.length} dependent claim${c.dependents.length===1?'':'s'}<div class="row-sub">Source: ${esc(c.sources.join(', '))}</div></td></tr>`).join('')}</tbody></table>${rows.length?'':empty('No matching claims','Try a broader search or a different evidence status.')}</div>`;
}
function territory() {
 return heading('COVERAGE & OPEN QUESTIONS','Leave room for the unexpected.','Documented exploration and proposed assignments are different signals. A source-intake task can enable a direction without having explored it.')+
 `<div class="toolbar"><span class="muted" style="font-size:12px;flex:1">${D.directions.length} research directions · ${D.questions.length} question records</span><button class="filter-button ${filters.territoryUnassigned?'active':''}" data-action="territory-filter" aria-pressed="${filters.territoryUnassigned}">Only unassigned research</button></div><div class="coverage-list">${D.directions.filter(d=>!filters.territoryUnassigned||!d.research.length).map(d=>`<article class="coverage-card"><div class="coverage-meta"><span class="mono muted">${esc(d.id)}</span><span class="pill neutral">${esc(d.status)}</span></div><h3>${esc(d.title)}</h3><span class="overline">Planned research</span><div class="coverage-links">${d.research.map(chip).join('')||'<span class="coverage-empty">No active research assignment</span>'}</div>${d.enabling.length?`<div class="coverage-note">Enabling work<div class="coverage-links">${d.enabling.map(chip).join('')}</div></div>`:''}<div class="coverage-note">${d.completed.length?esc(d.completed.join(', '))+' completed.':'No completed assignment recorded for this direction.'} ${link(d.path,'Read the direction')}</div></article>`).join('')}</div>
 <div class="section-head" style="margin-top:34px"><h2>Questions to carry forward</h2>${link('ledger/questions.md','Read the question ledger')}</div><div class="table-wrap"><table><thead><tr><th scope="col">Question</th><th scope="col">Recorded status</th><th scope="col">Current assignments</th></tr></thead><tbody>${D.questions.map(q=>`<tr><td><span class="row-id">${esc(q.id)}</span><span class="row-title" style="cursor:default">${esc(q.title)}</span></td><td>${esc(q.status)}</td><td><div class="coverage-links">${q.assignments.map(chip).join('')||'<span class="muted">Unassigned</span>'}</div></td></tr>`).join('')}</tbody></table></div>`;
}
function library() {
 return heading('THE EXTERNAL RESEARCH LIBRARY','Find a result. Check the bridge.','Browse the pinned manuscript catalogue. Retrieval, statement inspection, proof audit and a useful Yijing application each require their own evidence.')+
 `<section class="stats" aria-label="Library scope">${[[D.corpus.papers.length,'Manuscripts indexed'],[D.corpus.families,'Result families'],[D.corpus.inspected,'Statements inspected'],[D.corpus.papers.length-D.corpus.inspected,'Not individually reviewed']].map(([n,l])=>`<div class="stat"><div class="stat-label">${l}</div><div class="stat-value"><span class="stat-number">${n}</span></div></div>`).join('')}</section><div class="toolbar">${searchField('paper-search',filters.paperSearch,'Search manuscript titles, families or topics')}<button class="filter-button ${filters.paperReviewed?'active':''}" data-action="paper-reviewed" aria-pressed="${filters.paperReviewed}">Inspected statements only</button></div><div id="paper-results"></div><div class="guide-links">${link('roadmap/literature/openai-math/transfers.md','Priorities and failed transfers')}${link('roadmap/literature/openai-math/README.md','Search abstracts and review the snapshot')}</div>`;
}
function paperResults() {
 const terms=filters.paperSearch.toLowerCase().trim().split(/\s+/).filter(Boolean);
 const rows=D.corpus.papers.filter(p=>(!filters.paperReviewed||p.review.level?.startsWith('theorem'))&&terms.every(t=>[p.title,p.family_title,p.family,...p.tags].join(' ').toLowerCase().includes(t)));
 const shown=rows.slice(0,filters.paperLimit);
 document.getElementById('paper-results').innerHTML=`<div class="result-count">Showing ${shown.length} of ${rows.length} matches. Search covers titles, family descriptions and retrieval topics.</div><div class="table-wrap"><table><thead><tr><th scope="col">Manuscript</th><th scope="col">Review level</th><th scope="col">Transfer judgment</th></tr></thead><tbody>${shown.map(p=>`<tr><td><span class="row-id">FAMILY ${esc(p.family)}</span><a class="paper-title" href="${esc(safeHref(p.url))}" target="_blank" rel="noopener">${esc(p.title)} ↗</a><div class="paper-tags">${p.tags.slice(0,3).map(t=>`<span>${esc(titleCase(t))}</span>`).join('')}</div></td><td>${pill(p.review.level?.startsWith('theorem')?'completed':'prepared',p.review.level?.startsWith('theorem')?'Statement inspected':'Not individually reviewed')}<div class="fit-note">${p.review.level?.startsWith('theorem')?'Full proof not audited':''}</div></td><td>${esc(titleCase(p.review.priority||'unassigned'))}${p.review.disposition?`<div class="row-sub">${esc(p.review.disposition)}</div>`:''}</td></tr>`).join('')}</tbody></table>${rows.length?'':empty('No matching manuscripts','Try a different topic or clear the inspection filter.')}</div>${shown.length<rows.length?'<div class="show-more"><button class="button secondary" data-action="more-papers">Show 24 more</button></div>':''}`;
}
const updateCommands='python3 tools/yj.py index\npython3 tools/yj.py validate';
const serveCommand='python3 tools/yj.py dashboard --serve --port 0';
const coordinatorPrompt=`You are helping coordinate the Yijing mathematical research repository with full context. Read AGENTS.md and README.md, then the generated roadmap/dashboard.html and relevant assignment records. Follow the canonical methods linked there.\n\nRepository access means full context: use it for coordination or explicitly full-context synthesis. Prepare minimal or targeted research in a separate fresh session/workspace containing only its assembled package and supplied data; do not give that investigator the repository or this dashboard.\n\nBefore a human launches a run, reserve a unique investigation ID, check work already in flight, context mode, prerequisites, model-family fit and intentional overlap. Record the actual model and independence evidence. Preserve sent prompts and outputs verbatim and freeze their hashes. Reconcile findings without promoting the author's assertions to verified.\n\nUpdate the Markdown records, not the generated HTML. Run python3 tools/yj.py index followed by python3 tools/yj.py validate after changes. No push or other-model launch unless the human asks. Report which assignment/run you prepared and any unresolved input or overlap.`;
function guide() {
 return heading('A PRACTICAL WORKING GUIDE','A clear handoff, every time.','Use this page together with Claude, Codex and the canonical records. The browser is an overview; the Markdown files remain the shared source of truth.')+
 `<div class="callout"><div><span class="overline">FOR A CLAUDE COORDINATOR</span><h3 style="margin-top:8px">Share the record. Preserve the boundaries.</h3><p>A coordinator may inspect the repository and this page. An independent investigator receives only the assignment package in a fresh session or isolated workspace.</p></div><button class="button" data-action="coordinator-handoff">Open coordinator handoff</button></div>
 <section class="guide-grid"><article class="guide-step"><span class="step-number">01 / CHOOSE & RESERVE</span><h3>Start in the queue.</h3><p>Review the assignment’s status, prerequisites and existing runs. Have one coordinator reserve an unused investigation ID before launching work in parallel.</p><p>Ready assignments can be selected. Drafts need review and complete inputs. Claude can independently audit GPT-originated findings; Claude-originated claims require a different family for independent verification.</p><a class="text-link" href="#assignments">Review assignments ↗</a></article>
 <article class="guide-step"><span class="step-number">02 / PREPARE & INVESTIGATE</span><h3>Give each mind its context.</h3><p>Use the command in an assignment’s detail view to assemble its listed materials. Run minimal or targeted research in a fresh session or an empty workspace containing only that package and its supplied data.</p><p>A Claude agent attached to this repository has full context, suitable for coordination or explicitly full-context synthesis. Keep the dashboard and prior reports outside isolated investigation workspaces.</p>${link('methods/context-modes.md','Read the isolation procedure')}</article>
 <article class="guide-step"><span class="step-number">03 / RETURN & RECONCILE</span><h3>Make the work reusable.</h3><p>Save prompts and replies verbatim, record the actual model and isolation evidence, and freeze originals. Link the investigation to its assignment and register results with their exact evidence status.</p><p>A completed report awaits reconciliation. Update the records and regenerate the overview.</p>${link('methods/ledger-conventions.md','Follow registration and verification')}</article></section>
 <div class="two-col"><section class="panel"><span class="overline">KEEP THIS PAGE CURRENT</span><h2 style="margin-top:10px">One rebuild, shared everywhere.</h2><p class="guide-note" style="margin-top:15px">Every coordinator, including Claude, should run these commands after changing the research records. They update the index, coordination board and this HTML snapshot.</p><pre class="command-block">${esc(updateCommands)}</pre><button class="button secondary" data-copy="update">Copy update commands</button><p class="guide-note" style="margin-top:17px">The snapshot also opens directly as a local HTML file. Refresh that browser tab after a rebuild. Page controls filter and inspect the record; they do not change research statuses.</p></section>
 <section class="panel"><span class="overline">OPTIONAL LIVE VIEW</span><h2 style="margin-top:10px">Watch valid record changes.</h2><p class="guide-note" style="margin-top:15px">From the repository, start the local server and keep its terminal running. Open the local URL it prints. The page checks every five seconds and reloads after a valid source update.</p><pre class="command-block">${esc(serveCommand)}</pre><button class="button secondary" data-copy="serve">Copy live-view command</button><p class="guide-note" style="margin-top:17px">If an edit leaves invalid records, the last valid snapshot stays visible with an error notice. Correct the records to resume. Stop the local server with Ctrl+C.</p></section></div>
 <section class="panel" style="margin-top:23px"><div class="panel-head"><h2>Where updates belong</h2>${link('roadmap/DASHBOARD.md','Dashboard reference')}</div><div class="detail-grid" style="margin-bottom:0"><div><dt>Work and ownership</dt><dd><code>roadmap/assignments/</code><br><code>investigations/…/record.md</code></dd></div><div><dt>Statements and verification</dt><dd><code>ledger/claims/</code><br>Keep evidence and source correspondence explicit.</dd></div><div><dt>Coverage and open questions</dt><dd><code>ledger/directions.md</code><br><code>ledger/questions.md</code></dd></div><div><dt>Proposed priority cards</dt><dd><code>roadmap/dashboard-notes.json</code><br>Change when the coordinator changes the slate.</dd></div></div></section>
 <div class="guide-links">${link('methods/research-cycle.md','Assignment selection and coordination')}${link('investigations/_template/record.md','Investigation record template')}${link('prompts/README.md','Prompt assembly')}${link('methods/standards.md','Mathematical standards')}</div>`;
}
function showRecord(id) {
 const r=recordIndex.get(id);if(!r)return;
 document.querySelector('.dialog-top .eyebrow').textContent='RESEARCH RECORD';
 const isAssignment='work_items' in r,isClaim='depends_on' in r;
 let content=`<span class="mono muted">${esc(r.id)}</span><h2 id="detail-title">${esc(r.title)}</h2><div class="detail-labels">${pill(r.status,r.status==='completed'&&isAssignment?'Completed':undefined)}${isAssignment?'<span class="pill pill-outline">'+esc(r.context_mode)+' context</span>':''}${isClaim?'<span class="pill pill-outline">'+esc(r.domain)+'</span>':''}</div>`;
 if(isAssignment){
  content+=`<dl class="detail-grid">${block('Role',r.role)}${block('Purpose',r.purpose)}${block('Recommended model',r.recommended_model)}${block('Linked investigations',r.runs.join(', ')||'None recorded')}${block('Prerequisites',r.waiting_for.join(', ')||'No unfinished prerequisites')}${block('Claude family fit',r.claude_fit==='eligible'?'Suitable within the stated scope':r.claude_fit==='reproduction-only'?'Same-family reproduction only':r.claude_fit==='excluded'?'Excluded by the assignment':'Verify origin provenance first')}</dl>`;
  if(r.status==='draft')content+='<div class="sync-warning">This is a draft. Review its inputs and scope before promoting it to ready or launching a run.</div>';
  content+=`<div class="detail-section"><h4>Concrete work items</h4><p>${esc(r.work_items.join(', '))}</p></div><div class="detail-section"><h4>Coverage</h4><p>${esc([...r.directions,...r.questions].join(' · ')||'No coverage tags recorded')}</p></div><div class="detail-section"><h4>Intentional overlap</h4><div class="coverage-links">${r.intentional_overlap.map(chip).join('')||'<span class="muted">None declared.</span>'}</div></div><div class="detail-section"><h4>Prepare the first package</h4><p>Run from the repository. This prints the package; it does not reserve an ID or launch a model. Save exactly what you send and follow the assignment’s phase instructions.</p><pre class="command-block">python3 tools/yj.py assemble ${esc(r.id)} --part 1</pre><button class="button secondary" data-copy="assembly" data-id="${attr(r.id)}">Copy assembly command</button></div>`;
 }else if(isClaim){
  content+=`<dl class="detail-grid">${block('Type',r.type)}${block('Dependence on choices',r.contingency)}${block('Source investigations',r.sources.join(', '))}${block('Verifier records',r.verifiers.join(', ')||'None recorded')}${block('Further investigation value',r.value)}${block('Dependent claims',String(r.dependents.length))}</dl><div class="detail-section"><h4>Evidence as it currently exists</h4><p>${esc(r.evidence)}</p></div><div class="detail-section"><h4>Recorded dependencies</h4><p>${esc(r.depends_on.join(', ')||'None recorded')}</p></div><div class="detail-section"><h4>Planned verification</h4><div class="coverage-links">${r.verification_work.map(chip).join('')||'<span class="muted">No active verification assignment targets this claim.</span>'}</div></div>`;
 }else{
  content+=`<dl class="detail-grid">${block('Model as recorded',r.model)}${block('Model family',r.model_family)}${block('Context mode',r.context_mode)}${block('Independence',r.independence)}${block('Date run',r.date_run)}${block('Assignment',r.assignment)}</dl><div class="detail-section"><h4>What to do next</h4><p>${esc(r.status==='completed'?'Reconcile this output and its proposed registration before counting new registered claims.':r.status==='missing-output'?'Recover the original report and its known provenance. Coverage remains unknown while the output is missing.':r.status==='running'?'Return the original output and record completion before registration.':'Read the record for provenance, source materials and registration.')}</p></div>`;
  if(r.output&&!['missing','unknown','none'].includes(r.output))content+=link(r.output,'Read the original output','button secondary');
 }
 content+=`<div class="detail-actions">${link(r.path,isAssignment?'Read the complete assignment':'Read the source record','button')}</div>`;
 document.getElementById('detail-content').innerHTML=content;
 const dialog=document.getElementById('detail-dialog');if(!dialog.open)dialog.showModal();
}
function route() {
 const name=location.hash.slice(1)||'overview';currentView=['overview','assignments','evidence','territory','library','guide'].includes(name)?name:'overview';
 const labels={overview:'Overview',assignments:'Assignments',evidence:'Evidence',territory:'Research territory',library:'Manuscript library',guide:'How to use this'};
 document.getElementById('page-label').textContent=labels[currentView];
 document.querySelectorAll('[data-nav]').forEach(a=>{const active=a.dataset.nav===currentView;a.classList.toggle('active',active);if(active)a.setAttribute('aria-current','page');else a.removeAttribute('aria-current');});
 view.innerHTML=({overview,assignments,evidence,territory,library,guide}[currentView])();
 if(currentView==='assignments')assignmentResults();if(currentView==='evidence')claimResults();if(currentView==='library')paperResults();
 document.title=`${labels[currentView]} · Yijing research`;
}
function coordinatorHandoff() {
 document.querySelector('.dialog-top .eyebrow').textContent='COORDINATOR HANDOFF';
 document.getElementById('detail-content').innerHTML=`<h2 id="detail-title">Start a Claude coordinator.</h2><p class="guide-note">Give this to a full-context coordinator with the repository attached. Prepare an isolated investigator separately with its assignment package.</p><textarea id="handoff-text" class="handoff-text" readonly aria-label="Claude coordinator instructions">${esc(coordinatorPrompt)}</textarea><div class="detail-actions"><button class="button" data-copy="coordinator">Copy instructions</button><button class="button secondary" data-action="select-handoff">Select text</button></div><p class="tiny">If your browser blocks clipboard access, select the text and copy it with your keyboard.</p>`;
 const dialog=document.getElementById('detail-dialog');if(!dialog.open)dialog.showModal();
}
async function copyText(text) {
 let copied=false;
 try {await navigator.clipboard.writeText(text);copied=true;}catch{
  const t=document.createElement('textarea');t.value=text;document.body.append(t);t.select();copied=document.execCommand('copy');t.remove();
 }
 const toast=document.getElementById('toast');toast.textContent=copied?'Copied. Run commands from the repository.':'Clipboard access is unavailable. Select the displayed text and copy it with your keyboard.';toast.hidden=false;setTimeout(()=>toast.hidden=true,5000);
}
document.addEventListener('click',e=>{
 const record=e.target.closest('[data-record]');if(record){showRecord(record.dataset.record);return;}
 const copy=e.target.closest('[data-copy]');if(copy){const value=copy.dataset.copy;copyText(value==='coordinator'?coordinatorPrompt:value==='update'?updateCommands:value==='serve'?serveCommand:`python3 tools/yj.py assemble ${copy.dataset.id} --part 1`);return;}
 const action=e.target.closest('[data-action]')?.dataset.action;if(!action)return;
 if(action==='coordinator-handoff')coordinatorHandoff();
 if(action==='select-handoff'){const t=document.getElementById('handoff-text');t.focus();t.select();}
 if(action==='claude-opportunities'){filters.claudeOnly=true;filters.assignmentStatus='all';filters.assignmentRole='all';filters.assignmentSearch='';remember();if(location.hash==='#assignments')route();else location.hash='assignments';}
 if(action==='claude-filter'){filters.claudeOnly=!filters.claudeOnly;remember();route();}
 if(action==='territory-filter'){filters.territoryUnassigned=!filters.territoryUnassigned;remember();route();}
 if(action==='paper-reviewed'){filters.paperReviewed=!filters.paperReviewed;filters.paperLimit=24;remember();route();}
 if(action==='more-papers'){filters.paperLimit+=24;remember();paperResults();}
});
document.addEventListener('input',e=>{
 const id=e.target.id;
 if(id==='assignment-search'){filters.assignmentSearch=e.target.value;assignmentResults();}
 if(id==='claim-search'){filters.claimSearch=e.target.value;claimResults();}
 if(id==='paper-search'){filters.paperSearch=e.target.value;filters.paperLimit=24;paperResults();}
 remember();
});
document.addEventListener('change',e=>{
 const id=e.target.id;
 if(id==='assignment-status')filters.assignmentStatus=e.target.value;
 if(id==='assignment-role')filters.assignmentRole=e.target.value;
 if(id==='claim-status')filters.claimStatus=e.target.value;
 if(id==='claim-domain')filters.claimDomain=e.target.value;
 remember();if(currentView==='assignments')assignmentResults();if(currentView==='evidence')claimResults();
});
document.getElementById('close-dialog').addEventListener('click',()=>document.getElementById('detail-dialog').close());
document.getElementById('detail-dialog').addEventListener('click',e=>{if(e.target===document.getElementById('detail-dialog')&&e.clientX<e.target.getBoundingClientRect().left)e.target.close();});
window.addEventListener('hashchange',()=>{if(document.getElementById('detail-dialog').open)document.getElementById('detail-dialog').close();route();window.scrollTo({top:0});});
document.getElementById('assignment-count').textContent=D.assignments.length;
document.getElementById('claim-count').textContent=D.claims.length;
document.getElementById('snapshot-label').textContent=`Ledger ${D.version}${D.record_date?' · Records through '+new Intl.DateTimeFormat('en-GB',{day:'numeric',month:'short',year:'numeric',timeZone:'Europe/Berlin'}).format(new Date(D.record_date+'T12:00:00Z')):''}`;
let liveConnected=false, pollBusy=false;
async function poll(manual=false) {
 if(!['http:','https:'].includes(location.protocol)){if(manual)location.reload();return;}
 if(pollBusy)return;pollBusy=true;
 try {
  const response=await fetch('/__dashboard_status',{cache:'no-store'});if(!response.ok)throw new Error('No status endpoint');
  const state=await response.json();if(typeof state.valid!=='boolean')throw new Error('Not a dashboard server');
  liveConnected=true;
  const warning=document.getElementById('sync-warning');warning.hidden=state.valid;
  if(!state.valid)warning.textContent='Updates paused. Showing the last valid snapshot.\n'+(state.errors||[]).slice(0,5).join('\n');
  document.getElementById('live-dot').classList.toggle('live-pulse',state.valid);
  document.getElementById('freshness-label').textContent=state.valid?'Live · checked '+new Intl.DateTimeFormat('en-GB',{hour:'2-digit',minute:'2-digit',second:'2-digit',timeZone:'Europe/Berlin'}).format(new Date(state.checked_at)):'Live · update needs attention';
  if(state.valid&&state.fingerprint!==D.fingerprint)location.reload();
 }catch{
  document.getElementById('live-dot').classList.remove('live-pulse');document.getElementById('freshness-label').textContent=liveConnected?'Snapshot · live view disconnected':'Repository snapshot';
  if(manual)location.reload();
 }finally{pollBusy=false;}
}
document.getElementById('refresh-button').addEventListener('click',()=>poll(true));
route();poll();setInterval(()=>{if(document.visibilityState==='visible')poll();},5000);
