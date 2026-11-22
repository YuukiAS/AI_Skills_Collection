#!/usr/bin/env python3
"""Check source identity and declared coverage, then refresh index.html."""
import argparse
import json
import re
from html.parser import HTMLParser
from pathlib import Path

BASE = Path(__file__).resolve().parent


def coverage_rows(path):
    section = path.read_text(encoding="utf-8").split("## 1.", 1)[1].split("## 2.", 1)[0]
    rows = []
    for line in section.splitlines():
        if re.match(r"\|\s*\d+[–-]\d+\s*\|", line):
            cells = [s.strip() for s in line.strip().strip("|").split("|")]
            rows.append({"lines": cells[0], "title": cells[1], "problem": cells[2],
                         "layer": cells[4].split("；", 1)[0].removeprefix("主：")})
    return rows


def check_data(data, root):
    expected = coverage_rows(root / data["sources"]["coverage"])
    todos = [t for t in data["todos"] if not t.get("supplement")]
    mismatches = []
    for i, row in enumerate(expected, 1):
        matches = [t for t in todos if t["id"] == f"T{i:02}"]
        if len(matches) != 1 or any(matches[0].get(k) != v for k, v in row.items()):
            mismatches.append(f"T{i:02}")
    ok = len(todos) == len(expected) and not mismatches
    first = {"status": "通过" if ok else "不通过",
             "result": f"待办逐条对应：{len(todos)} / {len(expected)}。" + ("差异：" + "、".join(mismatches) if not ok else "")}
    missing = []
    for rule in data["rules"]:
        path = root / rule["file"]
        if not rule["first_sentence"] or not path.is_file() or rule["first_sentence"] not in path.read_text(encoding="utf-8"):
            missing.append(f'{rule["id"]}@{rule["file"]}')
    second = {"status": "不通过" if missing else "通过",
              "result": ("规则原文未找到：" + "、".join(missing)) if missing else f'规则第一句逐字存在：{len(data["rules"])} / {len(data["rules"])} 个文件位置。'}
    covered = {id_ for r in data["regressions"] for id_ in r["covers"]}
    uncovered = [t["id"] for t in data["todos"] if t["id"] not in covered]
    unknown = sorted(covered - {t["id"] for t in data["todos"]})
    third = {"status": "不通过" if uncovered or unknown else "通过",
             "result": "未被任何回归覆盖的待办：" + ("、".join(uncovered) if uncovered else "无") + "。" + ("未知待办编号：" + "、".join(unknown) if unknown else "")}
    fourth = {"status": "待下一轮", "result": "已选 0.1 的待办，其目标规则写在 skill 正文。"}
    fields = {"by", "need", "case", "status", "change", "rule_id", "rule_quote", "why", "proposal"}
    assessed = all(isinstance(t.get("assessment"), dict) and fields <= t["assessment"].keys()
                   and all(isinstance(t["assessment"][key], str) and t["assessment"][key] for key in fields)
                   for t in data["todos"])
    assessment = {"status": "通过" if assessed else "不通过",
                  "result": "每条待办都有 assessment：" + ("是" if assessed else "否") + "。"}
    invalid_assessments = []
    for todo in data["todos"]:
        a = todo.get("assessment")
        a = a if isinstance(a, dict) else {}
        changes = a.get("change")
        changes = [c.strip() for c in changes.split("；")] if isinstance(changes, str) else []
        if (a.get("status") not in ("约束不足", "约束适当", "约束过度")
                or not changes or any(c not in ("不改", "只改措辞", "补充", "重写", "挪进正文") for c in changes)
                or (a.get("status") == "约束适当" and any(c not in ("不改", "只改措辞", "挪进正文") for c in changes))):
            invalid_assessments.append(todo["id"])
    assessment_values = {"status": "不通过" if invalid_assessments else "通过",
                         "result": "assessment.status / assessment.change：" + ("、".join(invalid_assessments) if invalid_assessments else "通过") + "。"}
    from build_blueprint import regression_prompts, load
    turns, sources = regression_prompts(data, root)
    incomplete = [r["id"] for r in data["regressions"]
                  if not str(r.get("scenario") or "").strip()
                  or not any(t.get('prompt', '').strip() for t in turns[r['id']])
                  or not any(c.get('text', '').strip() for c in r.get('criteria', []))]
    regression = {"status": "不通过" if incomplete else "通过",
                  "result": "回归场景、Prompt、判定标准非空：" + ("、".join(incomplete) if incomplete else f'{len(data["regressions"])} / {len(data["regressions"])}') + "。"}
    from build_blueprint import source_files, rule_ids
    available = {r["id"] for f in source_files(data, root) for r in f["rules"]}
    missing_paragraphs = [f'{t["id"]} → {id_}' for t in data["todos"] for id_ in rule_ids(t) if id_ not in available]
    paragraphs = {"status": "不通过" if missing_paragraphs else "通过",
                  "result": "待办 rule_id 对应原文段落：" + ("、".join(missing_paragraphs) if missing_paragraphs else "全部找到") + "。"}
    from build_blueprint import regression_prompts
    _, sources = regression_prompts(data, root)
    unmatched = [s['id'] for s in sources if not s['matched']]
    prompts = {'status': '不通过' if unmatched else '通过',
               'result': '回归 prompt 案例对应：' + ('、'.join(unmatched) if unmatched else '全部找到') + '。'}
    source_errors = []
    for r in data['regressions']:
        case = load(root / r['case_source'])
        for field, key in [('name', 'name'), ('scenario', 'scenario'), ('criteria', 'criteria'),
                           ('why_01', 'why_v0_1'), ('pro_pick', 'top_three'), ('covers', 'coverage')]:
            if r.get(field) != case[key]:
                source_errors.append(f'{r["id"]}.{field}')
        if r['environment'] != {'模型': case['model'], **case['environment']}:
            source_errors.append(r['id'] + '.environment')
        review = (root / r['pro_source']).read_text()
        if r['name'] not in review or r['scenario'] not in review or r['why_01'] not in review:
            source_errors.append(r['id'] + '.review')
    review = (root / data['regressions'][0]['pro_source']).read_text()
    expected_pro = {t['id']: [] for t in data['todos']}
    for section in re.split(r'(?m)^## [23]\. ', review)[1:]:
        for chunk in re.split(r'(?m)(?=^### )', section)[1:]:
            chunk = chunk.strip()
            title = chunk.split('\n', 1)[0]
            ids = re.findall(r'\b(?:T\d+|U\d+)\b', title)
            if 'T14' in ids and 'T13' not in ids:
                ids.append('T13')
            for id_ in ids:
                expected_pro[id_].append(chunk)
    for t in data['todos']:
        if t.get('pro') != '\n\n'.join(expected_pro[t['id']]):
            source_errors.append(t['id'] + '.pro')
        if t.get('merged_into') != {'T14': 'T13', 'U1': 'T01'}.get(t['id']):
            source_errors.append(t['id'] + '.merged_into')
    pro_check = {'status': '不通过' if source_errors else '通过',
                 'result': 'GPT Pro 原文与合并关系：' + ('、'.join(source_errors) if source_errors else '全部对应') + '。'}
    return [first, assessment, assessment_values, second, third, fourth, regression, paragraphs, prompts, pro_check]


