#!/usr/bin/env python3
"""Deck-level rhythm review consumer for research presentation production."""

from __future__ import annotations

import hashlib
import json
from copy import deepcopy
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
    "SANITIZE_AUDIENCE_COPY",
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
    render_input_identity: dict[str, Any],
    contact_sheet_path: str | None,
    contact_sheet_sha256: str | None,
) -> dict[str, Any]:
    rendered = render_status.get("rendered_png", [])
    render_ok = render_status.get("status") == "ok"
    pages = []
    for index, (spec, layout) in enumerate(zip(specs, layouts), start=1):
        rendered_index = index
        rendered_page = rendered[rendered_index] if rendered_index < len(rendered) else {}
        rendered_sha = rendered_page.get("sha256")
        rendered_path = rendered_page.get("path")
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
                "source_grounded_copy_candidates": {
                    key: spec.get(key)
                    for key in ["key_message", "annotation", "caption"]
                    if spec.get(key)
                },
                "forbidden_audience_terms": _forbidden_audience_terms(),
                "visual_density": visual_density(spec, layout),
                "rendered_page_path": rendered_path,
                "rendered_page_sha256": rendered_sha,
                "rendered_pixel_status": "AVAILABLE" if rendered_path and rendered_sha else "UNAVAILABLE_RENDER_NOT_OK",
                "transition_cue": spec.get("storyline_transition"),
            }
        )
    all_page_pixels_available = all(page["rendered_page_sha256"] for page in pages)
    pixel_evidence_available = render_ok and all_page_pixels_available and bool(contact_sheet_sha256)
    pixel_identity_payload = {
        "page_order": [page["logical_id"] for page in pages],
        "rendered_page_sha256": [page["rendered_page_sha256"] for page in pages],
        "contact_sheet_sha256": contact_sheet_sha256,
    }
    rendered_pixel_identity = stable_sha(pixel_identity_payload) if pixel_evidence_available else None
    pixel_status = {
        "status": "AVAILABLE" if pixel_evidence_available else "UNAVAILABLE_RENDER_NOT_OK",
        "render_status": render_status.get("status"),
        "rendered_png_count": render_status.get("png_count", len(rendered)),
        "rendered_page_sha256_nullable": not pixel_evidence_available,
        "contact_sheet_sha256_nullable": not pixel_evidence_available,
    }
    deck_identity_payload = {
        "render_input_identity_sha256": render_input_identity["sha256"],
        "rendered_pixel_identity_sha256": rendered_pixel_identity,
        "pixel_evidence_status": pixel_status["status"],
        "page_order": [page["logical_id"] for page in pages],
        "workstream_sequence": [page["workstream_id"] for page in pages],
        "title_sequence": [page["title"] for page in pages],
    }
    return {
        "schema": "RESEARCH_PRESENTATION_DECK_SEQUENCE_SUMMARY_V1",
        "page_count": len(pages),
        "render_input_identity_sha256": render_input_identity["sha256"],
        "render_input_manifest": render_input_identity,
        "pixel_evidence_status": pixel_status,
        "rendered_pixel_identity_sha256": rendered_pixel_identity,
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
        "deck_identity_sha256": stable_sha(deck_identity_payload),
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


def _as_list(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def _normalized_text(*values: Any) -> str:
    parts: list[str] = []
    for value in values:
        if isinstance(value, dict):
            parts.extend(str(item) for item in value.values())
        elif isinstance(value, list):
            parts.extend(str(item) for item in value)
        elif value is not None:
            parts.append(str(value))
    return " ".join(parts).lower()


def _resolve_target_logical_ids(finding: dict[str, Any], sequence_summary: dict[str, Any]) -> tuple[list[str], str | None]:
    pages = _page_by_logical_id(sequence_summary)
    by_page_id = {page["page_id"]: page["logical_id"] for page in sequence_summary.get("pages", [])}
    by_job: dict[str, list[str]] = {}
    for page in sequence_summary.get("pages", []):
        by_job.setdefault(str(page["page_job"]).upper(), []).append(page["logical_id"])

    raw_targets: list[Any] = []
    for key in ["target_logical_ids", "target_items", "target_page_ids", "target_logical_id", "target_page_id", "item_id"]:
        raw_targets.extend(_as_list(finding.get(key)))

    targets: list[str] = []
    for raw in raw_targets:
        target = str(raw)
        if target in pages:
            targets.append(target)
        elif target in by_page_id:
            targets.append(by_page_id[target])

    for job in _as_list(finding.get("target_page_job") or finding.get("page_job")):
        matches = by_job.get(str(job).upper(), [])
        if len(matches) == 1:
            targets.extend(matches)
        elif len(matches) > 1:
            return [], f"finding target page_job is not unique: {job}"

    deduped = list(dict.fromkeys(targets))
    if not deduped:
        return [], "finding lacks a structured target deck page"
    return deduped, None


def _requirement_text(finding: dict[str, Any]) -> str:
    return _normalized_text(
        finding.get("requirement_id"),
        finding.get("requirement_ids"),
        finding.get("category"),
        finding.get("scope"),
    )


def _finding_evidence_text(finding: dict[str, Any]) -> str:
    return _normalized_text(
        finding.get("summary"),
        finding.get("evidence"),
        finding.get("observation"),
        finding.get("observations"),
        finding.get("recommendation"),
    )


def _contains_any(text: str, terms: tuple[str, ...]) -> bool:
    return any(term in text for term in terms)


def _source_grounded_copy_candidates(page: dict[str, Any]) -> list[dict[str, str]]:
    candidates = []
    for field, value in page.get("source_grounded_copy_candidates", {}).items():
        text = str(value or "").strip()
        if text:
            candidates.append({"field": field, "text": text})
    return candidates


def _has_safe_audience_replacement(page: dict[str, Any]) -> bool:
    forbidden = tuple(str(term).lower() for term in page.get("forbidden_audience_terms", []))
    for candidate in _source_grounded_copy_candidates(page):
        lowered = candidate["text"].lower()
        if not _contains_any(lowered, forbidden):
            return True
    return False


def _infer_intent_for_page(finding: dict[str, Any], page: dict[str, Any]) -> tuple[str | None, str | None]:
    requirement = _requirement_text(finding)
    evidence = _finding_evidence_text(finding)
    combined = f"{requirement} {evidence}"
    page_job = str(page.get("page_job") or "").upper()
    object_kind = str(page.get("primary_scientific_object_type") or "").lower()
    density = page.get("visual_density", {})
    capacity_status = density.get("capacity_status")

    audience_terms = ("audience", "internal", "workflow", "provenance", "meta", "source bundle", "repo path", "qa")
    if _contains_any(requirement, ("audience", "internal", "workflow", "provenance", "meta")) and _contains_any(combined, audience_terms):
        if _has_safe_audience_replacement(page):
            return "SANITIZE_AUDIENCE_COPY", None
        return None, "audience-copy repair requires a same-page source-grounded replacement"

    if page_job == "MEDICAL_IMAGE_COMPARISON" and _contains_any(requirement, ("medical", "legend", "callout", "obstruction", "readable")):
        if _contains_any(evidence, ("legend", "callout", "obstruct", "cover", "overlay", "crop", "panel")):
            return "REPAIR_ANNOTATION_LEGEND", None

    if page_job in {"EXPERIMENT_DESIGN", "NEXT_EXPERIMENT"} and _contains_any(requirement, ("diagram", "process", "next", "collision", "layout", "readability")):
        if _contains_any(evidence, ("collision", "overlap", "crowd", "clipping", "label", "diagram")):
            return "SWAP_COMPATIBLE_GOLD_LAYOUT", None

    if object_kind in {"figure", "result_figure", "plot table", "presentation_native_coverage_figure", "negative_evidence_plot"}:
        if _contains_any(requirement, ("caption", "support", "layout", "overlap", "collision")) and _contains_any(evidence, ("caption", "support", "overlap", "collision", "clipping", "crowd")):
            return "REPAIR_ANNOTATION_LEGEND", None
        if _contains_any(requirement, ("readable", "readability", "primary", "scientific_object", "projection")) and _contains_any(evidence, ("small", "undersized", "unreadable", "projection", "scale")):
            if capacity_status == "SPLIT_REQUIRED":
                return "SPLIT_OVERDENSE_PAGE", None
            return "RESCALE_PRIMARY_OBJECT", None

    return None, "finding does not uniquely map to a frozen safe repair family"


def normalize_finding_for_repair(finding: dict[str, Any], sequence_summary: dict[str, Any]) -> tuple[dict[str, Any], str | None]:
    explicit_intent = str(finding.get("repair_intent") or finding.get("intent") or "")
    if explicit_intent:
        return finding, None

    target_logical_ids, reason = _resolve_target_logical_ids(finding, sequence_summary)
    if reason:
        return finding, reason

    pages = _page_by_logical_id(sequence_summary)
    inferred: list[str] = []
    for logical_id in target_logical_ids:
        intent, page_reason = _infer_intent_for_page(finding, pages[logical_id])
        if intent is None:
            return finding, page_reason
        inferred.append(intent)

    unique_intents = set(inferred)
    if len(unique_intents) != 1:
        return finding, f"finding maps to multiple repair families: {sorted(unique_intents)}"

    normalized = dict(finding)
    normalized["repair_intent"] = inferred[0]
    normalized["target_logical_ids"] = target_logical_ids
    normalized["normalized_repair_mapping"] = {
        "source": "structured_visual_finding_without_repair_intent",
        "requirement_basis": finding.get("requirement_id") or finding.get("requirement_ids"),
        "target_basis": target_logical_ids,
    }
    return normalized, None


def map_finding_to_directive(finding: dict[str, Any], sequence_summary: dict[str, Any]) -> tuple[dict[str, Any] | None, str | None]:
    finding, normalization_reason = normalize_finding_for_repair(finding, sequence_summary)
    if normalization_reason:
        return None, normalization_reason
    intent = str(finding.get("repair_intent") or finding.get("intent") or "")
    if intent not in ALLOWED_REPAIR_INTENTS:
        return None, f"unsupported repair intent: {intent or '<missing>'}"

    pages = _page_by_logical_id(sequence_summary)
    targets, target_reason = _resolve_target_logical_ids(finding, sequence_summary)
    if target_reason:
        return None, target_reason

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
    if finding.get("normalized_repair_mapping"):
        directive["normalized_repair_mapping"] = finding["normalized_repair_mapping"]
    if intent == "SANITIZE_AUDIENCE_COPY":
        directive["audience_copy_repair"] = {
            "remove_internal_meta_language": True,
            "replacement_scope": "same_page_source_grounded_copy_only",
            "candidate_fields": ["key_message", "annotation", "caption"],
        }
    return directive, None


def consume_review_evidence(
    *,
    review_evidence: dict[str, Any] | None,
    review_evidence_sha256: str | None,
    sequence_summary: dict[str, Any],
    initial_render_identity: str,
    initial_rendered_pixel_identity: str | None = None,
    initial_render_input_manifest: dict[str, Any] | None = None,
    repair_cycle_count: int = 0,
) -> dict[str, Any]:
    state: dict[str, Any] = {
        "schema": "RESEARCH_PRESENTATION_DECK_QUALITY_LOOP_STATE_V1",
        "max_repair_cycles": MAX_REPAIR_CYCLES,
        "repair_cycle_count": repair_cycle_count,
        "render_identity_kind": "render_input_identity_sha256",
        "initial_render_identity": initial_render_identity,
        "initial_render_input_identity": initial_render_identity,
        "initial_rendered_pixel_identity": initial_rendered_pixel_identity,
        "initial_render_input_manifest": initial_render_input_manifest,
        "review_evidence_identity": review_evidence_sha256,
        "deck_level_decision": None,
        "blocking_findings": [],
        "selected_repair_directives": [],
        "repair_allowed": False,
        "fail_closed_reason": None,
        "repaired_render_identity": None,
        "repaired_render_input_identity": None,
        "repaired_rendered_pixel_identity": None,
        "repaired_render_input_manifest": None,
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
    repaired = [deepcopy(spec) for spec in specs]
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
            elif directive["intent"] == "SWAP_COMPATIBLE_GOLD_LAYOUT":
                spec["compatible_layout_reflow_hint"] = "deck_quality_repair_source_faithful_reflow"
            elif directive["intent"] == "SPLIT_OVERDENSE_PAGE":
                spec["split_overdense_page_hint"] = "deck_quality_repair_split_required"
            elif directive["intent"] == "SANITIZE_AUDIENCE_COPY":
                replacement = _select_audience_copy_replacement(spec)
                if replacement:
                    field, text = replacement
                    trace = spec.setdefault("audience_copy_repair_trace", [])
                    changed = False
                    for target_field in ["annotation", "caption"]:
                        if target_field in spec and _contains_any(str(spec[target_field]).lower(), tuple(term.lower() for term in _forbidden_audience_terms())):
                            trace.append(
                                {
                                    "field": target_field,
                                    "original": spec[target_field],
                                    "replacement_source_field": field,
                                }
                            )
                            spec[target_field] = text
                            changed = True
                    if not changed and spec.get("annotation") != text:
                        trace.append(
                            {
                                "field": "annotation",
                                "original": spec.get("annotation"),
                                "replacement_source_field": field,
                                "reason": "reviewer identified internal/meta audience copy without a narrower local field match",
                            }
                        )
                        spec["annotation"] = text
    return repaired


def _forbidden_audience_terms() -> list[str]:
    return [
        "RRL-",
        "SRC-",
        "GSC-",
        "Reference retrieval",
        "EVIDENCE_MANIFEST",
        "Diagram contract",
        "QA",
        "repo path",
        "run ID",
        "implementation commit",
        "implementation language",
        "source bundle",
        "provenance",
        "review target",
        "fixture",
        "workflow",
    ]


def _select_audience_copy_replacement(spec: dict[str, Any]) -> tuple[str, str] | None:
    forbidden = tuple(term.lower() for term in _forbidden_audience_terms())
    for field in ["key_message", "caption", "annotation"]:
        text = str(spec.get(field) or "").strip()
        if text and not _contains_any(text.lower(), forbidden):
            return field, text
    return None
