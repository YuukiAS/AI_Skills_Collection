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
    candidates: list[Path] = []
    for base in ancestor_dirs(root):
        candidates.extend(
            [
                base / "render_resources" / "chinese_math_pdf",
                base / "texmf",
                base / ".texlive" / "texmf",
            ]
        )
    found: list[str] = []
    seen: set[Path] = set()
    for candidate in candidates:
        if candidate in seen:
            continue
        seen.add(candidate)
        if candidate.exists():
            found.append(str(candidate))
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

    result = {
        "root": str(args.root.resolve()),
        "commands": commands,
        "tex_files": tex_files,
        "project_resources": find_project_resources(args.root),
        "summary": {
            "markdown_to_pdf_candidate": commands["pandoc"]["available"]
            and (commands["xelatex"]["available"] or commands["lualatex"]["available"]),
            "cjk_xelatex_candidate": commands["xelatex"]["available"]
            and tex_files["xeCJK.sty"]["available"]
            and tex_files["fontspec.sty"]["available"],
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
