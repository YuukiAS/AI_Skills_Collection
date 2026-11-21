#!/usr/bin/env python3
"""Full source/DOM comparison and local/offline browser acceptance checks."""
import argparse
import json
import re
import sys
from pathlib import Path

import yaml
from playwright.sync_api import sync_playwright

from build_blueprint import BASE, initial_decisions, load, repo_root
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
            assert case["id"] == "R4" and case["test"] == ""
    expected_rule_positions = set()
    for source in (root / data["sources"]["skill_root"]).rglob("*"):
        if source.is_file() and source.suffix in (".md", ".yaml"):
            for n, line in enumerate(source.read_text().splitlines(), 1):
                match = re.match(r"- \*\*((?:JI|SD|TS)-\d+) ", line)
                if match:
                    expected_rule_positions.add((match[1], str(source.relative_to(root)), n))
    assert {(r["id"], r["file"], r["line"]) for r in data["rules"]} == expected_rule_positions
    console_errors = []
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(executable_path=args.browser, headless=True,
                                             args=["--no-sandbox", "--disable-dev-shm-usage"])
        context = browser.new_context(viewport={"width": 1440, "height": 1000}, accept_downloads=True)
        page = context.new_page()
        page.on("pageerror", lambda error: console_errors.append(str(error)))
        page.on("console", lambda msg: console_errors.append(msg.text) if msg.type == "error" else None)
        page.goto(f"http://127.0.0.1:{args.port}/")
        page.evaluate("window.blueprintReady")
        page.evaluate("document.fonts.ready")
        assert page.title() == data["title"]
        assert page.locator("h1").inner_text() == data["title"]
        assert not page.locator("#offline").is_visible()
        assert page.evaluate("document.documentElement.scrollWidth <= window.innerWidth")
        assert page.evaluate("document.fonts.check('15px \"Noto Sans SC Local\"')")
        assert page.locator("main").evaluate("e=>getComputedStyle(e).maxWidth") == "1100px"
        assert page.locator("body").evaluate("e=>getComputedStyle(e).fontSize") == "15px"
        assert page.locator("body").evaluate("e=>getComputedStyle(e).lineHeight") == "24px"
        for todo in data["todos"]:
            assert page.locator(f'[data-todo="{todo["id"]}"] .todo-title').inner_text() == todo["title"]
            detail = page.locator(f'#detail-{todo["id"]}')
            page.locator(f'[data-detail="detail-{todo["id"]}"]').click()
            if todo.get("problem"):
                assert detail.locator(".problem").text_content() == todo["problem"]
            if todo.get("source_text"):
                assert detail.locator(".source").text_content() == todo["source_text"]
            if todo["user_words"]:
                assert detail.locator(".quote").text_content() == "\n".join(todo["user_words"])
            else:
                assert detail.locator(".quote").count() == 0
            if todo.get("note"):
                assert detail.locator(".note").text_content() == todo["note"]
        for case in data["regressions"]:
            assert page.locator(f'[data-regression="{case["id"]}"] .test-text').text_content() == (case["test"] or "—")
            page.locator(f'[data-detail="detail-{case["id"]}"]').click()
            assert page.locator(f'#detail-{case["id"]} .judgment').text_content() == (case["judgment"] or "—")
        assert page.locator(".first-sentence").all_text_contents() == [r["first_sentence"] for s in data["skills"] for r in data["rules"] if r["file"] in s["rule_files"]] + [r["first_sentence"] for r in data["rules"] if r["file"] in data["shared_files"]]
        assert page.locator(".description").all_text_contents() == [s["description"] for s in data["skills"]]
        page.screenshot(path=str(output / "expanded-full-1440.png"), full_page=True)
        page.locator('[data-group="regressions"][data-id="R1"][data-value="0.1"]').click()
        page.locator('[data-group="regressions"][data-id="R2"][data-value="搁置"]').click()
        page.locator('[data-group="todos"][data-id="T03"][data-value="0.2"]').click()
        page.evaluate("saveQueue")
        persisted = load(decisions_file)
        assert persisted["regressions"]["R1"] == "0.1"
        assert persisted["regressions"]["R2"] == "搁置"
        assert persisted["todos"]["T03"] == "0.2"
        assert page.locator('[data-card="4"]').inner_text() == "1"
        assert page.locator("#saved").is_visible()
        page.wait_for_timeout(2200)
        assert not page.locator("#saved").is_visible()
        page.reload()
        page.evaluate("window.blueprintReady")
        for group, id_, value in [("regressions", "R1", "0.1"), ("regressions", "R2", "搁置"), ("todos", "T03", "0.2")]:
            assert page.locator(f'[data-group="{group}"][data-id="{id_}"][data-value="{value}"]').get_attribute("aria-pressed") == "true"
        # Restore by the same UI path, including clearing the two regression choices.
        page.locator('[data-group="regressions"][data-id="R1"][data-value="0.1"]').click()
        page.locator('[data-group="regressions"][data-id="R2"][data-value="搁置"]').click()
        page.locator('[data-group="todos"][data-id="T03"][data-value="0.1"]').click()
        page.evaluate("saveQueue")
        assert load(decisions_file) == original
        assert decisions_file.read_bytes() == initial_bytes
        page.reload()
        page.evaluate("window.blueprintReady")
        page.evaluate("document.fonts.ready")
        assert page.locator(".number").all_text_contents() == ["2", "16 + 1", "7", "0", "0"]
        page.screenshot(path=str(output / "full-1440.png"), full_page=True)
        offline_context = browser.new_context(viewport={"width": 1440, "height": 1000}, accept_downloads=True)
        offline = offline_context.new_page()
        offline.on("pageerror", lambda error: console_errors.append(str(error)))
        offline.goto((directory / "index.html").as_uri())
        offline.evaluate("window.blueprintReady")
        offline.evaluate("document.fonts.ready")
        assert offline.locator("#offline").is_visible()
        assert offline.locator("#offline span").inner_text() == "未连接本地服务，选择只存在本浏览器"
        assert offline.locator("#export").is_enabled()
        offline.locator('[data-group="regressions"][data-id="R3"][data-value="0.2"]').click()
        with offline.expect_download() as event:
            offline.locator("#export").click()
        download = event.value
        assert download.suggested_filename == "decisions.yaml"
        exported_path = output / "export-selfcheck.yaml"
        download.save_as(str(exported_path))
        exported = load(exported_path)
        assert exported["regressions"]["R3"] == "0.2"
        exported_path.unlink()
        offline.reload()
        offline.evaluate("window.blueprintReady")
        assert offline.locator('[data-group="regressions"][data-id="R3"][data-value="0.2"]').get_attribute("aria-pressed") == "true"
        offline.locator('[data-group="regressions"][data-id="R3"][data-value="0.2"]').click()
        offline.evaluate("saveQueue")
        offline.screenshot(path=str(output / "offline-full-1440.png"), full_page=True)
        assert load(decisions_file) == original
        assert not console_errors, console_errors
        browser.close()
    result = {
        "self_checks": [
            {"id": 1, "status": "不通过", "result": "全部已有来源与页面逐字一致；R4 缺少测什么的来源原文，无法核对。"},
            {"id": 2, "status": "通过", "result": "R1=0.1、R2=搁置、T03=0.2 写入并读回，随后恢复初始文件。"},
            {"id": 3, "status": "通过", "result": "file:// 黄色提示、浏览器保存、导出和重新打开均已验证。"},
            {"id": 4, "status": "通过", "result": "1440 宽整页截图共三张。"}
        ],
        "viewport": {"width": 1440, "height": 1000},
        "browser_path": "Playwright / " + args.browser,
        "browser_plugin": "Browser plugin not available",
        "source_identity": {"todos": len(rows), "supplement": len(supplemental),
                            "regression_test_texts": len(source_tests), "regression_judgments": 3,
                            "rule_locations": len(expected_rule_positions),
                            "available_source_and_dom_comparisons": "PASS",
                            "missing_test_sources": ["R4"], "missing_judgment_sources": ["R4", "R5", "R6", "R7"]},
        "service_choices_and_restoration": "PASS", "initial_decisions_bytes_restored": True,
        "offline_warning_export_and_persistence": "PASS", "screenshots": ["full-1440.png", "expanded-full-1440.png", "offline-full-1440.png"],
        "console_errors": console_errors,
        "cards": ["2", "16 + 1", "7", "0", "0"]}
    (output / "self-check.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
