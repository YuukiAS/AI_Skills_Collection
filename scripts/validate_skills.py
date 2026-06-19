#!/usr/bin/env python3
"""Compatibility wrapper for scripts/skills.py validate."""

from __future__ import annotations

from skills import main


if __name__ == "__main__":
    raise SystemExit(main(["validate"]))
