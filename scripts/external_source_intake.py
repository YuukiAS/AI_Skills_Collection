#!/usr/bin/env python3
"""Plan external source intake without committing temporary source material."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path

from skill_utils import ROOT


def source_id(source: str) -> str:
    slug = "".join(ch.lower() if ch.isalnum() else "-" for ch in source).strip("-")
    slug = "-".join(part for part in slug.split("-") if part)[:48] or "source"
    digest = hashlib.sha1(source.encode("utf-8")).hexdigest()[:8]
    return f"{slug}-{digest}"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", required=True, help="GitHub URL, Notion page id, URL, or local source label")
    parser.add_argument("--target", default="", help="Intended target skill or plugin")
    parser.add_argument("--dry-run", action="store_true", help="Only print the planned intake directory")
    args = parser.parse_args()

    sid = source_id(args.source)
    intake = ROOT / ".tmp" / "skill-intake" / sid
    print(f"source: {args.source}")
    print(f"target: {args.target or '(undecided)'}")
    print(f"intake_dir: {intake.relative_to(ROOT).as_posix()}")
    print("policy: record source identity, revision, license/permission, decision, target, and final integration commit")
    if not args.dry_run:
        intake.mkdir(parents=True, exist_ok=True)
        (intake / "README.md").write_text(
            "# External Source Intake\n\n"
            f"- source: {args.source}\n"
            f"- target: {args.target or '(undecided)'}\n"
            "- decision: pending\n",
            encoding="utf-8",
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
