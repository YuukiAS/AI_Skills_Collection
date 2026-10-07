"""Rendered review packet construction and reviewer-row validation.

The generic core deliberately does not author final rendered-review verdicts.
Fresh read-only reviewer workers must inspect exact page PNGs and write rows.
This module builds packets and validates those externally authored rows.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

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
    applicability: dict[str, bool] | None = None,
    forbidden_identifier_patterns: list[str] | None = None,
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
        "applicability": applicability or {},
        "forbidden_identifier_patterns": forbidden_identifier_patterns or [],
        "features": {"image": image, "text": text},
    }


def blocked_rendered_review_row(packet: dict[str, Any], *, reason: str) -> dict[str, Any]:
    checks = {
        check_id: {
            "check_id": check_id,
            "status": "BLOCKED",
            "evidence": reason,
            "finding_class": "RENDERED_REVIEW_BLOCKED",
            "locations": [],
            "positive_evidence": [],
            "negative_evidence": [reason],
            "not_applicable_reason": None,
        }
        for check_id in CHECK_ORDER + ["historical_guard_closure"]
    }
    return {
        "artifact_id": packet["artifact_id"],
        "physical_page": packet["physical_page"],
        "page_png_sha256": packet["page_png_sha256"],
        "reviewer_run_id": "BLOCKED_RENDER_REVIEW_RUNTIME",
        "fresh_context": "NO",
        "read_only_candidate": "YES",
        "image_inspection_runtime": "UNAVAILABLE",
        "review_scope": "WHOLE_SLIDE",
        "checks": checks,
        "problem_locations": [],
        "positive_visible_evidence": [],
        "negative_visible_evidence": [reason],
        "issue_classes": ["RENDERED_REVIEW_BLOCKED"],
        "overall_visual_verdict": "BLOCKED",
        "substantive_observation": reason,
    }


def normalize_reviewer_row(packet: dict[str, Any], row: dict[str, Any]) -> dict[str, Any]:
    normalized_checks: dict[str, dict[str, Any]] = {}
    source_checks = row.get("checks") or {}
    for check_id in CHECK_ORDER:
        if isinstance(source_checks, dict):
            source = source_checks.get(check_id)
        else:
            source = next((c for c in source_checks if c.get("check_id") == check_id), None)
        if not source:
            source = {"check_id": check_id, "status": "BLOCKED", "evidence": f"Reviewer omitted {check_id}.", "finding_class": "REVIEWER_SCHEMA_MISSING_CHECK"}
        status = source.get("status")
        if status not in {"PASS", "REVISE", "N/A", "BLOCKED"}:
            source["status"] = "BLOCKED"
            source["finding_class"] = "REVIEWER_SCHEMA_INVALID_STATUS"
            source["evidence"] = f"Invalid reviewer status for {check_id}: {status}"
        normalized_checks[check_id] = source
    hist = (row.get("checks") or {}).get("historical_guard_closure") if isinstance(row.get("checks"), dict) else None
    normalized_checks["historical_guard_closure"] = hist or {
        "check_id": "historical_guard_closure",
        "status": "BLOCKED",
        "finding_class": "HISTORICAL_GUARD_CLOSURE_MISSING",
        "evidence": "Reviewer row omitted historical_guard_closure.",
    }
    if row.get("page_png_sha256") != packet["page_png_sha256"]:
        normalized_checks["image_binding"] = {
            "check_id": "image_binding",
            "status": "BLOCKED",
            "finding_class": "REVIEWER_IMAGE_HASH_MISMATCH",
            "evidence": "Reviewer row page_png_sha256 does not match packet.",
        }
    positive = [p for c in normalized_checks.values() for p in c.get("positive_evidence", [])]
    negative = [n for c in normalized_checks.values() for n in c.get("negative_evidence", [])]
    locations = [loc for c in normalized_checks.values() for loc in c.get("locations", [])]
    issue_classes = sorted({c.get("finding_class") for c in normalized_checks.values() if c.get("finding_class")})
    verdict = row.get("overall_visual_verdict")
    if verdict not in {"PASS", "REVISE", "BLOCKED"}:
        verdict = "BLOCKED"
        issue_classes.append("REVIEWER_SCHEMA_INVALID_VERDICT")
    return {
        "artifact_id": packet["artifact_id"],
        "physical_page": packet["physical_page"],
        "page_png_sha256": packet["page_png_sha256"],
        "reviewer_run_id": row.get("reviewer_run_id"),
        "fresh_context": row.get("fresh_context"),
        "read_only_candidate": row.get("read_only_candidate"),
        "image_inspection_runtime": row.get("image_inspection_runtime"),
        "review_scope": "WHOLE_SLIDE",
        "checks": normalized_checks,
        "problem_locations": locations,
        "positive_visible_evidence": positive,
        "negative_visible_evidence": negative,
        "issue_classes": issue_classes,
        "overall_visual_verdict": verdict,
        "substantive_observation": row.get("substantive_observation", ""),
    }


def review_rendered_page(packet: dict[str, Any], *, reviewer_context_id: str) -> dict[str, Any]:
    return blocked_rendered_review_row(
        packet,
        reason="The deterministic generic core cannot author rendered-review verdicts in V3; provide an external fresh reviewer row.",
    )
