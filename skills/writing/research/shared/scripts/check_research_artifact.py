#!/usr/bin/env python3
from __future__ import annotations

import argparse
import difflib
import hashlib
import importlib.util
import json
import re
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

UNOBSERVED = "未观察"
CHECKS = ("files", "correspondence", "edit_scope", "exact_items", "format", "readback", "evidence")


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def renderer_root(explicit=None):
    if explicit:
        root = Path(explicit).resolve()
        if not (root / "scripts/validate_pdf_layout.py").is_file():
            raise ValueError("renderer_root: validate_pdf_layout.py missing")
        return root
    for parent in Path(__file__).resolve().parents:
        root = parent / "skills/tools/documents-media/render-chinese-math-pdf"
        if (root / "scripts/validate_pdf_layout.py").is_file():
            return root
    raise FileNotFoundError("render-chinese-math-pdf")


def pdf_result(path, source, root):
    spec = importlib.util.spec_from_file_location("research_pdf_qa", root / "scripts/validate_pdf_layout.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    with tempfile.TemporaryDirectory(prefix="research-pages-") as temp:
        result = module.validate_pdf(path, source=source, preview_dir=Path(temp), preview_pages="all")
        pages = result.get("pages")
        previews = result.get("preview_paths", [])
        result["preview_count"] = len(previews)
        result["all_pages_generated"] = isinstance(pages, int) and pages > 0 and len(previews) == pages
        result.pop("preview_paths", None)
        result.pop("preview_prefix", None)
    return result


def markdown_result(path):
    text = path.read_text(encoding="utf-8")
    errors, links = [], []
    if re.search(r"[\x00-\x08\x0b\x0c\x0e-\x1f\ufffd]", text):
        errors.append("invalid_text_codepoint")
    fence = None
    visible = []
    for number, line in enumerate(text.splitlines(), 1):
        match = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line)
        if match:
            marker, tail = match.groups()
            if fence is None:
                fence = (marker[0], len(marker))
            elif marker[0] == fence[0] and len(marker) >= fence[1] and not tail.strip():
                fence = None
            continue
        if fence:
            continue
        visible.append(line)
        line = re.sub(r"(`+).*?\1", "", line)
        for target in re.findall(r"!?\[[^\]]*\]\(([^\s)]+)(?:\s+[^)]*)?\)", line):
            if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("#"):
                continue
            from urllib.parse import unquote
            local = unquote(target.split("#", 1)[0])
            links.append({"line": number, "path": local})
            if local and not (path.parent / local).is_file():
                errors.append(f"resource_missing:{number}:{local}")
    if fence:
        errors.append("unclosed_code_fence")
    return {"errors": errors, "local_links": links, "math_semantics": UNOBSERVED,
            "math_rendering": UNOBSERVED, "target_page": UNOBSERVED}


