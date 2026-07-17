#!/usr/bin/env python3
"""Probe local support for rendering Chinese/math documents to PDF."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
from pathlib import Path
from typing import Any


COMMANDS = [
    "pandoc",
    "xelatex",
    "lualatex",
    "kpsewhich",
    "pdfinfo",
    "pdftotext",
    "pdffonts",
    "pdftoppm",
]

TEX_FILES = [
    "xeCJK.sty",
    "ctexart.cls",
    "fontspec.sty",
    "amsmath.sty",
    "booktabs.sty",
    "longtable.sty",
    "hyperref.sty",
]


def run_version(command: str) -> str | None:
    for flag in ("--version", "-version", "-v"):
        try:
            proc = subprocess.run(
                [command, flag],
                check=False,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                timeout=5,
            )
        except (OSError, subprocess.TimeoutExpired):
            continue
        text = proc.stdout.strip().splitlines()
        if proc.returncode == 0 and text:
            return text[0]
    return None


def command_info(command: str) -> dict[str, Any]:
    path = shutil.which(command)
    return {
        "available": path is not None,
        "path": path,
        "version": run_version(command) if path else None,
    }


def kpsewhich_lookup(filename: str) -> dict[str, Any]:
    kpsewhich = shutil.which("kpsewhich")
    if not kpsewhich:
        return {"available": False, "path": None, "reason": "kpsewhich not found"}
    try:
        proc = subprocess.run(
            [kpsewhich, filename],
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=5,
        )
    except subprocess.TimeoutExpired:
        return {"available": False, "path": None, "reason": "kpsewhich timed out"}
    path = proc.stdout.strip()
    return {
        "available": proc.returncode == 0 and bool(path),
        "path": path or None,
        "reason": None if proc.returncode == 0 and path else proc.stderr.strip() or None,
    }


def ancestor_dirs(root: Path) -> list[Path]:
    root = root.resolve()
    return [root, *root.parents]


def find_project_resources(root: Path) -> list[str]:
    return [item["path"] for item in find_project_resource_bundles(root)]


def find_file(root: Path, filename: str) -> str | None:
    matches = sorted(root.rglob(filename)) if root.exists() else []
    return str(matches[0]) if matches else None


def resource_bundle_info(path: Path) -> dict[str, Any]:
    texmf = path / "texmf" if (path / "texmf").exists() else path
    scripts = path / "scripts"
    templates = path / "templates"
    tex_files = {filename: find_file(texmf, filename) for filename in TEX_FILES}
    font_files = {
        "FandolSong-Regular.otf": find_file(texmf, "FandolSong-Regular.otf"),
        "FandolHei-Regular.otf": find_file(texmf, "FandolHei-Regular.otf"),
        "FandolKai-Regular.otf": find_file(texmf, "FandolKai-Regular.otf"),
    }
    wrappers = {
        "render_markdown_pdf.sh": str(scripts / "render_markdown_pdf.sh") if (scripts / "render_markdown_pdf.sh").exists() else None,
        "validate_pdf.sh": str(scripts / "validate_pdf.sh") if (scripts / "validate_pdf.sh").exists() else None,
    }
    template = templates / "chinese_math_pandoc_header.tex.in"
    usable = bool(tex_files.get("xeCJK.sty") and tex_files.get("ctexart.cls") and font_files.get("FandolSong-Regular.otf"))
    return {
        "path": str(path),
        "texmf": str(texmf),
        "usable_chinese_math_bundle": usable,
        "tex_files": tex_files,
        "font_files": font_files,
        "header_template": str(template) if template.exists() else None,
        "wrappers": wrappers,
    }


def find_project_resource_bundles(root: Path) -> list[dict[str, Any]]:
    candidates: list[Path] = []
    for base in ancestor_dirs(root):
        candidates.extend(
            [
                base / "render_resources" / "chinese_math_pdf",
                base / "texmf",
                base / ".texlive" / "texmf",
            ]
        )
    found: list[dict[str, Any]] = []
    seen: set[Path] = set()
    for candidate in candidates:
        if candidate.name == "texmf" and candidate.parent.name == "chinese_math_pdf":
            bundle_path = candidate.parent
        else:
            bundle_path = candidate
        if not bundle_path.exists():
            continue
        key = bundle_path.resolve()
        if key in seen:
            continue
        seen.add(key)
        found.append(resource_bundle_info(bundle_path))
    return found


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=Path.cwd(),
        help="Project root or source directory to inspect for local render resources.",
    )
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON output.")
    args = parser.parse_args()

    commands = {command: command_info(command) for command in COMMANDS}
    tex_files = {filename: kpsewhich_lookup(filename) for filename in TEX_FILES}
    resource_bundles = find_project_resource_bundles(args.root)
    usable_bundles = [item for item in resource_bundles if item["usable_chinese_math_bundle"]]

    result = {
        "root": str(args.root.resolve()),
        "commands": commands,
        "tex_files": tex_files,
        "project_resources": [item["path"] for item in resource_bundles],
        "project_resource_bundles": resource_bundles,
        "summary": {
            "markdown_to_pdf_candidate": commands["pandoc"]["available"]
            and (commands["xelatex"]["available"] or commands["lualatex"]["available"]),
            "cjk_xelatex_candidate": commands["xelatex"]["available"]
            and tex_files["fontspec.sty"]["available"]
            and (tex_files["xeCJK.sty"]["available"] or bool(usable_bundles)),
            "usable_resource_bundle_count": len(usable_bundles),
            "recommended_resource_dir": usable_bundles[0]["path"] if usable_bundles else None,
            "pdf_qa_tools": [
                name
                for name in ("pdfinfo", "pdftotext", "pdffonts", "pdftoppm")
                if commands[name]["available"]
            ],
        },
    }
    print(json.dumps(result, indent=2 if args.pretty else None, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
