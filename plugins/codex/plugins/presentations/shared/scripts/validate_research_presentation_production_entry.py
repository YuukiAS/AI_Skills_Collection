#!/usr/bin/env python3
"""Validate one-call research presentation production-entry artifacts."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[6]
DEFAULT_TASK_KEY = "031_research_presentation_one_call_production_entry"
DEFAULT_OUT = REPO_ROOT / "results" / DEFAULT_TASK_KEY / "generated"
FORBIDDEN_AUDIENCE_TERMS = [
    "RRL-",
    "SRC-",
    "GSC-",
    "Reference retrieval",
    "EVIDENCE_MANIFEST",
    "Diagram contract",
    "QA",
    "repo path",
    "run ID",
    "implementation commit",
    "implementation language",
    "production regression",
    "source bundle",
    "provenance",
    "review target",
    "fixture",
    "workflow",
    "Workstream transition",
    "independent workstream",
    "no causal bridge asserted",
]


def resolve(path: str) -> Path:
    candidate = Path(path)
    return candidate if candidate.is_absolute() else REPO_ROOT / candidate


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def validate(out_dir: Path, *, task_key: str = DEFAULT_TASK_KEY, allow_missing_render: bool = False) -> list[str]:
    errors: list[str] = []
    required = {
        "manifest": out_dir / "BUILD_MANIFEST.json",
        "deck_plan": out_dir / "deck_plan.json",
        "source_fidelity": out_dir / "source_fidelity_map.json",
        "trace": out_dir / "runtime_trace.json",
        "storyline": out_dir / "storyline_trace.json",
        "deck_sequence": out_dir / "deck_sequence_summary.json",
        "quality_loop": out_dir / "quality_loop_state.json",
        "layouts": out_dir / "resolved_layouts.json",
        "dependency": out_dir / "dependency_probe.json",
        "render_probe": out_dir / "render_chinese_math_pdf_probe.json",
        "visual_inputs": out_dir / "visual_inputs.json",
    }
    for path in required.values():
        if not path.exists():
            errors.append(f"{path}: missing")
    if errors:
        return errors

    manifest = load_json(required["manifest"])
    deck_plan = load_json(required["deck_plan"])
    fidelity = load_json(required["source_fidelity"])
    trace = load_json(required["trace"])
    storyline = load_json(required["storyline"])
    deck_sequence = load_json(required["deck_sequence"])
    quality_loop = load_json(required["quality_loop"])
    layouts = load_json(required["layouts"])
    dependency = load_json(required["dependency"])
    render_probe = load_json(required["render_probe"])
    visual_inputs = load_json(required["visual_inputs"])
    render_status = manifest.get("render_status", {})

    if manifest.get("schema") != "RESEARCH_PRESENTATION_PRODUCTION_BUILD_MANIFEST_V1":
        errors.append("BUILD_MANIFEST.json: invalid schema")
    if manifest.get("task_key") != task_key:
        errors.append("BUILD_MANIFEST.json: task_key mismatch")
    if "storyline_trace" not in manifest:
        errors.append("BUILD_MANIFEST.json: storyline_trace not recorded")
    if "templates/cuhk/beamer/source" not in manifest.get("canonical_cuhk_source", ""):
        errors.append("BUILD_MANIFEST.json: canonical exact CUHK source not recorded")
    if not re.fullmatch(r"[0-9a-f]{64}", str(manifest.get("render_input_identity_sha256", ""))):
        errors.append("BUILD_MANIFEST.json: missing render-input identity sha")
    if manifest.get("render_input_identity", {}).get("sha256") != manifest.get("render_input_identity_sha256"):
        errors.append("BUILD_MANIFEST.json: render-input identity manifest mismatch")
    handoff_status = manifest.get("quality_loop_handoff", {}).get("status")
    if handoff_status not in {
        "WAITING_FOR_DECK_VISUAL_REVIEW",
        "WAITING_FOR_REPAIRED_DECK_REVIEW",
        "READY_TO_DELIVER",
        "QUALITY_LOOP_FAIL_NO_WINNER",
        "UNSAFE_REPAIR_MAPPING",
        "REPAIR_SELECTED",
        "PASS",
    }:
        errors.append("BUILD_MANIFEST.json: missing machine-readable deck quality-loop handoff")
    if "Stage 4 PASS" not in manifest.get("stage4_boundary", ""):
        errors.append("BUILD_MANIFEST.json: Stage 4 non-PASS boundary not documented")

    if deck_plan.get("metadata", {}).get("production_entry") != "research-presentations one-call production":
        errors.append("deck_plan.json: normal production entry not recorded")
    if deck_plan.get("metadata", {}).get("output") != "tex":
        errors.append("deck_plan.json: production route did not resolve to tex")
    if any("UNKNOWN" in json.dumps(slide, ensure_ascii=False) for slide in deck_plan.get("slides", [])):
        errors.append("deck_plan.json: generated slide still contains UNKNOWN planning placeholders")
    for field in ["title", "subtitle"]:
        text = str(deck_plan.get("metadata", {}).get(field, ""))
        lower_text = text.lower()
        for forbidden in FORBIDDEN_AUDIENCE_TERMS:
            if forbidden.lower() in lower_text:
                errors.append(f"deck_plan.json: metadata.{field} leaks audience-facing internal term {forbidden}")

    pages = fidelity.get("pages", [])
    if fidelity.get("schema") != "RESEARCH_PRESENTATION_SOURCE_FIDELITY_MAP_V1":
        errors.append("source_fidelity_map.json: invalid schema")
    if fidelity.get("stage5_holdout_eligible") is not False:
        errors.append("source_fidelity_map.json: engineering bundle is not excluded from Stage 5 holdouts")
    if len(pages) < 4:
        errors.append("source_fidelity_map.json: too few source-mapped pages")
    for page in pages:
        if not page.get("anchors"):
            errors.append(f"source_fidelity_map.json: {page.get('page_id')} has no anchors")
        if not page.get("source_recipe_fields_consumed"):
            errors.append(f"source_fidelity_map.json: {page.get('page_id')} records no consumed recipe fields")

    expected_jobs = {
        "STATISTICAL_MODEL",
        "REAL_DATA_APPLICATION",
        "EXPERIMENT_DESIGN",
        "NEGATIVE_RESULT",
        "MEDICAL_IMAGE_COMPARISON",
        "NEXT_EXPERIMENT",
    }
    trace_jobs = {item.get("page_job") for item in trace.get("slides", [])}
    if trace.get("schema") != "RESEARCH_PRESENTATION_PRODUCTION_TRACE_V1":
        errors.append("runtime_trace.json: invalid schema")
    if trace.get("task_key") != task_key:
        errors.append("runtime_trace.json: task_key mismatch")
    if trace.get("entrypoint") != "research-presentations one-call production":
        errors.append("runtime_trace.json: not the normal production entry")
    if trace.get("benchmark_generators_called_as_entrypoint"):
        errors.append("runtime_trace.json: benchmark generator used as entrypoint")
    if not {"STATISTICAL_MODEL", "REAL_DATA_APPLICATION"}.issubset(trace_jobs):
        errors.append(f"runtime_trace.json: missing required method/result jobs {sorted(trace_jobs)}")
    if not expected_jobs.issubset(trace_jobs):
        errors.append(f"runtime_trace.json: missing Stage 3 page jobs {sorted(expected_jobs - trace_jobs)}")
    for item in trace.get("slides", []):
        if not item.get("normal_selector_matches"):
            errors.append(f"runtime_trace.json: {item.get('page_id')} has no compatible gold selection")
        if item.get("force_gold_id_used") or item.get("score_override_used"):
            errors.append(f"runtime_trace.json: {item.get('page_id')} bypassed normal selector")
        if item.get("benchmark_helper_orchestration_surface_used"):
            errors.append(f"runtime_trace.json: {item.get('page_id')} used benchmark helper orchestration")
        if not item.get("source_derived_composition_fields_consumed"):
            errors.append(f"runtime_trace.json: {item.get('page_id')} did not consume Stage 3 fields")

    if storyline.get("schema") != "RESEARCH_PRESENTATION_STORYLINE_TRACE_V1":
        errors.append("storyline_trace.json: invalid schema")
    workstreams = storyline.get("workstreams", [])
    assignments = storyline.get("page_assignments", [])
    if len(workstreams) >= 2:
        order = storyline.get("storyline_order", [])
        coverage_order = [
            "STATISTICAL_MODEL",
            "REAL_DATA_APPLICATION",
            "EXPERIMENT_DESIGN",
            "NEGATIVE_RESULT",
            "NEXT_EXPERIMENT",
        ]
        if order[:5] != coverage_order:
            errors.append(f"storyline_trace.json: clustered coverage workstream is not continuous: {order}")
        if order[5:6] != ["MEDICAL_IMAGE_COMPARISON"]:
            errors.append(f"storyline_trace.json: medical page is not the independent second workstream: {order}")
        medical = next((item for item in assignments if item.get("page_job") == "MEDICAL_IMAGE_COMPARISON"), None)
        if not medical or medical.get("workstream_id") == assignments[0].get("workstream_id"):
            errors.append("storyline_trace.json: medical page was not assigned to an independent workstream")
        second = next((item for item in workstreams if item.get("workstream_order") == 2), {})
        if second.get("source_supported_cross_workstream_relation_to_previous") is not False:
            errors.append("storyline_trace.json: independent cross-workstream relation not explicit")
        if "independent" not in str(second.get("relation_to_previous", "")).lower():
            errors.append("storyline_trace.json: transition does not state independent workstream relation")
    for item in assignments:
        if not item.get("assignment_basis"):
            errors.append(f"storyline_trace.json: {item.get('page_id')} has no workstream assignment basis")

    if deck_sequence.get("schema") != "RESEARCH_PRESENTATION_DECK_SEQUENCE_SUMMARY_V1":
        errors.append("deck_sequence_summary.json: invalid schema")
    if deck_sequence.get("page_count") != len(trace.get("slides", [])):
        errors.append("deck_sequence_summary.json: page_count mismatch")
    if len(deck_sequence.get("page_order", [])) != len(trace.get("slides", [])):
        errors.append("deck_sequence_summary.json: page order does not cover all content pages")
    if len(deck_sequence.get("pages", [])) != len(trace.get("slides", [])):
        errors.append("deck_sequence_summary.json: page summaries do not cover all content pages")
    if len(deck_sequence.get("title_sequence", [])) != len(trace.get("slides", [])):
        errors.append("deck_sequence_summary.json: missing title sequence")
    if len(deck_sequence.get("workstream_sequence", [])) != len(trace.get("slides", [])):
        errors.append("deck_sequence_summary.json: missing workstream sequence")
    if len(deck_sequence.get("storyline_order", [])) != len(trace.get("slides", [])):
        errors.append("deck_sequence_summary.json: missing storyline order")
    if not re.fullmatch(r"[0-9a-f]{64}", str(deck_sequence.get("deck_identity_sha256", ""))):
        errors.append("deck_sequence_summary.json: missing deck identity sha")
    if not re.fullmatch(r"[0-9a-f]{64}", str(deck_sequence.get("render_input_identity_sha256", ""))):
        errors.append("deck_sequence_summary.json: missing render-input identity sha")
    render_input_manifest = deck_sequence.get("render_input_manifest", {})
    if render_input_manifest.get("schema") != "RESEARCH_PRESENTATION_RENDER_INPUT_IDENTITY_V1":
        errors.append("deck_sequence_summary.json: invalid render-input identity manifest")
    if render_input_manifest.get("sha256") != deck_sequence.get("render_input_identity_sha256"):
        errors.append("deck_sequence_summary.json: render-input manifest sha mismatch")
    render_input_files = render_input_manifest.get("files", [])
    render_input_roles = {item.get("role") for item in render_input_files}
    if not {"main_tex", "scientific_layout_include"}.issubset(render_input_roles):
        errors.append("deck_sequence_summary.json: render-input identity does not bind generated TeX inputs")
    if "copied_scientific_asset" not in render_input_roles:
        errors.append("deck_sequence_summary.json: render-input identity does not bind copied scientific assets")
    for item in render_input_files:
        if not item.get("path") or not re.fullmatch(r"[0-9a-f]{64}", str(item.get("sha256", ""))):
            errors.append("deck_sequence_summary.json: render-input file entry missing path or sha")
            break
    pixel_status = deck_sequence.get("pixel_evidence_status", {})
    if pixel_status.get("status") not in {"AVAILABLE", "UNAVAILABLE_RENDER_NOT_OK"}:
        errors.append("deck_sequence_summary.json: invalid pixel evidence status")
    contact = deck_sequence.get("deck_contact_sheet", {})
    if render_status.get("status") == "ok":
        if contact.get("serves_audience") is not False:
            errors.append("deck_sequence_summary.json: contact sheet must be review-only")
        contact_path = resolve(str(contact.get("path", "")))
        if not contact_path.exists() or contact_path.suffix.lower() != ".png":
            errors.append("deck_sequence_summary.json: deck_contact_sheet PNG missing")
        if not re.fullmatch(r"[0-9a-f]{64}", str(contact.get("sha256", ""))):
            errors.append("deck_sequence_summary.json: deck_contact_sheet sha missing")
        if not re.fullmatch(r"[0-9a-f]{64}", str(deck_sequence.get("rendered_pixel_identity_sha256", ""))):
            errors.append("deck_sequence_summary.json: missing rendered-pixel identity sha")
        for page in deck_sequence.get("pages", []):
            if not re.fullmatch(r"[0-9a-f]{64}", str(page.get("rendered_page_sha256", ""))):
                errors.append(f"deck_sequence_summary.json: {page.get('logical_id')} missing rendered sha")
            if page.get("rendered_pixel_status") != "AVAILABLE":
                errors.append(f"deck_sequence_summary.json: {page.get('logical_id')} rendered pixel status not available")
            density = page.get("visual_density", {})
            if density.get("machine_density") not in {"low", "moderate", "high"}:
                errors.append(f"deck_sequence_summary.json: {page.get('logical_id')} missing machine density")
            if not page.get("primary_scientific_object_type"):
                errors.append(f"deck_sequence_summary.json: {page.get('logical_id')} missing primary object type")
    else:
        if deck_sequence.get("rendered_pixel_identity_sha256") is not None:
            errors.append("deck_sequence_summary.json: rendered-pixel identity must be null when render is unavailable")
        if contact.get("path") is not None or contact.get("sha256") is not None:
            errors.append("deck_sequence_summary.json: contact sheet pixel fields must be null when render is unavailable")
        for page in deck_sequence.get("pages", []):
            if page.get("rendered_page_sha256") is not None or page.get("rendered_page_path") is not None:
                errors.append(f"deck_sequence_summary.json: {page.get('logical_id')} pixel fields must be null when render is unavailable")
            if page.get("rendered_pixel_status") != "UNAVAILABLE_RENDER_NOT_OK":
                errors.append(f"deck_sequence_summary.json: {page.get('logical_id')} missing unavailable pixel status")

    if quality_loop.get("schema") != "RESEARCH_PRESENTATION_DECK_QUALITY_LOOP_STATE_V1":
        errors.append("quality_loop_state.json: invalid schema")
    if quality_loop.get("max_repair_cycles") != 1:
        errors.append("quality_loop_state.json: repair cycle cap is not 1")
    if quality_loop.get("repair_cycle_count", 0) > 1:
        errors.append("quality_loop_state.json: repair cycle count exceeds cap")
    if quality_loop.get("render_identity_kind") != "render_input_identity_sha256":
        errors.append("quality_loop_state.json: render identity kind is not explicit")
    if not re.fullmatch(r"[0-9a-f]{64}", str(quality_loop.get("initial_render_input_identity", ""))):
        errors.append("quality_loop_state.json: missing initial render-input identity")
    if quality_loop.get("initial_render_identity") != quality_loop.get("initial_render_input_identity"):
        errors.append("quality_loop_state.json: legacy initial render identity does not match render-input identity")
    if quality_loop.get("initial_render_input_manifest", {}).get("sha256") != quality_loop.get("initial_render_input_identity"):
        errors.append("quality_loop_state.json: initial render-input manifest mismatch")
    if quality_loop.get("repair_cycle_count", 0) > 0:
        if not re.fullmatch(r"[0-9a-f]{64}", str(quality_loop.get("repaired_render_input_identity", ""))):
            errors.append("quality_loop_state.json: missing repaired render-input identity")
        if quality_loop.get("repaired_render_identity") != quality_loop.get("repaired_render_input_identity"):
            errors.append("quality_loop_state.json: legacy repaired render identity does not match render-input identity")
        if quality_loop.get("repaired_render_input_manifest", {}).get("sha256") != quality_loop.get("repaired_render_input_identity"):
            errors.append("quality_loop_state.json: repaired render-input manifest mismatch")
    decision = quality_loop.get("final_decision") or quality_loop.get("deck_level_decision")
    if decision not in {
        "WAITING_FOR_DECK_VISUAL_REVIEW",
        "WAITING_FOR_REPAIRED_DECK_REVIEW",
        "READY_TO_DELIVER",
        "QUALITY_LOOP_FAIL_NO_WINNER",
        "UNSAFE_REPAIR_MAPPING",
        "REPAIR_SELECTED",
        "PASS",
    }:
        errors.append("quality_loop_state.json: invalid deck-level decision")
    for directive in quality_loop.get("selected_repair_directives", []):
        if directive.get("intent") not in {
            "REORDER_WITHIN_SOURCE_DEPENDENCY",
            "ADJUST_TRANSITION_CUE",
            "SPLIT_OVERDENSE_PAGE",
            "REMOVE_OR_MERGE_REDUNDANT_PAGE",
            "SWAP_COMPATIBLE_GOLD_LAYOUT",
            "RESCALE_PRIMARY_OBJECT",
            "REPAIR_ANNOTATION_LEGEND",
        }:
            errors.append(f"quality_loop_state.json: unsupported repair intent {directive.get('intent')}")
        constraints = directive.get("source_fidelity_constraints", {})
        if constraints.get("may_rewrite_scientific_claims") is not False:
            errors.append("quality_loop_state.json: repair directive may rewrite scientific claims")
        if constraints.get("may_invent_source_relationships") is not False:
            errors.append("quality_loop_state.json: repair directive may invent source relationships")
        if constraints.get("may_force_gold_id") is not False or constraints.get("may_override_scores") is not False:
            errors.append("quality_loop_state.json: repair directive allows selector bypass")

    if layouts.get("schema") != "RESEARCH_PRESENTATION_PRODUCTION_RESOLVED_LAYOUTS_V1":
        errors.append("resolved_layouts.json: invalid schema")
    for layout in layouts.get("layouts", []):
        if layout.get("content_capacity_check", {}).get("status") not in {"FIT", "SPLIT_REQUIRED", "NO_COMPATIBLE_LAYOUT"}:
            errors.append(f"resolved_layouts.json: invalid capacity status for {layout.get('page_id')}")

    if dependency.get("schema") != "RESEARCH_CUHK_STAGE3_BUILD_DEPENDENCY_PROBE_V1":
        errors.append("dependency_probe.json: invalid schema")
    if render_probe.get("schema") != "RENDER_CHINESE_MATH_PDF_PROBE_CAPTURE_V1":
        errors.append("render_chinese_math_pdf_probe.json: invalid schema")
    if render_probe.get("status") != "ok":
        errors.append("render_chinese_math_pdf_probe.json: render probe failed")

    tex_path = resolve(manifest.get("tex", ""))
    if not tex_path.exists():
        errors.append("BUILD_MANIFEST.json: generated tex missing")
    else:
        tex = tex_path.read_text(encoding="utf-8")
        for required_text in [r"\usetheme{sintef}", r"\titlebackground*{assets/background}", r"\input{scientific_layouts.tex}", "Coverage by ICC under imbalanced clusters", "Same-case ROI zoom"]:
            if required_text not in tex:
                errors.append(f"{tex_path}: missing {required_text}")
        for forbidden in FORBIDDEN_AUDIENCE_TERMS:
            if forbidden in tex:
                errors.append(f"{tex_path}: audience-facing TeX leaks {forbidden}")
        for source_like in [r"(?<![\\A-Za-z])beta_", r"(?<![\\A-Za-z])epsilon_", r"X'X"]:
            if re.search(source_like, tex):
                errors.append(f"{tex_path}: source-like math leak {source_like}")

    if render_status.get("status") == "ok":
        if render_status.get("png_count", 0) < len(trace.get("slides", [])) + 1:
            errors.append("BUILD_MANIFEST.json: expected title plus content rendered pages")
        if manifest.get("mechanical_qa", {}).get("status") != "MECHANICAL_PASS":
            errors.append("BUILD_MANIFEST.json: render ok but mechanical QA not PASS")
    elif not allow_missing_render:
        errors.append(f"BUILD_MANIFEST.json: real render not ok: {render_status.get('status')}")

    if visual_inputs.get("schema") != "AI_BRIDGE_VISUAL_INPUT_MANIFEST_V1":
        errors.append("visual_inputs.json: invalid schema")
    if visual_inputs.get("task_key") != task_key:
        errors.append("visual_inputs.json: task_key mismatch")
    rubric = visual_inputs.get("rubric", {}).get("instructions", "")
    for required_text in ["source-specific content", "exact CUHK", "internal RRL/GSC/SRC", "coherent research update", "deck_contact_sheet", "top-level package PASS is not enough"]:
        if required_text not in rubric:
            errors.append(f"visual_inputs.json: rubric missing {required_text}")
    if render_status.get("status") == "ok" and len(visual_inputs.get("inputs", [])) != len(trace.get("slides", [])) + 1:
        errors.append("visual_inputs.json: rendered page inputs do not match content pages")
    if render_status.get("status") == "ok" and not any(item.get("logical_id") == "deck_contact_sheet" for item in visual_inputs.get("inputs", [])):
        errors.append("visual_inputs.json: deck contact sheet input missing")
    bindings = visual_inputs.get("identity_bindings", {})
    for key in ["deck_sequence_summary", "deck_sequence_summary_sha256", "quality_loop_state", "quality_loop_state_sha256", "deck_identity_sha256", "render_input_identity_sha256"]:
        if not bindings.get(key):
            errors.append(f"visual_inputs.json: identity binding missing {key}")
    if bindings.get("render_input_identity_sha256") != deck_sequence.get("render_input_identity_sha256"):
        errors.append("visual_inputs.json: render-input identity binding does not match deck sequence")
    if render_status.get("status") == "ok":
        for key in ["deck_contact_sheet", "deck_contact_sheet_sha256"]:
            if not bindings.get(key):
                errors.append(f"visual_inputs.json: identity binding missing {key}")
        if bindings.get("rendered_pixel_identity_sha256") != deck_sequence.get("rendered_pixel_identity_sha256"):
            errors.append("visual_inputs.json: rendered-pixel identity binding does not match deck sequence")
        contact_sheet = manifest.get("deck_contact_sheet", {})
        if bindings.get("deck_contact_sheet") != contact_sheet.get("path"):
            errors.append("visual_inputs.json: deck_contact_sheet binding does not match BUILD_MANIFEST.json")
        if bindings.get("deck_contact_sheet_sha256") != contact_sheet.get("sha256"):
            errors.append("visual_inputs.json: deck_contact_sheet_sha256 binding does not match BUILD_MANIFEST.json")
        contact_input = next((item for item in visual_inputs.get("inputs", []) if item.get("logical_id") == "deck_contact_sheet"), {})
        if contact_input.get("path") != contact_sheet.get("path") or contact_input.get("sha256") != contact_sheet.get("sha256"):
            errors.append("visual_inputs.json: deck_contact_sheet input does not match BUILD_MANIFEST.json")
    elif bindings.get("rendered_pixel_identity_sha256") is not None:
        errors.append("visual_inputs.json: rendered-pixel identity binding must be null when render is unavailable")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out-dir", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--task-key", default=DEFAULT_TASK_KEY)
    parser.add_argument("--allow-missing-render", action="store_true")
    args = parser.parse_args()
    errors = validate(args.out_dir, task_key=args.task_key, allow_missing_render=args.allow_missing_render)
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    mode = "non-render contract" if args.allow_missing_render else "strict rendered contract"
    print(f"validated research presentation one-call production entry {mode}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
