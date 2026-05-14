#!/usr/bin/env python3
"""Generate registry.json from SKILL.md files with governance metadata."""

from __future__ import annotations

import argparse
import json

from skill_utils import ROOT, iter_skill_files, skill_record, utc_now


REGISTRY = ROOT / "registry.json"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--include-archive", action="store_true", help="Include archived skills and skills under skills/archive")
    args = parser.parse_args()

    records = [skill_record(path) for path in iter_skill_files(include_archive=args.include_archive)]
    output = {
        "version": "2.0.0",
        "generated_at": utc_now(),
        "description": "Generated skill registry for AI_Skills_Collection. Do not edit by hand.",
        "include_archive": bool(args.include_archive),
        "skill_count": len(records),
        "skills": records,
    }
    REGISTRY.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {REGISTRY.relative_to(ROOT)} with {len(records)} skills")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
