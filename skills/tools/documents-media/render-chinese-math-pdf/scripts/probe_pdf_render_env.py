#!/usr/bin/env python3
"""Probe the deterministic Pandoc + XeLaTeX Chinese math PDF route."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
from pathlib import Path
from typing import Any, Iterable


RESOURCE_REL = Path("render_resources/chinese_math_pdf")
OVERRIDE_REL = Path(".config/ai-skills/local-overrides.toml")
DEFAULT_RENDERER = "pandoc_xelatex"
FONT_FILES = {
    "texgyretermes_regular": Path("fonts/texgyre-termes/texgyretermes-regular.otf"),
    "texgyretermes_bold": Path("fonts/texgyre-termes/texgyretermes-bold.otf"),
    "texgyretermes_italic": Path("fonts/texgyre-termes/texgyretermes-italic.otf"),
    "texgyretermes_bolditalic": Path("fonts/texgyre-termes/texgyretermes-bolditalic.otf"),
    "texgyretermes_math": Path("fonts/texgyre-termes-math/texgyretermes-math.otf"),
    "noto_serif_sc_regular": Path("texmf/fonts/opentype/public/noto-cjk/NotoSerifSC-Regular.otf"),
    "noto_serif_sc_bold": Path("texmf/fonts/opentype/public/noto-cjk/NotoSerifSC-Bold.otf"),
    "noto_sans_sc_regular": Path("texmf/fonts/opentype/public/noto-cjk/NotoSansSC-Regular.otf"),
    "noto_sans_sc_bold": Path("texmf/fonts/opentype/public/noto-cjk/NotoSansSC-Bold.otf"),
}
LATEX_PACKAGES = [
    "fontspec.sty",
    "xeCJK.sty",
    "unicode-math.sty",
    "geometry.sty",
    "graphicx.sty",
    "booktabs.sty",
    "longtable.sty",
    "xcolor.sty",
    "mathtools.sty",
]


def _safe_resolve(path: Path) -> Path:
    try:
        return path.expanduser().resolve()
    except OSError:
        return path.expanduser().absolute()


def _exists(path: Path) -> bool:
    try:
        return path.exists()
    except OSError:
        return False


def unique_paths(paths: Iterable[Path]) -> list[Path]:
    seen: set[str] = set()
    result: list[Path] = []
    for path in paths:
        resolved = _safe_resolve(path)
        key = str(resolved)
        if key in seen:
            continue
        seen.add(key)
        result.append(resolved)
    return result


def env_resource_dirs() -> list[Path]:
    raw = os.environ.get("CHINESE_MATH_PDF_RESOURCE_DIRS", "")
    if not raw:
        return []
    return [Path(item).expanduser() for item in raw.split(os.pathsep) if item.strip()]


def local_override_paths(explicit: Path | None = None) -> list[Path]:
    candidates: list[Path] = []
    if explicit is not None:
        candidates.append(explicit)
    namespace_root = os.environ.get("CODEX_NAMESPACE_ROOT")
    if namespace_root:
        candidates.append(Path(namespace_root) / OVERRIDE_REL)
    global_home = os.environ.get("CODEX_GLOBAL_HOME")
    if global_home:
        gh = Path(global_home)
        candidates.append(gh / OVERRIDE_REL)
        candidates.append(gh.parent / OVERRIDE_REL)
    home = os.environ.get("HOME")
    if home:
        candidates.append(Path(home) / OVERRIDE_REL)
    return unique_paths(candidates)


def parse_render_resource_dirs(text: str) -> list[str]:
    values: list[str] = []
    for line in text.splitlines():
        stripped = line.split("#", 1)[0].strip()
        if not stripped.startswith("render_resource_dirs") or "=" not in stripped:
            continue
        rhs = stripped.split("=", 1)[1].strip()
        if rhs.startswith("[") and rhs.endswith("]"):
            values.extend(re.findall(r'["\']([^"\']+)["\']', rhs))
        else:
            match = re.match(r'["\']([^"\']+)["\']', rhs)
            if match:
                values.append(match.group(1))
            elif rhs:
                values.append(rhs)
    return values


def local_override_resource_roots(path: Path) -> list[Path]:
    try:
        if not path.exists():
            return []
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return []
    roots: list[Path] = []
    for value in parse_render_resource_dirs(text):
        for item in value.split(os.pathsep):
            if item.strip():
                roots.append(Path(item).expanduser())
    return roots


def ancestor_resource_dirs(starts: Iterable[Path]) -> list[Path]:
    candidates: list[Path] = []
    for start in starts:
        current = _safe_resolve(start)
        if current.is_file():
            current = current.parent
        for parent in [current, *current.parents]:
            candidates.append(parent / RESOURCE_REL)
    return unique_paths(candidates)


def resource_candidates(
    root: Path | None = None,
    resource_dir: Path | None = None,
    local_override: Path | None = None,
) -> list[Path]:
    candidates: list[Path] = []
    ancestor_starts: list[Path] = []
    if resource_dir is not None:
        candidates.append(resource_dir)
    if root is not None:
        candidates.append(root / RESOURCE_REL)
        ancestor_starts.append(root)
    candidates.extend(env_resource_dirs())
    for override in local_override_paths(local_override):
        candidates.extend(local_override_resource_roots(override))
    ancestor_starts.append(Path.cwd())
    candidates.extend(ancestor_resource_dirs(ancestor_starts))
    return unique_paths(candidates)


def is_resource_dir(path: Path) -> bool:
    return _exists(path) and (
        _exists(path / "scripts" / "render_markdown_pdf.sh")
        or _exists(path / "templates" / "chinese_math_pandoc_header.tex.in")
        or any(_exists(path / rel) for rel in FONT_FILES.values())
    )


def find_resource(
    root: Path | None = None,
    resource_dir: Path | None = None,
    local_override: Path | None = None,
) -> Path | None:
    for candidate in resource_candidates(root, resource_dir, local_override):
        if is_resource_dir(candidate):
            return candidate
    return None


def resolve_command(name: str) -> str | None:
    found = shutil.which(name)
    if found:
        return found
    tinytex = Path.home() / ".TinyTeX/bin/x86_64-linux" / name
    if tinytex.exists():
        return str(tinytex)
    return None


def run(cmd: list[str], env: dict[str, str] | None = None) -> dict[str, Any]:
    executable = resolve_command(cmd[0]) if len(cmd) == 1 or "/" not in cmd[0] else cmd[0]
    if executable is None:
        return {"available": False, "path": None, "first_line": None}
    actual = [executable, *cmd[1:]]
    try:
        proc = subprocess.run(actual, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, timeout=15, env=env)
    except FileNotFoundError:
        return {"available": False, "path": executable, "first_line": None}
    except subprocess.TimeoutExpired:
        return {"available": False, "path": executable, "first_line": "timed out"}
    return {
        "available": proc.returncode == 0,
        "path": executable,
        "first_line": proc.stdout.splitlines()[0] if proc.stdout else "",
    }


def sha256(path: Path) -> str | None:
    if not path.exists():
        return None
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def policy_flags() -> dict[str, bool]:
    return {
        "times_new_roman": False,
        "windows_fonts_mount": False,
        "fc_match_times_new_roman": False,
        "chromium_latex_fallback": False,
    }


def build_probe_result(args: argparse.Namespace) -> dict[str, Any]:
    resource = find_resource(args.root, args.resource_dir, args.local_override)
    env = os.environ.copy()
    if resource:
        env["TEXMFHOME"] = str(resource / "texmf")

    commands = {
        "pandoc": run(["pandoc", "--version"]),
        "xelatex": run(["xelatex", "--version"]),
        "kpsewhich": run(["kpsewhich", "--version"]),
        "pdffonts": run(["pdffonts", "-v"]),
        "pdftotext": run(["pdftotext", "-v"]),
        "pdftoppm": run(["pdftoppm", "-v"]),
    }

    kpse = commands["kpsewhich"]["path"]
    packages: dict[str, Any] = {}
    if kpse:
        for pkg in LATEX_PACKAGES:
            proc = subprocess.run([kpse, pkg], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, env=env)
            packages[pkg] = {"available": proc.returncode == 0 and bool(proc.stdout.strip()), "path": proc.stdout.strip() or None}
    else:
        packages = {pkg: {"available": False, "path": None} for pkg in LATEX_PACKAGES}

    fonts: dict[str, Any] = {}
    if resource:
        for name, rel in FONT_FILES.items():
            path = resource / rel
            fonts[name] = {"path": str(path), "available": path.exists(), "sha256": sha256(path)}

    ready = bool(resource) and commands["pandoc"]["available"] and commands["xelatex"]["available"]
    ready = ready and all(item["available"] for item in packages.values()) and all(item["available"] for item in fonts.values())
    return {
        "resource_dir": str(resource) if resource else None,
        "resource_candidates": [str(path) for path in resource_candidates(args.root, args.resource_dir, args.local_override)],
        "local_override_paths_checked": [str(path) for path in local_override_paths(args.local_override)],
        "default_renderer": DEFAULT_RENDERER,
        "commands": commands,
        "latex_packages": packages,
        "fonts": fonts,
        "forbidden_default_dependencies": policy_flags(),
        "ready": ready,
        "failure_status": None if ready else "blocked_missing_dependency",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=None)
    parser.add_argument("--resource-dir", type=Path, default=None)
    parser.add_argument("--local-override", type=Path, default=None)
    parser.add_argument("--pretty", action="store_true")
    args = parser.parse_args()

    result = build_probe_result(args)
    print(json.dumps(result, indent=2 if args.pretty else None, ensure_ascii=False))
    return 0 if result["ready"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
