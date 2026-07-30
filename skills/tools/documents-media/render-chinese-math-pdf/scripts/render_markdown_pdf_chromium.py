#!/usr/bin/env python3
"""Render Chinese Markdown to PDF through Pandoc HTML and headless Chromium."""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from probe_pdf_render_env import find_project_resource_bundles


CHROMIUM_COMMANDS = ["chromium-browser", "chromium", "google-chrome", "google-chrome-stable"]
FANDOL_FILES = {
    "regular": "FandolSong-Regular.otf",
    "bold": "FandolHei-Regular.otf",
    "italic": "FandolKai-Regular.otf",
}


def first_available_command(commands: list[str]) -> str | None:
    for command in commands:
        path = shutil.which(command)
        if path:
            return path
    return None


def find_font(resource_dir: Path, filename: str) -> Path | None:
    matches = sorted(resource_dir.rglob(filename)) if resource_dir.exists() else []
    return matches[0] if matches else None


def font_faces(resource_dir: Path | None) -> str:
    if not resource_dir:
        return ""
    regular = find_font(resource_dir, FANDOL_FILES["regular"])
    if not regular:
        return ""
    declarations = [
        "@font-face {",
        "  font-family: 'FandolSongLocal';",
        f"  src: url('{regular.as_uri()}') format('opentype');",
        "  font-weight: 400;",
        "  font-style: normal;",
        "}",
    ]
    bold = find_font(resource_dir, FANDOL_FILES["bold"])
    if bold:
        declarations.extend(
            [
                "@font-face {",
                "  font-family: 'FandolSongLocal';",
                f"  src: url('{bold.as_uri()}') format('opentype');",
                "  font-weight: 700;",
                "  font-style: normal;",
                "}",
            ]
        )
    italic = find_font(resource_dir, FANDOL_FILES["italic"])
    if italic:
        declarations.extend(
            [
                "@font-face {",
                "  font-family: 'FandolSongLocal';",
                f"  src: url('{italic.as_uri()}') format('opentype');",
                "  font-weight: 400;",
                "  font-style: italic;",
                "}",
            ]
        )
    return "\n".join(declarations)


def css_text(resource_dir: Path | None) -> str:
    faces = font_faces(resource_dir)
    return f"""<style>
{faces}
@page {{
  size: A4;
  margin: 22mm 18mm;
}}
html {{
  font-family: 'FandolSongLocal', 'Noto Serif CJK SC', 'Source Han Serif SC', serif;
  color: #111;
  line-height: 1.62;
}}
body {{
  max-width: 178mm;
  margin: 0 auto;
  font-size: 11.5pt;
}}
h1, h2, h3, strong, th {{
  font-family: 'FandolSongLocal', 'Noto Sans CJK SC', 'Source Han Sans SC', sans-serif;
}}
code, pre {{
  font-family: 'Noto Sans Mono CJK SC', 'Source Han Mono SC', monospace;
  overflow-wrap: anywhere;
}}
pre {{
  white-space: pre-wrap;
  word-break: break-word;
}}
table {{
  border-collapse: collapse;
  width: 100%;
  table-layout: fixed;
  display: table;
  margin: 1em 0;
  font-size: 9.5pt;
  overflow-wrap: anywhere;
}}
th, td {{
  border: 1px solid #bbb;
  padding: 4px 7px;
  vertical-align: top;
  word-break: break-word;
  overflow-wrap: anywhere;
}}
img {{
  max-width: 100%;
}}
</style>
"""


def choose_resource_dir(root: Path, explicit: Path | None) -> Path | None:
    if explicit:
        return explicit.resolve()
    bundles = find_project_resource_bundles(root)
    usable = [Path(item["path"]) for item in bundles if item["usable_chinese_math_bundle"]]
    return usable[0] if usable else None


def run(args: list[str], timeout: int = 120) -> None:
    proc = subprocess.run(args, check=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, timeout=timeout)
    if proc.returncode != 0:
        raise SystemExit(proc.stdout)


def render_markdown(args: argparse.Namespace) -> None:
    pandoc = first_available_command(["pandoc"])
    chromium = first_available_command(CHROMIUM_COMMANDS)
    if not pandoc:
        raise SystemExit("pandoc not found")
    if not chromium:
        raise SystemExit("chromium-browser/chromium/google-chrome not found")

    source = args.source.resolve()
    output = args.output.resolve()
    root = args.root.resolve() if args.root else source.parent
    resource_dir = choose_resource_dir(root, args.resource_dir)
    output.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(prefix="render-chinese-html-") as tmp:
        tmpdir = Path(tmp)
        css = tmpdir / "chinese-pdf-style.html"
        html = tmpdir / f"{source.stem}.html"
        css.write_text(css_text(resource_dir), encoding="utf-8")
        pandoc_args = [
            pandoc,
            str(source),
            "--from",
            "markdown+tex_math_dollars+tex_math_single_backslash",
            "--standalone",
            "--mathml",
            "--metadata",
            f"title={args.title or source.stem}",
            "--include-in-header",
            str(css),
            "-o",
            str(html),
        ]
        run(pandoc_args)
        if args.keep_html:
            args.keep_html.resolve().parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(html, args.keep_html.resolve())
        chrome_args = [
            chromium,
            "--headless",
            "--disable-gpu",
            "--no-sandbox",
            "--no-pdf-header-footer",
            "--allow-file-access-from-files",
            f"--print-to-pdf={output}",
            html.as_uri(),
        ]
        env = os.environ.copy()
        env.setdefault("XDG_RUNTIME_DIR", str(tmpdir / "xdg-runtime"))
        Path(env["XDG_RUNTIME_DIR"]).mkdir(parents=True, exist_ok=True)
        proc = subprocess.run(chrome_args, check=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, timeout=120, env=env)
        if proc.returncode != 0:
            legacy_args = [arg for arg in chrome_args if arg != "--no-pdf-header-footer"]
            legacy_args.insert(-2, "--print-to-pdf-no-header")
            proc = subprocess.run(legacy_args, check=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, timeout=120, env=env)
        if proc.returncode != 0:
            raise SystemExit(proc.stdout)
    if not output.exists() or output.stat().st_size == 0:
        raise SystemExit(f"Chromium did not create a non-empty PDF: {output}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="Input Markdown file.")
    parser.add_argument("output", type=Path, help="Output PDF path.")
    parser.add_argument("--root", type=Path, help="Project root used to locate render_resources/chinese_math_pdf.")
    parser.add_argument("--resource-dir", type=Path, help="Explicit Chinese render resource directory.")
    parser.add_argument("--title", help="PDF/HTML title.")
    parser.add_argument("--keep-html", type=Path, help="Optional path to keep the intermediate HTML for debugging.")
    args = parser.parse_args()
    render_markdown(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
