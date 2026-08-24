#!/usr/bin/env python3
"""Validate the gold scientific composition library."""

from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REFERENCES = ROOT / "references"
INDEX = REFERENCES / "research_gold_composition_index.json"
REFERENCE_INDEX = REFERENCES / "research_slide_reference_index.csv"
COMPOSITION_INDEX = REFERENCES / "research_slide_composition_index.json"
REPO_ROOT = ROOT.parents[4]
ADMISSION_REPORT = REPO_ROOT / "docs" / "audits" / "research_presentation_gold_composition_library" / "gold_admission_report.json"
ALLOWED_RIGHTS = {"COMPOSITION_ONLY", "COMPARATIVE_GOLD"}
FORBIDDEN_AUDIENCE_TERMS = ["RRL-", "SRC-", "GSC-", "gold", "QA", "provenance", "review"]


def _load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _reference_rows() -> dict[str, dict[str, str]]:
    return {
        row["reference_id"]: row
        for row in csv.DictReader(REFERENCE_INDEX.read_text(encoding="utf-8").splitlines())
    }


def _composition_refs() -> set[str]:
    index = _load_json(COMPOSITION_INDEX)
    return {record["reference_id"] for record in index["records"]}


def _bbox_valid(bbox: dict) -> bool:
    return (
        0 <= bbox.get("x", -1) <= 1
        and 0 <= bbox.get("y", -1) <= 1
        and 0 < bbox.get("w", 0) <= 1
        and 0 < bbox.get("h", 0) <= 1
        and bbox["x"] + bbox["w"] <= 1.001
        and bbox["y"] + bbox["h"] <= 1.001
    )


def _admission_decisions() -> dict[str, dict]:
    repo_root = REPO_ROOT
    decisions: dict[str, dict] = {}
    for folder in [
        repo_root / "results" / "025_research_presentation_gold_scientific_composition_library" / "visual_review" / "gold_admission",
        repo_root / "results" / "025_research_presentation_gold_scientific_composition_library" / "visual_review" / "gold_recovery_1",
        repo_root / "results" / "026_research_presentation_discussion_next_experiment_gold_recovery" / "visual_review" / "gold_admission_1",
        repo_root / "results" / "026_research_presentation_discussion_next_experiment_gold_recovery" / "visual_review" / "gold_admission_2",
    ]:
        review_path = folder / "VISUAL_REVIEW.json"
        identity_path = folder / "review_identity_map.json"
        if not review_path.exists() or not identity_path.exists():
            continue
        review = _load_json(review_path)
        identity = _load_json(identity_path)
        for item, item_review in zip(identity["items"], review["item_reviews"]):
            decisions[item["reference_id"]] = {
                "decision": item_review["decision"],
                "anonymous_id": item["anonymous_id"],
                "review_input_sha256": item["review_input_sha256"],
                "visual_review_path": str(review_path.relative_to(repo_root)),
                "identity_map_path": str(identity_path.relative_to(repo_root)),
                "evidence_id": review["evidence_id"],
            }
    return decisions