def check(handoff_path, *, renderer=None, required=()):
    handoff_path = Path(handoff_path).resolve()
    base = handoff_path.parent
    rows, observed, missing, findings = [], [], [], []

    def add(check_id, status, locator, **details):
        rows.append({"check": check_id, "status": status, "locator": str(locator), **details})
        if status == "PASS":
            observed.append(str(locator))
        elif status == UNOBSERVED:
            missing.append({"check": check_id, "locator": str(locator)})

    def locate(value):
        if isinstance(value, dict):
            value = value.get("path")
        if not isinstance(value, str) or not value:
            raise ValueError("path_missing")
        return (base / value).resolve()

    def file_check(value, check_id="files"):
        path = locate(value)
        if not path.is_file():
            add(check_id, "FAIL", path, error="file_missing")
            return None
        actual = sha256(path)
        expected = value.get("sha256") if isinstance(value, dict) else None
        add(check_id, "PASS" if not expected or actual == expected else "FAIL", path,
            sha256=actual, expected_sha256=expected)
        return path

    try:
        handoff = json.loads(handoff_path.read_text(encoding="utf-8"))
        if not isinstance(handoff, dict):
            raise ValueError("handoff_not_object")
        add("files", "PASS", handoff_path, sha256=sha256(handoff_path))
    except (OSError, ValueError) as exc:
        add("files", "FAIL", handoff_path, error=str(exc))
        return {"mechanical_results": rows, "observed_surfaces": observed,
                "unobserved_surfaces": missing, "findings": findings,
                "reader_review": UNOBSERVED, "exit_code": 1}

    identity = handoff.get("candidate_identity") or {}
    source = None
    try:
        source = file_check(identity.get("source"))
    except (OSError, ValueError, AttributeError) as exc:
        add("files", "FAIL", "candidate_identity.source", error=str(exc))
    if source and not isinstance(identity.get("source"), dict):
        add("correspondence", UNOBSERVED, source, reason="source_sha256_missing")
    elif source and not identity["source"].get("sha256"):
        add("correspondence", UNOBSERVED, source, reason="source_sha256_missing")
    elif source:
        add("correspondence", "PASS" if sha256(source) == identity["source"]["sha256"] else "FAIL", source)
    for ref in handoff.get("source_refs") or []:
        try:
            file_check(ref)
        except (OSError, ValueError) as exc:
            add("files", "FAIL", "source_refs", error=str(exc))

    targets = handoff.get("delivery_targets") or []
    if not isinstance(targets, list) or not targets:
        add("files", "FAIL", "delivery_targets", error="target_list_missing")
        targets = []
    for target in targets:
        try:
            path = file_check(target)
            if path is None:
                continue
            if source:
                if path.suffix.lower() in {".md", ".markdown", ".txt"}:
                    equal = path.read_bytes() == source.read_bytes()
                    if target.get("correspondence_file"):
                        declared = file_check(target["correspondence_file"], "correspondence")
                        equal = declared is not None and path.read_bytes() == declared.read_bytes()
                    add("correspondence", "PASS" if equal else "FAIL", path,
                        source_sha256=sha256(source))
                else:
                    add("correspondence", UNOBSERVED, path, reason="binary_content_correspondence")
            else:
                add("correspondence", UNOBSERVED, path, reason="source_missing")
            if path.suffix.lower() in {".md", ".markdown", ".txt"}:
                result = markdown_result(path)
                add("format", "FAIL" if result["errors"] else "PASS", path, measured=result)
                for surface in ("math_rendering", "target_page"):
                    add(surface, UNOBSERVED, path)
            elif path.suffix.lower() == ".pdf":
                try:
                    result = pdf_result(path, source, renderer_root(renderer))
                    ok = not result.get("errors") and result["all_pages_generated"]
                    add("format", "PASS" if ok else "FAIL", path, measured=result)
                    add("pdf_reading_quality", UNOBSERVED, path)
                    add("rendered_views", UNOBSERVED, path, reason="durable_all_page_views_required")
                except (OSError, ValueError, RuntimeError, ImportError, subprocess.SubprocessError) as exc:
                    add("format", UNOBSERVED, path, error=str(exc))
            elif path.suffix.lower() == ".zip":
                with zipfile.ZipFile(path) as archive:
                    names = archive.namelist()
                    components = target.get("components")
                    if not isinstance(components, dict):
                        add("format", UNOBSERVED, path, reason="component_manifest_missing")
                    else:
                        ok = len(names) == len(set(names)) and set(names) == set(components)
                        for name, value in components.items():
                            component = file_check(value)
                            if component is None or name not in names or archive.read(name) != component.read_bytes():
                                ok = False
                        evidence = handoff.get("execution_evidence")
                        if evidence and target.get("audience") == "student":
                            evidence_path = locate(evidence)
                            for name in names:
                                if Path(name).name == evidence_path.name or archive.read(name) == evidence_path.read_bytes():
                                    ok = False
                        add("format", "PASS" if ok else "FAIL", path, components=names)
            else:
                add("format", UNOBSERVED, path, reason="format_unsupported")
            readback = target.get("readback")
            if readback:
                remote = file_check(readback, "readback")
                if remote:
                    add("readback", "PASS" if path.read_bytes() == remote.read_bytes() else "FAIL", path,
                        readback_path=str(remote), readback_sha256=sha256(remote),
                        surface="provided_source_readback")
                add("published_page", UNOBSERVED, path)
            else:
                add("readback", UNOBSERVED, path)
        except (OSError, ValueError, AttributeError, TypeError, zipfile.BadZipFile) as exc:
            add("files", "FAIL", str(target), error=str(exc))

    scope = handoff.get("edit_scope")
    accepted = handoff.get("accepted_base")
    if accepted and source and isinstance(scope, dict) and isinstance(scope.get("allowed_patches"), list):
        try:
            before = file_check(accepted, "edit_scope")
            if before:
                expected = before.read_text(encoding="utf-8")
                for patch in scope["allowed_patches"]:
                    old, new = patch["before"], patch["after"]
                    if not isinstance(old, str) or not old or expected.count(old) != 1 or not isinstance(new, str):
                        raise ValueError("patch_not_unique")
                    expected = expected.replace(old, new, 1)
                actual = source.read_text(encoding="utf-8")
                add("edit_scope", "PASS" if expected == actual else "FAIL", source,
                    diff=list(difflib.unified_diff(expected.splitlines(), actual.splitlines(), lineterm="")))
        except (OSError, ValueError, KeyError, TypeError) as exc:
            add("edit_scope", "FAIL", "edit_scope", error=str(exc))
    else:
        add("edit_scope", UNOBSERVED, "edit_scope")
    exact_items = handoff.get("exact_items")
    if isinstance(exact_items, list) and exact_items:
        for item in exact_items:
            try:
                path = locate(item) if item.get("path") else source
                text = path.read_text(encoding="utf-8")
                if item.get("line") is not None:
                    number = item["line"]
                    if not isinstance(number, int) or number < 1:
                        raise ValueError("invalid_line")
                    text = text.splitlines()[number - 1]
                expected = item["text"]
                ok = isinstance(expected, str) and bool(expected) and expected in text
                add("exact_items", "PASS" if ok else "FAIL", path, item=item)
            except (OSError, ValueError, KeyError, TypeError, IndexError, AttributeError) as exc:
                add("exact_items", "FAIL", str(item), error=str(exc))
    else:
        add("exact_items", UNOBSERVED, "exact_items")
    evidence = handoff.get("execution_evidence")
    if evidence:
        try:
            path = file_check(evidence, "evidence")
            if path:
                text = path.read_text(encoding="utf-8")
                keys = ("插件/技能与版本", "规则编号", "成品中的原句或位置", "改前→改后")
                fields_present = all(re.search(r"^" + re.escape(k) + r":", text, re.M) for k in keys)
                empty_values = any(re.search(r"^" + re.escape(k) + r":\s*(?:null|~|\"\"|'')\s*$", text, re.M)
                                   for k in keys)
                status = "FAIL" if not fields_present else UNOBSERVED if empty_values or "GPT-WRITES:" in text else "PASS"
                add("evidence", status, path, scope="shared_template_fields_only")
                add("evidence_rule_judgment", UNOBSERVED, path)
        except (OSError, ValueError) as exc:
            add("evidence", "FAIL", "execution_evidence", error=str(exc))
    else:
        add("evidence", UNOBSERVED, "execution_evidence")
    for field in ("reader_review", "required_meanings", "required_relations", "rejected_content", "semantic_blocks"):
        findings.append({"field": field, "status": UNOBSERVED, "owner": "GPT"})
    required = set(required) | {"files", "correspondence", "format"}
    failed = any(r["status"] == "FAIL" for r in rows)
    incomplete = any(r["status"] == UNOBSERVED and r["check"] in required for r in rows)
    for check_id in required:
        if not any(r["check"] == check_id for r in rows):
            add(check_id, UNOBSERVED, check_id)
            incomplete = True
    return {"mechanical_results": rows, "observed_surfaces": sorted(set(observed)),
            "unobserved_surfaces": missing, "findings": findings,
            "reader_review": UNOBSERVED, "exit_code": int(failed or incomplete)}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("handoff", type=Path)
    parser.add_argument("--renderer-root", type=Path)
    parser.add_argument("--require", choices=CHECKS, action="append", default=[])
    parser.add_argument("--output", type=Path)
    parser.add_argument("--render", nargs=2, type=Path, metavar=("SOURCE", "PDF"))
    parser.add_argument("--render-project-root", type=Path)
    parser.add_argument("--preview-dir", type=Path)
    args = parser.parse_args()
    if args.render:
        source, pdf = (p.resolve() for p in args.render)
        try:
            root = renderer_root(args.renderer_root)
            command = [sys.executable, str(root / "scripts/render_scientific_pdf.py"), str(source), str(pdf),
                       "--preview-pages", "all", "--receipt", str(pdf.with_suffix(".render.json"))]
            if args.render_project_root:
                command += ["--root", str(args.render_project_root.resolve())]
            if args.preview_dir:
                command += ["--preview-dir", str(args.preview_dir.resolve())]
            result = subprocess.run(command, check=False)
            if result.returncode:
                return result.returncode
        except (OSError, ValueError) as exc:
            print(json.dumps({"render": UNOBSERVED, "error": str(exc)}, ensure_ascii=False))
            return 1
    result = check(args.handoff, renderer=args.renderer_root, required=args.require)
    payload = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.write_text(payload, encoding="utf-8")
    print(payload, end="")
    return result["exit_code"]


if __name__ == "__main__":
    raise SystemExit(main())
