#!/usr/bin/env python3
"""Compatibility wrapper for scripts/skills.py audit."""

from __future__ import annotations

import sys
from pathlib import Path

from skills import main


def translate(argv: list[str]) -> list[str]:
    if not argv:
        return ["audit"]
    if argv == ["--all"]:
        return ["audit", "--all"]
    if argv[0] == "--project":
        return ["doctor", "--project", argv[1]] if len(argv) > 1 else ["doctor"]
    if argv[0].startswith("profiles/") or Path(argv[0]).suffix == ".json":
        return ["audit", "--profile", Path(argv[0]).stem]
    return ["audit", *argv]


if __name__ == "__main__":
    raise SystemExit(main(translate(sys.argv[1:])))
