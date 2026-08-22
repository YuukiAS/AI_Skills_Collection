#!/usr/bin/env python3
"""Mechanically review the medical-imaging group-meeting benchmark render."""

from __future__ import annotations

import sys
from pathlib import Path


RESEARCH_FIXTURE = Path(__file__).resolve().parents[1] / "research_group_meeting"
sys.path.insert(0, str(RESEARCH_FIXTURE))

import review_research_group_meeting_regression as base_review  # noqa: E402


if __name__ == "__main__":
    raise SystemExit(base_review.main())
