#!/usr/bin/env python3
"""Probe the deterministic Pandoc + XeLaTeX Chinese math PDF route."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
from pathlib import Path
from typing import Any


RESOURCE_REL = Path("render_resources/chinese_math_pdf")
STANDARD_ROOTS = [
    Path("/overflow/htzhu/mingcheng_new/render_resources/chinese_math_pdf"),
    Path("/users/a/e/aereinh/render_resources/chinese_math_pdf"),
    Path("/home/yuukias/render_resources/chinese_math_pdf"),
]
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


def run(cmd: list[str], env: dict[str, str] | None = None) -> dict[str, Any]:
    try:
        proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, timeout=15, env=env)
    except FileNotFoundError:
        return {"available": False, "path": None, "first_line": None}
    except subprocess.TimeoutExpired:
        return {"available": False, "path": shutil.which(cmd[0]), "first_line": "timed out"}
    return {
        "available": proc.returncode == 0,
        "path": shutil.which(cmd[0]) or cmd[0],
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


def find_resource(root: Path | None, resource_dir: Path | None = None) -> Path | None:
    candidates: list[Path] = []
    if resource_dir is not None:
        candidates.append(resource_dir.expanduser())
    env_roots = os.environ.get("CHINESE_MATH_PDF_RESOURCE_DIRS", "")
    for item in env_roots.split(":"):
        if item:
            candidates.append(Path(item).expanduser())
    if root is not None:
        root = root.expanduser()
        candidates.extend([root, root / RESOURCE_REL])
    cwd = Path.cwd().resolve()
    candidates.extend([cwd / RESOURCE_REL, Path.home() / RESOURCE_REL])
    prefix_ranked = []
    for standard in STANDARD_ROOTS:
        parent_prefix = standard.parent.parent
        try:
            cwd.relative_to(parent_prefix)
            prefix_ranked.insert(0, standard)
        except ValueError:
            prefix_ranked.append(standard)
    candidates.extend(prefix_ranked)
    seen: set[Path] = set()
    for candidate in candidates:
        resolved = candidate.resolve()
        if resolved in seen:
            continue
        seen.add(resolved)
        if (resolved / "scripts" / "render_markdown_pdf.sh").exists():
            return resolved
    return None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=None)
    parser.add_argument("--resource-dir", type=Path, default=None)
    parser.add_argument("--pretty", action="store_true")
    args = parser.parse_args()

    resource = find_resource(args.root, args.resource_dir)
    env = os.environ.copy()
    if resource:
        env["TEXMFHOME"] = str(resource / "texmf")

    commands = {
        "pandoc": run(["pandoc", "--version"]),
        "xelatex": run(["xelatex", "--version"]),
        "kpsewhich": run(["kpsewhich", "--version"]),
        "pdffonts": run(["bash", "-lc", "pdffonts -v 2>&1"]),
        "pdftotext": run(["bash", "-lc", "pdftotext -v 2>&1"]),
        "pdftoppm": run(["bash", "-lc", "pdftoppm -v 2>&1"]),
    }
    tinytex = Path.home() / ".TinyTeX/bin/x86_64-linux"
    if not commands["xelatex"]["available"] and (tinytex / "xelatex").exists():
        commands["xelatex"] = run([str(tinytex / "xelatex"), "--version"])
    if not commands["kpsewhich"]["available"] and (tinytex / "kpsewhich").exists():
        commands["kpsewhich"] = run([str(tinytex / "kpsewhich"), "--version"])

    kpse = commands["kpsewhich"]["path"]
    packages: dict[str, Any] = {}
    if kpse:
        for pkg in LATEX_PACKAGES:
            proc = subprocess.run([kpse, pkg], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, env=env)
            packages[pkg] = {"available": proc.returncode == 0 and bool(proc.stdout.strip()), "path": proc.stdout.strip() or None}
    else:
        packages = {pkg: {"available": False, "path": None} for pkg in LATEX_PACKAGES}

    fonts = {}
    if resource:
        for name, rel in FONT_FILES.items():
            path = resource / rel
            fonts[name] = {"path": str(path), "available": path.exists(), "sha256": sha256(path)}

    result = {
        "resource_dir": str(resource) if resource else None,
        "default_renderer": "pandoc_xelatex",
        "commands": commands,
        "latex_packages": packages,
        "fonts": fonts,
        "forbidden_default_dependencies": {
            "times_new_roman": False,
            "windows_fonts_mount": False,
            "fc_match_times_new_roman": False,
            "chromium_latex_fallback": False,
        },
        "ready": bool(resource)
        and commands["pandoc"]["available"]
        and commands["xelatex"]["available"]
        and all(item["available"] for item in packages.values())
        and all(item["available"] for item in fonts.values()),
    }
    print(json.dumps(result, indent=2 if args.pretty else None, ensure_ascii=False))
    return 0 if result["ready"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
