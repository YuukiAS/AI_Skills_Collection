#!/usr/bin/env python3
"""Shared scientific-object semantic roles for research presentations."""

from __future__ import annotations

from typing import Any


UNKNOWN_ROLE = "unknown"


def _flatten(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, dict):
        flattened: list[str] = []
        for item in value.values():
            flattened.extend(_flatten(item))
        return flattened
    if isinstance(value, list):
        flattened = []
        for item in value:
            flattened.extend(_flatten(item))
        return flattened
    return [str(value)]


def semantic_tokens(*values: Any) -> set[str]:
    text = " ".join(part for value in values for part in _flatten(value))
    text = text.replace("_", " ").replace("-", " ").lower()
    return {token for token in "".join(ch if ch.isalnum() else " " for ch in text).split() if token}


def _has(tokens: set[str], *terms: str) -> bool:
    return any(term in tokens for term in terms)


def normalize_scientific_object_role(fields: dict[str, Any]) -> dict[str, Any]:
    """Return a finite presentation role from structural page/object evidence.

    The role is intentionally coarse. It supports compatibility checks between
    aliases that describe the same presentation object type, while leaving page
    function, domain, panel count, capacity, and rights as separate hard gates.
    """

    page_function = str(fields.get("page_function") or fields.get("page_job") or "").upper()
    tokens = semantic_tokens(
        fields.get("scientific_object"),
        fields.get("scientific_objects"),
        fields.get("dominant_object_type"),
        fields.get("dominant_object"),
        fields.get("content_kind"),
        fields.get("evidence_type"),
        fields.get("primary_scientific_object_role"),
        fields.get("composition_family"),
        fields.get("scientific_jobs"),
        fields.get("selection_keywords"),
        fields.get("supporting_region_roles"),
        fields.get("visual_hierarchy"),
        fields.get("alignment_groups"),
        fields.get("reading_flow"),
        fields.get("annotation_legend_caption_panel_relations"),
    )

    if page_function in {"STATISTICAL_MODEL", "ESTIMATOR", "THEOREM"} or _has(
        tokens,
        "equation",
        "formula",
        "estimator",
        "estimand",
        "objective",
        "theorem",
        "mathematical",
        "math",
        "latex",
    ):
        return {"role": "mathematical_model", "basis": sorted(tokens & {
            "equation",
            "formula",
            "estimator",
            "estimand",
            "objective",
            "theorem",
            "mathematical",
            "math",
            "latex",
        }) or [page_function.lower()]}

    if page_function in {"NEXT_EXPERIMENT", "SUPERVISOR_DECISION"} or _has(
        tokens,
        "discussion",
        "decision",
        "advisor",
        "supervisor",
        "next",
        "query",
        "batch",
        "go",
        "no",
        "proposal",
    ):
        return {"role": "discussion_decision_object", "basis": sorted(tokens & {
            "discussion",
            "decision",
            "advisor",
            "supervisor",
            "next",
            "query",
            "batch",
            "go",
            "no",
            "proposal",
        }) or [page_function.lower()]}

    if page_function in {"EXPERIMENT_DESIGN", "METHOD_DIAGRAM"} or _has(
        tokens,
        "diagram",
        "workflow",
        "flow",
        "process",
        "procedure",
        "procedures",
        "pipeline",
        "map",
        "connector",
        "connectors",
        "design",
    ):
        return {"role": "process_diagram", "basis": sorted(tokens & {
            "diagram",
            "workflow",
            "flow",
            "process",
            "procedure",
            "procedures",
            "pipeline",
            "map",
            "connector",
            "connectors",
            "design",
        }) or [page_function.lower()]}

    if page_function == "MEDICAL_IMAGE_COMPARISON" or (
        _has(tokens, "image", "imaging", "panel", "panels", "roi", "overlay", "segmentation")
        and _has(tokens, "comparison", "sample", "samples", "case", "lesion", "crop", "mask")
    ):
        return {"role": "medical_image_panel", "basis": sorted(tokens & {
            "medical",
            "image",
            "imaging",
            "panel",
            "panels",
            "roi",
            "overlay",
            "segmentation",
            "comparison",
            "sample",
            "samples",
            "case",
            "lesion",
            "crop",
            "mask",
        }) or [page_function.lower()]}

    if _has(
        tokens,
        "figure",
        "plot",
        "table",
        "chart",
        "curve",
        "surface",
        "quantitative",
        "numeric",
        "result",
        "results",
        "comparison",
        "coverage",
        "metric",
        "source",
    ):
        return {"role": "quantitative_source_object", "basis": sorted(tokens & {
            "figure",
            "plot",
            "table",
            "chart",
            "curve",
            "surface",
            "quantitative",
            "numeric",
            "result",
            "results",
            "comparison",
            "coverage",
            "metric",
            "source",
        }) or [page_function.lower()]}

    return {"role": UNKNOWN_ROLE, "basis": []}


def compatible_roles(left: dict[str, Any], right: dict[str, Any]) -> bool:
    left_role = str(left.get("role") or UNKNOWN_ROLE)
    right_role = str(right.get("role") or UNKNOWN_ROLE)
    return left_role != UNKNOWN_ROLE and left_role == right_role
