from __future__ import annotations

import sys
from pathlib import Path


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    scripts_dir = root / "scripts"
    if not scripts_dir.exists():
        raise SystemExit(
            "ai-skills must be run from an editable install of AI_Skills_Collection. "
            "Install with: python3 -m pip install --no-build-isolation -e /path/to/AI_Skills_Collection"
        )
    sys.path.insert(0, str(scripts_dir))
    from skills import main as skills_main

    return skills_main()
