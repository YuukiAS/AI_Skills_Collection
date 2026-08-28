#!/usr/bin/env python3
"""One-call production entry for exact-CUHK research presentations."""

from __future__ import annotations

import argparse
import json
import re
import shutil
from pathlib import Path
from typing import Any

import build_gold_composition_recipe
import deck_quality_loop
import generate_cuhk_scientific_layout_stage3 as stage3
import markdown_to_deck_plan


SHARED = Path(__file__).resolve().parents[1]
REPO_ROOT = Path(__file__).resolve().parents[6]
CANONICAL_CUHK = SHARED / "templates" / "cuhk" / "beamer" / "source"
DEFAULT_TASK_KEY = "031_research_presentation_one_call_production_entry"
DEFAULT_BUNDLE = SHARED / "fixtures" / "stage4_engineering_research_bundle" / "bundle.json"
DEFAULT_OUT = REPO_ROOT / "results" / DEFAULT_TASK_KEY / "generated"
FORBIDDEN_AUDIENCE_TERMS = stage3.FORBIDDEN_AUDIENCE_TERMS
STORYLINE_JOB_ORDER = {
    "STATISTICAL_MODEL": 10,
    "REAL_DATA_APPLICATION": 20,
    "EXPERIMENT_DESIGN": 30,
    "NEGATIVE_RESULT": 40,
    "NEXT_EXPERIMENT": 50,
}


def audience_metadata_violations(metadata: dict[str, Any]) -> list[str]:
    violations: list[str] = []
    forbidden = [term.lower() for term in FORBIDDEN_AUDIENCE_TERMS]
    for field in ["title", "subtitle"]:
        text = str(metadata.get(field, ""))
        lowered = text.lower()
        for term in forbidden:
            if term and term in lowered:
                violations.append(f"metadata.{field} leaks audience-facing internal term {term}")
    return violations


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
    if violations := audience_metadata_violations(bundle.get("metadata", {})):
        raise ValueError(f"{path}: " + "; ".join(violations))
    return bundle


def slug(value: str) -> str:
    normalized = re.sub(r"[^a-z0-9]+", "_", value.lower()).strip("_")
    return normalized or "general_research_update"


def classify_workstream(job: dict[str, Any], evidence_by_id: dict[str, dict[str, Any]]) -> dict[str, Any]:
    if explicit := job.get("workstream"):
        return {
            "id": slug(str(explicit.get("id") or explicit.get("label") or "explicit_workstream")),
            "label": str(explicit.get("label") or explicit.get("id") or "Research workstream"),
            "scope": str(explicit.get("scope") or "source-declared workstream"),
            "assignment_basis": ["explicit source workstream metadata"],
        }

    evidence_boards = [
        evidence_by_id[evidence_id]["board"]
        for evidence_id in job.get("source_evidence_ids", [])
        if evidence_id in evidence_by_id and evidence_by_id[evidence_id].get("board")
    ]
    board = evidence_boards[0] if evidence_boards else str(job.get("page_job", "research_update")).lower()
    label = board.replace("_", " ").title()
    return {
        "id": slug(board),
        "label": label,
        "scope": "source-local research update",
        "assignment_basis": [f"evidence board: {board}"],
    }


def storyline_job_rank(job: dict[str, Any]) -> int:
    return STORYLINE_JOB_ORDER.get(str(job.get("page_job", "")), 100)


