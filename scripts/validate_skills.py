#!/usr/bin/env python3
"""Validate basic skill and bundle layout."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    errors: list[str] = []

    for skill_file in sorted((ROOT / "skills").rglob("SKILL.md")):
        rel = skill_file.relative_to(ROOT)
        if len(rel.parts) < 5:
            errors.append(f"skill is not under skills/<scope>/<category>/<skill>: {rel}")
        if not skill_file.read_text(encoding="utf-8", errors="replace").strip():
            errors.append(f"empty SKILL.md: {rel}")

    for bundle_file in sorted((ROOT / "bundles").glob("*.json")):
        try:
            bundle = json.loads(bundle_file.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"invalid JSON in {bundle_file.relative_to(ROOT)}: {exc}")
            continue

        include = bundle.get("include")
        if not isinstance(include, list):
            errors.append(f"bundle missing include list: {bundle_file.relative_to(ROOT)}")
            continue
        for item in include:
            if not isinstance(item, str):
                errors.append(f"bundle include item is not a string: {bundle_file.relative_to(ROOT)}")
                continue
            if not (ROOT / item).exists():
                errors.append(f"bundle path does not exist: {bundle_file.relative_to(ROOT)} -> {item}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print("skills and bundles validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
