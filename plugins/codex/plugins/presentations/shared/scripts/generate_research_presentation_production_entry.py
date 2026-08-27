#!/usr/bin/env python3
"""One-call production entry for exact-CUHK research presentations."""

from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path
from typing import Any

import build_gold_composition_recipe
import generate_cuhk_scientific_layout_stage3 as stage3
import markdown_to_deck_plan


SHARED = Path(__file__).resolve().parents[1]
REPO_ROOT = Path(__file__).resolve().parents[6]
CANONICAL_CUHK = SHARED / "templates" / "cuhk" / "beamer" / "source"
DEFAULT_TASK_KEY = "031_research_presentation_one_call_production_entry"
DEFAULT_BUNDLE = SHARED / "fixtures" / "stage4_engineering_research_bundle" / "bundle.json"
DEFAULT_OUT = REPO_ROOT / "results" / DEFAULT_TASK_KEY / "generated"
FORBIDDEN_AUDIENCE_TERMS = stage3.FORBIDDEN_AUDIENCE_TERMS


def rel(path: Path) -> str:
    return stage3.rel(path)


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def load_bundle(path: Path) -> dict[str, Any]:
    bundle = json.loads(path.read_text(encoding="utf-8"))
    if bundle.get("schema") != "RESEARCH_PRESENTATION_PRODUCTION_BUNDLE_V1":
        raise ValueError(f"{path}: unsupported production bundle schema")
    if bundle.get("stage5_holdout_eligible") is not False:
        raise ValueError(f"{path}: engineering regression bundle must be excluded from Stage 5 holdouts")
    if not bundle.get("page_jobs"):
        raise ValueError(f"{path}: production bundle contains no page jobs")
    return bundle


def build_deck_plan(bundle: dict[str, Any], bundle_path: Path) -> dict[str, Any]:
    markdown_path = REPO_ROOT / bundle["source_material"]["primary_markdown"]
    plan = markdown_to_deck_plan.markdown_to_deck_plan(
        markdown_path.read_text(encoding="utf-8"),
        bundle["metadata"]["title"],
        output="tex",
        mode="research-group-meeting",
    )
    plan["metadata"].update(
        {
            "audience": bundle["metadata"].get("audience", "research group"),
            "language": bundle["metadata"].get("language", "en"),
            "source_files": [rel(bundle_path), bundle["source_material"]["primary_markdown"]],
            "template": "exact-cuhk-beamer-source",
            "production_entry": "research-presentations one-call production",
        }
    )
    evidence_board = {
        key: []
        for key in [
            "available_figures",
            "medical_images",
            "qualitative_examples",
            "quantitative_plots",
            "model_diagrams",
            "equations",
            "experiment_logs",
            "failed_experiments",
            "literature_figures_to_redraw",
            "missing_evidence",
        ]
    }
    for evidence in bundle["evidence"]:
        evidence_board[evidence["board"]].append(evidence)
    plan["evidence_board"] = evidence_board
    plan["research_state"] = bundle["research_state"]
    plan["slides"] = [
        {
            "id": f"s{index:02d}",
            "title": job["title"],
            "key_message": job["key_message"],
            "slide_purpose": job["slide_purpose"],
            "visual_intent": job["visual_intent"],
            "source_anchors": job["source_anchors"],
            "page_function": job["page_job"],
            "required_evidence": job["required_evidence"],
            "source_evidence_ids": job["source_evidence_ids"],
            "scientific_objects": job["scientific_objects"],
            "evidence_status": job["evidence_status"],
            "uncertainty_status": job["uncertainty_status"],
            "layout_rationale": job["layout_rationale"],
            "allowed_fallback": "missing evidence, next experiment, speaker notes, backup, or deletion",
            "forbidden_fallback": "rounded-card dashboard, giant empty table, decorative icon, or generic arrows",
            "qa_criteria": job["qa_criteria"],
            "content": job.get("audience_notes", []),
        }
        for index, job in enumerate(bundle["page_jobs"], start=1)
    ]
    return plan


