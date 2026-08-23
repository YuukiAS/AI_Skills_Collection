#!/usr/bin/env python3
"""Validate research slide composition records."""

from __future__ import annotations

import csv
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any


SHARED = Path(__file__).resolve().parents[1]
REFERENCES = SHARED / "references"
INDEX = REFERENCES / "research_slide_composition_index.json"
REFERENCE_INDEX = REFERENCES / "research_slide_reference_index.csv"
FAMILIES = REFERENCES / "RESEARCH_COMPOSITION_FAMILIES.md"
DEBUG_MONTAGE = Path(__file__).resolve().parents[6] / "docs" / "audits" / "research_presentation_composition_debug_montage.svg"


REQUIRED_TOP_LEVEL = {"schema", "records"}
REQUIRED_RECORD = {
    "reference_id",
    "source_id",
    "actual_page_number",
    "page_function",
    "scientific_object",
    "evidence_type",
    "rendered_page_sha256",
    "inspection_basis",
    "layout_family",
    "reading_flow",
    "regions",
    "primary_scientific_object_region_id",
    "primary_object_area_ratio",
    "alignment_groups",
    "visual_hierarchy",
    "color_role_summary",
    "composition_inspection_means",
    "portable_composition_lessons",
    "reuse_boundary",
}
ALLOWED_INSPECTION_BASIS = {"pptx_geometry", "rendered_page_annotation"}
ALLOWED_ROLES = {
    "title",
    "primary_scientific_object",
    "secondary_scientific_object",
    "equation",
    "body_text",
    "annotation",
    "caption",
    "legend",
    "decision_or_next_step",
}
ALLOWED_CONTENT_MODES = {"text", "figure", "equation", "medical_image", "diagram", "table", "mixed", "caption", "legend"}


def load_reference_rows() -> dict[str, dict[str, str]]:
    with REFERENCE_INDEX.open(encoding="utf-8", newline="") as fh:
        return {row["reference_id"]: row for row in csv.DictReader(fh)}


def load_family_vocabulary() -> set[str]:
    text = FAMILIES.read_text(encoding="utf-8")
    return set(re.findall(r"^### ([a-z0-9-]+)$", text, flags=re.MULTILINE))


def area(bbox: dict[str, Any]) -> float:
    return round(float(bbox["w"]) * float(bbox["h"]), 4)


def walk_strings(value: Any) -> list[str]:
    if isinstance(value, str):
        return [value]
    if isinstance(value, list):
        out: list[str] = []
        for item in value:
            out.extend(walk_strings(item))
        return out
    if isinstance(value, dict):
        out = []
        for item in value.values():
            out.extend(walk_strings(item))
        return out
    return []


