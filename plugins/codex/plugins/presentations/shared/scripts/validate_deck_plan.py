#!/usr/bin/env python3
"""Validate the repository deck-plan JSON subset without external packages."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


REQUIRED_METADATA = {"title", "audience", "mode", "purpose", "duration_minutes", "language", "template", "output"}
AUDIENCES = {"specialist", "mixed", "general", "executive"}
MODES = {"research", "business"}
PURPOSES = {"group-meeting", "conference", "defense", "journal-club", "company", "other"}
LANGUAGES = {"en", "zh", "mixed"}
OUTPUTS = {"pptx", "tex", "pdf", "google-slides"}


def validate_deck_plan(data: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if data.get("schema_version") != 1:
        errors.append("schema_version must be 1")
    metadata = data.get("metadata")
    if not isinstance(metadata, dict):
        errors.append("metadata must be an object")
        metadata = {}
    missing = sorted(REQUIRED_METADATA - set(metadata))
    if missing:
        errors.append(f"metadata missing required fields: {', '.join(missing)}")
    for key, allowed in {
        "audience": AUDIENCES,
        "mode": MODES,
        "purpose": PURPOSES,
        "language": LANGUAGES,
        "output": OUTPUTS,
    }.items():
        if key in metadata and metadata[key] not in allowed:
            errors.append(f"metadata.{key} must be one of {', '.join(sorted(allowed))}")
    if not isinstance(metadata.get("duration_minutes", 1), int) or metadata.get("duration_minutes", 1) < 1:
        errors.append("metadata.duration_minutes must be a positive integer")

    slides = data.get("slides")
    if not isinstance(slides, list) or not slides:
        errors.append("slides must be a non-empty array")
        return errors
    seen_ids: set[str] = set()
    for index, slide in enumerate(slides, start=1):
        if not isinstance(slide, dict):
            errors.append(f"slides[{index}] must be an object")
            continue
        for field in ("id", "title", "key_message"):
            if not slide.get(field):
                errors.append(f"slides[{index}] missing {field}")
        slide_id = str(slide.get("id") or "")
        if slide_id in seen_ids:
            errors.append(f"duplicate slide id: {slide_id}")
        seen_ids.add(slide_id)
        anchors = slide.get("source_anchors", [])
        if anchors and not isinstance(anchors, list):
            errors.append(f"slides[{index}].source_anchors must be an array")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("deck_plan", type=Path)
    parser.add_argument("--check", action="store_true", help="Return non-zero on validation errors")
    args = parser.parse_args()
    data = json.loads(args.deck_plan.read_text(encoding="utf-8"))
    errors = validate_deck_plan(data)
    for error in errors:
        print(f"ERROR: {error}")
    if not errors:
        print("deck plan validation passed")
    return 1 if args.check and errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