def build_specs(bundle: dict[str, Any]) -> list[dict[str, Any]]:
    specs: list[dict[str, Any]] = []
    for job in bundle["page_jobs"]:
        spec = {
            key: value
            for key, value in job.items()
            if key
            in {
                "page_id",
                "page_job",
                "section",
                "title",
                "query",
                "content_kind",
                "dominant_object",
                "math",
                "annotation",
                "caption",
                "required_panel_count",
                "data_source",
                "figure_filter",
                "methods",
                "nominal_coverage",
                "callout",
                "asset",
                "assets",
                "panel_labels",
                "roi_source_asset",
                "roi_crop_assets",
                "roi_crop_labels",
                "nodes",
                "design_factors",
                "procedures",
                "endpoints",
                "current_limit",
                "strategy_variation",
                "comparator_setup",
                "decision_criterion",
            }
        }
        spec["source_evidence_ids"] = list(job["source_evidence_ids"])
        specs.append(spec)
    return specs


def build_main_tex(bundle: dict[str, Any], specs: list[dict[str, Any]], layouts: list[dict[str, Any]], asset_map: dict[str, str]) -> str:
    frames = "\n".join(stage3.emit_frame(spec, layout, asset_map) for spec, layout in zip(specs, layouts))
    metadata = bundle["metadata"]
    title = stage3.tex_escape(metadata["title"])
    subtitle = stage3.tex_escape(metadata.get("subtitle", "Research update"))
    author = stage3.tex_escape(metadata.get("author", "Research Presentation Program"))
    institute = stage3.tex_escape(metadata.get("institute", "Department of Statistics & Data Science"))
    date = stage3.tex_escape(metadata.get("date", r"\today"))
    return rf"""% Generated by research-presentations one-call production entry.
\documentclass[aspectratio=169]{{beamer}}
\usepackage{{amsfonts,amsmath,amssymb,booktabs,graphicx}}
\makeatletter
\def\input@path{{{{styles/}}}}
\makeatother
\usetheme{{sintef}}
\titlebackground*{{assets/background}}
\input{{scientific_layouts.tex}}
\setbeameroption{{hide notes}}
\bibliographystyle{{unsrt}}

\title{{{title}}}
\subtitle{{{subtitle}}}
\author{{{author}}}
\institute{{{institute}}}
\date{{{date}}}

\begin{{document}}
\maketitle
{frames}
\end{{document}}
"""


def source_fidelity_map(bundle: dict[str, Any], specs: list[dict[str, Any]], layouts: list[dict[str, Any]]) -> dict[str, Any]:
    evidence_by_id = {item["id"]: item for item in bundle["evidence"]}
    pages = []
    for spec, layout in zip(specs, layouts):
        anchors = []
        for evidence_id in spec["source_evidence_ids"]:
            evidence = evidence_by_id[evidence_id]
            anchors.append(
                {
                    "evidence_id": evidence_id,
                    "source_path": evidence["source_path"],
                    "source_anchor": evidence["source_anchor"],
                    "claim_supported": evidence["supports"],
                    "consumed_as": evidence["consumed_as"],
                }
            )
        pages.append(
            {
                "page_id": spec["page_id"],
                "page_job": spec["page_job"],
                "source_evidence_ids": spec["source_evidence_ids"],
                "anchors": anchors,
                "generated_object_ids": [item["object_id"] for item in layout["native_objects"]],
                "selected_gold_id": layout["selected_gold_id"],
                "selected_reference_id": layout["selected_reference_id"],
                "source_recipe_fields_consumed": layout["source_recipe_fields_consumed"],
            }
        )
    return {
        "schema": "RESEARCH_PRESENTATION_SOURCE_FIDELITY_MAP_V1",
        "stage5_holdout_eligible": False,
        "holdout_exclusion_reason": bundle["holdout_exclusion_reason"],
        "pages": pages,
    }


