#!/usr/bin/env python3
"""Probe local support for rendering Chinese/math documents to PDF."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import tempfile
from pathlib import Path
from typing import Any


COMMANDS = [
    "pandoc",
    "chromium-browser",
    "chromium",
    "google-chrome",
    "google-chrome-stable",
    "xelatex",
    "lualatex",
    "kpsewhich",
    "pdfinfo",
    "pdftotext",
    "pdffonts",
    "pdftoppm",
    "fc-match",
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

CJK_FONT_CANDIDATES = [
    "Noto Serif CJK SC",
    "Noto Sans CJK SC",
    "Source Han Serif SC",
    "Source Han Sans SC",
    "FandolSong",
    "AR PL UMing CN",
    "WenQuanYi Micro Hei",
]

LATIN_FONT_CANDIDATES = [
    "TeX Gyre Termes",
    "Liberation Serif",
    "Nimbus Roman",
    "STIX Two Text",
    "Times New Roman",
]

SHARED_RESOURCE_ROOTS = [
    Path("/users/a/e/aereinh/render_resources/chinese_math_pdf"),
    Path("/overflow/htzhu/mingcheng_new/render_resources/chinese_math_pdf"),
    Path("/overflow/htzhu/render_resources/chinese_math_pdf"),
]
LOCAL_OVERRIDE_RELATIVE = Path(".config") / "ai-skills" / "local-overrides.toml"


def run_version(command: str) -> str | None:
    for flag in ("--version", "-version", "-v"):
        try:
            with tempfile.TemporaryDirectory(prefix="pdf-render-probe-") as tmp:
                tmpdir = Path(tmp)
                env = os.environ.copy()
                env.setdefault("XDG_CACHE_HOME", str(tmpdir / "cache"))
                env.setdefault("XDG_CONFIG_HOME", str(tmpdir / "config"))
                env.setdefault("XDG_RUNTIME_DIR", str(tmpdir / "runtime"))
                Path(env["XDG_CACHE_HOME"]).mkdir(parents=True, exist_ok=True)
                Path(env["XDG_CONFIG_HOME"]).mkdir(parents=True, exist_ok=True)
                Path(env["XDG_RUNTIME_DIR"]).mkdir(parents=True, exist_ok=True)
                proc = subprocess.run(
                    [command, flag],
                    check=False,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True,
                    timeout=5,
                    env=env,
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


def first_available_command(commands: list[str]) -> str | None:
    for command in commands:
        if shutil.which(command):
            return command
    return None


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


def fontconfig_match(font_name: str) -> dict[str, Any]:
    fc_match = shutil.which("fc-match")
    if not fc_match:
        return {"available": False, "matched": None, "path": None, "reason": "fc-match not found"}
    try:
        proc = subprocess.run(
            [fc_match, "-f", "%{file}\t%{family}\n", font_name],
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=5,
        )
    except subprocess.TimeoutExpired:
        return {"available": False, "matched": None, "path": None, "reason": "fc-match timed out"}
    output = proc.stdout.strip()
    if proc.returncode != 0 or not output:
        return {"available": False, "matched": None, "path": None, "reason": proc.stderr.strip() or None}
    path, _, family = output.partition("\t")
    families = [item.strip() for item in family.split(",") if item.strip()]
    requested = font_name.lower()
    matched = any(requested == item.lower() for item in families)
    return {
        "available": matched,
        "matched": families[0] if families else None,
        "path": path or None,
        "reason": None if matched else f"fontconfig matched fallback family: {family}",
    }


def ancestor_dirs(root: Path) -> list[Path]:
    root = root.resolve()
    return [root, *root.parents]


def split_resource_list(raw: str | None) -> list[Path]:
    if not raw:
        return []
    text = str(raw).strip()
    if text.startswith("[") and text.endswith("]"):
        text = text[1:-1]
    items: list[Path] = []
    for chunk in text.replace(",", os.pathsep).split(os.pathsep):
        value = chunk.strip().strip("\"'")
        if value:
            items.append(Path(value).expanduser())
    return items


def env_resource_roots() -> list[Path]:
    return split_resource_list(os.environ.get("CHINESE_MATH_PDF_RESOURCE_DIRS", ""))


def local_override_resource_roots(path: Path) -> list[Path]:
    if not path.exists():
        return []
    roots: list[Path] = []
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = [part.strip() for part in line.split("=", 1)]
        if key != "render_resource_dirs":
            continue
        comment_index = value.find(" #")
        if comment_index != -1:
            value = value[:comment_index].strip()
        roots.extend(split_resource_list(value))
    return roots


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


def inferred_namespace_roots(root: Path) -> list[Path]:
    roots: list[Path] = []
    for env_name in ("CODEX_NAMESPACE_ROOT",):
        value = os.environ.get(env_name)
        if value:
            roots.append(Path(value).expanduser())

    global_home = os.environ.get("CODEX_GLOBAL_HOME")
    if global_home:
        roots.append(Path(global_home).expanduser().parent)

    resolved = root.resolve()
    parts = resolved.parts
    if len(parts) >= 5 and parts[1:4] == ("users", "a", "e"):
        roots.append(Path(*parts[:5]))
    if len(parts) >= 4 and parts[1:4] == ("overflow", "htzhu", "mingcheng_new"):
        roots.append(Path(*parts[:4]))

    roots.append(Path.home())

    found: list[Path] = []
    seen: set[Path] = set()
    for candidate in roots:
        try:
            key = candidate.resolve()
        except OSError:
            key = candidate
        if key in seen:
            continue
        seen.add(key)
        found.append(candidate)
    return found


def default_local_override_paths(root: Path) -> list[Path]:
    return [base / LOCAL_OVERRIDE_RELATIVE for base in inferred_namespace_roots(root)]


def find_project_resource_bundles(
    root: Path,
    local_overrides: list[Path] | None = None,
    local_override: Path | None = None,
) -> list[dict[str, Any]]:
    if local_override is not None:
        local_overrides = [local_override]
    candidates: list[Path] = []
    for base in ancestor_dirs(root):
        candidates.extend(
            [
                base / "render_resources" / "chinese_math_pdf",
                base / "texmf",
                base / ".texlive" / "texmf",
            ]
        )
    candidates.extend(env_resource_roots())
    for local_override in local_overrides or default_local_override_paths(root):
        candidates.extend(local_override_resource_roots(local_override))
    candidates.extend(SHARED_RESOURCE_ROOTS)
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
    parser.add_argument(
        "--local-override",
        type=Path,
        default=None,
        help="Explicit local ai-skills override file containing render_resource_dirs.",
    )
    args = parser.parse_args()

    local_overrides = (
        [args.local_override.expanduser()] if args.local_override else default_local_override_paths(args.root)
    )
    commands = {command: command_info(command) for command in COMMANDS}
    tex_files = {filename: kpsewhich_lookup(filename) for filename in TEX_FILES}
    fontconfig_fonts = {font: fontconfig_match(font) for font in CJK_FONT_CANDIDATES}
    latin_fontconfig_fonts = {font: fontconfig_match(font) for font in LATIN_FONT_CANDIDATES}
    local_override_roots: list[Path] = []
    for local_override in local_overrides:
        local_override_roots.extend(local_override_resource_roots(local_override))
    resource_bundles = find_project_resource_bundles(args.root, local_overrides=local_overrides)
    usable_bundles = [item for item in resource_bundles if item["usable_chinese_math_bundle"]]
    chromium_command = first_available_command(["chromium-browser", "chromium", "google-chrome", "google-chrome-stable"])
    usable_system_cjk_fonts = [font for font, info in fontconfig_fonts.items() if info["available"]]
    usable_latin_fonts = [font for font, info in latin_fontconfig_fonts.items() if info["available"]]
    xelatex_named_fonts_candidate = (
        commands["pandoc"]["available"]
        and commands["xelatex"]["available"]
        and tex_files["fontspec.sty"]["available"]
        and (tex_files["xeCJK.sty"]["available"] or bool(usable_bundles))
        and (bool(usable_bundles) or bool(usable_system_cjk_fonts))
    )
    html_chromium_candidate = (
        bool(chromium_command)
        and commands["pandoc"]["available"]
        and (bool(usable_bundles) or bool(usable_system_cjk_fonts))
    )
    if xelatex_named_fonts_candidate:
        preferred_route = "pandoc_xelatex_named_fonts"
    elif html_chromium_candidate:
        preferred_route = "pandoc_html_chromium_fallback"
    elif commands["xelatex"]["available"] or commands["lualatex"]["available"]:
        preferred_route = "direct_latex_if_source_is_tex"
    else:
        preferred_route = "blocked_missing_dependency"

    result = {
        "root": str(args.root.resolve()),
        "namespace_roots": [str(path) for path in inferred_namespace_roots(args.root)],
        "commands": commands,
        "tex_files": tex_files,
        "fontconfig_fonts": fontconfig_fonts,
        "latin_fontconfig_fonts": latin_fontconfig_fonts,
        "local_override": {
            "paths": [str(path) for path in local_overrides],
            "existing_paths": [str(path) for path in local_overrides if path.exists()],
            "exists": any(path.exists() for path in local_overrides),
            "render_resource_dirs": [str(path) for path in local_override_roots],
        },
        "project_resources": [item["path"] for item in resource_bundles],
        "project_resource_bundles": resource_bundles,
        "summary": {
            "markdown_to_pdf_candidate": commands["pandoc"]["available"]
            and (commands["xelatex"]["available"] or commands["lualatex"]["available"]),
            "cjk_xelatex_candidate": xelatex_named_fonts_candidate,
            "final_standard_pdf_candidate": xelatex_named_fonts_candidate,
            "html_chromium_candidate": html_chromium_candidate,
            "chromium_command": chromium_command,
            "usable_system_cjk_fonts": usable_system_cjk_fonts,
            "usable_latin_fonts": usable_latin_fonts,
            "usable_resource_bundle_count": len(usable_bundles),
            "recommended_resource_dir": usable_bundles[0]["path"] if usable_bundles else None,
            "preferred_route": preferred_route,
            "font_policy": {
                "preferred_latin": "TeX Gyre Termes",
                "preferred_cjk": "FandolSong from the selected resource bundle, or Noto/Source Han CJK",
                "avoid_required_times_new_roman": True,
                "chromium_type3_warning": "Chromium/Skia PDF output may embed local CJK fonts as unnamed Type 3 fonts.",
            },
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
