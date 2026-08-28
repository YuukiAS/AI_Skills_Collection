#!/usr/bin/env python3
"""Deck-level rhythm review consumer for research presentation production."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


MAX_REPAIR_CYCLES = 1
ALLOWED_REPAIR_INTENTS = {
    "REORDER_WITHIN_SOURCE_DEPENDENCY",
    "ADJUST_TRANSITION_CUE",
    "SPLIT_OVERDENSE_PAGE",
    "REMOVE_OR_MERGE_REDUNDANT_PAGE",
    "SWAP_COMPATIBLE_GOLD_LAYOUT",
    "RESCALE_PRIMARY_OBJECT",
    "REPAIR_ANNOTATION_LEGEND",
}
FINAL_DECISIONS = {"READY_TO_DELIVER", "QUALITY_LOOP_FAIL_NO_WINNER"}
WAITING_DECISIONS = {"WAITING_FOR_DECK_VISUAL_REVIEW", "WAITING_FOR_REPAIRED_DECK_REVIEW"}
BLOCKING_DECISIONS = {"BLOCKER", "FAIL", "REVISE", "NEEDS_REPAIR"}


def stable_sha(payload: Any) -> str:
    text = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def file_sha(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def visual_density(spec: dict[str, Any], layout: dict[str, Any]) -> dict[str, Any]:
    primary = layout.get("resolved_primary_geometry", {})
    primary_area = round(float(primary.get("w", 0.0)) * float(primary.get("h", 0.0)), 4)
    object_count = len(layout.get("native_objects", []))
    declared = spec.get("query", {}).get("density") or "unknown"
    if object_count >= 7 or primary_area > 0.48:
        machine = "high"
    elif object_count >= 4 or primary_area > 0.30:
        machine = "moderate"
    else:
        machine = "low"
    return {
        "declared_density": declared,
        "machine_density": machine,
        "primary_area": primary_area,
        "native_object_count": object_count,
        "capacity_status": layout.get("content_capacity_check", {}).get("status"),
    }


def build_sequence_summary(
    *,
    specs: list[dict[str, Any]],
    layouts: list[dict[str, Any]],
    render_status: dict[str, Any],
    storyline_trace: dict[str, Any],
    contact_sheet_path: str | None,
    contact_sheet_sha256: str | None,
) -> dict[str, Any]:
    rendered = render_status.get("rendered_png", [])
    pages = []
    for index, (spec, layout) in enumerate(zip(specs, layouts), start=1):
        rendered_index = index
        rendered_page = rendered[rendered_index] if rendered_index < len(rendered) else {}
        logical_id = f"slide_{index + 1}_{spec['page_job'].lower()}"
        story = spec.get("storyline", {})
        pages.append(
            {
                "sequence_index": index,
                "rendered_slide_number": index + 1,
                "logical_id": logical_id,
                "page_id": spec["page_id"],
                "page_job": spec["page_job"],
                "title": spec["title"],
                "section": spec["section"],
                "workstream_id": story.get("workstream_id"),
                "workstream_label": story.get("workstream_label"),
                "workstream_order": story.get("workstream_order"),
                "source_evidence_ids": spec.get("source_evidence_ids", []),
                "selected_gold_id": layout.get("selected_gold_id"),
                "selected_reference_id": layout.get("selected_reference_id"),
                "primary_scientific_object_type": spec.get("dominant_object") or spec.get("content_kind"),
                "scientific_objects": spec.get("scientific_objects", []),
                "visual_density": visual_density(spec, layout),
                "rendered_page_path": rendered_page.get("path"),
                "rendered_page_sha256": rendered_page.get("sha256"),
                "transition_cue": spec.get("storyline_transition"),
            }
        )
    identity_payload = {
        "page_order": [page["logical_id"] for page in pages],
        "rendered_page_sha256": [page["rendered_page_sha256"] for page in pages],
        "workstream_sequence": [page["workstream_id"] for page in pages],
        "title_sequence": [page["title"] for page in pages],
        "contact_sheet_sha256": contact_sheet_sha256,
    }
    return {
        "schema": "RESEARCH_PRESENTATION_DECK_SEQUENCE_SUMMARY_V1",
        "page_count": len(pages),
        "page_order": [page["logical_id"] for page in pages],
        "title_sequence": [page["title"] for page in pages],
        "section_sequence": [page["section"] for page in pages],
        "workstream_sequence": [
            {
                "logical_id": page["logical_id"],
                "workstream_id": page["workstream_id"],
                "workstream_label": page["workstream_label"],
                "workstream_order": page["workstream_order"],
            }
            for page in pages
        ],
        "storyline_order": storyline_trace.get("storyline_order", []),
        "pages": pages,
        "deck_contact_sheet": {
            "path": contact_sheet_path,
            "sha256": contact_sheet_sha256,
            "serves_audience": False,
            "review_role": "deck_sequence_context",
        },
        "deck_identity_sha256": stable_sha(identity_payload),
    }


def load_review_evidence(path: Path | None) -> tuple[dict[str, Any] | None, str | None]:
    if path is None:
        return None, None
    evidence = json.loads(path.read_text(encoding="utf-8"))
    return evidence, file_sha(path)


def deck_item_reviews(evidence: dict[str, Any]) -> list[dict[str, Any]]:
    reviews = []
    for review in evidence.get("item_reviews", []):
        item_id = str(review.get("item_id") or review.get("logical_id") or "")
        scope = str(review.get("scope") or review.get("review_scope") or "").lower()
        if item_id in {"deck_contact_sheet", "deck_sequence_board"} or item_id.startswith("deck_") or scope == "deck":
            reviews.append(review)
    return reviews


def blocking_findings(evidence: dict[str, Any]) -> list[dict[str, Any]]:
    explicit = list(evidence.get("blocking_findings", []))
    if explicit:
        return explicit
    for review in deck_item_reviews(evidence):
        if str(review.get("decision", "")).upper() in BLOCKING_DECISIONS:
            finding = dict(review)
            finding.setdefault("finding_id", review.get("item_id", "deck_item_blocker"))
            finding.setdefault("repair_intent", review.get("repair_intent"))
            explicit.append(finding)
    return explicit


def _page_by_logical_id(sequence_summary: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {page["logical_id"]: page for page in sequence_summary.get("pages", [])}


def map_finding_to_directive(finding: dict[str, Any], sequence_summary: dict[str, Any]) -> tuple[dict[str, Any] | None, str | None]:
    intent = str(finding.get("repair_intent") or finding.get("intent") or "")
    if intent not in ALLOWED_REPAIR_INTENTS:
        return None, f"unsupported repair intent: {intent or '<missing>'}"

    pages = _page_by_logical_id(sequence_summary)
    targets = list(finding.get("target_logical_ids") or finding.get("target_items") or [])
    if not targets:
        target = finding.get("target_logical_id") or finding.get("item_id")
        if target and target in pages:
            targets = [target]
    missing = [target for target in targets if target not in pages]
    if missing:
        return None, f"finding targets unknown deck pages: {missing}"

    if intent == "ADJUST_TRANSITION_CUE" and not any(pages[target].get("transition_cue") for target in targets):
        return None, "ADJUST_TRANSITION_CUE requires an existing source-supported transition cue"

    if intent == "REORDER_WITHIN_SOURCE_DEPENDENCY":
        workstreams = {pages[target].get("workstream_id") for target in targets}
        if len(workstreams) != 1 and finding.get("source_dependency_allowed") is not True:
            return None, "REORDER_WITHIN_SOURCE_DEPENDENCY requires same-workstream targets or explicit source dependency allowance"

    if intent == "SPLIT_OVERDENSE_PAGE":
        if not any(pages[target].get("visual_density", {}).get("capacity_status") == "SPLIT_REQUIRED" for target in targets):
            return None, "SPLIT_OVERDENSE_PAGE requires an existing SPLIT_REQUIRED capacity signal"

    if intent == "REMOVE_OR_MERGE_REDUNDANT_PAGE" and finding.get("source_dependency_allowed") is not True:
        return None, "REMOVE_OR_MERGE_REDUNDANT_PAGE requires explicit source dependency allowance"

    directive = {
        "directive_id": f"repair_{stable_sha(finding)[:12]}",
        "intent": intent,
        "target_logical_ids": targets,
        "finding_id": finding.get("finding_id") or finding.get("item_id"),
        "reason": finding.get("summary") or finding.get("observation") or finding.get("reason") or "deck-level reviewer finding",
        "source_fidelity_constraints": {
            "may_rewrite_scientific_claims": False,
            "may_invent_source_relationships": False,
            "may_force_gold_id": False,
            "may_override_scores": False,
            "must_preserve_cuhk_identity": True,
        },
    }
    return directive, None


def consume_review_evidence(
    *,
    review_evidence: dict[str, Any] | None,
    review_evidence_sha256: str | None,
    sequence_summary: dict[str, Any],
    initial_render_identity: str,
    repair_cycle_count: int = 0,
) -> dict[str, Any]:
    state: dict[str, Any] = {
        "schema": "RESEARCH_PRESENTATION_DECK_QUALITY_LOOP_STATE_V1",
        "max_repair_cycles": MAX_REPAIR_CYCLES,
        "repair_cycle_count": repair_cycle_count,
        "initial_render_identity": initial_render_identity,
        "review_evidence_identity": review_evidence_sha256,
        "deck_level_decision": None,
        "blocking_findings": [],
        "selected_repair_directives": [],
        "repair_allowed": False,
        "fail_closed_reason": None,
        "repaired_render_identity": None,
        "final_decision": None,
    }
    if review_evidence is None:
        state["deck_level_decision"] = "WAITING_FOR_DECK_VISUAL_REVIEW"
        return state

    reviews = deck_item_reviews(review_evidence)
    if not reviews:
        state["deck_level_decision"] = "WAITING_FOR_DECK_VISUAL_REVIEW"
        state["fail_closed_reason"] = "review evidence lacks item-level deck/contact-sheet judgement"
        return state

    findings = blocking_findings(review_evidence)
    state["blocking_findings"] = findings
    if not findings and all(str(review.get("decision", "")).upper() == "PASS" for review in reviews):
        state["deck_level_decision"] = "PASS"
        state["final_decision"] = "READY_TO_DELIVER"
        return state

    if repair_cycle_count >= MAX_REPAIR_CYCLES:
        state["deck_level_decision"] = "BLOCKER_AFTER_REPAIR_BUDGET"
        state["final_decision"] = "QUALITY_LOOP_FAIL_NO_WINNER"
        state["fail_closed_reason"] = "deck blocker remains after the single allowed repair cycle"
        return state

    directives = []
    for finding in findings:
        directive, reason = map_finding_to_directive(finding, sequence_summary)
        if directive is None:
            state["deck_level_decision"] = "UNSAFE_REPAIR_MAPPING"
            state["final_decision"] = "QUALITY_LOOP_FAIL_NO_WINNER"
            state["fail_closed_reason"] = reason
            return state
        directives.append(directive)

    state["deck_level_decision"] = "REPAIR_SELECTED"
    state["selected_repair_directives"] = directives
    state["repair_allowed"] = True
    return state


def apply_repair_directives(specs: list[dict[str, Any]], directives: list[dict[str, Any]]) -> list[dict[str, Any]]:
    by_logical_id = {f"slide_{index + 1}_{spec['page_job'].lower()}": spec for index, spec in enumerate(specs, start=1)}
    repaired = [dict(spec) for spec in specs]
    repaired_by_logical_id = {f"slide_{index + 1}_{spec['page_job'].lower()}": spec for index, spec in enumerate(repaired, start=1)}
    for directive in directives:
        for logical_id in directive.get("target_logical_ids", []):
            if logical_id not in by_logical_id:
                continue
            spec = repaired_by_logical_id[logical_id]
            if directive["intent"] == "ADJUST_TRANSITION_CUE" and spec.get("storyline_transition"):
                transition = dict(spec["storyline_transition"])
                transition["cue_variant"] = "compact"
                transition["repair_directive_id"] = directive["directive_id"]
                spec["storyline_transition"] = transition
            elif directive["intent"] == "RESCALE_PRIMARY_OBJECT":
                spec["primary_object_scale_hint"] = "deck_quality_repair_projection_readability"
            elif directive["intent"] == "REPAIR_ANNOTATION_LEGEND":
                spec["legend_repair_hint"] = "deck_quality_repair_existing_annotation_only"
    return repaired
