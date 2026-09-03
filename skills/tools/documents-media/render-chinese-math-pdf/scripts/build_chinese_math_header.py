#!/usr/bin/env python3
"""Generate the deterministic XeLaTeX header used by chinese_math_pdf."""

from __future__ import annotations

import argparse
from pathlib import Path


HEADER_TEMPLATE = r"""\usepackage{fontspec}
\usepackage{xeCJK}
\usepackage{unicode-math}
\usepackage{amsmath}
\usepackage{mathtools}
\usepackage{booktabs}
\usepackage{longtable}
\usepackage{array}
\usepackage{xcolor}
\usepackage{hyperref}

\defaultfontfeatures{Ligatures=TeX}

\setmainfont[
  Path=__RESOURCE_DIR__/fonts/texgyre-termes/,
  Extension=.otf,
  UprightFont=texgyretermes-regular,
  BoldFont=texgyretermes-bold,
  ItalicFont=texgyretermes-italic,
  BoldItalicFont=texgyretermes-bolditalic
]{texgyretermes-regular}

\setmathfont[
  Path=__RESOURCE_DIR__/fonts/texgyre-termes-math/,
  Extension=.otf
]{texgyretermes-math}

\setCJKmainfont[
  Path=__RESOURCE_DIR__/texmf/fonts/opentype/public/noto-cjk/,
  Extension=.otf,
  UprightFont=NotoSerifSC-Regular,
  BoldFont=NotoSerifSC-Bold,
  AutoFakeSlant=0.18
]{NotoSerifSC-Regular}

\setCJKsansfont[
  Path=__RESOURCE_DIR__/texmf/fonts/opentype/public/noto-cjk/,
  Extension=.otf,
  UprightFont=NotoSansSC-Regular,
  BoldFont=NotoSansSC-Bold,
  AutoFakeSlant=0.18
]{NotoSansSC-Regular}

\setCJKmonofont[
  Path=__RESOURCE_DIR__/texmf/fonts/opentype/public/noto-cjk/,
  Extension=.otf,
  UprightFont=NotoSansSC-Regular,
  BoldFont=NotoSansSC-Bold
]{NotoSansSC-Regular}

\hypersetup{colorlinks=true,linkcolor=blue,urlcolor=blue,citecolor=blue}
\emergencystretch=3em
"""


def resolve_resource_dir(root: Path | None) -> Path:
    candidates: list[Path] = []
    if root is not None:
        root = root.expanduser().resolve()
        candidates.extend([root, root / "render_resources" / "chinese_math_pdf"])
    candidates.extend(
        [
            Path.cwd() / "render_resources" / "chinese_math_pdf",
            Path.home() / "render_resources" / "chinese_math_pdf",
            Path("/overflow/htzhu/mingcheng_new/render_resources/chinese_math_pdf"),
            Path("/users/a/e/aereinh/render_resources/chinese_math_pdf"),
            Path("/home/yuukias/render_resources/chinese_math_pdf"),
        ]
    )
    for candidate in candidates:
        if (candidate / "templates" / "chinese_math_pandoc_header.tex.in").exists():
            return candidate
    raise SystemExit("blocked_missing_dependency: chinese_math_pdf resource root not found")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=None)
    parser.add_argument("--resource-dir", type=Path, default=None)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    resource_dir = args.resource_dir.expanduser().resolve() if args.resource_dir else resolve_resource_dir(args.root)
    text = HEADER_TEMPLATE.replace("__RESOURCE_DIR__", resource_dir.as_posix())
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(text, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