def build_storyline(bundle: dict[str, Any]) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    evidence_by_id = {item["id"]: item for item in bundle["evidence"]}
    assignments: list[dict[str, Any]] = []
    workstreams: dict[str, dict[str, Any]] = {}
    for original_index, job in enumerate(bundle["page_jobs"], start=1):
        profile = classify_workstream(job, evidence_by_id)
        workstream = workstreams.setdefault(
            profile["id"],
            {
                "workstream_id": profile["id"],
                "label": profile["label"],
                "scope": profile["scope"],
                "first_source_order": original_index,
                "page_jobs": [],
            },
        )
        workstream["page_jobs"].append(job["page_id"])
        assignments.append(
            {
                "page_id": job["page_id"],
                "page_job": job["page_job"],
                "original_order": original_index,
                "workstream_id": profile["id"],
                "workstream_label": profile["label"],
                "workstream_scope": profile["scope"],
                "assignment_basis": profile["assignment_basis"],
                "intra_workstream_sort_key": [storyline_job_rank(job), original_index],
            }
        )

    ordered_workstreams = sorted(workstreams.values(), key=lambda item: item["first_source_order"])
    workstream_order = {item["workstream_id"]: index for index, item in enumerate(ordered_workstreams, start=1)}
    assignment_by_page = {item["page_id"]: item for item in assignments}
    ordered_jobs = sorted(
        bundle["page_jobs"],
        key=lambda job: (
            workstream_order[assignment_by_page[job["page_id"]]["workstream_id"]],
            storyline_job_rank(job),
            assignment_by_page[job["page_id"]]["original_order"],
        ),
    )

    for new_index, job in enumerate(ordered_jobs, start=1):
        assignment_by_page[job["page_id"]]["storyline_order"] = new_index
        assignment_by_page[job["page_id"]]["workstream_order"] = workstream_order[assignment_by_page[job["page_id"]]["workstream_id"]]

    ordered_workstream_payload = []
    previous_workstream: dict[str, Any] | None = None
    for workstream in ordered_workstreams:
        payload = dict(workstream)
        payload["workstream_order"] = workstream_order[workstream["workstream_id"]]
        if previous_workstream is None:
            payload["source_supported_cross_workstream_relation_to_previous"] = None
            payload["transition_label"] = workstream["label"]
        else:
            payload["source_supported_cross_workstream_relation_to_previous"] = False
            payload["transition_label"] = f"{workstream['label']}: {workstream['scope']}"
            payload["relation_to_previous"] = "independent workstream; no source-supported causal bridge is asserted"
        ordered_workstream_payload.append(payload)
        previous_workstream = workstream

    first_page_by_workstream = {
        workstream_id: min(item["storyline_order"] for item in assignments if item["workstream_id"] == workstream_id)
        for workstream_id in workstream_order
    }
    enriched_jobs = []
    for job in ordered_jobs:
        enriched = dict(job)
        assignment = assignment_by_page[job["page_id"]]
        workstream_payload = ordered_workstream_payload[assignment["workstream_order"] - 1]
        enriched["section"] = assignment["workstream_label"]
        enriched["storyline"] = {
            "workstream_id": assignment["workstream_id"],
            "workstream_label": assignment["workstream_label"],
            "workstream_scope": assignment["workstream_scope"],
            "storyline_order": assignment["storyline_order"],
            "workstream_order": assignment["workstream_order"],
            "assignment_basis": assignment["assignment_basis"],
        }
        if len(ordered_workstreams) > 1 and assignment["storyline_order"] == first_page_by_workstream[assignment["workstream_id"]] and assignment["workstream_order"] > 1:
            enriched["storyline_transition"] = {
                "label": assignment["workstream_label"],
                "audience_text": "independent workstream; no causal bridge asserted",
                "relation_to_previous": workstream_payload["relation_to_previous"],
            }
        enriched_jobs.append(enriched)

    trace = {
        "schema": "RESEARCH_PRESENTATION_STORYLINE_TRACE_V1",
        "source_derivation": "workstream assignment uses explicit page-job/source workstream metadata when present, otherwise evidence-board fallback; titles, page numbers, domain token profiles, and gold IDs are not classification keys",
        "cross_workstream_relation_policy": "do not infer causal bridges between distinct workstreams without explicit source support",
        "workstreams": ordered_workstream_payload,
        "page_assignments": sorted(assignments, key=lambda item: item["storyline_order"]),
        "storyline_order": [job["page_job"] for job in enriched_jobs],
    }
    return enriched_jobs, trace


