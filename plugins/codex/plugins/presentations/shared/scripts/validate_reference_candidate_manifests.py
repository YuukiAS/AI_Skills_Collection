#!/usr/bin/env python3
"""Validate reference-calibrated candidate search manifests."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


SHARED = Path(__file__).resolve().parents[1]
REPO_ROOT = Path(__file__).resolve().parents[6]
COMPOSITION_INDEX = SHARED / "references" / "research_slide_composition_index.json"

FORBIDDEN_AUDIENCE_TERMS = [
    "Candidate A",
    "Candidate B",
    "Candidate C",
    "reference_faithful",
    "alternative_composition",
    "controlled_wildcard",
    "RRL-",
    "Reference retrieval",
    "EVIDENCE_MANIFEST",
    "Diagram contract",
    "QA",
    "repo path",
    "implementation commit",
    "review target",
]


def sha256(path: Path) -> str:
    import hashlib

    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def composition_records_by_id() -> dict[str, dict[str, Any]]:
    records = json.loads(COMPOSITION_INDEX.read_text(encoding="utf-8"))["records"]
    return {record["reference_id"]: record for record in records}


def area(bbox: dict[str, Any]) -> float:
    return round(float(bbox["w"]) * float(bbox["h"]), 4)


def validate_manifest(path: Path) -> list[str]:
    errors: list[str] = []
    data = json.loads(path.read_text(encoding="utf-8"))
    records_by_id = composition_records_by_id()
    request = data.get("request", {})
    candidates = data.get("candidates", [])
    if data.get("schema") != "RESEARCH_SLIDE_CANDIDATE_MANIFEST_V1":
        errors.append(f"{path}: invalid schema")
    if request.get("candidate_count") != 3:
        errors.append(f"{path}: request candidate_count must be 3")
    if len(candidates) != 3:
        errors.append(f"{path}: manifest must contain exactly 3 candidates")
        return errors
    if sorted(candidate["strategy"] for candidate in candidates) != ["alternative_composition", "controlled_wildcard", "reference_faithful"]:
        errors.append(f"{path}: missing required candidate strategies")

    payload_sha = data.get("content_payload_sha256")
    if not re.fullmatch(r"[0-9a-f]{64}", str(payload_sha)):
        errors.append(f"{path}: invalid content_payload_sha256")
    preview_shas = [candidate.get("preview_sha256") for candidate in candidates]
    if len(set(preview_shas)) != 3:
        errors.append(f"{path}: candidate preview SHA values must be distinct")
    families = {candidate.get("layout_family") for candidate in candidates}
    if len(families) < 2:
        errors.append(f"{path}: candidates must use at least two composition families")

    signatures = [json.dumps(candidate.get("distinctness_signature", {}), sort_keys=True) for candidate in candidates]
    if len(set(signatures)) != 3:
        errors.append(f"{path}: candidates must not share identical geometry signatures")

    for candidate in candidates:
        cid = candidate.get("candidate_id", "<missing>")
        if candidate.get("source_reference_pixels_used") is not False:
            errors.append(f"{path}/{cid}: source_reference_pixels_used must be false")
        artifact = candidate.get("preview_artifact", {})
        artifact_path = REPO_ROOT / artifact.get("path", "")
        if not artifact_path.exists():
            errors.append(f"{path}/{cid}: preview artifact missing")
        elif sha256(artifact_path) != candidate.get("preview_sha256") or sha256(artifact_path) != artifact.get("sha256"):
            errors.append(f"{path}/{cid}: preview SHA mismatch")
        if artifact.get("mime_type") != "image/png":
            errors.append(f"{path}/{cid}: preview artifact must be image/png")

        source_ids = candidate.get("source_reference_ids", [])
        if not source_ids:
            errors.append(f"{path}/{cid}: source_reference_ids missing")
        for reference_id in source_ids:
            if reference_id not in records_by_id:
                errors.append(f"{path}/{cid}: source reference {reference_id} not in composition index")
        regions = candidate.get("regions", [])
        primary_regions = [region for region in regions if region.get("role") == "primary_scientific_object"]
        if not primary_regions:
            errors.append(f"{path}/{cid}: primary scientific object region missing")
        else:
            primary_area = sum(area(region["bbox"]) for region in primary_regions)
            if primary_area < 0.08:
                errors.append(f"{path}/{cid}: primary scientific object is too small")
        for region in regions:
            bbox = region.get("bbox", {})
            if not all(key in bbox for key in ["x", "y", "w", "h"]):
                errors.append(f"{path}/{cid}: region bbox incomplete")
                continue
            x, y, w, h = [float(bbox[key]) for key in ["x", "y", "w", "h"]]
            if x < 0 or y < 0 or w <= 0 or h <= 0 or x + w > 1.001 or y + h > 1.001:
                errors.append(f"{path}/{cid}: region bbox out of bounds")
        if not candidate.get("content_bindings"):
            errors.append(f"{path}/{cid}: content_bindings missing")
        transfer = candidate.get("geometry_transfer", [])
        if not transfer:
            errors.append(f"{path}/{cid}: geometry_transfer missing")
        for item in transfer:
            if item.get("source_reference_id") not in records_by_id:
                errors.append(f"{path}/{cid}: transfer source reference not in composition index")
            if item.get("adaptation_type") not in {"preserve", "scale", "translate", "merge", "split", "reorder"}:
                errors.append(f"{path}/{cid}: invalid adaptation_type")
            for field in ["source_bbox", "candidate_bbox"]:
                bbox = item.get(field, {})
                if not all(key in bbox for key in ["x", "y", "w", "h"]):
                    errors.append(f"{path}/{cid}: transfer {field} incomplete")
        audience = "\n".join(candidate.get("audience_text", []))
        for forbidden in FORBIDDEN_AUDIENCE_TERMS:
            if forbidden in audience:
                errors.append(f"{path}/{cid}: audience text leaks internal term {forbidden}")
        if request.get("page_function") == "ESTIMATOR":
            if not any(region.get("content_mode") == "equation" for region in regions):
                errors.append(f"{path}/{cid}: estimator request lacks equation content")
        if request.get("page_function") == "MEDICAL_IMAGE_COMPARISON":
            if not any(region.get("content_mode") == "medical_image" for region in regions):
                errors.append(f"{path}/{cid}: medical request lacks image content")

    comparison = data.get("comparison_sheet", {})
    comparison_path = REPO_ROOT / comparison.get("path", "")
    if not comparison_path.exists():
        errors.append(f"{path}: comparison sheet missing")
    elif sha256(comparison_path) != comparison.get("sha256"):
        errors.append(f"{path}: comparison sheet SHA mismatch")
    for artifact in [candidate.get("preview_artifact", {}) for candidate in candidates] + [comparison]:
        value = artifact.get("path", "")
        for forbidden in ["/home/", ".cache/", "source", "reference_screenshot"]:
            if forbidden in value:
                errors.append(f"{path}: artifact path contains forbidden marker {forbidden}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifests", nargs="+")
    args = parser.parse_args()
    errors: list[str] = []
    for item in args.manifests:
        errors.extend(validate_manifest(REPO_ROOT / item if not Path(item).is_absolute() else Path(item)))
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print(f"validated {len(args.manifests)} candidate manifest(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
