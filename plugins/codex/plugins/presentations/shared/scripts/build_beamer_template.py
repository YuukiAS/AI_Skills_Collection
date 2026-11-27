#!/usr/bin/env python3
"""Stage an editable Beamer source tree and build it with the shared fixed fonts."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

import generate_research_standard_scientific_layout_stage3 as renderer

TEMPLATES = renderer.SHARED / "templates"
SKINS = ("research_standard",)


def build(skin: str, destination: Path, source: Path | None = None, document: Path | None = None) -> dict:
    source = source or TEMPLATES / skin / "beamer" / "source"
    if not (source / "main.tex").is_file():
        raise ValueError(f"Expected an editable main.tex in {source}")
    if destination.exists():
        raise ValueError(f"Build directory already exists: {destination}")
    if destination.resolve().is_relative_to(source.resolve()):
        raise ValueError("Use a separate build directory outside the source tree")
    renderer.copy_beamer_source(source, destination)
    if document is not None:
        (destination / "main.tex").write_bytes(document.read_bytes())
    return renderer.compile_pdf(destination)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skin", choices=SKINS, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    parser.add_argument("--source-dir", type=Path, help="Editable source directory containing main.tex and its assets")
    args = parser.parse_args()
    try:
        result = build(args.skin, args.out_dir.resolve(), args.source_dir)
    except (OSError, ValueError) as error:
        parser.error(str(error))
    (args.out_dir / "build-receipt.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    return 0 if result["status"] == "COMPILED" else 2


if __name__ == "__main__":
    sys.exit(main())