def check_visible_language(source, decisions=None):
    """Scan all reader prose, including foldouts, excluding file paths and code."""
    pattern = re.compile(r'(?<![A-Za-z0-9_])[A-Z][A-Z0-9]*(?:_[A-Z0-9]+)+(?![A-Za-z0-9_])|(?<![A-Za-z0-9-])[A-Za-z]+(?:-[A-Za-z]+){2,}(?![A-Za-z0-9-])')

    class Scan(HTMLParser):
        def __init__(self):
            super().__init__(convert_charrefs=True)
            self.stack, self.hits = [], []

        def handle_starttag(self, tag, attrs):
            attrs = dict(attrs)
            if tag not in {'meta', 'link', 'br', 'hr', 'input', 'img', 'wbr'}:
                self.stack.append((tag, attrs))

        def handle_endtag(self, tag):
            for i in range(len(self.stack) - 1, -1, -1):
                if self.stack[i][0] == tag:
                    del self.stack[i:]
                    break

        def handle_data(self, value):
            if any(tag in {'script', 'style', 'code', 'pre'} or
                   set(attrs.get('class', '').split()) & {'path', 'file-path'} for tag, attrs in self.stack):
                return
            # Paths may also occur within original quoted paragraphs.
            value = re.sub(r'(?:[A-Za-z0-9_.-]+/)+[A-Za-z0-9_./-]+', '', value)
            locator = next((a['id'] for _, a in reversed(self.stack) if 'id' in a), 'document')
            for match in pattern.finditer(value):
                self.hits.append({'text': match[0], 'location': locator, 'html_line': self.getpos()[0]})

    scan = Scan()
    scan.feed(source)
    for id_, value in (decisions or {}).get('todos', {}).items():
        note = re.sub(r'(?:[A-Za-z0-9_.-]+/)+[A-Za-z0-9_./-]+', '', value.get('note', ''))
        for match in pattern.finditer(note):
            scan.hits.append({'text': match[0], 'location': 'note-' + id_, 'source': 'decisions.yaml'})
    return {'status': '不通过' if scan.hits else '通过', 'hits': scan.hits, 'count': len(scan.hits),
            'result': f'可见文字扫描命中 {len(scan.hits)} 处。'}


