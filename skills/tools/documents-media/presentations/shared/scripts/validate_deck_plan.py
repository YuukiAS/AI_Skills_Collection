#!/usr/bin/env python3
"""Validate the repository deck-plan JSON subset without external packages."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


REQUIRED_METADATA = {"title", "audience", "mode", "purpose", "duration_minutes", "language", "template", "output", "editability"}
AUDIENCES = {"specialist", "mixed", "general", "executive"}
MODES = {"research", "research-group-meeting", "business"}
PURPOSES = {"group-meeting", "conference", "defense", "journal-club", "company", "other"}
LANGUAGES = {"en", "zh", "mixed"}
OUTPUTS = {"pptx", "tex", "pdf", "google-slides"}
EDITABILITY = {"editable", "source-editable", "static", "plan-only"}
RESEARCH_STATE_FIELDS = {
    "previous_question",
    "prior_belief",
    "new_evidence",
    "evidence_quality",
    "belief_update",
    "successes",
    "failures",
    "largest_uncertainty",
    "frozen_items",
    "stop_items",
    "next_discriminating_experiment",
    "decision_needed",
}
EVIDENCE_BOARD_FIELDS = {
    "available_figures",
    "medical_images",
    "qualitative_examples",
    "quantitative_plots",
    "model_diagrams",
    "equations",
    "experiment_logs",
    "failed_experiments",
    "literature_figures_to_redraw",
    "missing_evidence",
}
RESEARCH_SLIDE_FIELDS = {
    "page_function",
    "required_evidence",
    "source_evidence_ids",
    "scientific_objects",
    "evidence_status",
    "layout_rationale",
    "allowed_fallback",
    "forbidden_fallback",
    "qa_criteria",
}
EVIDENCE_STATUSES = {"available", "partial", "missing", "planned", "not-needed"}
ANTI_PATTERN_TERMS = {
    "strategic pillar",
    "unlock",
    "key lever",
    "value proposition",
    "evidence-free roadmap",
    "rounded-card dashboard",
    "giant empty table",
    "decorative icon",
    "generic arrows",
}
WEAK_LAYOUT_HINTS = {"card", "cards", "table", "matrix", "dashboard", "timeline"}


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
        "editability": EDITABILITY,
    }.items():
        if key in metadata and metadata[key] not in allowed:
            errors.append(f"metadata.{key} must be one of {', '.join(sorted(allowed))}")
    if not isinstance(metadata.get("duration_minutes", 1), int) or metadata.get("duration_minutes", 1) < 1:
        errors.append("metadata.duration_minutes must be a positive integer")
    research_group_mode = metadata.get("mode") == "research-group-meeting"
    if research_group_mode:
        if metadata.get("purpose") != "group-meeting":
            errors.append("research-group-meeting mode requires metadata.purpose=group-meeting")
        research_state = data.get("research_state")
        if not isinstance(research_state, dict):
            errors.append("research_state must be an object for research-group-meeting mode")
            research_state = {}
        missing_state = sorted(field for field in RESEARCH_STATE_FIELDS if not research_state.get(field))
        if missing_state:
            errors.append(f"research_state missing required fields: {', '.join(missing_state)}")
        evidence_board = data.get("evidence_board")
        if not isinstance(evidence_board, dict):
            errors.append("evidence_board must be an object for research-group-meeting mode")
            evidence_board = {}
        missing_board = sorted(field for field in EVIDENCE_BOARD_FIELDS if field not in evidence_board)
        if missing_board:
            errors.append(f"evidence_board missing required fields: {', '.join(missing_board)}")
        for field in sorted(EVIDENCE_BOARD_FIELDS & set(evidence_board)):
            if not isinstance(evidence_board[field], list):
                errors.append(f"evidence_board.{field} must be an array")

    slides = data.get("slides")
    if not isinstance(slides, list) or not slides:
        errors.append("slides must be a non-empty array")
        return errors
    seen_ids: set[str] = set()
    for index, slide in enumerate(slides, start=1):
        if not isinstance(slide, dict):
            errors.append(f"slides[{index}] must be an object")
            continue
        for field in ("id", "title", "key_message", "slide_purpose", "visual_intent"):
            if not slide.get(field):
                errors.append(f"slides[{index}] missing {field}")
        slide_id = str(slide.get("id") or "")
        if slide_id in seen_ids:
            errors.append(f"duplicate slide id: {slide_id}")
        seen_ids.add(slide_id)
        anchors = slide.get("source_anchors", [])
        if anchors and not isinstance(anchors, list):
            errors.append(f"slides[{index}].source_anchors must be an array")
        if research_group_mode:
            for field in sorted(RESEARCH_SLIDE_FIELDS):
                if not slide.get(field):
                    errors.append(f"slides[{index}] missing {field} for research-group-meeting mode")
            evidence_status = slide.get("evidence_status")
            if evidence_status and evidence_status not in EVIDENCE_STATUSES:
                errors.append(f"slides[{index}].evidence_status must be one of {', '.join(sorted(EVIDENCE_STATUSES))}")
            for field in ("required_evidence", "source_evidence_ids", "scientific_objects", "qa_criteria"):
                if field in slide and not isinstance(slide[field], list):
                    errors.append(f"slides[{index}].{field} must be an array")
            if evidence_status in {"available", "partial"} and not slide.get("source_evidence_ids"):
                errors.append(f"slides[{index}] available evidence requires source_evidence_ids")
            if evidence_status == "missing" and not (
                str(slide.get("allowed_fallback", "")).lower().find("missing evidence") >= 0
                or str(slide.get("allowed_fallback", "")).lower().find("next experiment") >= 0
                or str(slide.get("speaker_notes", "")).lower().find("missing evidence") >= 0
            ):
                errors.append(f"slides[{index}] missing evidence must fallback to missing evidence, next experiment, or speaker notes")
            scanned_text_fields = (
                "title",
                "key_message",
                "slide_purpose",
                "visual_intent",
                "layout_hint",
                "layout_rationale",
                "speaker_notes",
                "audience_decision",
            )
            text_blob = "\n".join(str(slide.get(field, "")) for field in scanned_text_fields).lower()
            for term in ANTI_PATTERN_TERMS:
                if term in text_blob:
                    errors.append(f"slides[{index}] contains research presentation anti-pattern term: {term}")
            layout_hint = str(slide.get("layout_hint", "")).strip().lower()
            if layout_hint in WEAK_LAYOUT_HINTS:
                errors.append(f"slides[{index}].layout_hint cannot be only {layout_hint}; describe the scientific object topology")
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
