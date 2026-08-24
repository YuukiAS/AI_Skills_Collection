#!/usr/bin/env python3
"""Generate deterministic runtime probe artifacts for the gold library."""

from __future__ import annotations

import json
from pathlib import Path

import build_gold_composition_recipe


REPO_ROOT = Path(__file__).resolve().parents[6]
OUT_DIR = REPO_ROOT / "docs" / "audits" / "research_presentation_gold_composition_library"


PROBES = [
    {
        "probe_id": "statistics_estimator_identity",
        "query": {
            "page_function": "ESTIMATOR",
            "scientific_object": "estimator equation identity formula",
            "domain_family": "statistics",
            "dominant_object_type": "equation",
            "evidence_type": "estimator formula",
            "density": "low",
            "panel_count": 0,
        },
        "alternate_gold_id": "GSC-003"
    },
    {
        "probe_id": "medical_aligned_prediction_error",
        "query": {
            "page_function": "MEDICAL_IMAGE_COMPARISON",
            "scientific_object": "medical image aligned panel prediction ground truth error overlay",
            "domain_family": "medical_imaging",
            "dominant_object_type": "medical_image",
            "evidence_type": "same-case prediction error",
            "density": "high",
            "panel_count": 4,
        },
        "alternate_gold_id": "GSC-008"
    }
]


def generate() -> dict:
    traces = []
    for probe in PROBES:
        baseline = build_gold_composition_recipe.build_recipe(probe["query"])
        alternate = build_gold_composition_recipe.build_recipe(probe["query"], force_gold_id=probe["alternate_gold_id"])
        traces.append({
            "probe_id": probe["probe_id"],
            "query": probe["query"],
            "baseline_recipe": baseline,
            "alternate_recipe": alternate,
            "checks": {
                "runtime_selected": bool(baseline["selected_gold_id"]),
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


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    payload = generate()
    (OUT_DIR / "runtime_probe_traces.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    report = {
        "schema": "RESEARCH_GOLD_COMPOSITION_ADMISSION_REPORT_V1",
        "task_key": "025_research_presentation_gold_scientific_composition_library",
        "admission_policy": "Only existing inspected references with rendered-page identity, rights boundary, composition lesson, and mature-bar evidence are admitted.",
        "admitted_gold_ids": [probe["baseline_recipe"]["selected_gold_id"] for probe in payload["probes"]],
        "runtime_probe_artifact": "docs/audits/research_presentation_gold_composition_library/runtime_probe_traces.json",
        "coverage_summary": [
            "motivation / research question",
            "estimator / mathematical identity",
            "metric definition with examples",
            "method / experiment design",
            "quantitative result with uncertainty",
            "negative result / model check",
            "medical-image aligned panels",
            "discussion / next experiment"
        ],
        "rejected_candidate_examples": [
            {"reference_id": "RRL-034", "reason": "model teaching page retained as inspected reference but primary scientific object is too small for first production gold set"},
            {"reference_id": "RRL-031", "reason": "open-problems page retained as inspected reference; coverage is better represented by RRL-005 for next-experiment decisions"},
            {"reference_id": "RRL-002", "reason": "method diagram retained as inspected reference; RRL-019 provides stronger scientific task-flow coverage for this first gold set"}
        ]
    }
    (OUT_DIR / "gold_admission_report.json").write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"status": payload["status"], "out_dir": str(OUT_DIR), "probe_count": len(payload["probes"])}, indent=2))
    return 0 if payload["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