def validate_gold_index(index: dict) -> list[str]:
    errors: list[str] = []
    if index.get("schema") != "RESEARCH_GOLD_COMPOSITION_INDEX_V1":
        errors.append("schema must be RESEARCH_GOLD_COMPOSITION_INDEX_V1")
    records = index.get("records", [])
    if not records:
        errors.append("records must be non-empty")
        return errors

    rows = _reference_rows()
    composition_refs = _composition_refs()
    gold_ids: set[str] = set()
    refs: set[str] = set()
    sources: set[str] = set()
    jobs: set[str] = set()
    from_019 = 0
    admission_decisions = _admission_decisions()

    for record in records:
        prefix = record.get("gold_id", "<missing>")
        if record.get("gold_id") in gold_ids:
            errors.append(f"{prefix}: duplicate gold_id")
        gold_ids.add(record.get("gold_id", ""))
        refs.add(record.get("reference_id", ""))
        sources.add(record.get("source_id", ""))
        jobs.update(record.get("scientific_jobs", []))

        row = rows.get(record.get("reference_id"))
        if not row:
            errors.append(f"{prefix}: reference_id not present in inspected reference index")
            continue
        if row["verification_status"] != "inspected":
            errors.append(f"{prefix}: reference row is not inspected")
        for field, row_field in [
            ("source_id", "source_id"),
            ("actual_page_number", "actual_page_number"),
            ("source_file_sha256", "source_file_sha256"),
            ("canonical_rendered_page_sha256", "rendered_page_sha256"),
        ]:
            expected = str(row[row_field])
            actual = str(record.get(field))
            if actual != expected:
                errors.append(f"{prefix}: {field}={actual} does not match reference index {expected}")

        if record.get("reference_id") in composition_refs:
            from_019 += 1
        if record.get("rights_reuse_boundary") not in ALLOWED_RIGHTS:
            errors.append(f"{prefix}: invalid rights_reuse_boundary")
        if not _bbox_valid(record.get("primary_bbox", {})):
            errors.append(f"{prefix}: invalid primary_bbox")
        if not record.get("gold_admission_evidence", {}).get("evidence_paths"):
            errors.append(f"{prefix}: gold admission evidence missing evidence_paths")
        evidence = record.get("gold_admission_evidence", {})
        if "metadata" in evidence.get("basis", "").lower():
            errors.append(f"{prefix}: gold admission evidence cannot be metadata-only")
        if evidence.get("item_level_judgement") != "PASS":
            errors.append(f"{prefix}: gold admission item_level_judgement must be PASS")
        if not any(path.endswith("VISUAL_REVIEW.json") for path in evidence.get("evidence_paths", [])):
            errors.append(f"{prefix}: gold admission evidence must include VISUAL_REVIEW.json")
        decision = admission_decisions.get(record.get("reference_id"))
        if not decision:
            errors.append(f"{prefix}: no admission visual-review decision for reference")
        elif decision["decision"] != "PASS":
            errors.append(f"{prefix}: admission visual-review decision is {decision['decision']}, not PASS")
        else:
            if record.get("gold_admission_review_input_sha256") != decision["review_input_sha256"]:
                errors.append(f"{prefix}: gold_admission_review_input_sha256 does not match visual-review input")
            if evidence.get("visual_review_item_id") != decision["anonymous_id"]:
                errors.append(f"{prefix}: visual_review_item_id does not match identity map")
            if evidence.get("visual_review_path") != decision["visual_review_path"]:
                errors.append(f"{prefix}: visual_review_path does not match admission evidence")
            if evidence.get("identity_map_path") != decision["identity_map_path"]:
                errors.append(f"{prefix}: identity_map_path does not match admission evidence")
            if evidence.get("visual_review_evidence_id") != decision["evidence_id"]:
                errors.append(f"{prefix}: visual_review_evidence_id does not match review output")
        if not record.get("annotation_legend_caption_panel_relations"):
            errors.append(f"{prefix}: missing annotation/legend/caption/panel relations")
        if not record.get("selection_keywords"):
            errors.append(f"{prefix}: missing selection keywords")
        audience_contract = " ".join([
            record.get("portable_composition_lesson", ""),
            " ".join(record.get("scientific_jobs", [])),
        ])
        for forbidden in FORBIDDEN_AUDIENCE_TERMS:
            if forbidden in audience_contract:
                errors.append(f"{prefix}: audience-facing contract leaks {forbidden}")

    if len(records) == from_019:
        errors.append("gold library cannot be only a rename of every 019 composition record")
    if from_019 >= 13:
        errors.append("gold library selected all 019 records; it must be a screened subset")
    if len(sources) < 3:
        errors.append("gold library must include multiple source decks")

    required_job_fragments = [
        "motivation",
        "estimator",
        "method",
        "quantitative_result",
        "negative_result",
        "medical_image_comparison",
        "discussion",
        "next_experiment",
    ]
    for fragment in required_job_fragments:
        if not any(fragment in job for job in jobs):
            errors.append(f"missing required scientific job coverage: {fragment}")
    if ADMISSION_REPORT.exists():
        report = _load_json(ADMISSION_REPORT)
        if set(report.get("admitted_gold_ids", [])) != gold_ids:
            errors.append("gold admission report admitted_gold_ids must match index gold_ids")
        limitations = " ".join(report.get("coverage_limitations", [])).lower()
        if any("discussion" in job for job in jobs) and "no discussion" in limitations:
            errors.append("gold admission report still claims a discussion coverage limitation")
    return errors


def main() -> int:
    errors = validate_gold_index(_load_json(INDEX))
    if errors:
        for error in errors:
            print(f"ERROR {error}")
        return 1
    print(f"validated {len(_load_json(INDEX)['records'])} gold scientific composition records")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