def production_trace(bundle: dict[str, Any], specs: list[dict[str, Any]], layouts: list[dict[str, Any]], bundle_path: Path) -> dict[str, Any]:
    slides = []
    for spec, layout in zip(specs, layouts):
        selection = build_gold_composition_recipe.build_recipe(spec["query"])["runtime_trace"]["selection"]
        slides.append(
            {
                "page_id": spec["page_id"],
                "page_job": spec["page_job"],
                "scientific_object_query": spec["query"],
                "source_evidence_ids": spec["source_evidence_ids"],
                "normal_selector_matches": selection["matches"],
                "selected_gold_id": layout["selected_gold_id"],
                "selected_reference_id": layout["selected_reference_id"],
                "source_composition_identity": {
                    "recipe_sha256": layout["recipe_sha256"],
                    "resolved_layout_sha256": layout["resolved_layout_sha256"],
                },
                "source_derived_composition_fields_consumed": layout["source_recipe_fields_consumed"],
                "resolved_stage3_layout_family": layout["executable_layout_family"],
                "content_capacity_check": layout["content_capacity_check"],
                "benchmark_helper_orchestration_surface_used": False,
                "force_gold_id_used": False,
                "score_override_used": False,
            }
        )
    return {
        "schema": "RESEARCH_PRESENTATION_PRODUCTION_TRACE_V1",
        "task_key": DEFAULT_TASK_KEY,
        "entrypoint": "research-presentations one-call production",
        "input_bundle": rel(bundle_path),
        "normal_skill_route": "research-presentations",
        "benchmark_generators_called_as_entrypoint": [],
        "stage5_holdout_eligible": False,
        "slides": slides,
    }


def visual_manifest(
    *,
    bundle: dict[str, Any],
    specs: list[dict[str, Any]],
    layouts: list[dict[str, Any]],
    render_status: dict[str, Any],
    build_manifest: dict[str, Any],
    build_manifest_path: Path,
    source_fidelity_path: Path,
    implementation_commit: str | None,
) -> dict[str, Any]:
    rendered = render_status.get("rendered_png", [])
    inputs = []
    page_jobs: dict[str, str] = {}
    evidence: dict[str, list[str]] = {}
    for idx, item in enumerate(rendered, start=1):
        if idx < 2 or idx - 2 >= len(specs):
            continue
        spec = specs[idx - 2]
        logical_id = f"slide_{idx}_{spec['page_job'].lower()}"
        inputs.append(
            {
                "logical_id": logical_id,
                "path": item["path"],
                "mime_type": "image/png",
                "sha256": item["sha256"],
                "description": f"Rendered exact-CUHK production page for {spec['page_job']} using source evidence {', '.join(spec['source_evidence_ids'])}.",
            }
        )
        page_jobs[logical_id] = spec["page_job"]
        evidence[logical_id] = spec["source_evidence_ids"]
    return {
        "schema": "AI_BRIDGE_VISUAL_INPUT_MANIFEST_V1",
        "task_key": DEFAULT_TASK_KEY,
        "workflow_type": "reviewed_handoff",
        "review_kind": f"{DEFAULT_TASK_KEY}-one-call-production-research-deck-review",
        "privacy_policy": "PUBLIC_SAFE_ONLY",
        "prompt_version": "ai-bridge.visual-review.v1",
        "external_upload_authorization": "",
        "rubric": {
            "instructions": (
                "Review the rendered pixels from one normal research-presentations production invocation. "
                "Check that each page contains source-specific content from the supplied engineering bundle rather than placeholders; exact CUHK Beamer identity is visible; the main scientific object is prominent and projection-readable; math, native plots, and medical images are semantically correct where present; no internal RRL/GSC/SRC, QA, provenance, workflow, repo path, run ID, or implementation language leaks into audience-facing slides; repeated generic cards or one-template pages are rejected; and the deck reads as one coherent research update rather than disconnected benchmark pages. "
                "Do not infer visual quality from filenames or hashes."
            ),
            "source_contracts": [
                "The engineering regression bundle is public-safe and explicitly excluded from Stage 5 holdouts.",
                "Stage 2 gold/reference pixels are used only for compatible composition selection.",
                "031 is a bounded Stage 4 production-entry proof, not full Stage 4 PASS or ONE_SHOT_QUALITY_PASS.",
            ],
        },
        "identity_bindings": {
            "task_key": DEFAULT_TASK_KEY,
            "implementation_commit": implementation_commit,
            "input_title": bundle["metadata"]["title"],
            "build_manifest": rel(build_manifest_path),
            "build_manifest_sha256": stage3.file_sha(build_manifest_path),
            "source_fidelity_map": rel(source_fidelity_path),
            "source_fidelity_map_sha256": stage3.file_sha(source_fidelity_path),
            "pdf_sha256": build_manifest.get("compile_status", {}).get("pdf_sha256"),
            "page_job_by_logical_id": page_jobs,
            "source_evidence_ids_by_logical_id": evidence,
            "selected_gold_by_page_id": {spec["page_id"]: layout["selected_gold_id"] for spec, layout in zip(specs, layouts)},
        },
        "inputs": inputs,
    }


