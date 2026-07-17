#!/usr/bin/env python3
"""Validate rendered Chinese/math PDF text and layout quality."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from pathlib import Path
from typing import Any

CJK_RE = re.compile(r"[\u3400-\u9fff]")
BAD_GLYPH_RE = re.compile(r"[\ue000-\uf8ff\ufffd]")


def run_command(args: list[str], timeout: int = 30) -> tuple[int, str]:
    try:
        proc = subprocess.run(args, check=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, timeout=timeout)
    except (OSError, subprocess.TimeoutExpired) as exc:
        return 127, str(exc)
    return proc.returncode, proc.stdout


def has_bad_glyphs(text: str) -> bool:
    return bool(BAD_GLYPH_RE.search(text))


def cjk_line_fragmentation(text: str) -> dict[str, Any]:
    lines = [line.strip() for line in text.splitlines() if CJK_RE.search(line)]
    short = [line for line in lines if len(CJK_RE.findall(line)) <= 2 and len(line) <= 8]
    ratio = (len(short) / len(lines)) if lines else 0.0
    return {"cjk_lines": len(lines), "short_cjk_lines": len(short), "short_ratio": ratio, "failed": len(lines) >= 8 and ratio > 0.45}


def markdown_table_rows(source_text: str) -> list[list[str]]:
    rows: list[list[str]] = []
    pending: list[list[str]] = []
    for line in source_text.splitlines():
        stripped = line.strip()
        if "|" not in stripped:
            if pending:
                rows.extend(pending)
                pending = []
            continue
        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        if len(cells) < 2:
            continue
        if all(re.fullmatch(r":?-{3,}:?", cell.replace(" ", "")) for cell in cells if cell):
            continue
        pending.append([cell for cell in cells if cell])
    if pending:
        rows.extend(pending)
    return rows


def normalize_token(text: str) -> str:
    return re.sub(r"\s+", "", text).strip()


def table_survival(source_text: str, extracted_text: str) -> dict[str, Any]:
    rows = markdown_table_rows(source_text)
    if not rows:
        return {"source_table_rows": 0, "matched_rows": 0, "failed": False}
    layout_lines = [normalize_token(line) for line in extracted_text.splitlines() if line.strip()]
    matched = 0
    checked_rows = 0
    for row in rows[:12]:
        tokens = [normalize_token(cell) for cell in row if len(normalize_token(cell)) >= 1]
        if len(tokens) < 2:
            continue
        checked_rows += 1
        if any(sum(1 for token in tokens if token and token in line) >= 2 for line in layout_lines):
            matched += 1
    failed = checked_rows > 0 and matched / checked_rows < 0.75
    return {"source_table_rows": len(rows), "checked_rows": checked_rows, "matched_rows": matched, "failed": failed}


def parse_pdfinfo_pages(pdfinfo: str) -> int | None:
    match = re.search(r"^Pages:\s*(\d+)\s*$", pdfinfo, re.MULTILINE)
    return int(match.group(1)) if match else None


def fonts_embedded(pdffonts: str) -> bool | None:
    lines = [line for line in pdffonts.splitlines() if line.strip()]
    body = [line for line in lines if not line.startswith("name") and not set(line.strip()) <= {"-", " "}]
    if not body:
        return None
    return any(re.search(r"\byes\b", line) for line in body)


def validate_text(extracted_text: str, source_text: str | None = None) -> dict[str, Any]:
    errors: list[str] = []
    warnings: list[str] = []
    fragmentation = cjk_line_fragmentation(extracted_text)
    if has_bad_glyphs(extracted_text):
        errors.append("private-use or replacement glyphs found in extracted text")
    if fragmentation["failed"]:
        errors.append("abnormal CJK line fragmentation detected")
    table = table_survival(source_text or "", extracted_text)
    if table["failed"]:
        errors.append("Markdown table rows did not survive in extracted PDF layout text")
    if not extracted_text.strip():
        errors.append("empty extracted text layer")
    elif len(extracted_text.strip()) < 40:
        warnings.append("very short extracted text layer")
    return {"errors": errors, "warnings": warnings, "fragmentation": fragmentation, "table_survival": table}


def validate_pdf(pdf: Path, source: Path | None = None, preview_dir: Path | None = None) -> dict[str, Any]:
    result: dict[str, Any] = {"pdf": str(pdf), "errors": [], "warnings": []}
    if not pdf.exists() or pdf.stat().st_size == 0:
        result["errors"].append("PDF missing or empty")
        return result
    code, pdfinfo = run_command(["pdfinfo", str(pdf)])
    result["pdfinfo"] = pdfinfo
    pages = parse_pdfinfo_pages(pdfinfo)
    result["pages"] = pages
    if code != 0:
        result["errors"].append("pdfinfo failed")
    if pages is not None and pages < 1:
        result["errors"].append("PDF has no pages")
    code, pdffonts = run_command(["pdffonts", str(pdf)])
    result["pdffonts"] = pdffonts
    embedded = fonts_embedded(pdffonts)
    result["fonts_embedded"] = embedded
    if code == 0 and embedded is False:
        result["errors"].append("no embedded fonts reported by pdffonts")
    text_path = pdf.with_suffix(".layout.txt")
    code, text_output = run_command(["pdftotext", "-layout", str(pdf), str(text_path)])
    if code != 0:
        result["errors"].append("pdftotext -layout failed")
        extracted = text_output
    else:
        extracted = text_path.read_text(encoding="utf-8", errors="replace")
        try:
            text_path.unlink()
        except OSError:
            pass
    source_text = source.read_text(encoding="utf-8", errors="replace") if source else None
    text_result = validate_text(extracted, source_text)
    result["text_checks"] = text_result
    result["errors"].extend(text_result["errors"])
    result["warnings"].extend(text_result["warnings"])
    if preview_dir:
        preview_dir.mkdir(parents=True, exist_ok=True)
        prefix = preview_dir / pdf.stem
        code, preview_output = run_command(["pdftoppm", "-f", "1", "-l", "1", "-r", "120", "-png", str(pdf), str(prefix)])
        result["preview_prefix"] = str(prefix)
        if code != 0:
            result["warnings"].append(f"pdftoppm preview failed: {preview_output.strip()}")
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf", type=Path)
    parser.add_argument("--source", type=Path)
    parser.add_argument("--preview-dir", type=Path)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    result = validate_pdf(args.pdf, source=args.source, preview_dir=args.preview_dir)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        for error in result["errors"]:
            print(f"ERROR: {error}")
        for warning in result["warnings"]:
            print(f"WARNING: {warning}")
        print(f"pages: {result.get('pages')}")
        print(f"fonts_embedded: {result.get('fonts_embedded')}")
    return 1 if result["errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
