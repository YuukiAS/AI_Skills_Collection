#!/usr/bin/env python3
"""Render source-faithful, offline-capable plugin blueprints."""
import argparse
import html
import json
import re
from datetime import datetime
from pathlib import Path

BASE = Path(__file__).resolve().parent
ID_PATTERN = re.compile(r"(?<![A-Za-z0-9_])(?:(?:JI|SD|TS)-\d+|T\d+|R\d+|U\d+)(?![A-Za-z0-9_])")
ASSESSMENT_STATUSES = {
    "约束不足": ("insufficient", "规则是可选的、覆盖太窄、太抽象或有漏洞，模型可以合法跳过"),
    "约束适当": ("appropriate", "已能起作用，内容不需要实质改动"),
    "约束过度": ("excessive", "写得太死或绑定具体案例，会在其他正当场景误伤"),
}


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
    return {"regressions": {r["id"]: None for r in data["regressions"]},
            "todos": {t["id"]: {"stance": None, "note": ""} for t in data["todos"]}}


def normalize_decisions(data, value):
    result = initial_decisions(data)
    for id_, choice in value.get("regressions", {}).items():
        if id_ in result["regressions"] and choice in (None, "0.1", "0.2", "搁置"):
            result["regressions"][id_] = choice
    for id_, choice in value.get("todos", {}).items():
        if id_ in result["todos"] and isinstance(choice, dict):
            result["todos"][id_] = {
                "stance": choice.get("stance") if choice.get("stance") in (None, "同意", "不同意", "有疑问") else None,
                "note": choice.get("note") if isinstance(choice.get("note"), str) else ""}
    return result


def regression_prompts(data, root):
    """Match case identities/names only; never infer or author missing prompts."""
    directory = root / "tools/regression-runner/examples" / data["plugin"]
    cases = [(p, load(p)) for p in sorted(directory.rglob("case.yaml"))]
    matched, audit = {}, []
    for regression in data["regressions"]:
        candidates = [(p, c) for p, c in cases if c.get("id") in
                      (regression["id"], "RD-" + regression["id"])
                      or c.get("name") == regression["name"]]
        if len(candidates) != 1:
            audit.append({"id": regression["id"], "matched": False,
                          "candidates": [str(p.relative_to(root)) for p, _ in candidates]})
            matched[regression["id"]] = []
            continue
        path, case = candidates[0]
        turns = case.get("turns", [])
        matched[regression["id"]] = turns
        audit.append({"id": regression["id"], "matched": True,
                      "path": str(path.relative_to(root)), "turns": len(turns),
                      "prompt_turns": [t["n"] for t in turns if t.get("prompt", "").strip()]})
    return matched, audit


def repo_root():
    return next(p for p in BASE.parents if (p / "AGENTS.md").is_file())


def rule_ids(todo):
    return re.findall(r"(?:JI|SD|TS)-\d+", todo.get("assessment", {}).get("rule_id", ""))


def source_files(data, root):
    """Read every skill body/reference and shared file, without changing sources."""
    paths = []
    for skill in data["skills"]:
        paths.append(skill["file"])
        references = root / skill["file"]
        paths.extend(str(p.relative_to(root)) for p in sorted((references.parent / "references").rglob("*")) if p.is_file())
    paths.extend(data.get("shared_files", []))
    paths.extend(r["file"] for r in data["rules"])
    result = []
    for path in dict.fromkeys(paths):
        lines = (root / path).read_text(encoding="utf-8").splitlines()
        rules = []
        for rule in data["rules"]:
            if rule["file"] != path:
                continue
            start = rule["line"]
            if not 1 <= start <= len(lines) or not re.search(r"(?<![\w-])" + re.escape(rule["id"]) + r"(?![\w-])", lines[start - 1]):
                continue
            end = start
            while end < len(lines) and lines[end].strip():
                end += 1
            rules.append({**rule, "end": end,
                          "todos": [t["id"] for t in data["todos"] if rule["id"] in rule_ids(t)]})
        result.append({"path": path, "id": f"file-{len(result) + 1}", "lines": lines, "rules": rules})
    return result


