#!/usr/bin/env python3
"""Deprecated compatibility shim for legacy bundle installs."""

from __future__ import annotations

import argparse
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

COMMAND_HINTS = {
    "base": "python scripts/skills.py install --target repo --profile global-baseline --mode symlink --write-agents-md",
    "full": "python scripts/skills.py install --target repo --profile research-main --mode symlink --write-agents-md",
    "research-writing": "python scripts/skills.py install --target repo --profile research-main --mode symlink --write-agents-md",
    "frontend": "python scripts/skills.py install --target repo --profile frontend-research-product --mode symlink --write-agents-md",
    "bioinformatics": "python scripts/skills.py install --target repo --profile bioinformatics-project --mode symlink --write-agents-md",
    "cmr": "python scripts/skills.py install --target repo --profile medical-imaging-project --mode symlink --write-agents-md",
}


def bundle_name(path_text: str) -> str:
    path = Path(path_text)
    return path.stem


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("bundle", help="Legacy bundle path, now archived under archive/legacy-bundles/")
    parser.add_argument("--target", help="Ignored legacy option")
    parser.add_argument("--mode", help="Ignored legacy option")
    args = parser.parse_args()

    name = bundle_name(args.bundle)
    archived = ROOT / "archive" / "legacy-bundles" / f"{name}.json"
    print("ERROR: scripts/install_bundle.py is deprecated and no longer installs files.")
    print(f"Archived bundle definition: {archived.relative_to(ROOT).as_posix()}")
    print("Use profile/domain/single-skill installs through scripts/skills.py instead.")
    print("")
    print("Recommended replacement:")
    print(f"  {COMMAND_HINTS.get(name, 'python scripts/skills.py install --target repo --profile research-main --mode symlink --write-agents-md')}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