def build_deck_plan(bundle: dict[str, Any], bundle_path: Path, page_jobs: list[dict[str, Any]], storyline_trace: dict[str, Any]) -> dict[str, Any]:
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
    plan["storyline"] = storyline_trace
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
            "storyline": job["storyline"],
            **({"storyline_transition": job["storyline_transition"]} if "storyline_transition" in job else {}),
            "layout_rationale": job["layout_rationale"],
            "allowed_fallback": "missing evidence, next experiment, speaker notes, backup, or deletion",
            "forbidden_fallback": "rounded-card dashboard, giant empty table, decorative icon, or generic arrows",
            "qa_criteria": job["qa_criteria"],
            "content": job.get("audience_notes", []),
        }
        for index, job in enumerate(page_jobs, start=1)
    ]
    return plan


def build_specs(page_jobs: list[dict[str, Any]]) -> list[dict[str, Any]]:
    specs: list[dict[str, Any]] = []
    for job in page_jobs:
        spec = {
            key: value
            for key, value in job.items()
            if key
            in {
                "page_id",
                "page_job",
                "section",
                "title",
                "key_message",
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
                "storyline",
                "storyline_transition",
                "scientific_objects",
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


def build_render_input_identity(build_dir: Path) -> dict[str, Any]:
    files = []
    for path in sorted(item for item in build_dir.rglob("*") if item.is_file()):
        relative = path.relative_to(build_dir).as_posix()
        if relative == "main.tex":
            role = "main_tex"
        elif relative == "scientific_layouts.tex":
            role = "scientific_layout_include"
        elif relative.startswith("stage3_assets/"):
            role = "copied_scientific_asset"
        elif relative.startswith("styles/"):
            role = "canonical_cuhk_style"
        elif relative.startswith("assets/"):
            role = "canonical_cuhk_asset"
        else:
            role = "canonical_cuhk_support"
        files.append({"path": rel(path), "role": role, "sha256": stage3.file_sha(path)})
    payload = {
        "schema": "RESEARCH_PRESENTATION_RENDER_INPUT_IDENTITY_V1",
        "build_workspace": rel(build_dir),
        "files": files,
    }
    payload["sha256"] = deck_quality_loop.stable_sha(payload)
    return payload


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


def production_trace(bundle: dict[str, Any], specs: list[dict[str, Any]], layouts: list[dict[str, Any]], bundle_path: Path, task_key: str, storyline_trace: dict[str, Any]) -> dict[str, Any]:
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
                "storyline": spec["storyline"],
                "storyline_transition": spec.get("storyline_transition"),
                "resolved_stage3_layout_family": layout["executable_layout_family"],
                "content_capacity_check": layout["content_capacity_check"],
                "benchmark_helper_orchestration_surface_used": False,
                "force_gold_id_used": False,
                "score_override_used": False,
            }
        )
    return {
        "schema": "RESEARCH_PRESENTATION_PRODUCTION_TRACE_V1",
        "task_key": task_key,
        "entrypoint": "research-presentations one-call production",
        "input_bundle": rel(bundle_path),
        "normal_skill_route": "research-presentations",
        "storyline_trace": storyline_trace,
        "benchmark_generators_called_as_entrypoint": [],
        "stage5_holdout_eligible": False,
        "slides": slides,
    }