def render_body(data, files, prompts):
    esc = html.escape
    targets = {t["id"]: "todo-" + t["id"] for t in data["todos"]}
    targets.update({r["id"]: "reg-" + r["id"] for r in data["regressions"]})
    targets.update({r["id"]: "rule-" + r["id"] for r in data["rules"]})
    titles = {t["id"]: t["title"] for t in data["todos"]}
    titles.update({r["id"]: r["name"] for r in data["regressions"]})

    def link(id_, pill=False):
        return f'<a class="{"pill" if pill else "id-link"}" href="#{esc(targets[id_])}" title="{esc(titles.get(id_, id_), quote=True)}">{esc(id_)}</a>'

    def text(value):
        value = str(value or "")
        parts, last = [], 0
        for match in ID_PATTERN.finditer(value):
            parts.append(esc(value[last:match.start()]))
            parts.append(link(match[0]) if match[0] in targets else esc(match[0]))
            last = match.end()
        return "".join(parts) + esc(value[last:])

    def pills(ids):
        return "".join(link(id_, True) for id_ in ids)

    def block(label, value, class_):
        return f'<div class="assessment-block"><strong>{label}</strong><div class="assessment-text {class_}">{text(value)}</div></div>'

    active_todos = [t for t in data["todos"] if not t.get("merged_into")]
    existing = sum(r["source"] == "已有" for r in data["regressions"])
    uncovered = [t for t in active_todos if not any(t["id"] in r["covers"] for r in data["regressions"])]
    rewrite_todos = [t for t in active_todos if t["assessment"]["status"] in ("约束不足", "约束过度")]
    insufficient = sum(t["assessment"]["status"] == "约束不足" for t in active_todos)
    excessive = sum(t["assessment"]["status"] == "约束过度" for t in active_todos)
    rewrite_count = len(rewrite_todos)
    cards = [(len(data["skills"]), "Skill", " · ".join(s["name"] for s in data["skills"]), ""),
             (len(active_todos), f'待办 {len(active_todos)} 条（全部在 0.1 解决）', "", ""),
             (len(data["regressions"]), "回归", f'已有 {existing} · 新增 {len(data["regressions"])-existing}', ""),
             (len(uncovered), "未被回归覆盖的待办", "", "danger" if uncovered else "zero"),
             (0, "已选 0.1 的回归", "", ""),
             (rewrite_count, f"约束不足 {insufficient} · 过度 {excessive}", "", "attention" if rewrite_count else "zero")]
    output = ['<div class="cards" id="cards">']
    card_targets = ["structure", "todos", "regressions", "todos" if uncovered else None, "regressions", "rewrite-todos"]
    for i, (number, label, sub, class_) in enumerate(cards):
        target = card_targets[i]
        opening = f'<a class="card" href="#{target}">' if target else '<div class="card">'
        closing = '</a>' if target else '</div>'
        output.append(f'{opening}<div class="number {class_}" data-card="{i}">{number}</div><div>{label}</div><div class="small">{text(sub)}</div>{closing}')
    output.append('</div><section id="actions"><h2>你要做的</h2>')
    output.append(f'<p>选 {len(data["regressions"])} 个回归的版本（0.1 / 0.2 / 搁置），已选 <span id="selected-count">0</span> 个 <a href="#regressions">去选</a></p>')
    picks = [r['id'] for r in data['regressions'] if r.get('pro_pick')]
    output.append(f'<p class="small" id="pro-picks">GPT Pro 建议 0.1 先跑：{"、".join(link(id_) for id_ in picks)}</p>')
    rewrite_pills = ''.join(f'<a class="pill" href="#todo-{esc(t["id"])}" title="{esc(t["assessment"]["need"], quote=True)}">{esc(t["id"])}</a>' for t in rewrite_todos)
    output.append(f'<p id="rewrite-todos">约束不足或过度的 {rewrite_count} 条待办，下一轮由 GPT Pro 改写：{rewrite_pills}</p>')
    output.append(f'<p id="todo-progress">对 {len(active_todos)} 条待办的建议表态，已表态 <span id="stance-count">0</span> 条，其中不同意 <span id="disagree-count">0</span>、有疑问 <span id="question-count">0</span> <a href="#todos">去表态</a></p></section>')
    output.append('<h2>插件结构与原文</h2><section id="structure">')
    by_path = {f["path"]: f for f in files}

    def file_link(path, label):
        return f'<a href="#{by_path[path]["id"]}">{text(label)}</a>'

    output.append(f'<div class="tree"><strong>{esc(data["plugin"])}</strong><ul>')
    for skill in data["skills"]:
        parent = str(Path(skill["file"]).parent) + "/"
        output.append(f'<li><strong>{esc(skill["name"])}</strong><div class="description">{text(skill["description"])}</div><ul>')
        for f in files:
            if f["path"].startswith(parent):
                output.append(f'<li>{file_link(f["path"], f["path"][len(parent):])}</li>')
        output.append('</ul></li>')
    output.append('<li><strong>任务状态（附带文件）</strong><div class="small">同一内容在 3 个文件里各有一份</div><ul>')
    for path in data.get("shared_files", []):
        output.append(f'<li>{file_link(path, str(Path(path).relative_to(data["sources"]["skill_root"])))}</li>')
    output.append('</ul></li></ul></div>')
    seen_rules = set()
    for f in files:
        file_todos = [t["id"] for t in data["todos"] if any(r["id"] in rule_ids(t) for r in f["rules"])]
        output.append(f'<details class="source-file" id="{f["id"]}" data-file="{esc(f["path"])}"><summary><span class="file-path">{esc(f["path"])}</span><span class="file-todos">管着的待办：{pills(file_todos)}</span></summary><div class="source-lines">')
        for n, line in enumerate(f["lines"], 1):
            starts = [r for r in f["rules"] if r["line"] == n]
            # Consecutive rules can share the same next blank line. Their own
            # lines take precedence, so an unreferenced rule stays uncoloured.
            owners = [r for r in f["rules"] if r["line"] <= n <= r["end"]]
            owner = max(owners, key=lambda r: r["line"], default=None)
            active = owner and owner["todos"]
            anchors = []
            for r in starts:
                id_ = 'rule-' + r['id'] if r['id'] not in seen_rules else f'{f["id"]}-rule-{r["id"]}'
                seen_rules.add(r['id'])
                anchors.append(f'<span class="rule-anchor" id="{id_}" data-rule="{r["id"]}" data-start="{r["line"]}" data-end="{r["end"]}"></span>')
            badges = list(dict.fromkeys(t for r in starts for t in r["todos"]))
            output.append(f'<div class="source-line{" highlighted" if active else ""}" data-line="{n}">{"".join(anchors)}<span class="line-todos">{pills(badges)}</span><span class="line-number">{n}</span><code class="source-text">{text(line)}</code></div>')
        output.append('</div></details>')
    output.append('</section><h2>待办</h2><div id="todos">')
    for t in data["todos"]:
        id_, a = t['id'], t['assessment']
        merged = t.get('merged_into')
        merge_label = f'已并入 {merged} · ' if merged else ''
        pro_badge = '<span class="pro-badge">Pro 有意见</span>' if t.get('pro') else ''
        status_class, definition = ASSESSMENT_STATUSES[a['status']]
        rs = [r["id"] for r in data["regressions"] if id_ in r["covers"]]
        reference = any(r["id"] in rule_ids(t) and r["location_type"] == "引用文件" for r in data["rules"])
        output.append(f'<article class="entry{" merged" if merged else ""}" id="todo-{id_}" data-todo="{id_}"><div class="todo-row"><span class="id">{link(id_)}</span><span class="todo-need">{text(merge_label)}{text(a["need"])}</span><div><span class="assessment-labels"><span class="assessment-status {status_class}" title="{esc(definition, quote=True)}">{esc(a["status"])}</span>{pro_badge}<span class="assessment-change-summary">改动：{esc(a["change"])}</span></span>{"<span class=\"rule-location\">规则只在附带文件里</span>" if reference else ""}{"<span class=\"tag\">用户补充</span>" if t.get("supplement") else ""}</div><div class="coverage">{pills(rs) if rs else "<span class=\"danger\">无</span>"}</div>')
        output.append(f'<div class="segments todo-stance" role="group" aria-label="{id_} 建议改成">')
        for stance in ('同意', '不同意', '有疑问'):
            output.append(f'<button data-group="todos" data-id="{id_}" data-value="{stance}" aria-pressed="false" {"disabled" if merged else ""}>{stance}</button>')
        output.append(f'</div><button class="toggle" data-detail="detail-{id_}" aria-expanded="false" aria-controls="detail-{id_}" aria-label="展开 {id_}">⌄</button></div><div class="todo-note" id="note-{id_}" hidden><textarea data-note="{id_}" rows="3" {"readonly" if merged else ""} placeholder="写具体原因" aria-label="{id_} 写具体原因"></textarea></div><div class="detail" id="detail-{id_}" hidden>')
        output.append(block('案例：', a['case'], 'assessment-case'))
        output.append(block('现在怎么写的：', a['rule_quote'], 'assessment-rule-quote'))
        output.append(f'<div class="assessment-rule-id">{text(a["rule_id"])}</div>')
        output.append(block('为什么：', a['why'], 'assessment-why'))
        output.append(block('改动：', a['change'], 'assessment-change'))
        output.append(block('建议改成：', a['proposal'], 'assessment-proposal'))
        if t.get('pro'):
            paragraphs = []
            for paragraph in t['pro'].split('\n\n'):
                if paragraph.startswith('### '):
                    paragraphs.append('<h4>' + text(paragraph[4:]) + '</h4>')
                elif paragraph.startswith('> '):
                    paragraphs.append('<blockquote>' + text(re.sub(r'(?m)^> ?', '', paragraph)) + '</blockquote>')
                else:
                    paragraphs.append('<p>' + text(paragraph) + '</p>')
            output.append('<div class="assessment-block"><strong>GPT Pro 意见：</strong><div class="pro-opinion">' + ''.join(paragraphs) + '</div></div>')
        output.append(f'<div class="todo-meta"><span class="assessment-by">{text(a["by"])}</span> · <span class="todo-title">{text(t["title"])}</span> · ')
        output.append(f'<span class="note">{text(t["note"])}</span>' if t.get('supplement') else f'<span class="path">{esc(t["lines"])}</span>')
        output.append('</div><details class="todo-original"><summary>看待办原文</summary>')
        for key, class_ in [('problem', 'problem'), ('source_text', 'source')]:
            if t.get(key):
                output.append(f'<p class="{class_}">{text(t[key])}</p>')
        if t['user_words']:
            output.append('<p class="quote">' + text('\n'.join(t['user_words'])) + '</p>')
        output.append('</details>')
        output.append('</div></article>')
    output.append('</div><h2>回归</h2><div id="regressions"><div class="reg-head"><span>编号</span><span>名称</span><span>覆盖的待办</span><span>选择</span></div>')
    for r in data['regressions']:
        id_ = r['id']
        pick = '<span class="pro-pick">GPT Pro 推荐先做</span>' if r.get('pro_pick') else ''
        output.append(f'<article class="entry" id="reg-{id_}" data-regression="{id_}"><div class="reg-row"><span class="id">{link(id_)}</span><div><div class="name">{text(r["name"])}</div>{pick}</div><div class="coverage">{pills(r["covers"])}</div><div><div class="segments" role="group" aria-label="{id_} 选择">')
        for v in ('0.1', '0.2', '搁置'):
            output.append(f'<button data-group="regressions" data-id="{id_}" data-value="{v}" aria-pressed="false">{v}</button>')
        output.append(f'</div><button class="toggle" data-detail="detail-{id_}" aria-expanded="false" aria-controls="detail-{id_}" aria-label="展开 {id_}">⌄</button></div></div><div class="detail" id="detail-{id_}" hidden>')
        output.append(block('场景：', r['scenario'], 'reg-scenario'))
        output.append('<div class="assessment-block reg-environment"><strong>环境：</strong>')
        for label in ('模型', '端', '插件', '附件', '网络'):
            output.append(f'<div><b>{label}：</b><span data-environment="{label}">{text(r["environment"][label])}</span></div>')
        output.append('</div><div class="prompt-section"><strong>Prompt</strong>')
        turns = prompts.get(id_, [])
        if not any(turn.get('prompt', '').strip() for turn in turns):
            output.append('<p class="small prompt-empty">尚未设计 prompt</p>')
        else:
            for turn in turns:
                conversation = turn['conversation']
                position = {'new': '新对话', 'continue': '接着上一轮',
                            'branch': f'从第 {conversation.get("after_turn")} 轮分支'}[conversation['mode']]
                output.append(f'<details class="prompt-turn"><summary>第 {turn["n"]} 轮 · {position}</summary>')
                if turn.get('prompt', '').strip():
                    output.append(f'<pre class="prompt-text"><code>{text(turn["prompt"])}</code></pre>')
                else:
                    output.append('<p class="small prompt-empty">本轮 prompt 待补</p>')
                output.append('</details>')
        output.append('</div><div class="reg-criteria assessment-block"><strong>怎么判：</strong>')
        for kind, label in [('failure_condition', '出现即失败'), ('requirement', '通过时必须有')]:
            output.append(f'<div class="criteria-group" data-kind="{kind}"><b>{label}</b><ul>')
            for criterion in r['criteria']:
                if criterion['kind'] == kind:
                    output.append('<li>' + text(criterion['text']) + '</li>')
            output.append('</ul></div>')
        output.append('</div>' + block('为什么放进 0.1：', r['why_01'], 'reg-why'))
        output.append('<p class="path">' + '<br>'.join(text(path) for path in (r['case_source'], r['pro_source'])) + '</p></div></article>')
    output.append('</div>')
    return ''.join(output)


