#!/usr/bin/env python3
"""Render a plugin blueprint from YAML without modifying its source."""
import argparse
import html
import json
from datetime import datetime
from pathlib import Path


BASE = Path(__file__).resolve().parent


def load(path):
    source = Path(path).read_text(encoding="utf-8")
    try:
        return json.loads(source)
    except json.JSONDecodeError:
        import yaml
        return yaml.safe_load(source)


def write_yaml(path, value):
    Path(path).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def initial_decisions(data):
    return {"todos": {t["id"]: "0.1" for t in data["todos"]},
            "regressions": {r["id"]: None for r in data["regressions"]}}


def repo_root():
    return next(p for p in BASE.parents if (p / "AGENTS.md").is_file())


TEMPLATE = r'''<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>__TITLE__</title><style>
@font-face{font-family:'Noto Sans SC Local';src:url('__FONT__') format('truetype');font-weight:100 900;font-display:swap}
*{box-sizing:border-box}body{margin:0;background:#fafafa;color:#202020;font:15px/1.6 'Noto Sans SC','Noto Sans SC Local',sans-serif}
main{max-width:1100px;margin:44px auto 80px}h1{font-size:30px;line-height:1.4;margin:0 0 8px;font-weight:700}h2{font-size:21px;margin:38px 0 16px}h3{font-size:17px;margin:22px 0 8px}.muted{color:#707070}.updated{margin:0 0 24px;font-size:13px}
.cards{display:grid;grid-template-columns:repeat(5,1fr);gap:12px}.card{background:white;border:1px solid #ddd;border-radius:8px;padding:15px 16px;min-height:132px}.number{font-size:30px;line-height:1.35;font-weight:700;margin-bottom:6px}.small{font-size:12px;color:#707070;margin-top:5px;overflow-wrap:anywhere}.zero{color:#888}.danger{color:#b42318}
.table-wrap{border:1px solid #ddd;border-radius:8px;background:#fff;overflow:hidden}table{width:100%;border-collapse:collapse;table-layout:fixed}th{text-align:left;background:#f3f3f3;color:#555;font-weight:500;font-size:13px}td,th{padding:14px 10px;vertical-align:top;border-bottom:1px solid #e5e5e5}tr:last-child td{border-bottom:0}td{overflow-wrap:anywhere}.id{font-size:13px;font-weight:600;white-space:nowrap}.name{font-weight:650}.tag{display:inline-block;font-size:11px;line-height:1.8;padding:0 6px;border-radius:4px;background:#eee;color:#555;white-space:nowrap;margin-top:5px}.tag.new{background:#e0ecff;color:#1d4ed8}.pill{display:inline-block;padding:1px 6px;border:1px solid #ddd;border-radius:12px;font-size:12px;color:#444;background:#fafafa;margin:2px 3px 2px 0;cursor:help}.segments{display:inline-flex;border:1px solid #ccc;border-radius:5px;overflow:hidden;white-space:nowrap}button{font:inherit;cursor:pointer;color:#333;background:white;border:1px solid #ccc;border-radius:4px;padding:5px 10px}button:focus-visible{outline:2px solid #333;outline-offset:2px}.segments button{font-size:12px;border:0;border-right:1px solid #ddd;border-radius:0;padding:5px 9px;line-height:1.5}.segments button:last-child{border:0}.segments button[aria-pressed=true][data-value="0.1"]{color:white;background:#252525}.segments button[aria-pressed=true][data-value="0.2"]{background:#e6e6e6;color:#222}.segments button[aria-pressed=true][data-value="搁置"]{background:white;text-decoration:line-through;color:#777}.toggle{border:0;background:none;font-size:17px;padding:0 3px;color:#666}.detail td{padding:18px 22px;background:#fafafa}.detail[hidden]{display:none}.detail p{margin:0 0 12px}.detail p:last-child{margin-bottom:0}.quote{border-left:2px solid #2563eb;padding-left:12px;white-space:pre-wrap}.source{border-left:2px solid #ddd;padding-left:12px;font-size:13px;color:#777;white-space:pre-wrap}.path{font-size:12px;color:#777;overflow-wrap:anywhere}.ref{color:#9a6700}.skill{margin-bottom:22px}.description{margin:0 0 14px;color:#555}.rule-table{font-size:14px}.rule-file{display:block;font-size:11px;color:#777;margin-top:4px}.shared-files{font-size:12px;color:#777;padding:0;list-style:none}.check{padding:12px 0;border-bottom:1px solid #ddd;display:flex;gap:16px}.check-status{min-width:70px;font-weight:600}.check-result{flex:1}#offline{background:#fff3cd;border:1px solid #e4cf84;color:#65521a;padding:12px 16px;margin:0 0 24px;border-radius:5px;display:flex;justify-content:space-between;align-items:center;gap:20px}#offline[hidden]{display:none}#saved{position:fixed;top:18px;right:24px;color:#444;background:#fff;border:1px solid #ddd;border-radius:5px;padding:5px 12px;z-index:2}#saved[hidden]{display:none}
.cards{grid-template-columns:repeat(6,minmax(0,1fr))}.soft{color:#9a6700}
#todos .id{color:#777;font-weight:400;font-size:12px}.todo-need{font-weight:700}.assessment-status{display:inline-block;border-radius:12px;padding:2px 9px;font-size:12px;white-space:nowrap}.assessment-status.hard{color:#1a7f37;background:#e6f4ea}.assessment-status.soft{color:#9a6700;background:#fff4d6}.rule-location{display:block;color:#9a6700;font-size:12px;margin-top:5px}.assessment-block{margin-bottom:16px}.assessment-block strong{display:block;margin-bottom:4px}.assessment-text{white-space:pre-wrap}.assessment-rule-quote{border-left:2px solid #ddd;padding-left:12px;font-size:9.5pt;color:#555}.assessment-proposal{border-left:2px solid #2563eb;padding-left:12px}.assessment-rule-id,.todo-meta{color:#777;font-size:12px}.todo-meta{margin-top:18px}.todo-original{margin-top:14px}.todo-original summary,#all-rules>summary{cursor:pointer;color:#555}.todo-original[open] summary{margin-bottom:14px}.skill{display:flex;gap:16px;padding:17px 0;margin:0;border-bottom:1px solid #ddd;align-items:baseline}.skill-name{font-weight:700;min-width:175px}.skill-content{flex:1}.skill .description{display:inline;margin:0}.skill-todos{margin-top:7px}.shared-note{font-size:12px;color:#777}#all-rules{margin-top:38px}#all-rules>summary{font-size:21px;font-weight:700;margin-bottom:16px}
@media(max-width:1150px){main{margin:28px 20px 60px}}@media(max-width:760px){.cards{grid-template-columns:repeat(2,1fr)}.table-wrap{overflow-x:auto}.table-wrap>table{min-width:850px}.card{min-height:120px}.skill{display:block}}
</style></head><body><main>
<div id="offline" role="status" hidden><span>未连接本地服务，选择只存在本浏览器</span><button id="export">导出选择</button></div>
<h1>__TITLE__</h1><p class="updated muted">更新于 __TIME__</p>
<div class="cards" id="cards"></div>
<h2>待办</h2><div id="todos" class="table-wrap"></div>
<h2>回归</h2><div id="regressions" class="table-wrap"></div>
<h2>Skill</h2><div id="skills"></div>
<h2>机械检查</h2><div id="checks"></div>
<details id="all-rules"><summary>全部规则原文</summary><div id="rules"></div></details>
</main><div id="saved" role="status" hidden>已保存</div>
<script id="blueprint-data" type="application/json">__DATA__</script>
<script id="decisions-data" type="application/json">__DECISIONS__</script>
<script id="checks-data" type="application/json">__CHECKS__</script>
<script>
'use strict';
const data=JSON.parse(document.getElementById('blueprint-data').textContent);
const checks=JSON.parse(document.getElementById('checks-data').textContent);
let decisions=JSON.parse(document.getElementById('decisions-data').textContent);
const esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const storageKey='plugin-blueprint:'+data.plugin;
let online=false,saveQueue=Promise.resolve(),savedTimer;
const todoById=Object.fromEntries(data.todos.map(t=>[t.id,t]));
const uncovered=data.todos.filter(t=>!data.regressions.some(r=>r.covers.includes(t.id)));
const text=s=>s?esc(s):'—';
const ruleIds=t=>(t.assessment?.rule_id||'').match(/(?:JI|SD|TS)-\d+/g)||[];
const sharedRules=data.rules.filter(r=>r.id.startsWith('TS-')).filter((r,i,rs)=>rs.findIndex(other=>other.id===r.id)===i);
const pills=ids=>ids.map(id=>`<span class="pill" title="${esc(todoById[id]?.title||data.regressions.find(r=>r.id===id)?.name||id)}">${esc(id)}</span>`).join('');
function segments(group,id){return `<div class="segments" role="group" aria-label="${id} 选择">${['0.1','0.2','搁置'].map(v=>`<button data-group="${group}" data-id="${id}" data-value="${v}" aria-pressed="${decisions[group][id]===v}">${v}</button>`).join('')}</div>`;}
function cards(){
 const original=data.todos.filter(t=>!t.supplement).length,extra=data.todos.length-original;
 const existing=data.regressions.filter(r=>r.source==='已有').length;
 const values=[
  [data.skills.length,'Skill',data.skills.map(s=>s.name).join(' · '),''],
  [extra?`${original} + ${extra}`:original,'待办','',''],
  [data.regressions.length,'回归',`已有 ${existing} · 新增 ${data.regressions.length-existing}`,''],
  [uncovered.length,'未被回归覆盖的待办','',''+(uncovered.length?'danger':'zero')],
  [Object.values(decisions.regressions).filter(v=>v==='0.1').length,'已选 0.1 的回归','',''],
  [data.todos.filter(t=>t.assessment?.status==='写软了').length,'写软了','',data.todos.some(t=>t.assessment?.status==='写软了')?'soft':'zero']];
 document.getElementById('cards').innerHTML=values.map(([n,label,sub,cls],i)=>`<div class="card"><div class="number ${cls}" data-card="${i}">${esc(n)}</div><div>${label}</div>${sub?`<div class="small">${esc(sub)}</div>`:''}</div>`).join('');
}
function ruleTable(rules){return `<div class="table-wrap"><table class="rule-table"><colgroup><col style="width:90px"><col><col style="width:130px"></colgroup><thead><tr><th>编号</th><th>第一句</th><th>位置类型</th></tr></thead><tbody>${rules.map(r=>`<tr data-rule="${esc(r.id)}" data-file="${esc(r.file)}"><td class="id">${esc(r.id)}</td><td><span class="first-sentence">${esc(r.first_sentence)}</span><span class="rule-file">${esc(r.file)}:${r.line}</span></td><td class="${r.location_type==='引用文件'?'ref':''}">${esc(r.location_type)}</td></tr>`).join('')}</tbody></table></div>`;}
function render(){
 cards();
 document.getElementById('regressions').innerHTML=`<table><colgroup><col style="width:54px"><col style="width:210px"><col><col style="width:160px"><col style="width:172px"></colgroup><thead><tr><th>编号</th><th>名称</th><th>测什么</th><th>覆盖的待办</th><th>选择</th></tr></thead><tbody>${data.regressions.map(r=>`<tr data-regression="${r.id}"><td class="id">${r.id}</td><td><div class="name">${esc(r.name)}</div><span class="tag ${r.source==='新增'?'new':''}">${r.source}</span></td><td class="test-text">${text(r.test)}</td><td>${pills(r.covers)}</td><td>${segments('regressions',r.id)} <button class="toggle" data-detail="detail-${r.id}" aria-expanded="false" aria-label="展开 ${r.id}">⌄</button></td></tr><tr class="detail" id="detail-${r.id}" hidden><td colspan="5"><p class="judgment">${text(r.judgment)}</p><p class="path">${r.materials.map(esc).join('<br>')}</p></td></tr>`).join('')}</tbody></table>`;
 document.getElementById('todos').innerHTML=`<table><colgroup><col style="width:50px"><col><col style="width:155px"><col style="width:130px"><col style="width:172px"></colgroup><thead><tr><th>编号</th><th>待办</th><th></th><th>被哪些回归覆盖</th><th>选择</th></tr></thead><tbody>${data.todos.map(t=>{
 const rs=data.regressions.filter(r=>r.covers.includes(t.id)).map(r=>r.id);
 const a=t.assessment||{},reference=data.rules.some(r=>ruleIds(t).includes(r.id)&&r.location_type==='引用文件');
 return `<tr data-todo="${t.id}"><td class="id">${t.id}</td><td><span class="todo-need">${esc(a.need)}</span>${t.supplement?'<br><span class="tag">用户补充</span>':''}</td><td><span class="assessment-status ${a.status==='写软了'?'soft':'hard'}">${esc(a.status)}</span>${reference?'<span class="rule-location">规则只在附带文件里</span>':''}</td><td>${rs.length?pills(rs):'<span class="danger">无</span>'}</td><td>${segments('todos',t.id)} <button class="toggle" data-detail="detail-${t.id}" aria-expanded="false" aria-label="展开 ${t.id}">⌄</button></td></tr><tr class="detail" id="detail-${t.id}" hidden><td colspan="5"><div class="assessment-block"><strong>案例：</strong><div class="assessment-text assessment-case">${esc(a.case)}</div></div><div class="assessment-block"><strong>现在怎么写的：</strong><div class="assessment-text assessment-rule-quote">${esc(a.rule_quote)}</div><span class="assessment-rule-id">${esc(a.rule_id)}</span></div><div class="assessment-block"><strong>为什么：</strong><div class="assessment-text assessment-why">${esc(a.why)}</div></div><div class="assessment-block"><strong>建议改成：</strong><div class="assessment-text assessment-proposal">${esc(a.proposal)}</div></div><div class="todo-meta"><span class="assessment-by">${esc(a.by)}</span> · <span class="todo-title">${esc(t.title)}</span> · ${t.supplement?`<span class="note">${esc(t.note)}</span>`:`<span class="path">${esc(t.lines)}</span>`}</div><details class="todo-original"><summary>看待办原文</summary>${t.problem?`<p class="problem">${esc(t.problem)}</p>`:''}${t.source_text?`<p class="source">${esc(t.source_text)}</p>`:''}${t.user_words.length?`<p class="quote">${esc(t.user_words.join('\n'))}</p>`:''}</details></td></tr>`;
 }).join('')}</tbody></table>`;
 const skillTodos=rules=>pills(data.todos.filter(t=>ruleIds(t).some(id=>rules.some(r=>r.id===id))).map(t=>t.id));
 document.getElementById('skills').innerHTML=data.skills.map(s=>`<div class="skill" data-skill="${esc(s.name)}"><span class="skill-name">${esc(s.name)}</span><div class="skill-content"><span class="description">${esc(s.description)}</span><div class="skill-todos">承接的待办：${skillTodos(data.rules.filter(r=>!r.id.startsWith('TS-')&&s.rule_files.includes(r.file)))}</div></div></div>`).join('')+`<div class="skill" data-skill="TS"><span class="skill-name">任务状态（附带文件）</span><div class="skill-content"><span class="shared-note">同一内容在 3 个文件里各有一份</span><div class="skill-todos">承接的待办：${skillTodos(sharedRules)}</div></div></div>`;
 document.getElementById('rules').innerHTML=data.skills.map(s=>`<div><h3>${esc(s.name)}</h3>${ruleTable(data.rules.filter(r=>!r.id.startsWith('TS-')&&s.rule_files.includes(r.file)))}</div>`).join('')+`<h3>任务状态（附带文件）</h3><div class="shared-note">同一内容在 3 个文件里各有一份</div><ul class="shared-files">${[...new Set(data.rules.filter(r=>r.id.startsWith('TS-')).map(r=>r.file))].map(f=>`<li>${esc(f)}</li>`).join('')}</ul>${ruleTable(sharedRules)}`;
 document.getElementById('checks').innerHTML=checks.map(c=>`<div class="check"><span class="check-status">${esc(c.status)}</span><span class="check-result">${esc(c.result)}</span></div>`).join('');
}
function offline(){online=false;document.getElementById('offline').hidden=false;}
function localSave(){try{localStorage.setItem(storageKey,JSON.stringify(decisions));}catch{}}
function saved(){clearTimeout(savedTimer);document.getElementById('saved').hidden=false;savedTimer=setTimeout(()=>document.getElementById('saved').hidden=true,2000);}
async function request(url,options={}){
 const controller=new AbortController(),timer=setTimeout(()=>controller.abort(),2000);
 try{const response=await fetch(url,{...options,signal:controller.signal});if(!response.ok)throw Error(response.status);return await response.json();}finally{clearTimeout(timer);}
}
document.addEventListener('click',e=>{
 const toggle=e.target.closest('[data-detail]');
 if(toggle){const detail=document.getElementById(toggle.dataset.detail);detail.hidden=!detail.hidden;toggle.setAttribute('aria-expanded',String(!detail.hidden));toggle.textContent=detail.hidden?'⌄':'⌃';return;}
 const button=e.target.closest('button[data-value]');if(!button)return;
 const {group,id,value}=button.dataset;
 const next=decisions[group][id]===value?null:value;
 decisions[group][id]=next;
 button.parentElement.querySelectorAll('button').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.value===next)));
 cards();localSave();
 saveQueue=saveQueue.then(async()=>{
  if(online){try{await request('api/decisions',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({group,id,value:next})});saved();}catch{offline();localSave();}}
 });
});
document.getElementById('export').addEventListener('click',()=>{
 const blob=new Blob([JSON.stringify(decisions,null,2)+'\n'],{type:'application/yaml;charset=utf-8'});
 const link=document.createElement('a');link.href=URL.createObjectURL(blob);link.download='decisions.yaml';link.click();setTimeout(()=>URL.revokeObjectURL(link.href),1000);
});
function restoreLocal(){try{const local=JSON.parse(localStorage.getItem(storageKey));for(const group of ['todos','regressions'])for(const id of Object.keys(decisions[group]))if(local?.[group]&&Object.hasOwn(local[group],id)&&[null,'0.1','0.2','搁置'].includes(local[group][id]))decisions[group][id]=local[group][id];}catch{}}
render();
window.blueprintReady=(async()=>{
 if(location.protocol==='file:'){offline();restoreLocal();render();return;}
 try{const result=await request('api/decisions');if(result.plugin!==data.plugin)throw Error('plugin');decisions=result.decisions;online=true;localSave();render();}catch{offline();restoreLocal();render();}
})();
</script></body></html>'''


def build(path, checks=None):
    from check_blueprint import check_data
    path = Path(path).resolve()
    data = load(path)
    decisions_file = path.with_name("decisions.yaml")
    if not decisions_file.exists():
        write_yaml(decisions_file, initial_decisions(data))
    values = {"TITLE": html.escape(data["title"]),
              "FONT": html.escape(data.get("font", "NotoSansSC.ttf"), quote=True),
              "TIME": datetime.now().astimezone().isoformat(timespec="seconds"),
              "DATA": json.dumps(data, ensure_ascii=False).replace("<", "\\u003c"),
              "DECISIONS": json.dumps(load(decisions_file), ensure_ascii=False).replace("<", "\\u003c"),
              "CHECKS": json.dumps(checks if checks is not None else check_data(data, repo_root()), ensure_ascii=False).replace("<", "\\u003c")}
    output = TEMPLATE
    # One pass: source strings containing a template token stay verbatim.
    import re
    output = re.sub(r"__(TITLE|FONT|TIME|DATA|DECISIONS|CHECKS)__", lambda m: values[m[1]], output)
    path.with_name("index.html").write_text(output, encoding="utf-8")
    return path.with_name("index.html")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("blueprint", type=Path)
    args = parser.parse_args()
    print(build(args.blueprint))