def validate() -> list[str]:
    errors: list[str] = []
    data = json.loads(INDEX.read_text(encoding="utf-8"))
    reference_rows = load_reference_rows()
    families = load_family_vocabulary()

    if set(data) - {"schema", "schema_path", "generated_from", "records"}:
        errors.append("top-level index has unexpected fields")
    if not REQUIRED_TOP_LEVEL.issubset(data):
        errors.append("top-level index missing required fields")
    if data.get("schema") != "RESEARCH_SLIDE_COMPOSITION_INDEX_V1":
        errors.append("index schema must be RESEARCH_SLIDE_COMPOSITION_INDEX_V1")
    records = data.get("records")
    if not isinstance(records, list):
        return errors + ["records must be a list"]
    if len(records) < 12:
        errors.append("composition index must contain at least 12 records")

    source_ids: set[str] = set()
    page_functions: set[str] = set()
    families_used: set[str] = set()
    has_equation = False
    has_quant_results = 0
    has_method_flow = 0
    has_image_panel = 0
    has_negative_or_check = 0
    has_next_or_decision = 0
    seen_ids: set[str] = set()

    for record in records:
        rid = record.get("reference_id", "<missing>")
        if rid in seen_ids:
            errors.append(f"{rid}: duplicate reference_id")
        seen_ids.add(rid)
        missing = REQUIRED_RECORD - set(record)
        if missing:
            errors.append(f"{rid}: missing fields {sorted(missing)}")
            continue
        extra = set(record) - REQUIRED_RECORD
        if extra:
            errors.append(f"{rid}: unexpected fields {sorted(extra)}")
        row = reference_rows.get(rid)
        if not row:
            errors.append(f"{rid}: reference_id not found in research_slide_reference_index.csv")
            continue
        if row.get("verification_status") != "inspected":
            errors.append(f"{rid}: reference row is not inspected")
        for field in ["source_id", "page_function", "scientific_object", "evidence_type", "rendered_page_sha256"]:
            if str(record[field]) != str(row[field]):
                errors.append(f"{rid}: {field} does not match reference index")
        if str(record["actual_page_number"]) != row["actual_page_number"]:
            errors.append(f"{rid}: actual_page_number does not match reference index")
        if record["inspection_basis"] not in ALLOWED_INSPECTION_BASIS:
            errors.append(f"{rid}: invalid inspection_basis")
        if record["layout_family"] not in families:
            errors.append(f"{rid}: layout_family not in RESEARCH_COMPOSITION_FAMILIES.md")

        source_ids.add(record["source_id"])
        page_functions.add(record["page_function"])
        families_used.add(record["layout_family"])

        regions = record["regions"]
        if not isinstance(regions, list) or not regions:
            errors.append(f"{rid}: regions must be a non-empty list")
            continue
        region_ids = [region.get("region_id") for region in regions]
        if len(region_ids) != len(set(region_ids)):
            errors.append(f"{rid}: duplicate region_id")
        primary_id = record["primary_scientific_object_region_id"]
        primary_region = None
        for region in regions:
            region_id = region.get("region_id", "<missing>")
            if region.get("role") not in ALLOWED_ROLES:
                errors.append(f"{rid}/{region_id}: invalid role")
            if region.get("content_mode") not in ALLOWED_CONTENT_MODES:
                errors.append(f"{rid}/{region_id}: invalid content_mode")
            if not isinstance(region.get("hierarchy_rank"), int) or region["hierarchy_rank"] < 1:
                errors.append(f"{rid}/{region_id}: invalid hierarchy_rank")
            bbox = region.get("bbox")
            if not isinstance(bbox, dict):
                errors.append(f"{rid}/{region_id}: bbox missing")
                continue
            for key in ["x", "y", "w", "h"]:
                if key not in bbox or not isinstance(bbox[key], (int, float)):
                    errors.append(f"{rid}/{region_id}: bbox.{key} missing or non-numeric")
            if all(key in bbox for key in ["x", "y", "w", "h"]):
                x, y, w, h = (float(bbox[key]) for key in ["x", "y", "w", "h"])
                if x < 0 or y < 0 or w <= 0 or h <= 0 or x + w > 1.001 or y + h > 1.001:
                    errors.append(f"{rid}/{region_id}: bbox outside normalized page bounds")
            if region_id == primary_id:
                primary_region = region
        if primary_region is None:
            errors.append(f"{rid}: primary scientific object region missing")
        elif primary_region.get("role") not in {"primary_scientific_object", "decision_or_next_step"}:
            errors.append(f"{rid}: primary region has invalid role")
        elif abs(area(primary_region["bbox"]) - float(record["primary_object_area_ratio"])) > 0.002:
            errors.append(f"{rid}: primary_object_area_ratio does not match primary bbox area")

        for group in record["alignment_groups"]:
            for region_id in group.get("region_ids", []):
                if region_id not in region_ids:
                    errors.append(f"{rid}: alignment group references unknown region {region_id}")
        for item in record["visual_hierarchy"]:
            if item.get("region_id") not in region_ids:
                errors.append(f"{rid}: hierarchy references unknown region {item.get('region_id')}")
            if not isinstance(item.get("rank"), int) or item["rank"] < 1:
                errors.append(f"{rid}: invalid hierarchy rank")

        strings = "\n".join(walk_strings(record))
        for forbidden in ["/home/", ".cache/", "data:image", "<image", "base64,", "whole-slide screenshot copy"]:
            if forbidden in strings:
                errors.append(f"{rid}: forbidden path or embedded-image marker found")

        text = " ".join([record["page_function"], record["evidence_type"], record["scientific_object"], record["layout_family"], " ".join(r["content_mode"] for r in regions)])
        if any(mode in text for mode in ["equation", "formula", "STATISTICAL_MODEL", "ESTIMATOR", "THEOREM"]):
            has_equation = True
        if record["page_function"] in {"RESULT_FIGURE", "CONFIDENCE_INTERVAL", "REAL_DATA_APPLICATION"}:
            has_quant_results += 1
        if record["page_function"] in {"METHOD_DIAGRAM", "EXPERIMENT_DESIGN", "ESTIMATOR"} and record["layout_family"] in {"horizontal-process-flow", "split-visual-explanation"}:
            has_method_flow += 1
        if record["page_function"] == "MEDICAL_IMAGE_COMPARISON" or "medical_image" in [r["content_mode"] for r in regions]:
            has_image_panel += 1
        if record["page_function"] in {"NEGATIVE_RESULT", "MODEL_CHECK"} or record["layout_family"] == "model-check-or-negative":
            has_negative_or_check += 1
        if record["page_function"] in {"NEXT_EXPERIMENT", "SUPERVISOR_DECISION", "REFERENCE_COVERAGE_GAP"} or any(r["role"] == "decision_or_next_step" for r in regions):
            has_next_or_decision += 1

    if len(source_ids) < 4:
        errors.append("composition index must cover at least 4 source_ids")
    if len(page_functions) < 6:
        errors.append("composition index must cover at least 6 page functions")
    if len(families_used) < 6:
        errors.append("composition index must use at least 6 layout families")
    if not has_equation:
        errors.append("composition index must include an equation/statistical-model exemplar")
    if has_quant_results < 2:
        errors.append("composition index must include at least 2 quantitative result exemplars")
    if has_method_flow < 2:
        errors.append("composition index must include at least 2 method/experiment flow exemplars")
    if has_image_panel < 2:
        errors.append("composition index must include at least 2 image/aligned-panel exemplars")
    if has_negative_or_check < 1:
        errors.append("composition index must include a negative-result/model-check exemplar")
    if has_next_or_decision < 1:
        errors.append("composition index must include a next-experiment/decision exemplar")

    if DEBUG_MONTAGE.exists():
        svg = DEBUG_MONTAGE.read_text(encoding="utf-8")
        for forbidden in ["<image", "data:image", "base64,", ".png", ".jpg", ".jpeg", ".pdf", "/home/", ".cache/"]:
            if forbidden in svg:
                errors.append(f"debug montage contains forbidden source-pixel marker: {forbidden}")
    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    record_count = len(json.loads(INDEX.read_text(encoding="utf-8"))["records"])
    print(f"validated {record_count} research slide composition records")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
