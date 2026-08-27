#!/usr/bin/env python3
"""Validate Stage 3 CUHK scientific-layout integration artifacts."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[6]
DEFAULT_TASK_KEY = "027_research_presentation_executable_cuhk_scientific_layout_system"
TASK_KEY = DEFAULT_TASK_KEY
DEFAULT_OUT = REPO_ROOT / "docs" / "audits" / "research_presentation_cuhk_scientific_layout_stage3" / "generated"
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
    "review target",
    "fixture",
    "workflow",
]


def resolve(path: str) -> Path:
    if Path(path).is_absolute():
        return Path(path)
    return REPO_ROOT / path


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def validate(out_dir: Path, *, allow_missing_render: bool = False, task_key: str = DEFAULT_TASK_KEY) -> list[str]:
    errors: list[str] = []
    manifest_path = out_dir / "BUILD_MANIFEST.json"
    layouts_path = out_dir / "resolved_layouts.json"
    trace_path = out_dir / "runtime_trace.json"
    mutation_path = out_dir / "mutation_regression.json"
    capacity_path = out_dir / "capacity_failure_contract.json"
    dependency_path = out_dir / "dependency_probe.json"
    render_probe_path = out_dir / "render_chinese_math_pdf_probe.json"
    for path in [manifest_path, layouts_path, trace_path, mutation_path, capacity_path, dependency_path, render_probe_path]:
        if not path.exists():
            errors.append(f"{path}: missing")
            return errors

    manifest = load_json(manifest_path)
    layouts_payload = load_json(layouts_path)
    trace = load_json(trace_path)
    mutation = load_json(mutation_path)
    capacity_failure = load_json(capacity_path)
    dependency_probe = load_json(dependency_path)
    render_probe = load_json(render_probe_path)
    if manifest.get("schema") != "RESEARCH_CUHK_STAGE3_BUILD_MANIFEST_V1":
        errors.append(f"{manifest_path}: invalid schema")
    if manifest.get("task_key") != task_key:
        errors.append(f"{manifest_path}: task_key mismatch")
    if "templates/cuhk/beamer/source" not in manifest.get("canonical_cuhk_source", ""):
        errors.append(f"{manifest_path}: canonical CUHK source not recorded")
    required_canonical = [
        "main.tex",
        "styles/beamerthemesintef.sty",
        "styles/sintefcolor.sty",
        "assets/background.png",
        "assets/logo_RGB.png",
    ]
    canonical_files = manifest.get("canonical_files", {})
    for suffix in required_canonical:
        if not any(path.endswith(suffix) for path in canonical_files):
            errors.append(f"{manifest_path}: missing canonical file identity {suffix}")

    tex_path = resolve(manifest.get("tex", ""))
    include_path = resolve(manifest.get("scientific_layout_include", ""))
    if not tex_path.exists():
        errors.append(f"{manifest_path}: generated tex missing")
    if not include_path.exists():
        errors.append(f"{manifest_path}: scientific layout include missing")
    if tex_path.exists():
        tex = tex_path.read_text(encoding="utf-8")
        for required in [
            r"\usetheme{sintef}",
            r"\titlebackground*{assets/background}",
            r"\input{scientific_layouts.tex}",
            r"\begin{tikzpicture}",
            r"\includegraphics",
            r"\displaystyle",
        ]:
            if required not in tex:
                errors.append(f"{tex_path}: missing required TeX primitive {required}")
        for forbidden in FORBIDDEN_AUDIENCE_TERMS:
            if forbidden in tex:
                errors.append(f"{tex_path}: audience-facing TeX leaks {forbidden}")
        for source_like in [r"(?<![\\A-Za-z])beta_", r"(?<![\\A-Za-z])sum_", r"X'X", r"\^\(-1\)", r"(?<![\\A-Za-z])epsilon_"]:
            if re.search(source_like, tex):
                errors.append(f"{tex_path}: source-like math leak {source_like}")
        if "coverage_by_icc.png" in tex:
            errors.append(f"{tex_path}: quantitative result still uses raster coverage plot")
        if "centers -> subjects" in tex or "Error zoom:" in tex:
            errors.append(f"{tex_path}: old visual-maturity blocker text still present")
        if "Native axes, facets, method key, nominal line, and interval callout" in tex:
            errors.append(f"{tex_path}: quantitative result leaks implementation/QA wording")
        if "small_g_negative_result.png" in tex and r"\scriptsize coverage" not in tex:
            errors.append(f"{tex_path}: negative result plot lacks readable coverage y-axis label")
        connector_pattern = re.compile(r"\\StageThreeConnector\{([0-9.]+)\}\{([0-9.]+)\}\{([0-9.]+)\}\{([0-9.]+)\};")
        leftward_midline_connectors = [
            (float(x1), float(y1), float(x2), float(y2))
            for x1, y1, x2, y2 in connector_pattern.findall(tex)
            if abs(float(y1) - float(y2)) < 0.0001 and float(x2) <= float(x1)
        ]
        if leftward_midline_connectors:
            errors.append(f"{tex_path}: found non-left-to-right Stage 3 connector {leftward_midline_connectors[0]}")
        for required in [
            "Coverage by ICC under imbalanced clusters",
            "Subject records nested inside each center",
            "Same-case ROI zoom",
            "Failure evidence",
            "Decision rule",
        ]:
            if required not in tex:
                errors.append(f"{tex_path}: missing Stage 3 recovery primitive text {required}")

    if layouts_payload.get("schema") != "RESEARCH_CUHK_STAGE3_RESOLVED_LAYOUTS_V1":
        errors.append(f"{layouts_path}: invalid schema")
    layouts = layouts_payload.get("layouts", [])
    if len(layouts) != 6:
        errors.append(f"{layouts_path}: expected 6 content layouts")
    required_jobs = {
        "STATISTICAL_MODEL",
        "REAL_DATA_APPLICATION",
        "EXPERIMENT_DESIGN",
        "NEGATIVE_RESULT",
        "MEDICAL_IMAGE_COMPARISON",
        "NEXT_EXPERIMENT",
    }
    jobs = {layout.get("page_job") for layout in layouts}
    if jobs != required_jobs:
        errors.append(f"{layouts_path}: page-job coverage mismatch {sorted(jobs)}")
    selected = {layout.get("selected_gold_id") for layout in layouts}
    if "GSC-018" not in selected:
        errors.append(f"{layouts_path}: discussion/next-experiment gold GSC-018 not consumed")
    for layout in layouts:
        if layout.get("schema") != "RESEARCH_CUHK_SCIENTIFIC_RESOLVED_LAYOUT_V1":
            errors.append(f"{layouts_path}: invalid resolved layout schema")
        if not layout.get("recipe_sha256") or len(layout.get("recipe_sha256", "")) != 64:
            errors.append(f"{layouts_path}: missing recipe sha for {layout.get('page_id')}")
        consumed = set(layout.get("source_recipe_fields_consumed", []))
        for required in [
            "primary_bbox",
            "primary_object_area_ratio",
            "visual_hierarchy",
            "alignment_groups",
            "reading_flow",
            "annotation_legend_caption_panel_relations",
            "content_capacity",
        ]:
            if required not in consumed:
                errors.append(f"{layouts_path}: {layout.get('page_id')} did not consume {required}")
        bbox = layout.get("resolved_primary_object_geometry", {})
        safe = layout.get("exact_cuhk_content_safe_region", {})
        if bbox and safe:
            if bbox["x"] < safe["x"] or bbox["y"] < safe["y"]:
                errors.append(f"{layouts_path}: {layout.get('page_id')} primary bbox starts outside safe region")
            if bbox["x"] + bbox["w"] > safe["x"] + safe["w"] + 0.0001:
                errors.append(f"{layouts_path}: {layout.get('page_id')} primary bbox exceeds safe width")
            if bbox["y"] + bbox["h"] > safe["y"] + safe["h"] + 0.0001:
                errors.append(f"{layouts_path}: {layout.get('page_id')} primary bbox exceeds safe height")
        for role, support in layout.get("resolved_supporting_object_geometry", {}).items():
            if support and safe:
                if support["x"] < safe["x"] - 0.0001 or support["y"] < safe["y"] - 0.0001:
                    errors.append(f"{layouts_path}: {layout.get('page_id')} {role} bbox starts outside safe region")
                if support["x"] + support["w"] > safe["x"] + safe["w"] + 0.0001:
                    errors.append(f"{layouts_path}: {layout.get('page_id')} {role} bbox exceeds safe width")
                if support["y"] + support["h"] > safe["y"] + safe["h"] + 0.0001:
                    errors.append(f"{layouts_path}: {layout.get('page_id')} {role} bbox exceeds safe height")
        if layout.get("content_capacity_check", {}).get("status") not in {"FIT", "SPLIT_REQUIRED", "NO_COMPATIBLE_LAYOUT"}:
            errors.append(f"{layouts_path}: invalid capacity status for {layout.get('page_id')}")
        packing = layout.get("text_region_packing", {})
        if packing.get("non_overlapping") is not True:
            errors.append(f"{layouts_path}: emitted text regions overlap for {layout.get('page_id')}")
        page_job = layout.get("page_job")
        family = layout.get("executable_layout_family")
        contract = layout.get("job_specific_runtime_contract", {})
        if page_job == "REAL_DATA_APPLICATION" and bbox.get("w", 0) * bbox.get("h", 0) < 0.34:
            errors.append(f"{layouts_path}: quantitative result figure below projection-scale area")
        if page_job == "REAL_DATA_APPLICATION":
            if family != "presentation_native_quantitative_result":
                errors.append(f"{layouts_path}: quantitative result did not use presentation-native layout family")
            if contract.get("primitive") != "csv_driven_tikz_result_figure":
                errors.append(f"{layouts_path}: quantitative result did not record csv-driven native figure primitive")
            native_types = {item.get("native_type") for item in layout.get("native_objects", [])}
            if "presentation_native_result_figure" not in native_types:
                errors.append(f"{layouts_path}: quantitative result still lacks native result figure object")
        if page_job == "MEDICAL_IMAGE_COMPARISON" and (bbox.get("w", 0) < 0.84 or bbox.get("h", 0) < 0.48):
            errors.append(f"{layouts_path}: medical panel band below readable-area floor")
        if page_job == "MEDICAL_IMAGE_COMPARISON":
            zoom = contract.get("same_case_roi_zoom")
            if family != "same_case_medical_roi_zoom" or contract.get("primitive") != "same_case_roi_crop_zoom":
                errors.append(f"{layouts_path}: medical comparison did not use same-case ROI zoom family")
            if not isinstance(zoom, dict) or not zoom.get("crop_records"):
                errors.append(f"{layouts_path}: medical comparison missing same-case crop ROI records")
            else:
                build_workspace = manifest.get("build_workspace", "")
                for record in zoom["crop_records"]:
                    zoom_asset = record.get("zoom_asset")
                    if not zoom_asset or not resolve(str(Path(build_workspace) / zoom_asset)).exists():
                        errors.append(f"{layouts_path}: medical ROI zoom asset missing {zoom_asset}")
                    if record.get("same_case_coordinate_space") is not True:
                        errors.append(f"{layouts_path}: medical ROI crop not marked same-case coordinate space")
        if page_job in {"EXPERIMENT_DESIGN", "NEXT_EXPERIMENT"} and bbox.get("w", 0) * bbox.get("h", 0) < 0.36:
            errors.append(f"{layouts_path}: scientific diagram region below specificity floor for {layout.get('page_id')}")
        if page_job == "EXPERIMENT_DESIGN":
            if family != "typed_experiment_design_hierarchy":
                errors.append(f"{layouts_path}: experiment design did not use typed hierarchy family")
            if contract.get("primitive") != "typed_scientific_hierarchy_relation_map":
                errors.append(f"{layouts_path}: experiment design did not record typed relation primitive")
        if page_job == "NEXT_EXPERIMENT":
            if family != "evidence_to_decision_next_experiment":
                errors.append(f"{layouts_path}: next experiment did not use evidence-to-decision family")
            if contract.get("primitive") != "evidence_manipulation_comparator_decision_map":
                errors.append(f"{layouts_path}: next experiment did not record evidence-to-decision primitive")
        if layout.get("audience_safe_output_contract", {}).get("internal_ids_exposed") is not False:
            errors.append(f"{layouts_path}: audience-safe contract violated for {layout.get('page_id')}")

    if trace.get("schema") != "RESEARCH_CUHK_STAGE3_TRACE_V1":
        errors.append(f"{trace_path}: invalid schema")
    if len(trace.get("slides", [])) != 6:
        errors.append(f"{trace_path}: expected 6 trace slides")
    for item in trace.get("slides", []):
        if not item.get("selected_gold_id"):
            errors.append(f"{trace_path}: trace item missing selected gold")
        if not item.get("emitted_tex_object_ids"):
            errors.append(f"{trace_path}: trace item missing emitted object ids")

    if mutation.get("schema") != "RESEARCH_CUHK_STAGE3_MUTATION_REGRESSION_V1":
        errors.append(f"{mutation_path}: invalid schema")
    if mutation.get("status") != "PASS":
        errors.append(f"{mutation_path}: mutation regression did not pass")
    checks = mutation.get("checks", {})
    for key in ["source_geometry_changed", "resolved_geometry_changed", "emitted_geometry_changes_with_recipe", "page_job_unchanged"]:
        if checks.get(key) is not True:
            errors.append(f"{mutation_path}: mutation check failed: {key}")
    if mutation.get("baseline_geometry_signature") == mutation.get("mutated_geometry_signature"):
        errors.append(f"{mutation_path}: geometry signature did not change")

    if capacity_failure.get("schema") != "RESEARCH_CUHK_STAGE3_CAPACITY_FAILURE_CONTRACT_V1":
        errors.append(f"{capacity_path}: invalid schema")
    if capacity_failure.get("status") != "SPLIT_REQUIRED":
        errors.append(f"{capacity_path}: capacity mismatch did not return SPLIT_REQUIRED")
    if capacity_failure.get("generic_layout_fallback_used") is not False:
        errors.append(f"{capacity_path}: generic layout fallback was used")

    if dependency_probe.get("schema") != "RESEARCH_CUHK_STAGE3_BUILD_DEPENDENCY_PROBE_V1":
        errors.append(f"{dependency_path}: invalid schema")
    commands = dependency_probe.get("commands", {})
    for command in ["xelatex", "lualatex", "pdflatex", "tectonic", "pdftoppm"]:
        if command not in commands:
            errors.append(f"{dependency_path}: missing command probe {command}")
    if dependency_probe.get("tex_engine_available") is not True and manifest.get("compile_status", {}).get("status") == "COMPILED":
        errors.append(f"{dependency_path}: compile succeeded without a recorded TeX engine")
    if dependency_probe.get("tex_engine_available") is not True and manifest.get("compile_status", {}).get("status") != "BLOCKED_MISSING_TEX_ENGINE":
        errors.append(f"{dependency_path}: missing TeX engine did not map to BLOCKED_MISSING_TEX_ENGINE")
    if render_probe.get("schema") != "RENDER_CHINESE_MATH_PDF_PROBE_CAPTURE_V1":
        errors.append(f"{render_probe_path}: invalid schema")
    if render_probe.get("status") != "ok":
        errors.append(f"{render_probe_path}: render-chinese-math-pdf probe failed")
    expected_render_probe = str(render_probe_path.resolve())
    try:
        expected_render_probe = str(render_probe_path.resolve().relative_to(REPO_ROOT))
    except ValueError:
        pass
    if manifest.get("render_chinese_math_pdf_probe") != expected_render_probe:
        errors.append(f"{manifest_path}: render_chinese_math_pdf_probe path not recorded")

    render_status = manifest.get("render_status", {})
    mechanical = manifest.get("mechanical_qa", {})
    if render_status.get("status") == "ok":
        if render_status.get("png_count", 0) < 7:
            errors.append(f"{manifest_path}: expected title plus 6 rendered pages")
        for item in render_status.get("rendered_png", []):
            path = resolve(item.get("path", ""))
            if not path.exists() or path.stat().st_size < 10_000:
                errors.append(f"{manifest_path}: rendered PNG missing or too small {path}")
        if mechanical.get("status") != "MECHANICAL_PASS":
            errors.append(f"{manifest_path}: mechanical QA did not pass")
    elif allow_missing_render and render_status.get("status") == "BLOCKED_MISSING_TEX_ENGINE":
        if mechanical.get("status") == "MECHANICAL_PASS":
            errors.append(f"{manifest_path}: missing render cannot be mechanical pass")
    else:
        errors.append(f"{manifest_path}: real render not ok: {render_status.get('status')}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out-dir", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--allow-missing-render", action="store_true")
    parser.add_argument("--task-key", default=DEFAULT_TASK_KEY)
    args = parser.parse_args()
    errors = validate(args.out_dir, allow_missing_render=args.allow_missing_render, task_key=args.task_key)
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    mode = "non-render contract" if args.allow_missing_render else "strict rendered contract"
    print(f"validated Stage 3 CUHK scientific-layout {mode}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