def render_specs(bundle: dict[str, Any], specs: list[dict[str, Any]], out_dir: Path, task_key: str) -> dict[str, Any]:
    build_dir = out_dir / "cuhk_production_build"
    if build_dir.exists():
        shutil.rmtree(build_dir)
    shutil.copytree(CANONICAL_CUHK, build_dir)
    previous_task_key = stage3.TASK_KEY
    stage3.TASK_KEY = task_key
    try:
        asset_map = stage3.copy_assets(specs, build_dir)
        layouts = [stage3.resolve_layout(spec) for spec in specs]
        (build_dir / "scientific_layouts.tex").write_text(stage3.scientific_layout_macros(), encoding="utf-8")
        (build_dir / "main.tex").write_text(build_main_tex(bundle, specs, layouts, asset_map), encoding="utf-8")
        render_input_identity = build_render_input_identity(build_dir)
        dependency_probe = stage3.dependency_probe()
        render_probe = stage3.render_skill_probe()
        compile_status = stage3.compile_pdf(build_dir)
        render_status = stage3.render_pdf(build_dir, compile_status)
        cleaned = stage3.clean_latex_intermediates(build_dir)
        normalized = stage3.normalize_generated_logs(build_dir)
    finally:
        stage3.TASK_KEY = previous_task_key
    return {
        "build_dir": build_dir,
        "layouts": layouts,
        "render_input_identity": render_input_identity,
        "dependency_probe": dependency_probe,
        "render_probe": render_probe,
        "compile_status": compile_status,
        "render_status": render_status,
        "cleaned": cleaned,
        "normalized": normalized,
    }


def make_deck_contact_sheet(render_status: dict[str, Any], out_dir: Path) -> dict[str, Any]:
    rendered = render_status.get("rendered_png", [])
    if render_status.get("status") != "ok" or not rendered:
        return {"status": "NOT_GENERATED_RENDER_UNAVAILABLE", "path": None, "sha256": None}
    from PIL import Image, ImageDraw, ImageFont

    thumbs = []
    for item in rendered:
        source = REPO_ROOT / item["path"]
        with Image.open(source) as image:
            thumbnail = image.convert("RGB")
            thumbnail.thumbnail((360, 204), Image.Resampling.LANCZOS)
            canvas = Image.new("RGB", (360, 236), "white")
            x = (360 - thumbnail.width) // 2
            canvas.paste(thumbnail, (x, 0))
            thumbs.append((canvas, f"{len(thumbs) + 1}: {Path(item['path']).name}"))

    columns = min(3, len(thumbs))
    rows = (len(thumbs) + columns - 1) // columns
    sheet = Image.new("RGB", (columns * 380 + 20, rows * 268 + 20), "#f7f7f7")
    draw = ImageDraw.Draw(sheet)
    font = ImageFont.load_default()
    for index, (thumb, label) in enumerate(thumbs):
        col = index % columns
        row = index // columns
        x = 20 + col * 380
        y = 20 + row * 268
        sheet.paste(thumb, (x, y))
        draw.text((x, y + 216), label, fill="#222222", font=font)
    path = out_dir / "deck_contact_sheet.png"
    sheet.save(path)
    return {"status": "GENERATED", "path": rel(path), "sha256": stage3.file_sha(path)}


def update_deck_plan_from_specs(deck_plan: dict[str, Any], specs: list[dict[str, Any]]) -> dict[str, Any]:
    updated = dict(deck_plan)
    slides = []
    for slide, spec in zip(deck_plan.get("slides", []), specs):
        enriched = dict(slide)
        if "storyline_transition" in spec:
            enriched["storyline_transition"] = spec["storyline_transition"]
        slides.append(enriched)
    updated["slides"] = slides
    return updated


