#!/usr/bin/env python3
"""Validate task 021 comparative visual-review manifests and evidence."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[6]
TASK_KEY = "021_research_presentation_comparative_reference_calibrated_visual_review"
VISIBLE_TASK_KEY = "021_visual_comparison"
VISIBLE_WORKFLOW_TYPE = "generic"
RESULT_ROOT = REPO_ROOT / "results" / TASK_KEY / "visual_review"
REFERENCE_INDEX = REPO_ROOT / "skills/tools/documents-media/presentations/shared/references/research_slide_reference_index.csv"
COMPOSITION_INDEX = REPO_ROOT / "skills/tools/documents-media/presentations/shared/references/research_slide_composition_index.json"
FORBIDDEN_VISIBLE = [
    "RRL-",
    "SRC-",
    "candidate",
    "reference",
    "generated",
    "gold",
    "baseline",
    "reference_faithful",
    "alternative_composition",
    "controlled_wildcard",
    "MIT",
    "CMU",
    "SFU",
    "Columbia",
    "Harvard",
    "Gelman",
    "Kumar",
    "Abhishek",
]


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def validate_case(case_dir: Path, require_review: bool = False, require_bytes: bool = False) -> list[str]:
    errors: list[str] = []
    manifest_path = case_dir / "visual_inputs.json"
    map_path = case_dir / "review_identity_map.json"
    identity_path = case_dir / "review_identity.json"
    for path in [manifest_path, map_path, identity_path]:
        if not path.exists():
            errors.append(f"{case_dir}: missing {path.name}")
            return errors
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    identity_map = json.loads(map_path.read_text(encoding="utf-8"))
    identity = json.loads(identity_path.read_text(encoding="utf-8"))
    visible_text = json.dumps(manifest, sort_keys=True)
    for forbidden in FORBIDDEN_VISIBLE:
        if forbidden in visible_text:
            errors.append(f"{manifest_path}: Terra-visible manifest leaks {forbidden}")
    if manifest.get("schema") != "AI_BRIDGE_VISUAL_INPUT_MANIFEST_V1":
        errors.append(f"{manifest_path}: invalid manifest schema")
    if manifest.get("task_key") != VISIBLE_TASK_KEY:
        errors.append(f"{manifest_path}: invalid task_key")
    if manifest.get("workflow_type") != VISIBLE_WORKFLOW_TYPE:
        errors.append(f"{manifest_path}: invalid workflow_type")
    inputs = manifest.get("inputs", [])
    items = identity_map.get("items", [])
    if len(inputs) != 5 or len(items) != 5:
        errors.append(f"{case_dir}: expected 5 anonymous items")
    candidate_items = [item for item in items if item.get("item_class") == "candidate"]
    reference_items = [item for item in items if item.get("item_class") == "reference"]
    if len(candidate_items) != 3:
        errors.append(f"{case_dir}: expected 3 candidate items")
    if not 2 <= len(reference_items) <= 4:
        errors.append(f"{case_dir}: expected 2-4 reference items")
    logical_ids = [item.get("logical_id") for item in inputs]
    if logical_ids != [f"item_{chr(ord('A') + i)}" for i in range(len(inputs))]:
        errors.append(f"{case_dir}: inputs must use item_A... anonymous ids")
    mapped_ids = sorted(item.get("anonymous_id") for item in items)
    if mapped_ids != sorted(logical_ids):
        errors.append(f"{case_dir}: identity map ids do not match manifest inputs")
    for item in inputs:
        path_value = item.get("path", "")
        if not re.fullmatch(r"\.cache/research-presentation-comparative-review/021/[a-z]+/item_[A-Z]\.png", path_value):
            errors.append(f"{case_dir}: non-anonymous input path {path_value}")
        if item.get("mime_type") != "image/png":
            errors.append(f"{case_dir}: input {item.get('logical_id')} is not image/png")
        if require_bytes:
            actual = REPO_ROOT / path_value
            if not actual.exists():
                errors.append(f"{case_dir}: input bytes missing for {path_value}")
            elif sha256(actual) != item.get("sha256"):
                errors.append(f"{case_dir}: input SHA mismatch for {path_value}")
    for item in candidate_items:
        if item.get("sha256") != item.get("review_input_sha256"):
            errors.append(f"{case_dir}: candidate copied bytes changed unexpectedly for {item.get('anonymous_id')}")
    for item in reference_items:
        for key in ["reference_id", "source_id", "source_file_sha256", "canonical_rendered_page_sha256", "review_input_sha256", "actual_page_number", "materialization_method", "rights_note"]:
            if not item.get(key):
                errors.append(f"{case_dir}: reference item {item.get('anonymous_id')} missing {key}")
    if identity.get("review_identity_sha256") != identity_map.get("review_identity_sha256"):
        errors.append(f"{case_dir}: identity mismatch")
    if require_review:
        review_path = case_dir / "VISUAL_REVIEW.json"
        if not review_path.exists():
            errors.append(f"{case_dir}: missing VISUAL_REVIEW.json")
        else:
            review = json.loads(review_path.read_text(encoding="utf-8"))
            if review.get("review_model") != "gpt-5.6-terra":
                errors.append(f"{case_dir}: visual review model is not gpt-5.6-terra")
            reviewed_ids = {item.get("item_id") for item in review.get("item_reviews", [])}
            if reviewed_ids and reviewed_ids != set(logical_ids):
                errors.append(f"{case_dir}: visual review item ids do not match inputs")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case", choices=["statistical", "medical"], action="append")
    parser.add_argument("--require-review", action="store_true")
    parser.add_argument("--require-bytes", action="store_true")
    args = parser.parse_args()
    cases = args.case or ["statistical", "medical"]
    errors: list[str] = []
    for case in cases:
        errors.extend(validate_case(RESULT_ROOT / case, require_review=args.require_review, require_bytes=args.require_bytes))
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print(f"validated {len(cases)} comparative visual-review case(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