def check_html_ids(source):
    from build_blueprint import ID_PATTERN

    class Scan(HTMLParser):
        def __init__(self):
            super().__init__(convert_charrefs=True)
            self.stack, self.errors, self.links, self.ids = [], [], [], []
            self.count = 0

        def handle_starttag(self, tag, attrs):
            attrs = dict(attrs)
            if "id" in attrs:
                self.ids.append(attrs["id"])
            if tag not in {"meta", "link", "br", "hr", "input", "img", "wbr"}:
                self.stack.append((tag, attrs.get("href", "")))

        def handle_endtag(self, tag):
            for i in range(len(self.stack) - 1, -1, -1):
                if self.stack[i][0] == tag:
                    del self.stack[i:]
                    break

        def handle_data(self, value):
            if any(tag in {"script", "style"} for tag, _ in self.stack):
                return
            for match in ID_PATTERN.finditer(value):
                id_ = match[0]
                expected = "#" + ("rule-" if "-" in id_ else "reg-" if id_.startswith("R") else "todo-") + id_
                self.count += 1
                if not any(tag == "a" and href == expected for tag, href in self.stack):
                    self.errors.append(id_)
                else:
                    self.links.append(expected[1:])

    scan = Scan()
    scan.feed(source)
    errors = scan.errors + [id_ for id_ in scan.links if id_ not in scan.ids]
    duplicates = len(scan.ids) != len(set(scan.ids))
    return {"status": "不通过" if errors or duplicates else "通过",
            "result": "页面编号链接：" + ("、".join(dict.fromkeys(errors)) if errors else f"{scan.count} / {scan.count}") + ("；重复锚点" if duplicates else "") + "。"}


if __name__ == "__main__":
    from build_blueprint import build, load, repo_root
    parser = argparse.ArgumentParser()
    parser.add_argument("plugin")
    args = parser.parse_args()
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", args.plugin):
        parser.error("invalid plugin")
    path = BASE / args.plugin / "blueprint.yaml"
    data = load(path)
    checks = check_data(data, repo_root())
    output = build(path, checks)
    checks.append(check_html_ids(output.read_text(encoding="utf-8")))
    checks.append(check_visible_language(output.read_text(encoding="utf-8"), load(path.with_name('decisions.yaml'))))
    for i, check in enumerate(checks, 1):
        print(f'{i}. {check["status"]}：{check["result"]}')
    raise SystemExit(1 if any(c["status"] == "不通过" for c in checks) else 0)