def visual_manifest(
    *,
    bundle: dict[str, Any],
    specs: list[dict[str, Any]],
    layouts: list[dict[str, Any]],
    render_status: dict[str, Any],
    build_manifest: dict[str, Any],
    build_manifest_path: Path,
    source_fidelity_path: Path,
    deck_sequence_summary_path: Path,
    quality_loop_state_path: Path,
    task_key: str,
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
    contact_sheet = build_manifest.get("deck_contact_sheet", {})
    if contact_sheet.get("status") == "GENERATED":
        inputs.append(
            {
                "logical_id": "deck_contact_sheet",
                "path": contact_sheet["path"],
                "mime_type": "image/png",
                "sha256": contact_sheet["sha256"],
                "description": "Deck-level contact sheet preserving the rendered slide sequence for rhythm, density, transition, and template-repeat review.",
                "review_role": "deck_sequence_context",
            }
        )
    return {
        "schema": "AI_BRIDGE_VISUAL_INPUT_MANIFEST_V1",
        "task_key": task_key,
        "workflow_type": "reviewed_handoff",
        "review_kind": f"{task_key}-one-call-production-research-deck-review",
        "privacy_policy": "PUBLIC_SAFE_ONLY",
        "prompt_version": "ai-bridge.visual-review.v1",
        "external_upload_authorization": "",
        "rubric": {
            "instructions": (
                "Review the rendered pixels from one normal research-presentations production invocation. "
                "Check that each page contains source-specific content from the supplied engineering bundle rather than placeholders; exact CUHK Beamer identity is visible; the main scientific object is prominent and projection-readable; math, native plots, and medical images are semantically correct where present; no internal RRL/GSC/SRC, QA, provenance, workflow, repo path, run ID, or implementation language leaks into audience-facing slides; repeated generic cards or one-template pages are rejected; and the deck reads as one coherent research update rather than disconnected benchmark pages. "
                "For multi-workstream bundles, confirm that each workstream stays internally continuous and that any independent workstream transition is visible without inventing a causal relation. "
                "Separately review the deck_contact_sheet item as a deck-level rhythm object: adjacent-page density jumps, repeated composition face, overfull or empty pages, redundant summary filler, result -> failure -> next-experiment rhythm, workstream transition balance, and title/object/formula/image alternation must meet a mature doctoral group-meeting or strong conference-talk bar. "
                "The top-level package PASS is not enough; provide item-level judgement and observations for deck_contact_sheet. Do not infer visual quality from filenames or hashes."
            ),
            "source_contracts": [
                "The engineering regression bundle is public-safe and explicitly excluded from Stage 5 holdouts.",
                "Stage 2 gold/reference pixels are used only for compatible composition selection.",
                "The deck-quality loop may repair at most once and must fail closed/no-winner for unsafe findings or unresolved blockers.",
            ],
        },
        "identity_bindings": {
            "task_key": task_key,
            "implementation_commit": implementation_commit,
            "input_title": bundle["metadata"]["title"],
            "build_manifest": rel(build_manifest_path),
            "build_manifest_sha256": stage3.file_sha(build_manifest_path),
            "source_fidelity_map": rel(source_fidelity_path),
            "source_fidelity_map_sha256": stage3.file_sha(source_fidelity_path),
            "deck_sequence_summary": rel(deck_sequence_summary_path),
            "deck_sequence_summary_sha256": stage3.file_sha(deck_sequence_summary_path),
            "quality_loop_state": rel(quality_loop_state_path),
            "quality_loop_state_sha256": stage3.file_sha(quality_loop_state_path),
            "deck_contact_sheet": contact_sheet.get("path"),
            "deck_contact_sheet_sha256": contact_sheet.get("sha256"),
            "deck_identity_sha256": build_manifest.get("deck_sequence_summary", {}).get("deck_identity_sha256"),
            "render_input_identity_sha256": build_manifest.get("deck_sequence_summary", {}).get("render_input_identity_sha256"),
            "render_input_identity": build_manifest.get("render_input_identity"),
            "rendered_pixel_identity_sha256": build_manifest.get("deck_sequence_summary", {}).get("rendered_pixel_identity_sha256"),
            "pdf_sha256": build_manifest.get("compile_status", {}).get("pdf_sha256"),
            "page_job_by_logical_id": page_jobs,
            "source_evidence_ids_by_logical_id": evidence,
            "selected_gold_by_page_id": {spec["page_id"]: layout["selected_gold_id"] for spec, layout in zip(specs, layouts)},
        },
        "inputs": inputs,
    }


def generate(
    bundle_path: Path,
    out_dir: Path,
    *,
    task_key: str = DEFAULT_TASK_KEY,
    implementation_commit: str | None = None,
    write_result_visual_inputs: bool = False,
    review_evidence_path: Path | None = None,
    rereview_evidence_path: Path | None = None,
) -> dict[str, Any]:
    bundle_path = bundle_path.resolve()
    out_dir = out_dir.resolve()
    bundle = load_bundle(bundle_path)
    deck_jobs, storyline_trace = build_storyline(bundle)
    deck_plan = build_deck_plan(bundle, bundle_path, deck_jobs, storyline_trace)
    specs = build_specs(deck_jobs)
    out_dir.mkdir(parents=True, exist_ok=True)
    initial_render = render_specs(bundle, specs, out_dir, task_key)
    initial_contact = make_deck_contact_sheet(initial_render["render_status"], out_dir)
    initial_sequence = deck_quality_loop.build_sequence_summary(
        specs=specs,
        layouts=initial_render["layouts"],
        render_status=initial_render["render_status"],
        storyline_trace=storyline_trace,
        render_input_identity=initial_render["render_input_identity"],
        contact_sheet_path=initial_contact.get("path"),
        contact_sheet_sha256=initial_contact.get("sha256"),
    )
    review_evidence, review_evidence_sha256 = deck_quality_loop.load_review_evidence(review_evidence_path.resolve() if review_evidence_path else None)
    quality_loop_state = deck_quality_loop.consume_review_evidence(
        review_evidence=review_evidence,
        review_evidence_sha256=review_evidence_sha256,
        sequence_summary=initial_sequence,
        initial_render_identity=initial_sequence["render_input_identity_sha256"],
        initial_rendered_pixel_identity=initial_sequence["rendered_pixel_identity_sha256"],
        initial_render_input_manifest=initial_sequence["render_input_manifest"],
    )
    final_render = initial_render
    final_contact = initial_contact
    final_sequence = initial_sequence
    if quality_loop_state["repair_allowed"]:
        specs = deck_quality_loop.apply_repair_directives(specs, quality_loop_state["selected_repair_directives"])
        deck_plan = update_deck_plan_from_specs(deck_plan, specs)
        final_render = render_specs(bundle, specs, out_dir, task_key)
        final_contact = make_deck_contact_sheet(final_render["render_status"], out_dir)
        final_sequence = deck_quality_loop.build_sequence_summary(
            specs=specs,
            layouts=final_render["layouts"],
            render_status=final_render["render_status"],
            storyline_trace=storyline_trace,
            render_input_identity=final_render["render_input_identity"],
            contact_sheet_path=final_contact.get("path"),
            contact_sheet_sha256=final_contact.get("sha256"),
        )
        quality_loop_state["repair_cycle_count"] = 1
        quality_loop_state["repaired_render_identity"] = final_sequence["render_input_identity_sha256"]
        quality_loop_state["repaired_render_input_identity"] = final_sequence["render_input_identity_sha256"]
        quality_loop_state["repaired_rendered_pixel_identity"] = final_sequence["rendered_pixel_identity_sha256"]
        quality_loop_state["repaired_render_input_manifest"] = final_sequence["render_input_manifest"]
        rereview_evidence, rereview_evidence_sha256 = deck_quality_loop.load_review_evidence(rereview_evidence_path.resolve() if rereview_evidence_path else None)
        rereview_state = deck_quality_loop.consume_review_evidence(
            review_evidence=rereview_evidence,
            review_evidence_sha256=rereview_evidence_sha256,
            sequence_summary=final_sequence,
            initial_render_identity=initial_sequence["render_input_identity_sha256"],
            initial_rendered_pixel_identity=initial_sequence["rendered_pixel_identity_sha256"],
            initial_render_input_manifest=initial_sequence["render_input_manifest"],
            repair_cycle_count=1,
        )
        quality_loop_state["rereview_evidence_identity"] = rereview_evidence_sha256
        if rereview_evidence is None:
            quality_loop_state["deck_level_decision"] = "WAITING_FOR_REPAIRED_DECK_REVIEW"
            quality_loop_state["final_decision"] = None
        else:
            quality_loop_state["post_repair_deck_level_decision"] = rereview_state["deck_level_decision"]
            quality_loop_state["final_decision"] = rereview_state["final_decision"]
            quality_loop_state["post_repair_blocking_findings"] = rereview_state["blocking_findings"]
            quality_loop_state["post_repair_fail_closed_reason"] = rereview_state["fail_closed_reason"]

    write_json(out_dir / "deck_plan.json", deck_plan)
    write_json(out_dir / "resolved_layouts.json", {"schema": "RESEARCH_PRESENTATION_PRODUCTION_RESOLVED_LAYOUTS_V1", "task_key": task_key, "layouts": final_render["layouts"]})
    fidelity = source_fidelity_map(bundle, specs, final_render["layouts"])
    fidelity_path = out_dir / "source_fidelity_map.json"
    write_json(fidelity_path, fidelity)
    write_json(out_dir / "storyline_trace.json", storyline_trace)
    trace = production_trace(bundle, specs, final_render["layouts"], bundle_path, task_key, storyline_trace)
    trace["deck_quality_loop"] = {
        "quality_loop_state": rel(out_dir / "quality_loop_state.json"),
        "deck_sequence_summary": rel(out_dir / "deck_sequence_summary.json"),
        "deck_contact_sheet": final_contact,
    }
    write_json(out_dir / "runtime_trace.json", trace)
    write_json(out_dir / "dependency_probe.json", final_render["dependency_probe"])
    write_json(out_dir / "render_chinese_math_pdf_probe.json", final_render["render_probe"])
    sequence_path = out_dir / "deck_sequence_summary.json"
    write_json(sequence_path, final_sequence)
    quality_loop_path = out_dir / "quality_loop_state.json"
    write_json(quality_loop_path, quality_loop_state)
    build_manifest = {
        "schema": "RESEARCH_PRESENTATION_PRODUCTION_BUILD_MANIFEST_V1",
        "task_key": task_key,
        "implementation_commit": implementation_commit,
        "input_bundle": rel(bundle_path),
        "canonical_cuhk_source": rel(CANONICAL_CUHK),
        "canonical_files": {rel(path): stage3.file_sha(path) for path in sorted(CANONICAL_CUHK.rglob("*")) if path.is_file()},
        "build_workspace": rel(final_render["build_dir"]),
        "render_input_identity_sha256": final_sequence["render_input_identity_sha256"],
        "render_input_identity": final_render["render_input_identity"],
        "tex": rel(final_render["build_dir"] / "main.tex"),
        "scientific_layout_include": rel(final_render["build_dir"] / "scientific_layouts.tex"),
        "deck_plan": rel(out_dir / "deck_plan.json"),
        "source_fidelity_map": rel(fidelity_path),
        "runtime_trace": rel(out_dir / "runtime_trace.json"),
        "storyline_trace": rel(out_dir / "storyline_trace.json"),
        "deck_sequence_summary_path": rel(sequence_path),
        "deck_sequence_summary": final_sequence,
        "deck_contact_sheet": final_contact,
        "quality_loop_state": rel(quality_loop_path),
        "dependency_probe": rel(out_dir / "dependency_probe.json"),
        "render_chinese_math_pdf_probe": rel(out_dir / "render_chinese_math_pdf_probe.json"),
        "compile_status": final_render["compile_status"],
        "render_status": final_render["render_status"],
        "mechanical_qa": {
            "status": "MECHANICAL_PASS" if final_render["render_status"].get("status") == "ok" and final_render["render_status"].get("png_count", 0) >= len(specs) + 1 else "BLOCKED_RENDER_QA",
            "checks": {
                "normal_research_presentations_entry": True,
                "input_bundle_read_from_path": True,
                "canonical_source_copied": True,
                "scientific_layout_include_loaded": True,
                "content_page_jobs": len(specs),
                "rendered_pages_available": final_render["render_status"].get("status") == "ok",
                "deck_contact_sheet_generated": final_contact.get("status") == "GENERATED",
                "quality_loop_budget_enforced": quality_loop_state["repair_cycle_count"] <= deck_quality_loop.MAX_REPAIR_CYCLES,
            },
        },
        "quality_loop_handoff": {
            "schema": "RESEARCH_PRESENTATION_STAGE4_QUALITY_HANDOFF_V1",
            "status": quality_loop_state["final_decision"] or quality_loop_state["deck_level_decision"],
            "visual_review_manifest": f"results/{task_key}/visual_review/visual_inputs.json",
            "visual_review_evidence": f"results/{task_key}/visual_review/VISUAL_REVIEW.json",
            "quality_loop_state": rel(quality_loop_path),
            "deck_contact_sheet": final_contact.get("path"),
            "render_input_identity_sha256": final_sequence["render_input_identity_sha256"],
            "rendered_pixel_identity_sha256": final_sequence["rendered_pixel_identity_sha256"],
        },
        "stage4_boundary": "This one-call production entry recovery does not claim Stage 4 PASS, PROGRAM_MATURE, or ONE_SHOT_QUALITY_PASS.",
        "cleaned_latex_intermediates": final_render["cleaned"],
        "normalized_generated_logs": final_render["normalized"],
    }
    manifest_path = out_dir / "BUILD_MANIFEST.json"
    write_json(manifest_path, build_manifest)
    visual_inputs = visual_manifest(
        bundle=bundle,
        specs=specs,
        layouts=final_render["layouts"],
        render_status=final_render["render_status"],
        build_manifest=build_manifest,
        build_manifest_path=manifest_path,
        source_fidelity_path=fidelity_path,
        deck_sequence_summary_path=sequence_path,
        quality_loop_state_path=quality_loop_path,
        task_key=task_key,
        implementation_commit=implementation_commit,
    )
    write_json(out_dir / "visual_inputs.json", visual_inputs)
    if write_result_visual_inputs:
        write_json(REPO_ROOT / "results" / task_key / "visual_review" / "visual_inputs.json", visual_inputs)
    return build_manifest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-bundle", type=Path, default=DEFAULT_BUNDLE)
    parser.add_argument("--out-dir", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--task-key", default=DEFAULT_TASK_KEY)
    parser.add_argument("--implementation-commit")
    parser.add_argument("--write-result-visual-inputs", action="store_true")
    parser.add_argument("--review-evidence", type=Path)
    parser.add_argument("--rereview-evidence", type=Path)
    args = parser.parse_args()
    manifest = generate(
        args.input_bundle,
        args.out_dir,
        task_key=args.task_key,
        implementation_commit=args.implementation_commit,
        write_result_visual_inputs=args.write_result_visual_inputs,
        review_evidence_path=args.review_evidence,
        rereview_evidence_path=args.rereview_evidence,
    )
    print(
        json.dumps(
            {
                "status": manifest["mechanical_qa"]["status"],
                "out_dir": rel(args.out_dir),
                "render_status": manifest["render_status"]["status"],
                "tex": manifest["tex"],
                "visual_inputs": f"results/{args.task_key}/visual_review/visual_inputs.json" if args.write_result_visual_inputs else manifest["runtime_trace"],
            },
            indent=2,
        )
    )
    return 0 if manifest["mechanical_qa"]["status"] == "MECHANICAL_PASS" else 2


if __name__ == "__main__":
    raise SystemExit(main())
