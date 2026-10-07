"""Rendered review packet construction and page review."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from .detectors import run_detectors
from .features import inspect_rendered_png, text_geometry_features


CHECK_ORDER = [
    "shell",
    "typography",
    "scientific_object_internal_readability",
    "primary_object_scale",
    "whitespace",
    "reading_path",
    "peer_layout",
    "q_a_geometry",
    "evidence_interpretation_proximity",
    "code_output_proximity",
    "protected_object",
    "internal_identifier_or_markup_leak",
    "audience_boundary",
]


def build_review_packet(
    *,
    artifact_id: str,
    physical_page: int,
    page_png_path: Path,
    pdf_text_page: dict[str, Any],
    page_job: str,
    stable_targets: list[str],
    component_targets: list[str],
    guards: list[dict[str, Any]],
    protected_objects: list[dict[str, Any]] | None = None,
    page_role: str = "ordinary",
) -> dict[str, Any]:
    image = inspect_rendered_png(page_png_path)
    text = text_geometry_features(pdf_text_page, image["width"], image["height"])
    return {
        "artifact_id": artifact_id,
        "physical_page": physical_page,
        "page_png_path": str(page_png_path),
        "page_png_sha256": image["png_sha256"],
        "review_scope": "WHOLE_SLIDE",
        "page_job": page_job,
        "stable_targets": stable_targets,
        "component_targets": component_targets,
        "guards": guards,
        "protected_objects": protected_objects or [],
        "page_role": page_role,
        "features": {"image": image, "text": text},
    }


def review_rendered_page(packet: dict[str, Any], *, reviewer_context_id: str) -> dict[str, Any]:
    checks = run_detectors(packet)
    by_id = {c["check_id"]: c for c in checks}
    normalized_checks = {}
    for check_id in CHECK_ORDER:
        source = by_id.get(check_id)
        if source:
            normalized_checks[check_id] = source
        elif check_id == "primary_object_scale":
            normalized_checks[check_id] = by_id.get("object_scale_whitespace", {"check_id": check_id, "status": "N/A", "not_applicable_reason": "No object-scale detector output."})
        elif check_id == "whitespace":
            normalized_checks[check_id] = by_id.get("object_scale_whitespace", {"check_id": check_id, "status": "N/A", "not_applicable_reason": "No whitespace detector output."})
        elif check_id == "audience_boundary":
            normalized_checks[check_id] = by_id.get("internal_identifier_or_markup_leak", {"check_id": check_id, "status": "N/A", "not_applicable_reason": "No audience-boundary detector output."})
        else:
            normalized_checks[check_id] = {"check_id": check_id, "status": "N/A", "not_applicable_reason": "No applicable signal."}

    revise = [c for c in normalized_checks.values() if c.get("status") == "REVISE"]
    blocked = [c for c in normalized_checks.values() if c.get("status") == "BLOCKED"]
    positive = [p for c in normalized_checks.values() for p in c.get("positive_evidence", [])]
    negative = [n for c in normalized_checks.values() for n in c.get("negative_evidence", [])]
    if blocked:
        verdict = "BLOCKED"
    elif revise:
        verdict = "REVISE"
    elif positive:
        verdict = "PASS"
    else:
        verdict = "REVISE"
        negative.append("No positive visible evidence was produced; PASS fallthrough is forbidden.")
        normalized_checks["pass_fallthrough_guard"] = {
            "check_id": "pass_fallthrough_guard",
            "status": "REVISE",
            "finding_class": "PASS_FALLTHROUGH",
            "evidence": "No positive visible evidence was produced.",
        }

    locations = [loc for c in normalized_checks.values() for loc in c.get("locations", [])]
    issue_classes = sorted({c.get("finding_class") for c in normalized_checks.values() if c.get("finding_class")})
    image = packet["features"]["image"]
    text = packet["features"]["text"]
    largest = image.get("largest_component") or {}
    targets = ",".join((packet.get("stable_targets") or packet.get("component_targets") or ["unmapped"])[:3])
    guard_ids = ",".join(str(g.get("guard_id", "guard")) for g in packet.get("guards", [])[:3]) or "none"
    excerpt = " ".join((text.get("text_excerpt") or "").split()[:10])
    visible_context = (
        f"{packet['artifact_id']} P{packet['physical_page']} targets={targets} "
        f"guards={guard_ids} whole-slide PNG opened; words={text.get('word_count', 0)}, "
        f"median_word_px={text.get('median_word_height_px', 0)}, components={len(image.get('content_components', []))}, "
        f"body_bbox_ratio={image.get('body_bbox_area_ratio', 0)}, largest_bbox=({largest.get('x0')},{largest.get('y0')},{largest.get('x1')},{largest.get('y1')}), "
        f"text_start='{excerpt}'."
    )
    if revise:
        finding_summary = " ".join(f"{c.get('finding_class')}: {c.get('evidence', '')}" for c in revise[:3])
        headline = f"{visible_context} Visible finding(s): {finding_summary}"
    else:
        positive_summary = " ".join(positive[:3])
        headline = f"{visible_context} Positive visible evidence: {positive_summary}"
    return {
        "artifact_id": packet["artifact_id"],
        "physical_page": packet["physical_page"],
        "page_png_sha256": packet["page_png_sha256"],
        "reviewer_context_id": reviewer_context_id,
        "review_scope": "WHOLE_SLIDE",
        "checks": normalized_checks,
        "problem_locations": locations,
        "positive_visible_evidence": positive,
        "negative_visible_evidence": negative,
        "issue_classes": issue_classes,
        "overall_visual_verdict": verdict,
        "substantive_observation": headline,
    }