TEMPLATE = r'''<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>__TITLE__</title><style>
@font-face{font-family:'Noto Sans SC Local';src:url('__FONT__') format('truetype');font-weight:100 900;font-display:swap}
*{box-sizing:border-box}body{margin:0;background:#fafafa;color:#202020;font:15px/1.6 'Noto Sans SC','Noto Sans SC Local',sans-serif}main{max-width:1100px;margin:44px auto 80px}h1{font-size:30px;line-height:1.4;margin:0 0 8px}h2{font-size:21px;margin:38px 0 16px}a{color:inherit;text-underline-offset:3px}a:hover{text-decoration-thickness:2px}.updated{margin:0 0 24px;font-size:13px;color:#707070}.cards{display:grid;grid-template-columns:repeat(6,minmax(0,1fr));gap:12px}.card{background:white;border:1px solid #ddd;border-radius:8px;padding:15px 16px;min-height:132px}a.card{display:block;text-decoration:none}a.card:hover{border-color:#888}#actions p{margin:10px 0}#rewrite-todos{scroll-margin-top:22px}.number{font-size:30px;line-height:1.35;font-weight:700;margin-bottom:6px}.small{font-size:12px;color:#707070;margin-top:5px;overflow-wrap:anywhere}.zero{color:#888}.danger{color:#b42318}.attention{color:#9a6700}.tree{border:1px solid #ddd;border-radius:8px;background:white;padding:22px 26px;margin-bottom:22px}.tree ul{list-style:none;padding-left:22px;border-left:1px solid #ddd}.tree li{margin:12px 0}.tree li li{margin:5px 0;font-size:13px}.tree .description{color:#555;font-size:13px;max-width:800px;margin:3px 0 10px}.source-file{background:white;border:1px solid #ddd;border-radius:6px;margin-bottom:10px;scroll-margin-top:20px}.source-file>summary{padding:14px 18px;cursor:pointer;font-size:12px;overflow-wrap:anywhere}.file-path{font-family:monospace}.file-todos{display:block;margin:6px 0 0 16px;color:#777}.source-lines{border-top:1px solid #ddd;padding:12px 0}.source-line{display:grid;grid-template-columns:125px 38px minmax(0,1fr);position:relative;padding:2px 16px 2px 8px;min-height:24px}.source-text{white-space:pre-wrap;overflow-wrap:anywhere;font:11.5px/1.8 ui-monospace,SFMono-Regular,Consolas,monospace}.line-number{font:11px/2 monospace;color:#888;text-align:right;padding-right:12px;user-select:none}.line-todos{display:flex;flex-wrap:wrap;align-content:start}.highlighted{background:#fff9e5}.rule-anchor{position:absolute;top:0;scroll-margin-top:24px}.source-line.flashing{animation:rule-flash .5s ease-in-out 3}@keyframes rule-flash{0%,100%{box-shadow:inset 4px 0 #b79b52;background:#fff4d6}50%{box-shadow:inset 4px 0 #333;background:#ead79c}}.entry{background:white;border:1px solid #ddd;border-radius:7px;margin-bottom:10px;scroll-margin-top:22px}.todo-row{display:grid;grid-template-columns:40px minmax(0,1fr) 155px 130px 26px;gap:12px;padding:17px 16px;align-items:start}.id{font-size:12px;color:#777;white-space:nowrap}.todo-need,.name{font-weight:700}.pill{display:inline-block;padding:1px 6px;border:1px solid #ddd;border-radius:12px;font-size:12px;color:#444;background:#fafafa;margin:2px 3px 2px 0;text-decoration:none}.pill:hover{border-color:#555;text-decoration:underline}.assessment-status{display:inline-block;border-radius:12px;padding:2px 9px;font-size:12px;white-space:nowrap}.assessment-labels{display:flex;flex-wrap:wrap;align-items:center;gap:5px 7px}.assessment-change-summary{font-size:12px;color:#777;overflow-wrap:anywhere}.assessment-status.appropriate{color:#1a7f37;background:#e6f4ea}.assessment-status.insufficient{color:#9a6700;background:#fff4d6}.assessment-status.excessive{color:#b42318;background:#fde8e8}.rule-location{display:block;color:#9a6700;font-size:12px;margin-top:5px}.tag{display:inline-block;font-size:11px;line-height:1.8;padding:0 6px;border-radius:4px;background:#eee;color:#555;margin-top:5px}.tag.new{background:#e0ecff;color:#1d4ed8}button{font:inherit;cursor:pointer;color:#333;background:white;border:1px solid #ccc;border-radius:4px;padding:5px 10px}button:focus-visible,a:focus-visible,summary:focus-visible{outline:2px solid #333;outline-offset:3px}.toggle{border:0;background:none;font-size:17px;padding:0 3px;color:#666}.detail{padding:22px;background:#fafafa;border-top:1px solid #ddd}.detail[hidden]{display:none}.detail p{margin:12px 0}.assessment-block{margin-bottom:16px}.assessment-block strong{display:block;margin-bottom:4px}.assessment-text,.quote,.source{white-space:pre-wrap;overflow-wrap:anywhere}.assessment-rule-quote{border-left:2px solid #ddd;padding-left:12px;font-size:9.5pt;color:#555}.assessment-proposal,.quote{border-left:2px solid #2563eb;padding-left:12px}.assessment-rule-id,.todo-meta,.path{color:#777;font-size:12px;overflow-wrap:anywhere}.assessment-rule-id{margin:-8px 0 16px}.todo-meta{margin-top:18px}.todo-original{margin-top:14px}.todo-original summary{cursor:pointer;color:#555}.source{border-left:2px solid #ddd;padding-left:12px;font-size:13px;color:#777}.known-note{margin-top:14px}.reg-row,.reg-head{display:grid;grid-template-columns:32px 142px minmax(0,1fr) minmax(0,1fr) 106px 138px;gap:12px;padding:17px 16px;font-size:13px;overflow-wrap:anywhere}.reg-head{font-size:12px;color:#777;padding-top:0;padding-bottom:9px}.segments{display:inline-flex;border:1px solid #ccc;border-radius:5px;overflow:hidden;white-space:nowrap}.segments button{font-size:12px;border:0;border-right:1px solid #ddd;border-radius:0;padding:5px 8px;line-height:1.5}.segments button:last-child{border:0}.segments button[aria-pressed=true][data-value="0.1"]{color:white;background:#252525}.segments button[aria-pressed=true][data-value="0.2"]{background:#e6e6e6}.segments button[aria-pressed=true][data-value="搁置"]{text-decoration:line-through;color:#777}.check{padding:12px 0;border-bottom:1px solid #ddd;display:flex;gap:16px}.check-status{min-width:70px;font-weight:600}.check-result{flex:1;overflow-wrap:anywhere}#offline{background:#fff3cd;border:1px solid #e4cf84;color:#65521a;padding:12px 16px;margin:0 0 24px;border-radius:5px;display:flex;justify-content:space-between;align-items:center;gap:20px}#offline[hidden],#saved[hidden]{display:none}#saved{position:fixed;top:18px;right:24px;background:white;border:1px solid #ddd;border-radius:5px;padding:5px 12px;z-index:2}.entry.shelved{background:#f1f1f1;border-color:#e2e2e2}.entry.shelved .reg-row>*:not(:last-child){text-decoration:line-through;text-decoration-thickness:1.5px;color:#999}#back-top{position:fixed;bottom:18px;right:18px;background:white;border:1px solid #ccc;border-radius:5px;padding:7px 12px;font-size:12px;text-decoration:none;z-index:2}
@media(max-width:1150px){main{margin:28px 20px 60px}}@media(max-width:760px){main{margin:22px 16px 70px}h1{font-size:25px}.cards{grid-template-columns:repeat(2,minmax(0,1fr));gap:8px}.card{min-height:108px;padding:12px}.number{font-size:27px}.tree{padding:16px}.tree ul{padding-left:15px}.source-file>summary{padding:12px}.source-line{grid-template-columns:65px 28px minmax(0,1fr);padding-right:9px;padding-left:4px}.line-number{padding-right:6px}.line-todos .pill{font-size:10px;padding:0 4px}.todo-row{grid-template-columns:32px minmax(0,1fr) 22px;gap:9px;padding:14px 12px}.todo-row>.id{grid-column:1;grid-row:1}.todo-need{grid-column:2;grid-row:1}.todo-row>div:not(.coverage){grid-column:2;grid-row:2}.todo-row>.coverage{grid-column:2;grid-row:3}.todo-row>.toggle{grid-column:3;grid-row:1}.detail{padding:16px}.reg-head{display:none}.reg-row{grid-template-columns:30px minmax(0,1fr);gap:12px;padding:14px 12px}.reg-row>div{grid-column:2}.reg-row>.id{grid-column:1;grid-row:1}.reg-row .test-text:before{content:'测什么';display:block;font-weight:700;margin-bottom:4px}.reg-row .judgment:before{content:'怎么判';display:block;font-weight:700;margin-bottom:4px}.file-todos{margin-left:0}}
.todo-row{grid-template-columns:32px minmax(0,1fr) 190px 98px 194px 22px}.todo-stance button{padding:5px 10px}.todo-stance button[aria-pressed=true]{background:#252525;color:white}.todo-note{padding:0 16px 16px}.todo-note[hidden]{display:none}.todo-note textarea{display:block;width:100%;resize:vertical;min-height:90px;border:1px solid #ccc;border-radius:5px;padding:10px;font:inherit;line-height:1.6}.prompt-section>strong{display:block;margin-bottom:10px}.prompt-turn{border:1px solid #ddd;border-radius:5px;background:white;margin:8px 0}.prompt-turn>summary{padding:10px 12px;cursor:pointer;font-size:13px}.prompt-text{white-space:pre-wrap;overflow-wrap:anywhere;user-select:text;font:12px/1.8 ui-monospace,SFMono-Regular,Consolas,monospace;padding:12px;margin:0;border-top:1px solid #ddd}.prompt-turn .prompt-empty{padding:0 12px}
@media(max-width:760px){.todo-row{grid-template-columns:32px minmax(0,1fr) 22px}.todo-row>.todo-stance{grid-column:2;grid-row:4;justify-self:start}}
.todo-stance{justify-self:start}
.pro-badge{color:#7c3aed;font-size:12px}.pro-opinion{border-left:2px solid #7c3aed;padding-left:12px;white-space:pre-wrap;overflow-wrap:anywhere}.pro-opinion h4{font-size:15px;margin:14px 0 8px}.pro-opinion p{margin:10px 0}.pro-opinion blockquote{margin:10px 0;padding-left:12px;border-left:2px solid #ddd}.pro-pick{display:inline-block;border-radius:12px;background:#f3edff;color:#7c3aed;font-size:12px;padding:2px 9px;margin-top:6px}.reg-row,.reg-head{grid-template-columns:32px minmax(0,1fr) 180px 155px}.reg-environment>div{margin:5px 0}.reg-criteria{margin-top:20px}.criteria-group{margin-top:12px}.criteria-group ul{padding-left:22px;margin:6px 0}.criteria-group li{margin:7px 0}.entry.merged{background:#f1f1f1;border-color:#ddd;color:#888}.entry.merged .todo-row *{color:#888}.entry.merged .assessment-status{background:#e5e5e5}.entry.merged button{cursor:default}.entry.merged .detail{color:#777}
@media(max-width:760px){.reg-row{grid-template-columns:30px minmax(0,1fr)}.reg-row>div{grid-column:2}}
</style></head><body><main id="top">
<div id="offline" role="status" hidden><span>未连接本地服务，选择只存在本浏览器</span><button id="export">导出选择</button></div>
<h1>__TITLE__</h1><p class="updated">更新于 __TIME__</p>
__BODY__
</main><div id="saved" role="status" hidden>已保存</div><a id="back-top" href="#top">回到顶部</a>
<script id="blueprint-data" type="application/json">__DATA__</script>
<script id="decisions-data" type="application/json">__DECISIONS__</script>
<script>
'use strict';
const data=JSON.parse(document.getElementById('blueprint-data').textContent);
const storageKey='plugin-blueprint:'+data.plugin;
const normalize=value=>({regressions:Object.fromEntries(data.regressions.map(r=>[r.id,[null,'0.1','0.2','搁置'].includes(value?.regressions?.[r.id])?value.regressions[r.id]:null])),todos:Object.fromEntries(data.todos.map(t=>{const v=value?.todos?.[t.id];return [t.id,{stance:[null,'同意','不同意','有疑问'].includes(v?.stance)?v.stance:null,note:typeof v?.note==='string'?v.note:''}];}))});
let decisions=normalize(JSON.parse(document.getElementById('decisions-data').textContent));
let online=false,saveQueue=Promise.resolve(),savedTimer,flashTimer;
const noteTimers=new Map();
function updateChoices(){
 document.querySelectorAll('button[data-value]').forEach(b=>b.setAttribute('aria-pressed',String((b.dataset.group==='todos'?decisions.todos[b.dataset.id].stance:decisions.regressions[b.dataset.id])===b.dataset.value)));document.querySelectorAll('[data-regression]').forEach(e=>e.classList.toggle('shelved',decisions.regressions[e.dataset.regression]==='搁置'));
 document.querySelectorAll('textarea[data-note]').forEach(input=>{const value=decisions.todos[input.dataset.note];document.getElementById('note-'+input.dataset.note).hidden=!['不同意','有疑问'].includes(value.stance)||(data.todos.find(t=>t.id===input.dataset.note).merged_into&&document.getElementById('detail-'+input.dataset.note).hidden);if(input.value!==value.note)input.value=value.note;});
 document.querySelector('[data-card="4"]').textContent=Object.values(decisions.regressions).filter(v=>v==='0.1').length;
 document.getElementById('selected-count').textContent=Object.values(decisions.regressions).filter(v=>v!==null).length;
 const stances=data.todos.filter(t=>!t.merged_into).map(t=>decisions.todos[t.id].stance);
 document.getElementById('stance-count').textContent=stances.filter(v=>v!==null).length;
 document.getElementById('disagree-count').textContent=stances.filter(v=>v==='不同意').length;
 document.getElementById('question-count').textContent=stances.filter(v=>v==='有疑问').length;
}
function openDetail(id){const d=document.getElementById('detail-'+id),b=document.querySelector('[data-detail="detail-'+id+'"]');if(d&&b){d.hidden=false;b.setAttribute('aria-expanded','true');b.textContent='⌃';updateChoices();}}
function followHash(restore=true){
 const target=document.getElementById(decodeURIComponent(location.hash.slice(1)));if(!target)return;
 const file=target.closest('.source-file');if(file)file.open=true;
 const entry=target.closest('.entry');if(entry)openDetail(entry.dataset.todo||entry.dataset.regression);
 const position=restore&&history.state?.blueprintPosition;
 const previous=position&&document.getElementById(position.id);
 if(previous)window.scrollBy(0,previous.getBoundingClientRect().top-position.offset);
 else target.scrollIntoView({block:'start'});
 document.querySelectorAll('.flashing').forEach(e=>e.classList.remove('flashing'));clearTimeout(flashTimer);
 if(target.matches('.rule-anchor')){
  const start=Number(target.dataset.start),end=Number(target.dataset.end);
  const lines=[...file.querySelectorAll('.source-line')].filter(e=>Number(e.dataset.line)>=start&&Number(e.dataset.line)<=end);
  void target.offsetWidth;lines.forEach(e=>e.classList.add('flashing'));
  flashTimer=setTimeout(()=>lines.forEach(e=>e.classList.remove('flashing')),1500);
 }
}
window.addEventListener('hashchange',()=>followHash());
// Save the viewport relative to an element: opening a file changes page height.
document.addEventListener('click',e=>{
 const anchor=e.target.closest('a[href^="#"]');if(!anchor||anchor.hash===location.hash)return;
 let current=document.getElementById(location.hash.slice(1));
 if(!current){current=[...document.querySelectorAll('.entry,.source-file,#top')].filter(e=>e.getClientRects().length).sort((a,b)=>Math.abs(a.getBoundingClientRect().top)-Math.abs(b.getBoundingClientRect().top))[0];}
 if(current)history.replaceState({...history.state,blueprintPosition:{id:current.id,offset:current.getBoundingClientRect().top}},'');
},true);
document.addEventListener('click',e=>{
 const anchor=e.target.closest('a[href^="#"]');
 if(anchor){e.stopPropagation();if(anchor.getAttribute('href')===location.hash){e.preventDefault();followHash(false);}return;}
 const toggle=e.target.closest('[data-detail]');
 if(toggle){const detail=document.getElementById(toggle.dataset.detail);detail.hidden=!detail.hidden;toggle.setAttribute('aria-expanded',String(!detail.hidden));toggle.textContent=detail.hidden?'⌄':'⌃';updateChoices();return;}
 const button=e.target.closest('button[data-value]');if(!button)return;
 const {group,id,value}=button.dataset;
 if(group==='todos'){const current=decisions.todos[id];current.stance=current.stance===value?null:value;clearTimeout(noteTimers.get(id));noteTimers.delete(id);}
 else decisions.regressions[id]=decisions.regressions[id]===value?null:value;
 updateChoices();persist(group,id);
});
document.addEventListener('input',e=>{const input=e.target.closest('textarea[data-note]');if(!input)return;const id=input.dataset.note;decisions.todos[id].note=input.value;localSave();clearTimeout(noteTimers.get(id));noteTimers.set(id,setTimeout(()=>{noteTimers.delete(id);persist('todos',id);},1000));});
function persist(group,id){
 localSave();const value=structuredClone(decisions[group][id]);
 saveQueue=saveQueue.then(async()=>{if(online){try{await request('api/decisions',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({group,id,value})});clearTimeout(savedTimer);document.getElementById('saved').hidden=false;savedTimer=setTimeout(()=>document.getElementById('saved').hidden=true,2000);}catch{offline();localSave();}}});
}
// Links inside a file summary navigate without toggling that file closed.
document.querySelectorAll('.source-file>summary a').forEach(a=>a.addEventListener('click',e=>{e.preventDefault();if(a.hash===location.hash)followHash(false);else location.hash=a.hash;}));
function offline(){online=false;document.getElementById('offline').hidden=false;}
function localSave(){try{localStorage.setItem(storageKey,JSON.stringify(decisions));}catch{}}
async function request(url,options={}){const controller=new AbortController(),timer=setTimeout(()=>controller.abort(),2000);try{const response=await fetch(url,{...options,signal:controller.signal});if(!response.ok)throw Error(response.status);return await response.json();}finally{clearTimeout(timer);}}
document.getElementById('export').addEventListener('click',()=>{
 const blob=new Blob([JSON.stringify(decisions,null,2)+'\n'],{type:'application/yaml;charset=utf-8'}),link=document.createElement('a');link.href=URL.createObjectURL(blob);link.download='decisions.yaml';link.click();setTimeout(()=>URL.revokeObjectURL(link.href),1000);
});
function restoreLocal(){try{decisions=normalize(JSON.parse(localStorage.getItem(storageKey))??decisions);localSave();}catch{}}
updateChoices();
window.blueprintReady=(async()=>{
 if(location.protocol==='file:'){offline();restoreLocal();}else{try{const result=await request('api/decisions');if(result.plugin!==data.plugin)throw Error('plugin');decisions=normalize(result.decisions);online=true;localSave();}catch{offline();restoreLocal();}}
 updateChoices();followHash();
})();
</script></body></html>'''


