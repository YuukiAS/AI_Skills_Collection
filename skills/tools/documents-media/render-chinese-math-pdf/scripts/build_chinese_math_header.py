#!/usr/bin/env python3
"""Generate the deterministic XeLaTeX header used by chinese_math_pdf."""

from __future__ import annotations

import argparse
import importlib.util
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


def _load_probe_module():
    probe_path = Path(__file__).with_name("probe_pdf_render_env.py")
    spec = importlib.util.spec_from_file_location("probe_pdf_render_env", probe_path)
    if spec is None or spec.loader is None:
        raise SystemExit("blocked_missing_dependency: cannot load probe_pdf_render_env.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def resolve_resource_dir(root: Path | None, resource_dir: Path | None = None, local_override: Path | None = None) -> Path:
    if resource_dir is not None:
        return resource_dir.expanduser().resolve()
    probe = _load_probe_module()
    resolved = probe.find_resource(root=root, local_override=local_override)
    if resolved is None:
        raise SystemExit("blocked_missing_dependency: chinese_math_pdf resource root not found")
    return resolved


def build_header(args: argparse.Namespace) -> str:
    resource_dir = resolve_resource_dir(
        getattr(args, "root", None),
        getattr(args, "resource_dir", None),
        getattr(args, "local_override", None),
    )
    return HEADER_TEMPLATE.replace("__RESOURCE_DIR__", resource_dir.as_posix())


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=None)
    parser.add_argument("--resource-dir", type=Path, default=None)
    parser.add_argument("--local-override", type=Path, default=None)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    text = build_header(args)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(text, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
