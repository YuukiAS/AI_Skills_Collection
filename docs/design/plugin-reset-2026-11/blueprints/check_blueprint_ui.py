#!/usr/bin/env python3
"""Full source/DOM comparison and local/offline browser acceptance checks."""
import argparse
from copy import deepcopy
import hashlib
import json
import re
import sys
from pathlib import Path

import yaml
from playwright.sync_api import sync_playwright

from build_blueprint import BASE, initial_decisions, load, repo_root, regression_prompts, render_body
from check_blueprint import coverage_rows


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("plugin")
    parser.add_argument("--port", type=int, default=8765)
    parser.add_argument("--browser", default="/usr/bin/chromium-browser")
    args = parser.parse_args()
    directory = BASE / args.plugin
    output = directory / "previews"
    output.mkdir(exist_ok=True)
    data = load(directory / "blueprint.yaml")
    blueprint_hash = hashlib.sha256((directory / "blueprint.yaml").read_bytes()).hexdigest()
    original = initial_decisions(data)
    decisions_file = directory / "decisions.yaml"
    assert load(decisions_file) == original, "acceptance starts with initial decisions"
    initial_bytes = decisions_file.read_bytes()
    root = repo_root()
    todo_lines = (root / data["sources"]["todo"]).read_text().splitlines()
    rows = coverage_rows(root / data["sources"]["coverage"])
    expected_todos = []
    for number, row in enumerate(rows, 1):
        todo = next(t for t in data["todos"] if t["id"] == f"T{number:02}")
        for key in ("title", "problem", "lines", "layer"):
            assert todo[key] == row[key], (todo["id"], key)
        start, end = map(int, re.split("[–-]", row["lines"]))
        chunk = "\n".join(todo_lines[start - 1:end])
        # Independent paragraph extraction, without the extractor's regex.
        after = chunk.split("problem: ", 1)[1]
        paragraph = after.split("\n\n", 1)[0].split("\nproject-specific context:", 1)[0].rstrip("\n")
        assert todo["source_text"] == paragraph, todo["id"]
        for word, line in zip(todo["user_words"], todo["user_word_lines"], strict=True):
            assert start <= line <= end and word in todo_lines[line - 1], (todo["id"], word)
        expected_todos.append(todo)
    supplemental = [t for t in data["todos"] if t.get("supplement")]
    assert len(supplemental) == 1 and supplemental[0]["id"] == "U1"
    assert supplemental[0]["title"] == "默认必查中文和英文论坛"
    assert supplemental[0]["user_words"] == ["“我需要知道是否已经包含了所有我要求的问题都必须先搜论坛(中文的v2ex, nga, 英文的reddit等), 而不是每次都要我提醒搜论坛, 否则天天搜openai doc, arxiv这种”"]
    assert supplemental[0]["note"] == "待办第 10 行写的是“不能机械硬编码成固定站点清单”，与用户这次的要求不一致，留给后续裁决。"
    candidate_rows = {}
    for line in (root / data["sources"]["candidates"]).read_text().splitlines():
        if line.startswith("| Reasoned Decision |"):
            cells = [c.strip() for c in line.strip("|").split("|")]
            candidate_rows[cells[1].strip("`")] = cells[2]
    source_tests = {}
    for case in data["regressions"]:
        if case["source"] == "已有":
            source = yaml.safe_load((root / case["test_source"]).read_text())
            assert case["test"] == source["期望行为"]
            assert case["judgment"] == source["判定方式"]
            source_tests[case["id"]] = source["期望行为"]
        elif case["name"] in candidate_rows:
            assert case["test"] == candidate_rows[case["name"]]
            source_tests[case["id"]] = candidate_rows[case["name"]]
        else:
            assert case["id"] == "R4" and case["test"] and case["judgment"] and case["draft_by"]
            source_tests[case["id"]] = case["test"]  # v3 canonical draft is blueprint.yaml.
    expected_rule_positions = set()
    for source in (root / data["sources"]["skill_root"]).rglob("*"):
        if source.is_file() and source.suffix in (".md", ".yaml"):
            for n, line in enumerate(source.read_text().splitlines(), 1):
                match = re.match(r"- \*\*((?:JI|SD|TS)-\d+) ", line)
                if match:
                    expected_rule_positions.add((match[1], str(source.relative_to(root)), n))
    assert {(r["id"], r["file"], r["line"]) for r in data["rules"]} == expected_rule_positions
    from build_blueprint import source_files, rule_ids
    from check_blueprint import check_data, check_html_ids
    from urllib.request import Request, urlopen
    from urllib.error import HTTPError
    files = source_files(data, root)
    prompts, prompt_sources = regression_prompts(data, root)
    prompt_hashes = {s['path']: hashlib.sha256((root / s['path']).read_bytes()).hexdigest()
                     for s in prompt_sources if s['matched']}
    source_hashes = {f['path']: hashlib.sha256((root / f['path']).read_bytes()).hexdigest() for f in files}
    assert check_html_ids((directory / 'index.html').read_text())['status'] == '通过'
    assert all(c['status'] != '不通过' for c in check_data(data, root))
    # Validate the new enums and the restricted changes for an appropriate rule.
    for status, change, valid in [
            ('约束不足', '补充；挪进正文', True),
            ('约束过度', '重写', True),
            ('约束适当', '不改', True),
            ('约束适当', '只改措辞；挪进正文', True),
            ('未知', '不改', False),
            ('约束适当', '补充', False),
            ('约束适当', '重写；挪进正文', False),
            ('约束不足', '未知', False),
            ('约束不足', '补充；', False),
            ('约束不足', '', False)]:
        variant = deepcopy(data)
        variant['todos'][0]['assessment'].update(status=status, change=change)
        value_check = next(c for c in check_data(variant, root)
                           if c['result'].startswith('assessment.status / assessment.change：'))
        assert (value_check['status'] == '通过') == valid, (status, change)
    console_errors = []
    screenshots = []
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(executable_path=args.browser, headless=True,
                                             args=['--no-sandbox', '--disable-dev-shm-usage'])
        context = browser.new_context(viewport={'width': 1440, 'height': 1000}, accept_downloads=True)
        page = context.new_page()
        page.on('pageerror', lambda error: console_errors.append(str(error)))
        page.on('console', lambda msg: console_errors.append(msg.text) if msg.type == 'error' else None)
        url = f'http://127.0.0.1:{args.port}/'
        page.goto(url)
        page.evaluate('window.blueprintReady')
        page.evaluate('document.fonts.ready')
        assert page.url == url and page.title() == data['title']
        assert page.locator('h1').inner_text() == data['title']
        assert page.locator('.entry').count() == 24
        assert not page.locator('#offline').is_visible()
        assert page.evaluate('document.documentElement.scrollWidth <= window.innerWidth')
        assert page.evaluate('document.fonts.check(\'15px "Noto Sans SC Local"\')')
        assert page.locator('main').evaluate('e=>getComputedStyle(e).maxWidth') == '1100px'
        assert page.locator('body').evaluate('e=>getComputedStyle(e).fontSize') == '15px'
        assert page.locator('body').evaluate('e=>getComputedStyle(e).lineHeight') == '24px'
        assert page.locator('main>h2').all_text_contents() == ['插件结构与原文', '待办', '回归']
        assert page.locator('#all-rules, #skills, #checks, #checks-data').count() == 0
        assert page.locator('#todos .segments').count() == 17
        assert page.locator('#todos button[data-value][aria-pressed="true"]').count() == 0
        assert not re.search(r'(?<!\d)0\.[12](?!\d)', page.locator('#todos').text_content())
        assert page.locator('.source-file[open], .todo-original[open]').count() == 0
        assert page.locator('.check').count() == 0
        assert json.loads(page.locator('#blueprint-data').text_content()) == data
        assert page.locator('.description').all_text_contents() == [s['description'] for s in data['skills']]
        assert '待办 17 条（全部在 0.1 解决）' in page.locator('#cards').text_content()
        rewrite_todos = [t for t in data['todos'] if t['assessment']['status'] in ('约束不足', '约束过度')]
        insufficient = sum(t['assessment']['status'] == '约束不足' for t in data['todos'])
        excessive = sum(t['assessment']['status'] == '约束过度' for t in data['todos'])
        expected_cards = ['2', '17', '7', '0', '0', str(len(rewrite_todos))]
        assert page.locator('#cards .card').nth(5).locator('div').nth(1).inner_text() == f'约束不足 {insufficient} · 过度 {excessive}'
        assert page.locator('.number').all_text_contents() == expected_cards
        assert page.locator('[data-card="5"]').evaluate('e=>getComputedStyle(e).color') == 'rgb(154, 103, 0)'

        def shot(name, full=False):
            if name in {'first-screen-1440.png', 'todo-expanded-1440.png'}:
                page.screenshot(path=str(output / name), full_page=full)
                screenshots.append(name)

        shot('first-screen-1440.png')
        shot('full-1440.png', True)

        def check_home_navigation(tab):
            assert tab.locator('#actions h2').inner_text() == '你要做的'
            assert tab.locator('#actions>p').count() == 3
            assert tab.locator('#actions>p').first.inner_text() == '选 7 个回归的版本（0.1 / 0.2 / 搁置），已选 0 个 去选'
            assert tab.evaluate('''() => {
                const cards=document.getElementById('cards'), actions=document.getElementById('actions');
                return cards.nextElementSibling===actions && actions.nextElementSibling.textContent==='插件结构与原文';
            }''')
            assert tab.locator('#rewrite-todos').inner_text().startswith(f'约束不足或过度的 {len(rewrite_todos)} 条待办，下一轮由 GPT Pro 改写：')
            assert tab.locator('#rewrite-todos .pill').all_text_contents() == [t['id'] for t in rewrite_todos]
            for i, target in [(0, 'structure'), (1, 'todos'), (2, 'regressions'), (4, 'regressions'), (5, 'rewrite-todos')]:
                card = tab.locator('#cards .card').nth(i)
                assert card.get_attribute('href') == '#' + target
                # Click the card padding to exercise the whole card hit area.
                card.click(position={'x': 5, 'y': 5})
                tab.wait_for_function('hash=>location.hash===hash', arg='#' + target)
                assert abs(tab.locator('#' + target).bounding_box()['y']) < 50
            disabled = tab.locator('#cards .card').nth(3)
            assert disabled.evaluate('e=>e.tagName') == 'DIV'
            assert disabled.locator('a,button').count() == 0
            before_hash = tab.evaluate('location.hash')
            disabled.click()
            assert tab.evaluate('location.hash') == before_hash
            tab.locator('#actions a[href="#regressions"]').click()
            tab.wait_for_function('location.hash === "#regressions"')
            assert tab.locator('#todo-progress').inner_text() == '对 17 条待办的建议表态，已表态 0 条，其中不同意 0、有疑问 0 去表态'
            tab.locator('#todo-progress a').click()
            tab.wait_for_function('location.hash === "#todos"')
            for todo in rewrite_todos:
                capsule = tab.locator(f'#rewrite-todos a[href="#todo-{todo["id"]}"]')
                capsule.hover()
                assert capsule.get_attribute('title') == todo['assessment']['need']
                capsule.click()
                tab.wait_for_function('hash=>location.hash===hash', arg='#todo-' + todo['id'])
                tab.locator('#detail-' + todo['id']).wait_for(state='visible')
                assert tab.locator(f'#todo-{todo["id"]} .toggle').get_attribute('aria-expanded') == 'true'
            assert tab.evaluate('document.documentElement.scrollWidth <= innerWidth')
            tab.goto(url)
            tab.evaluate('window.blueprintReady')

        check_home_navigation(page)
        # Compare every source line, line number and expected highlight union.
        # Ranges end at the next blank line; a later rule owns its own lines.
        for f in files:
            details = page.locator(f'#{f["id"]}')
            assert not details.evaluate('e=>e.open')
            assert details.locator('.source-text').all_text_contents() == f['lines']
            assert details.locator('.line-number').all_text_contents() == [str(n) for n in range(1, len(f['lines']) + 1)]
            expected = [t['id'] for t in data['todos'] if any(r['id'] in rule_ids(t) for r in f['rules'])]
            assert details.locator('summary .pill').all_text_contents() == expected
            for n in range(1, len(f['lines']) + 1):
                row = details.locator(f'[data-line="{n}"]')
                owners = [r for r in f['rules'] if r['line'] <= n <= r['end']]
                owner = max(owners, key=lambda r: r['line'], default=None)
                active = bool(owner and owner['todos'])
                assert ('highlighted' in row.get_attribute('class')) == active
                badges = list(dict.fromkeys(t for r in f['rules'] if r['line'] == n for t in r['todos']))
                assert row.locator('.line-todos .pill').all_text_contents() == badges
        assert page.locator('.rule-anchor').count() == len(data['rules'])
        assert page.locator('.rule-anchor[id^="rule-"]').count() == len({r['id'] for r in data['rules']})

        # Full DOM fidelity, including all nine assessment fields.
        for todo in data['todos']:
            id_, a = todo['id'], todo['assessment']
            row = page.locator(f'#todo-{id_}')
            detail = page.locator(f'#detail-{id_}')
            assert row.locator('.todo-need').text_content() == a['need']
            assert row.locator('.assessment-status').text_content() == a['status']
            colors = row.locator('.assessment-status').evaluate('e=>[getComputedStyle(e).color,getComputedStyle(e).backgroundColor]')
            assert colors == {
                '约束不足': ['rgb(154, 103, 0)', 'rgb(255, 244, 214)'],
                '约束适当': ['rgb(26, 127, 55)', 'rgb(230, 244, 234)'],
                '约束过度': ['rgb(180, 35, 24)', 'rgb(253, 232, 232)'],
            }[a['status']]
            row.locator('.assessment-status').hover()
            assert row.locator('.assessment-status').get_attribute('title') == {
                '约束不足': '规则是可选的、覆盖太窄、太抽象或有漏洞，模型可以合法跳过',
                '约束适当': '已能起作用，内容不需要实质改动',
                '约束过度': '写得太死或绑定具体案例，会在其他正当场景误伤',
            }[a['status']]
            assert row.locator('.assessment-change-summary').text_content() == '改动：' + a['change']
            assert row.locator('.assessment-change-summary').evaluate('e=>getComputedStyle(e).color') == 'rgb(119, 119, 119)'
            assert row.locator('.assessment-change-summary').evaluate('e=>getComputedStyle(e).fontSize') == '12px'
            reference = any(r['id'] in rule_ids(todo) and r['location_type'] == '引用文件' for r in data['rules'])
            assert row.locator('.rule-location').count() == int(reference)
            assert row.locator('.coverage .pill').all_text_contents() == [r['id'] for r in data['regressions'] if id_ in r['covers']]
            row.locator('.toggle').click()
            assert detail.is_visible()
            assert detail.locator('.todo-title').text_content() == todo['title']
            for field in ('by', 'case', 'rule_quote', 'rule_id', 'why', 'change', 'proposal'):
                assert detail.locator('.assessment-' + field.replace('_', '-')).text_content() == a[field], (id_, field)
            assert detail.locator('.assessment-block>strong').all_text_contents() == ['案例：', '现在怎么写的：', '为什么：', '改动：', '建议改成：']
            assert not detail.locator('.todo-original').evaluate('e=>e.open')
            detail.locator('.todo-original>summary').click()
            for key, class_ in [('problem', 'problem'), ('source_text', 'source')]:
                if todo.get(key):
                    assert detail.locator('.' + class_).text_content() == todo[key]
            if todo['user_words']:
                assert detail.locator('.quote').text_content() == '\n'.join(todo['user_words'])
            else:
                assert detail.locator('.quote').count() == 0
            if todo.get('note'):
                assert detail.locator('.note').text_content() == todo['note']
            detail.locator('.todo-original>summary').click()
            row.locator('.toggle').click()
        assert page.locator('#detail-T14 .known-note').text_content() == '与 T13 的需求文字相同，待 GPT Pro 拆分'
        assert page.locator('#detail-U1 .known-note').text_content() == '与 T01 相同，U1 是用户原话'
        for case in data['regressions']:
            row = page.locator(f'#reg-{case["id"]}')
            assert row.locator('.test-text').text_content() == case['test']
            assert row.locator('.judgment').text_content() == case['judgment']
            if case.get('draft_by'):
                assert row.locator('.draft-by').text_content() == case['draft_by']
                assert row.locator('.draft-by').evaluate('e=>getComputedStyle(e).fontSize') == '12px'
            row.locator('.toggle').click()
            assert page.locator(f'#detail-{case["id"]}').is_visible()
            section = row.locator('.prompt-section')
            assert section.locator('strong').inner_text() == 'Prompt'
            turns = prompts[case['id']]
            if not any(t.get('prompt', '').strip() for t in turns):
                assert section.locator('.prompt-empty').inner_text() == '尚未设计 prompt'
                assert section.locator('.prompt-turn').count() == 0
            else:
                assert section.locator('.prompt-turn').count() == len(turns)
                for index, turn in enumerate(turns):
                    fold = section.locator('.prompt-turn').nth(index)
                    assert not fold.evaluate('e=>e.open')
                    fold.locator('summary').click()
                    if turn.get('prompt', '').strip():
                        assert fold.locator('.prompt-text').text_content() == turn['prompt']
                    else:
                        assert fold.locator('.prompt-empty').inner_text() == '本轮 prompt 待补'
            if case['id'] == 'R1':
                row.evaluate('e=>e.scrollIntoView({block:"start"})')
                shot('regression-prompt-1440.png')
            row.locator('.toggle').click()

        # Real clicks: todo -> source + 1.5s flash -> todo, with browser back.
        page.locator('#todo-T10 .id a').click()
        page.wait_for_function('location.hash === "#todo-T10" && !document.getElementById("detail-T10").hidden')
        shot('todo-expanded-1440.png')
        origin_top = page.locator('#todo-T10').bounding_box()['y']
        rule_link = page.locator('#detail-T10 .assessment-rule-id a').first
        rule_hash = rule_link.get_attribute('href')
        rule_link.click()
        page.wait_for_function('location.hash === "#rule-SD-06" && document.querySelectorAll(".flashing").length > 0')
        assert rule_hash == '#rule-SD-06'
        target = page.locator(rule_hash)
        file = target.locator('xpath=ancestor::details')
        assert file.evaluate('e=>e.open')
        assert 0 <= target.bounding_box()['y'] <= 50
        assert target.locator('xpath=..').evaluate('e=>getComputedStyle(e).animationDuration') == '0.5s'
        assert target.locator('xpath=..').evaluate('e=>getComputedStyle(e).animationIterationCount') == '3'
        shot('rule-flashing-1440.png')
        page.wait_for_timeout(1600)
        assert page.locator('.flashing').count() == 0
        file.evaluate('e=>e.scrollIntoView({block:"start"})')
        shot('source-highlight-1440.png')
        target.evaluate('e=>e.scrollIntoView({block:"start"})')
        source_y = page.evaluate('scrollY')
        target.locator('xpath=..').locator('a[href="#todo-T10"]').click()
        page.wait_for_function('location.hash === "#todo-T10"')
        assert page.locator('#detail-T10').is_visible()
        page.go_back()
        page.wait_for_function('location.hash === "#rule-SD-06"')
        assert file.evaluate('e=>e.open')
        assert abs(page.evaluate('scrollY') - source_y) < 5
        page.go_back()
        page.wait_for_function('location.hash === "#todo-T10"')
        assert page.locator('#detail-T10').is_visible()
        assert abs(page.locator('#todo-T10').bounding_box()['y'] - origin_top) < 5
        # Todo regression capsule expands its destination; regression -> todo.
        page.locator('#todo-T10 .coverage a[href="#reg-R5"]').click()
        page.wait_for_function('location.hash === "#reg-R5"')
        assert page.locator('#detail-R5').is_visible()
        page.locator('#reg-R4 .id a').click()
        page.wait_for_function('location.hash === "#reg-R4"')
        assert page.locator('#detail-R4').is_visible()
        page.locator('#reg-R4 .coverage a[href="#todo-T01"]').click()
        page.wait_for_function('location.hash === "#todo-T01"')
        assert page.locator('#detail-T01').is_visible()
        page.go_back()
        page.wait_for_function('location.hash === "#reg-R4"')
        assert page.locator('#detail-R4').is_visible()
        page.locator('#back-top').click()
        page.wait_for_function('location.hash === "#top"')
        assert page.evaluate('scrollY') < 50
        tree_link = page.locator('.tree a').first
        tree_hash = tree_link.get_attribute('href')
        tree_link.click()
        page.wait_for_function('hash => location.hash === hash', arg=tree_hash)
        assert page.locator(tree_hash).evaluate('e=>e.open')
        page.locator(tree_hash + ' summary .pill').first.click()
        page.wait_for_function('location.hash === "#todo-T07"')
        assert page.locator('#detail-T07').is_visible()
        assert page.locator(tree_hash).evaluate('e=>e.open')
        # Direct deep links open the file even in a fresh browser page.
        deep = context.new_page()
        deep.goto(url + '#rule-SD-06')
        deep.evaluate('window.blueprintReady')
        assert deep.locator('#rule-SD-06').locator('xpath=ancestor::details').evaluate('e=>e.open')
        deep.close()
        # All visible and collapsed IDs must be links with existing destinations.
        assert check_html_ids(page.content())['status'] == '通过'
        assert page.evaluate('''() => [...document.querySelectorAll('a[href^="#"]')].every(a=>document.getElementById(a.hash.slice(1)))''')

        # Persist regression choices; legacy todo version writes remain invalid.
        for id_, value in [('R1', '0.1'), ('R2', '搁置')]:
            page.locator(f'[data-id="{id_}"][data-value="{value}"]').click()
        page.evaluate('saveQueue')
        persisted = load(decisions_file)
        assert set(persisted) == {'regressions', 'todos'}
        assert persisted['regressions']['R1'] == '0.1' and persisted['regressions']['R2'] == '搁置'
        assert page.locator('[data-card="4"]').inner_text() == '1'
        assert page.locator('#selected-count').inner_text() == '2'
        assert page.locator('#saved').is_visible()
        page.wait_for_timeout(2200)
        assert not page.locator('#saved').is_visible()
        rejected = Request(url + 'api/decisions', data=json.dumps({'group': 'todos', 'id': 'T03', 'value': '0.2'}).encode(), headers={'Content-Type': 'application/json'})
        try:
            urlopen(rejected)
            raise AssertionError('legacy todo version writes must fail')
        except HTTPError as error:
            assert error.code == 400
        assert load(decisions_file) == persisted
        page.reload()
        page.evaluate('window.blueprintReady')
        assert page.locator('#selected-count').inner_text() == '2'
        for id_, value in [('R1', '0.1'), ('R2', '搁置')]:
            assert page.locator(f'[data-id="{id_}"][data-value="{value}"]').get_attribute('aria-pressed') == 'true'
            page.locator(f'[data-id="{id_}"][data-value="{value}"]').click()
        page.evaluate('saveQueue')
        assert load(decisions_file) == original
        assert decisions_file.read_bytes() == initial_bytes
        assert page.locator('#selected-count').inner_text() == '0'

        # Stance controls, one-second debounce, multiline note, reload and retention.
        choice = page.locator('#todo-T01')
        note = choice.locator('textarea')
        assert not note.is_visible()
        choice.locator('[data-value="不同意"]').click()
        page.evaluate('saveQueue')
        assert note.is_visible() and note.get_attribute('placeholder') == '写具体原因'
        assert load(decisions_file)['todos']['T01'] == {'stance': '不同意', 'note': ''}
        assert page.locator('#stance-count').inner_text() == '1'
        assert page.locator('#disagree-count').inner_text() == '1'
        posts = []
        page.on('request', lambda r: posts.append(r.post_data_json) if r.method == 'POST' else None)
        text = '自动保存验证：请明确建议的适用范围。\n第二行仅用于验证。'
        note.fill(text)
        page.wait_for_timeout(600)
        assert not posts and load(decisions_file)['todos']['T01']['note'] == ''
        note.fill(text + '（停止输入后保存）')
        page.wait_for_timeout(600)
        assert not posts
        page.wait_for_function('!noteTimers.size')
        page.evaluate('saveQueue')
        assert len(posts) == 1
        text += '（停止输入后保存）'
        assert load(decisions_file)['todos']['T01']['note'] == text
        page.reload()
        page.evaluate('window.blueprintReady')
        assert note.is_visible() and note.input_value() == text
        choice.locator('[data-value="同意"]').click()
        page.evaluate('saveQueue')
        assert not note.is_visible()
        assert load(decisions_file)['todos']['T01'] == {'stance': '同意', 'note': text}
        choice.locator('[data-value="有疑问"]').click()
        page.evaluate('saveQueue')
        assert note.is_visible() and note.input_value() == text
        assert page.locator('#todo-progress').inner_text() == '对 17 条待办的建议表态，已表态 1 条，其中不同意 0、有疑问 1 去表态'
        choice.locator('.toggle').click()
        choice.evaluate('e=>e.scrollIntoView({block:"start"})')
        shot('todo-stance-1440.png')
        note.fill('')
        # Immediate stance change also flushes the pending note without restoring an old stance.
        choice.locator('[data-value="有疑问"]').click()
        page.evaluate('saveQueue')
        page.wait_for_timeout(1100)
        assert load(decisions_file) == original
        assert decisions_file.read_bytes() == initial_bytes
        page.goto(url)
        page.evaluate('window.blueprintReady')
        page.evaluate('document.fonts.ready')
        # v2 expanded full-page evidence.
        page.locator('.source-file').evaluate_all('es=>es.forEach(e=>e.open=true)')
        page.locator('.entry .toggle').evaluate_all('es=>es.forEach(e=>e.click())')
        shot('expanded-full-1440.png', True)

        mobile_context = browser.new_context(viewport={'width': 390, 'height': 844})
        mobile = mobile_context.new_page()
        mobile.on('pageerror', lambda error: console_errors.append(str(error)))
        mobile.goto(url)
        mobile.evaluate('window.blueprintReady')
        mobile.evaluate('document.fonts.ready')
        assert mobile.evaluate('document.documentElement.scrollWidth <= innerWidth')
        check_home_navigation(mobile)
        mobile.locator('#todo-T10 .id a').click()
        mobile.wait_for_function('location.hash === "#todo-T10"')
        mobile.locator('#detail-T10 .assessment-rule-id a').first.click()
        mobile.wait_for_function('location.hash === "#rule-SD-06"')
        assert mobile.locator('#rule-SD-06').locator('xpath=ancestor::details').evaluate('e=>e.open')
        assert mobile.evaluate('document.documentElement.scrollWidth <= innerWidth')
        mobile.locator('#rule-SD-06').locator('xpath=..').locator('a[href="#todo-T10"]').click()
        mobile.locator('#todo-T10 .coverage a').first.click()
        mobile.locator('#detail-R5').wait_for(state='visible')
        assert mobile.evaluate('document.documentElement.scrollWidth <= innerWidth')
        mobile.locator('#todo-T10 [data-value="有疑问"]').click()
        mobile.evaluate('saveQueue')
        assert mobile.locator('#todo-T10 textarea').is_visible()
        assert mobile.evaluate('document.documentElement.scrollWidth <= innerWidth')
        mobile.locator('#todo-T10 [data-value="有疑问"]').click()
        mobile.evaluate('saveQueue')
        assert load(decisions_file) == original
        mobile_context.close()

        offline_context = browser.new_context(viewport={'width': 1440, 'height': 1000}, accept_downloads=True)
        offline = offline_context.new_page()
        offline.on('pageerror', lambda error: console_errors.append(str(error)))
        offline.goto((directory / 'index.html').as_uri())
        offline.evaluate('window.blueprintReady')
        offline.evaluate('document.fonts.ready')
        assert offline.locator('#offline').is_visible()
        assert offline.locator('#offline span').inner_text() == '未连接本地服务，选择只存在本浏览器'
        assert offline.locator('#export').is_enabled()
        # Upgrade old local storage without interpreting obsolete todo versions as stances.
        old_local = {'todos': {'T03': '0.2'}, 'regressions': {'R3': '0.2'}}
        offline.evaluate('(value)=>localStorage.setItem(storageKey,JSON.stringify(value))', old_local)
        offline.reload()
        offline.evaluate('window.blueprintReady')
        migrated = offline.evaluate('JSON.parse(localStorage.getItem(storageKey))')
        assert set(migrated) == {'regressions', 'todos'}
        assert migrated['todos'] == original['todos']
        assert offline.locator('[data-id="R3"][data-value="0.2"]').get_attribute('aria-pressed') == 'true'
        assert offline.locator('#selected-count').inner_text() == '1'
        offline.locator('#todo-T03 [data-value="有疑问"]').click()
        offline.locator('#todo-T03 textarea').fill('离线验证\n保留换行')
        offline.wait_for_function('!noteTimers.size')
        offline.evaluate('saveQueue')
        offline.reload()
        offline.evaluate('window.blueprintReady')
        assert offline.locator('#todo-T03 textarea').input_value() == '离线验证\n保留换行'
        assert offline.locator('#todo-T03 [data-value="有疑问"]').get_attribute('aria-pressed') == 'true'
        with offline.expect_download() as event:
            offline.locator('#export').click()
        download = event.value
        assert download.suggested_filename == 'decisions.yaml'
        exported_path = output / 'export-selfcheck.yaml'
        download.save_as(str(exported_path))
        exported = load(exported_path)
        assert set(exported) == {'regressions', 'todos'} and exported['regressions']['R3'] == '0.2'
        assert exported['todos']['T03'] == {'stance': '有疑问', 'note': '离线验证\n保留换行'}
        exported_path.unlink()
        offline.reload()
        offline.evaluate('window.blueprintReady')
        assert offline.locator('[data-id="R3"][data-value="0.2"]').get_attribute('aria-pressed') == 'true'
        offline.locator('[data-id="R3"][data-value="0.2"]').click()
        offline.locator('#todo-T03 textarea').fill('')
        offline.locator('#todo-T03 [data-value="有疑问"]').click()
        offline.evaluate('saveQueue')
        assert offline.evaluate('JSON.parse(localStorage.getItem(storageKey))') == original
        assert load(decisions_file) == original

        # Isolated renderer/browser fixture: real sources currently have no turns.
        # Exercise all conversation modes and partial gaps without editing a case file.
        fixture_prompts = {**prompts, 'R1': [
            {'n': 1, 'prompt': '\n第一行\n第二行 <原文> & 可复制\n', 'conversation': {'mode': 'new'}},
            {'n': 2, 'prompt': '', 'conversation': {'mode': 'continue'}},
            {'n': 3, 'prompt': '从第一轮分支。', 'conversation': {'mode': 'branch', 'after_turn': 1}}]}
        source = (directory / 'index.html').read_text()
        start, end = source.index('<div class="cards"'), source.index('</main>')
        fixture_data = deepcopy(data)
        fixture_data['todos'][0]['assessment']['status'] = '约束过度'
        fixture_html = source[:start] + render_body(fixture_data, files, fixture_prompts) + source[end:]
        fixture = context.new_page()
        fixture.route('**/prompt-fixture', lambda route: route.fulfill(body=fixture_html, content_type='text/html'))
        fixture.goto(url + 'prompt-fixture')
        fixture.evaluate('window.blueprintReady')
        badge = fixture.locator('#todo-T01 .assessment-status')
        badge.hover()
        assert badge.inner_text() == '约束过度'
        assert badge.get_attribute('title') == '写得太死或绑定具体案例，会在其他正当场景误伤'
        assert badge.evaluate('e=>[getComputedStyle(e).color,getComputedStyle(e).backgroundColor]') == ['rgb(180, 35, 24)', 'rgb(253, 232, 232)']
        assert fixture.locator('[data-card="5"]').inner_text() == str(len(rewrite_todos))
        assert fixture.locator('#cards .card').nth(5).locator('div').nth(1).inner_text() == f'约束不足 {insufficient - 1} · 过度 {excessive + 1}'
        fixture.locator('#rewrite-todos a[href="#todo-T01"]').click()
        fixture.locator('#detail-T01').wait_for(state='visible')
        fixture.locator('#reg-R1 .toggle').click()
        folds = fixture.locator('#reg-R1 .prompt-turn')
        assert folds.count() == 3
        assert folds.locator('summary').all_text_contents() == ['第 1 轮 · 新对话', '第 2 轮 · 接着上一轮', '第 3 轮 · 从第 1 轮分支']
        assert folds.evaluate_all('es=>es.every(e=>!e.open)')
        for index, turn in enumerate(fixture_prompts['R1']):
            fold = folds.nth(index)
            fold.locator('summary').click()
            if turn['prompt']:
                assert fold.locator('.prompt-text').text_content() == turn['prompt']
                assert fold.locator('.prompt-text').evaluate('e=>getComputedStyle(e).whiteSpace') == 'pre-wrap'
            else:
                assert fold.locator('.prompt-empty').inner_text() == '本轮 prompt 待补'
        assert fixture.locator('#reg-R1 textarea,input,[contenteditable]').count() == 0
        fixture.close()
        assert not console_errors, console_errors
        browser.close()
    assert hashlib.sha256((directory / 'blueprint.yaml').read_bytes()).hexdigest() == blueprint_hash
    assert all(hashlib.sha256((root / path).read_bytes()).hexdigest() == value for path, value in source_hashes.items())
    assert all(hashlib.sha256((root / path).read_bytes()).hexdigest() == value for path, value in prompt_hashes.items())
    result = {
        'self_checks': [
            {'id': 1, 'status': '通过', 'result': '全部待办来源与页面、17 条 assessment 的全部字段逐字一致；7 条回归 test / judgment 与当前 blueprint.yaml 逐字一致，已有来源另行核对；4 条 draft_by 如实展示。'},
            {'id': 2, 'status': '通过', 'result': 'R1=0.1、R2=搁置写入读回；待办不同意、1 秒防抖保存、多行输入刷新保留、同意收起且文件保留、有疑问与统计均实测，随后清空恢复。'},
            {'id': 3, 'status': '通过', 'result': 'file:// 黄色提示、旧本地数据迁移、回归与待办表态和备注导出、重新打开均已验证。'},
            {'id': 4, 'status': '通过', 'result': '1440 宽首屏、待办展开区两张截图；390 宽导航、表态与无溢出实测。'}],
        'browser_plugin': 'Browser plugin not available', 'browser_path': 'Playwright / ' + args.browser,
        'viewport': [{'width': 1440, 'height': 1000}, {'width': 390, 'height': 844}],
        'source_identity': {'todos': len(rows), 'supplement': len(supplemental),
                            'regression_test_texts': len(source_tests), 'regression_judgments': 7,
                            'rule_locations': len(expected_rule_positions), 'source_files': len(files),
                            'source_lines': sum(len(f['lines']) for f in files), 'source_files_sha256': source_hashes,
                            'assessment_fields': len(data['todos']) * 9, 'assessment_exact_dom_comparisons': 'PASS',
                            'blueprint_sha256_before_and_after': blueprint_hash,
                            'new_draft_authority': 'blueprint.yaml, R4 test / R4-R7 judgment; draft_by retained; no semantic review'},
        'mechanical_checks': check_data(data, root) + [check_html_ids((directory / 'index.html').read_text())],
        'prompt_sources': prompt_sources, 'prompt_source_sha256': prompt_hashes,
        'prompt_rendering': {'real_case_fidelity': 'PASS', 'synthetic_new_continue_branch_partial_gap': 'PASS',
                             'fixture_source_files_modified': False,
                             'real_cases_without_prompts': [s['id'] for s in prompt_sources if s['matched'] and not s['prompt_turns']]},
        'navigation': {'T10_to_rule_with_1500ms_flash': 'PASS', 'source_badge_to_T10': 'PASS',
                       'home_cards_desktop_and_mobile': 'PASS', 'zero_uncovered_card_inert': 'PASS',
                       'rewrite_todo_capsules_need_and_expand': 'PASS', 'selected_count_live_and_reload': 'PASS',
                       'R4_to_T01': 'PASS', 'todo_to_regression': 'PASS', 'browser_back_and_scroll': 'PASS',
                       'file_tree_and_direct_deep_link': 'PASS', 'back_to_top': 'PASS', 'mobile_links_and_overflow': 'PASS'},
        'service_choices_and_restoration': 'PASS', 'initial_decisions_bytes_restored': True,
        'offline_warning_export_and_persistence': 'PASS', 'screenshots': screenshots,
        'console_errors': console_errors, 'cards': expected_cards}
    (output / 'self-check.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
