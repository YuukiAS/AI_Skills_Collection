#!/usr/bin/env python3
"""Generate deterministic runtime probe artifacts for the gold library."""

from __future__ import annotations

import json
from pathlib import Path

import build_gold_composition_recipe


REPO_ROOT = Path(__file__).resolve().parents[6]
OUT_DIR = REPO_ROOT / "docs" / "audits" / "research_presentation_gold_composition_library"
VISUAL_REVIEW_DIR = REPO_ROOT / "results" / "025_research_presentation_gold_scientific_composition_library" / "visual_review"


PROBES = [
    {
        "probe_id": "statistics_estimator_identity",
        "query": {
            "page_function": "REAL_DATA_APPLICATION",
            "scientific_object": "biostatistics quantitative model comparison result table figure",
            "domain_family": "biostatistics",
            "dominant_object_type": "plot table",
            "evidence_type": "quantitative comparison result",
            "density": "moderate",
            "panel_count": 1,
        }
    },
    {
        "probe_id": "medical_aligned_prediction_error",
        "query": {
            "page_function": "MEDICAL_IMAGE_COMPARISON",
            "scientific_object": "medical image lesion samples task applications visual comparison",
            "domain_family": "medical_imaging",
            "dominant_object_type": "medical_image",
            "evidence_type": "representative image comparison",
            "density": "high",
            "panel_count": 4,
        }
    }
]


def generate() -> dict:
    traces = []
    for probe in PROBES:
        baseline = build_gold_composition_recipe.build_recipe(probe["query"])
        alternate = build_gold_composition_recipe.build_recipe(
            probe["query"],
            exclude_gold_id=baseline["selected_gold_id"],
        )
        traces.append({
            "probe_id": probe["probe_id"],
            "query": probe["query"],
            "baseline_recipe": baseline,
            "alternate_recipe": alternate,
            "checks": {
                "runtime_selected": bool(baseline["selected_gold_id"]),
                "alternate_runtime_selected": bool(alternate["selected_gold_id"]),
                "alternate_is_distinct": baseline["selected_gold_id"] != alternate["selected_gold_id"],
                "alternate_has_compatibility_reasons": bool(alternate["runtime_trace"]["selection"]["matches"][0]["compatibility_reasons"]),
                "actually_consumed": len(baseline["runtime_trace"]["actually_consumed_fields"]) >= 6,
                "output_affected": baseline["recipe_sha256"] != alternate["recipe_sha256"],
                "primary_bbox_changed": baseline["composition_constraints"]["primary_bbox"] != alternate["composition_constraints"]["primary_bbox"],
                "composition_family_available": bool(baseline["composition_constraints"]["composition_family"]),
            }
        })
    return {
        "schema": "RESEARCH_GOLD_COMPOSITION_RUNTIME_PROBES_V1",
        "task_key": "025_research_presentation_gold_scientific_composition_library",
        "status": "PASS" if all(all(item["checks"].values()) for item in traces) else "FAIL",
        "probes": traces,
    }


def _review_decisions() -> list[dict]:
    decisions: list[dict] = []
    for folder in [VISUAL_REVIEW_DIR / "gold_admission", VISUAL_REVIEW_DIR / "gold_recovery_1"]:
        review_path = folder / "VISUAL_REVIEW.json"
        identity_path = folder / "review_identity_map.json"
        if not review_path.exists() or not identity_path.exists():
            continue
        review = json.loads(review_path.read_text(encoding="utf-8"))
        identity = json.loads(identity_path.read_text(encoding="utf-8"))
        for item, item_review in zip(identity["items"], review["item_reviews"]):
            decisions.append({
                "reference_id": item["reference_id"],
                "source_id": item["source_id"],
                "page_function": item["page_function"],
                "visual_review_item_id": item["anonymous_id"],
                "decision": item_review["decision"],
                "summary": item_review["summary"],
                "visual_review_path": str(review_path.relative_to(REPO_ROOT)),
                "identity_map_path": str(identity_path.relative_to(REPO_ROOT)),
            })
    return decisions


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    payload = generate()
    (OUT_DIR / "runtime_probe_traces.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    decisions = _review_decisions()
    report = {
        "schema": "RESEARCH_GOLD_COMPOSITION_ADMISSION_REPORT_V1",
        "task_key": "025_research_presentation_gold_scientific_composition_library",
        "admission_policy": "Only existing inspected references with rendered-page identity, rights boundary, composition lesson, and mature-bar evidence are admitted.",
        "admitted_gold_ids": [
            record["gold_id"]
            for record in build_gold_composition_recipe._records_by_id().values()
        ],
        "admitted_references": [
            decision
            for decision in decisions
            if decision["decision"] == "PASS"
        ],
        "runtime_probe_artifact": "docs/audits/research_presentation_gold_composition_library/runtime_probe_traces.json",
        "coverage_summary": [
            "motivation / research question",
            "estimator / mathematical identity",
            "metric definition with examples",
            "method / experiment design",
            "quantitative result with uncertainty",
            "negative result / model check",
            "medical-image aligned panels",
            "discussion / next experiment: COVERAGE_LIMITATION_NO_ITEM_LEVEL_PASS_IN_EXISTING_SCREEN"
        ],
        "coverage_limitations": [
            "No discussion / next-experiment page reached 025 admission-specific production-gold maturity in the bounded existing-corpus screen.",
            "Medical-image runtime alternate uses a compatible medical visual-task introduction page because the only second aligned prediction grid candidate was rejected by 025 admission-specific Terra."
        ],
        "rejected_candidate_examples": [
            {
                "reference_id": decision["reference_id"],
                "page_function": decision["page_function"],
                "visual_review_item_id": decision["visual_review_item_id"],
                "reason": decision["summary"],
                "visual_review_path": decision["visual_review_path"],
            }
            for decision in decisions
            if decision["decision"] != "PASS"
        ]
    }
    (OUT_DIR / "gold_admission_report.json").write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"status": payload["status"], "out_dir": str(OUT_DIR), "probe_count": len(payload["probes"])}, indent=2))
    return 0 if payload["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