def build(path, checks=None):
    from check_blueprint import check_data, check_html_ids, check_visible_language
    path = Path(path).resolve()
    data = load(path)
    decisions_file = path.with_name("decisions.yaml")
    previous = load(decisions_file) if decisions_file.exists() else {}
    decisions = normalize_decisions(data, previous)
    if not decisions_file.exists() or previous != decisions:
        write_yaml(decisions_file, decisions)
    files = source_files(data, repo_root())
    prompts, prompt_sources = regression_prompts(data, repo_root())
    checks = list(checks if checks is not None else check_data(data, repo_root()))
    json_text = lambda value: json.dumps(value, ensure_ascii=False).replace("<", "\\u003c")
    values = {"TITLE": html.escape(data["title"]), "FONT": html.escape(data.get("font", "NotoSansSC.ttf"), quote=True),
              "TIME": datetime.now().astimezone().isoformat(timespec="seconds"),
              "BODY": render_body(data, files, prompts), "DATA": json_text(data),
              "DECISIONS": json_text(decisions)}
    def output():
        return re.sub(r"__(TITLE|FONT|TIME|BODY|DATA|DECISIONS|CHECKS)__", lambda m: values[m[1]], TEMPLATE)
    # Scan the actual generated HTML, excluding scripts/styles and attributes.
    scan = check_html_ids(output())
    checks.append(scan)
    checks.append(check_visible_language(output(), decisions))
    destination = path.with_name("index.html")
    destination.write_text(output(), encoding="utf-8")
    report = path.parent / 'previews/self-check.json'
    report.parent.mkdir(exist_ok=True)
    write_yaml(report, {'mechanical_checks': checks, 'prompt_sources': prompt_sources})
    return destination


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("blueprint", type=Path)
    print(build(parser.parse_args().blueprint))