def generate(bundle_path: Path, out_dir: Path, *, implementation_commit: str | None = None, write_result_visual_inputs: bool = False) -> dict[str, Any]:
    bundle_path = bundle_path.resolve()
    out_dir = out_dir.resolve()
    bundle = load_bundle(bundle_path)
    deck_plan = build_deck_plan(bundle, bundle_path)
    specs = build_specs(bundle)
    out_dir.mkdir(parents=True, exist_ok=True)
    build_dir = out_dir / "cuhk_production_build"
    if build_dir.exists():
        shutil.rmtree(build_dir)
    shutil.copytree(CANONICAL_CUHK, build_dir)
    previous_task_key = stage3.TASK_KEY
    stage3.TASK_KEY = DEFAULT_TASK_KEY
    try:
        asset_map = stage3.copy_assets(specs, build_dir)
        layouts = [stage3.resolve_layout(spec) for spec in specs]
        (build_dir / "scientific_layouts.tex").write_text(stage3.scientific_layout_macros(), encoding="utf-8")
        (build_dir / "main.tex").write_text(build_main_tex(bundle, specs, layouts, asset_map), encoding="utf-8")
        dependency_probe = stage3.dependency_probe()
        render_probe = stage3.render_skill_probe()
        compile_status = stage3.compile_pdf(build_dir)
        render_status = stage3.render_pdf(build_dir, compile_status)
        cleaned = stage3.clean_latex_intermediates(build_dir)
        normalized = stage3.normalize_generated_logs(build_dir)
    finally:
        stage3.TASK_KEY = previous_task_key

    write_json(out_dir / "deck_plan.json", deck_plan)
    write_json(out_dir / "resolved_layouts.json", {"schema": "RESEARCH_PRESENTATION_PRODUCTION_RESOLVED_LAYOUTS_V1", "task_key": DEFAULT_TASK_KEY, "layouts": layouts})
    fidelity = source_fidelity_map(bundle, specs, layouts)
    fidelity_path = out_dir / "source_fidelity_map.json"
    write_json(fidelity_path, fidelity)
    trace = production_trace(bundle, specs, layouts, bundle_path)
    write_json(out_dir / "runtime_trace.json", trace)
    write_json(out_dir / "dependency_probe.json", dependency_probe)
    write_json(out_dir / "render_chinese_math_pdf_probe.json", render_probe)
    build_manifest = {
        "schema": "RESEARCH_PRESENTATION_PRODUCTION_BUILD_MANIFEST_V1",
        "task_key": DEFAULT_TASK_KEY,
        "implementation_commit": implementation_commit,
        "input_bundle": rel(bundle_path),
        "canonical_cuhk_source": rel(CANONICAL_CUHK),
        "canonical_files": {rel(path): stage3.file_sha(path) for path in sorted(CANONICAL_CUHK.rglob("*")) if path.is_file()},
        "build_workspace": rel(build_dir),
        "tex": rel(build_dir / "main.tex"),
        "scientific_layout_include": rel(build_dir / "scientific_layouts.tex"),
        "deck_plan": rel(out_dir / "deck_plan.json"),
        "source_fidelity_map": rel(fidelity_path),
        "runtime_trace": rel(out_dir / "runtime_trace.json"),
        "dependency_probe": rel(out_dir / "dependency_probe.json"),
        "render_chinese_math_pdf_probe": rel(out_dir / "render_chinese_math_pdf_probe.json"),
        "compile_status": compile_status,
        "render_status": render_status,
        "mechanical_qa": {
            "status": "MECHANICAL_PASS" if render_status.get("status") == "ok" and render_status.get("png_count", 0) >= len(specs) + 1 else "BLOCKED_RENDER_QA",
            "checks": {
                "normal_research_presentations_entry": True,
                "input_bundle_read_from_path": True,
                "canonical_source_copied": True,
                "scientific_layout_include_loaded": True,
                "content_page_jobs": len(specs),
                "rendered_pages_available": render_status.get("status") == "ok",
            },
        },
        "quality_loop_handoff": {
            "schema": "RESEARCH_PRESENTATION_STAGE4_QUALITY_HANDOFF_V1",
            "status": "READY_FOR_PAGE_LEVEL_FINDINGS",
            "visual_review_manifest": f"results/{DEFAULT_TASK_KEY}/visual_review/visual_inputs.json",
            "visual_review_evidence": f"results/{DEFAULT_TASK_KEY}/visual_review/VISUAL_REVIEW.json",
            "next_bounded_stage4_task": "deck-rhythm review and bounded visual repair loop",
        },
        "stage4_boundary": "031 proves one-call production entry only; Stage 4 PASS, PROGRAM_MATURE, and ONE_SHOT_QUALITY_PASS are not claimed.",
        "cleaned_latex_intermediates": cleaned,
        "normalized_generated_logs": normalized,
    }
    manifest_path = out_dir / "BUILD_MANIFEST.json"
    write_json(manifest_path, build_manifest)
    visual_inputs = visual_manifest(
        bundle=bundle,
        specs=specs,
        layouts=layouts,
        render_status=render_status,
        build_manifest=build_manifest,
        build_manifest_path=manifest_path,
        source_fidelity_path=fidelity_path,
        implementation_commit=implementation_commit,
    )
    write_json(out_dir / "visual_inputs.json", visual_inputs)
    if write_result_visual_inputs:
        write_json(REPO_ROOT / "results" / DEFAULT_TASK_KEY / "visual_review" / "visual_inputs.json", visual_inputs)
    return build_manifest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-bundle", type=Path, default=DEFAULT_BUNDLE)
    parser.add_argument("--out-dir", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--implementation-commit")
    parser.add_argument("--write-result-visual-inputs", action="store_true")
    args = parser.parse_args()
    manifest = generate(
        args.input_bundle,
        args.out_dir,
        implementation_commit=args.implementation_commit,
        write_result_visual_inputs=args.write_result_visual_inputs,
    )
    print(
        json.dumps(
            {
                "status": manifest["mechanical_qa"]["status"],
                "out_dir": rel(args.out_dir),
                "render_status": manifest["render_status"]["status"],
                "tex": manifest["tex"],
                "visual_inputs": f"results/{DEFAULT_TASK_KEY}/visual_review/visual_inputs.json" if args.write_result_visual_inputs else manifest["runtime_trace"],
            },
            indent=2,
        )
    )
    return 0 if manifest["mechanical_qa"]["status"] == "MECHANICAL_PASS" else 2


if __name__ == "__main__":
    raise SystemExit(main())
