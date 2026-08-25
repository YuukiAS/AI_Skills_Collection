#!/usr/bin/env python3
"""Generate Stage 3 CUHK scientific-layout integration artifacts."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any

import build_gold_composition_recipe


SHARED = Path(__file__).resolve().parents[1]
REPO_ROOT = Path(__file__).resolve().parents[6]
TASK_KEY = "027_research_presentation_executable_cuhk_scientific_layout_system"
CANONICAL_CUHK = SHARED / "templates" / "cuhk" / "beamer" / "source"
DEFAULT_OUT = REPO_ROOT / "docs" / "audits" / "research_presentation_cuhk_scientific_layout_stage3" / "generated"
RESULT_VISUAL_REVIEW_DIR = REPO_ROOT / "results" / TASK_KEY / "visual_review"

SLIDE_W = 16.0
SLIDE_H = 9.0
SAFE_REGION = {"x": 0.060, "y": 0.185, "w": 0.880, "h": 0.675}
LOCAL_RENDER_RESOURCE_DIR = Path("/home/yuukias/render_resources/chinese_math_pdf")
LOCAL_RENDER_TEXMF = LOCAL_RENDER_RESOURCE_DIR / "texmf"
LOCAL_FANDOL_DIR = LOCAL_RENDER_TEXMF / "fonts" / "opentype" / "public" / "fandol"
LOCAL_NOTO_CJK_DIR = LOCAL_RENDER_TEXMF / "fonts" / "opentype" / "public" / "noto-cjk"
TRACE_TIMES_FONT_DIR = Path("/home/yuukias/code/TRACE/presentations/group_meetings/2026-07-16/cat_trace_demo/fonts")
LOCAL_TINYTEX_BIN = Path("/home/yuukias/.TinyTeX/bin/x86_64-linux")
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


def stable_sha(payload: Any) -> str:
    text = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def file_sha(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def rel(path: Path) -> str:
    resolved = path.resolve()
    try:
        return str(resolved.relative_to(REPO_ROOT))
    except ValueError:
        return str(resolved)


def tex_escape(text: str) -> str:
    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    return "".join(replacements.get(ch, ch) for ch in text)


def clamp(value: float, lower: float, upper: float) -> float:
    return max(lower, min(upper, value))


def fit_bbox(source_bbox: dict[str, float], capacity: dict[str, Any]) -> tuple[dict[str, float], list[str]]:
    """Map a source-normalized bbox into the CUHK safe content region."""

    transforms = ["source primary_bbox mapped into canonical CUHK content safe region"]
    safe = SAFE_REGION
    bbox = {
        "x": safe["x"] + float(source_bbox["x"]) * safe["w"],
        "y": safe["y"] + float(source_bbox["y"]) * safe["h"],
        "w": float(source_bbox["w"]) * safe["w"],
        "h": float(source_bbox["h"]) * safe["h"],
    }
    min_area = float(capacity.get("primary_object_min_area") or 0.12) * safe["w"] * safe["h"]
    current_area = bbox["w"] * bbox["h"]
    if current_area < min_area:
        scale = (min_area / max(current_area, 0.001)) ** 0.5
        bbox["w"] *= min(scale, 1.55)
        bbox["h"] *= min(scale, 1.55)
        transforms.append("primary object enlarged to satisfy recipe content_capacity minimum area")
    bbox["w"] = clamp(bbox["w"], 0.24, safe["w"])
    bbox["h"] = clamp(bbox["h"], 0.16, safe["h"])
    bbox["x"] = clamp(bbox["x"], safe["x"], safe["x"] + safe["w"] - bbox["w"])
    bbox["y"] = clamp(bbox["y"], safe["y"], safe["y"] + safe["h"] - bbox["h"])
    return ({key: round(value, 4) for key, value in bbox.items()}, transforms)


def expand_bbox_for_content(primary: dict[str, float], content_kind: str, transforms: list[str]) -> dict[str, float]:
    floors = {
        "equation": (0.62, 0.20),
        "figure": (0.78, 0.42),
        "image_panel": (0.86, 0.50),
        "flow": (0.80, 0.42),
        "next_experiment": (0.80, 0.42),
    }
    min_w, min_h = floors.get(content_kind, (primary["w"], primary["h"]))
    safe = SAFE_REGION
    if primary["w"] >= min_w and primary["h"] >= min_h:
        return primary
    center_x = primary["x"] + primary["w"] / 2
    center_y = primary["y"] + primary["h"] / 2
    width = min(max(primary["w"], min_w), safe["w"])
    height = min(max(primary["h"], min_h), safe["h"])
    expanded = {
        "x": clamp(center_x - width / 2, safe["x"], safe["x"] + safe["w"] - width),
        "y": clamp(center_y - height / 2, safe["y"], safe["y"] + safe["h"] - height),
        "w": width,
        "h": height,
    }
    transforms.append(f"{content_kind} primary object expanded to projection-readable floor")
    return {key: round(value, 4) for key, value in expanded.items()}


def job_primary_geometry(spec: dict[str, Any], primary: dict[str, float], transforms: list[str]) -> dict[str, float]:
    safe = SAFE_REGION
    page_job = spec["page_job"]
    if page_job == "REAL_DATA_APPLICATION":
        target = {"w": 0.84, "h": 0.47, "y": 0.230}
        transforms.append("quantitative-result plot receives dominant projection-scale figure region")
    elif page_job == "NEGATIVE_RESULT":
        target = {"w": 0.66, "h": 0.46, "x": safe["x"], "y": 0.285}
        transforms.append("negative-result evidence keeps a right diagnostic column without text overlap")
    elif page_job == "MEDICAL_IMAGE_COMPARISON":
        target = {"w": safe["w"], "h": 0.52, "x": safe["x"], "y": 0.270}
        transforms.append("four-panel medical comparison receives full-width projection-scale image band")
    elif page_job == "EXPERIMENT_DESIGN":
        target = {"w": 0.82, "h": 0.49, "x": 0.09, "y": 0.270}
        transforms.append("experiment design uses a scientific-factor diagram region")
    elif page_job == "NEXT_EXPERIMENT":
        target = {"w": 0.82, "h": 0.49, "x": 0.09, "y": 0.270}
        transforms.append("next-experiment reasoning uses a decision-and-comparator diagram region")
    else:
        return primary
    target.setdefault("x", primary["x"] + primary["w"] / 2 - target["w"] / 2)
    target.setdefault("y", primary["y"] + primary["h"] / 2 - target["h"] / 2)
    return {
        "x": round(clamp(target["x"], safe["x"], safe["x"] + safe["w"] - target["w"]), 4),
        "y": round(clamp(target["y"], safe["y"], safe["y"] + safe["h"] - target["h"]), 4),
        "w": round(min(target["w"], safe["w"]), 4),
        "h": round(min(target["h"], safe["h"]), 4),
    }


def support_bbox(primary: dict[str, float], role: str) -> dict[str, float]:
    safe = SAFE_REGION
    if role == "left":
        available = primary["x"] - safe["x"] - 0.025
        w = min(0.28, max(0.0, available))
        return {"x": safe["x"], "y": primary["y"], "w": w, "h": min(primary["h"], 0.42)}
    if role == "right":
        x = primary["x"] + primary["w"] + 0.025
        available = safe["x"] + safe["w"] - x
        w = min(0.28, max(0.0, available))
        return {"x": x, "y": primary["y"], "w": w, "h": min(primary["h"], 0.42)}
    if role == "below":
        y = primary["y"] + primary["h"] + 0.025
        if y + 0.08 > safe["y"] + safe["h"]:
            y = max(safe["y"], primary["y"] - 0.105)
        h = min(0.12, max(0.08, safe["y"] + safe["h"] - y))
        return {"x": primary["x"], "y": y, "w": primary["w"], "h": h}
    return {"x": safe["x"], "y": safe["y"], "w": safe["w"], "h": 0.09}


def support_geometry(spec: dict[str, Any], primary: dict[str, float]) -> dict[str, dict[str, float]]:
    safe = SAFE_REGION
    page_job = spec["page_job"]
    if page_job == "REAL_DATA_APPLICATION":
        return {
            "annotation": {"x": 0.08, "y": 0.735, "w": 0.52, "h": 0.055},
            "caption": {"x": 0.64, "y": 0.735, "w": 0.30, "h": 0.055},
        }
    if page_job == "NEGATIVE_RESULT":
        return {
            "annotation": {"x": 0.745, "y": 0.300, "w": 0.185, "h": 0.195},
            "caption": {"x": 0.745, "y": 0.535, "w": 0.185, "h": 0.170},
        }
    if page_job == "MEDICAL_IMAGE_COMPARISON":
        return {
            "annotation": {"x": safe["x"], "y": 0.810, "w": safe["w"], "h": 0.045},
            "caption": {"x": safe["x"], "y": 0.810, "w": safe["w"], "h": 0.045},
        }
    if page_job in {"EXPERIMENT_DESIGN", "NEXT_EXPERIMENT"}:
        return {
            "annotation": {"x": primary["x"], "y": 0.795, "w": primary["w"], "h": 0.060},
            "caption": {"x": primary["x"], "y": 0.795, "w": primary["w"], "h": 0.060},
        }
    annotation = annotation_bbox(primary)
    caption = {key: round(value, 4) for key, value in support_bbox(primary, "below").items()}
    return {"annotation": annotation, "caption": caption}


def bbox_overlap(a: dict[str, float], b: dict[str, float]) -> bool:
    return not (
        a["x"] + a["w"] <= b["x"] + 0.0001
        or b["x"] + b["w"] <= a["x"] + 0.0001
        or a["y"] + a["h"] <= b["y"] + 0.0001
        or b["y"] + b["h"] <= a["y"] + 0.0001
    )


def annotation_bbox(primary: dict[str, float]) -> dict[str, float]:
    right = support_bbox(primary, "right")
    if right["w"] >= 0.16:
        return {key: round(value, 4) for key, value in right.items()}
    left = support_bbox(primary, "left")
    if left["w"] >= 0.16:
        return {key: round(value, 4) for key, value in left.items()}
    below = support_bbox(primary, "below")
    return {key: round(value, 4) for key, value in below.items()}


def bbox_signature(bbox: dict[str, float]) -> str:
    return ",".join(f"{bbox[key]:.4f}" for key in ["x", "y", "w", "h"])


def capacity_status(spec: dict[str, Any], recipe: dict[str, Any]) -> dict[str, Any]:
    capacity = recipe["composition_constraints"]["content_capacity"]
    requested_panels = int(spec.get("required_panel_count") or 0)
    capacity_panels = int(capacity.get("panel_count") or 0)
    if requested_panels > capacity_panels + 2:
        return {
            "status": "SPLIT_REQUIRED",
            "reason": f"requested {requested_panels} panels exceeds selected layout capacity {capacity_panels}",
        }
    return {
        "status": "FIT",
        "reason": "requested content fits selected gold content_capacity",
    }


def tex_cache_env() -> dict[str, str]:
    user = os.environ.get("USER", "codex")
    return {
        "TEXMFVAR": f"/tmp/tex-cache-{user}/var",
        "TEXMFCONFIG": f"/tmp/tex-cache-{user}/config",
        "TEXMFCACHE": f"/tmp/tex-cache-{user}/cache",
    }


def render_search_path() -> str:
    path_parts = [os.environ.get("PATH", "")]
    if LOCAL_TINYTEX_BIN.exists():
        path_parts.insert(0, str(LOCAL_TINYTEX_BIN))
    return os.pathsep.join(part for part in path_parts if part)


def write_fontconfig(build_dir: Path) -> dict[str, Any]:
    fontconfig_dir = build_dir / "fontconfig"
    fontconfig_dir.mkdir(exist_ok=True)
    cache_dir = Path("/tmp/fontconfig-cache-027")
    cache_dir.mkdir(parents=True, exist_ok=True)
    config = fontconfig_dir / "fonts.conf"
    config.write_text(
        "\n".join(
            [
                '<?xml version="1.0"?>',
                '<!DOCTYPE fontconfig SYSTEM "urn:fontconfig:fonts.dtd">',
                "<fontconfig>",
                f"  <dir>{TRACE_TIMES_FONT_DIR}</dir>",
                "  <dir>/usr/share/fonts</dir>",
                f"  <cachedir>{cache_dir}</cachedir>",
                "</fontconfig>",
                "",
            ]
        ),
        encoding="utf-8",
    )
    return {
        "fontconfig_file": str(config),
        "fontconfig_file_repo_path": rel(config),
        "font_cache_dir": str(cache_dir),
        "times_font_dir": str(TRACE_TIMES_FONT_DIR),
        "times_font_dir_exists": TRACE_TIMES_FONT_DIR.exists(),
        "times_font_files_present": all((TRACE_TIMES_FONT_DIR / name).exists() for name in ["times.ttf", "timesbd.ttf", "timesbi.ttf", "timesi.ttf"]),
    }


def find_command(command: str) -> dict[str, Any]:
    path = shutil.which(command, path=render_search_path())
    return {
        "available": path is not None,
        "path": path,
        "source": "PATH" if path else None,
    }


def render_skill_probe() -> dict[str, Any]:
    probe = REPO_ROOT / "skills" / "tools" / "documents-media" / "render-chinese-math-pdf" / "scripts" / "probe_pdf_render_env.py"
    if not probe.exists():
        return {
            "schema": "RENDER_CHINESE_MATH_PDF_PROBE_CAPTURE_V1",
            "status": "MISSING_RENDER_SKILL_PROBE",
            "probe": rel(probe),
        }
    run = subprocess.run(
        [sys.executable, str(probe), "--root", str(REPO_ROOT), "--pretty"],
        check=False,
        capture_output=True,
        text=True,
    )
    try:
        payload = json.loads(run.stdout)
    except json.JSONDecodeError:
        payload = {"raw_stdout": run.stdout}
    return {
        "schema": "RENDER_CHINESE_MATH_PDF_PROBE_CAPTURE_V1",
        "status": "ok" if run.returncode == 0 else "PROBE_FAILED",
        "probe": rel(probe),
        "returncode": run.returncode,
        "stderr": run.stderr,
        "payload": payload,
    }


def page_specs() -> list[dict[str, Any]]:
    stat_assets = "tests/fixtures/presentations/statistical_method_group_meeting/visual_review_packet_source/assets"
    med_assets = "tests/fixtures/presentations/medical_imaging_group_meeting/visual_review_packet_source/assets"
    return [
        {
            "page_id": "equation_statistical_model",
            "page_job": "STATISTICAL_MODEL",
            "section": "Model",
            "title": "Clustered outcomes separate center and individual variation",
            "query": {
                "page_function": "STATISTICAL_MODEL",
                "scientific_object": "medical imaging objective equation mathematical model variance components",
                "domain_family": "medical_imaging",
                "dominant_object_type": "equation",
                "evidence_type": "mathematical model",
                "density": "low",
                "panel_count": 0,
            },
            "content_kind": "equation",
            "dominant_object": "native_latex_math",
            "math": r"Y_{ij}=\beta_0+\beta_1T_{ij}+u_j+\varepsilon_{ij},\quad u_j\sim N(0,\tau^2),\quad \varepsilon_{ij}\sim N(0,\sigma^2)",
            "annotation": r"Center effects set \(\rho=\tau^2/(\tau^2+\sigma^2)\), so interval calibration depends on cluster count.",
            "required_panel_count": 0,
        },
        {
            "page_id": "quantitative_result_uncertainty",
            "page_job": "REAL_DATA_APPLICATION",
            "section": "Results",
            "title": "Cluster-robust intervals recover coverage as ICC increases",
            "query": {
                "page_function": "REAL_DATA_APPLICATION",
                "scientific_object": "biostatistics quantitative model comparison result table figure coverage uncertainty",
                "domain_family": "biostatistics",
                "dominant_object_type": "plot table",
                "evidence_type": "quantitative comparison result",
                "density": "moderate",
                "panel_count": 1,
            },
            "content_kind": "figure",
            "dominant_object": "coverage_plot",
            "asset": f"{stat_assets}/coverage_by_icc.png",
            "image_trim": "30 40 55 80",
            "annotation": "Red = naive iid; teal = cluster-robust. Nominal 0.95 and the small-center stress point remain visible.",
            "caption": "Synthetic clustered-data example; intervals compared on coverage, width, and bias.",
            "required_panel_count": 1,
        },
        {
            "page_id": "method_experiment_design",
            "page_job": "EXPERIMENT_DESIGN",
            "section": "Design",
            "title": "Simulation varies clustering before interval procedures are compared",
            "query": {
                "page_function": "EXPERIMENT_DESIGN",
                "scientific_object": "medical imaging task map experiment design clustered simulation procedure comparison",
                "domain_family": "medical_imaging",
                "dominant_object_type": "diagram",
                "evidence_type": "experiment design",
                "density": "moderate",
                "panel_count": 4,
            },
            "content_kind": "flow",
            "dominant_object": "scientific_relation_diagram",
            "nodes": ["DGP knobs", "Clustered samples", "Interval procedures", "Coverage diagnostics"],
            "design_factors": [
                r"centers \(G=8,20,50\)",
                r"ICC \(\rho=0,.1,.3,.5\)",
                "balanced or imbalanced clusters",
            ],
            "procedures": [
                "naive iid OLS z interval",
                "cluster-robust z interval with center scores",
            ],
            "endpoints": [
                "95% coverage vs 0.95 target",
                "mean interval width",
                "bias of treatment-effect estimate",
            ],
            "annotation": "The connector direction encodes data generation before interval estimation and coverage diagnostics.",
            "required_panel_count": 4,
        },
        {
            "page_id": "negative_failure_model_check",
            "page_job": "NEGATIVE_RESULT",
            "section": "Failure",
            "title": "Small-G settings remain anti-conservative after robustification",
            "query": {
                "page_function": "NEGATIVE_RESULT",
                "scientific_object": "negative result failure analysis finite sample model check coverage comparison",
                "domain_family": "statistics",
                "dominant_object_type": "plot",
                "evidence_type": "failure evidence",
                "density": "moderate",
                "panel_count": 2,
            },
            "content_kind": "figure",
            "dominant_object": "negative_evidence_plot",
            "asset": f"{stat_assets}/small_g_negative_result.png",
            "annotation": "The failure region is adjacent to the diagnostic explanation instead of hidden in a note.",
            "caption": "Negative evidence is completed; CR2 and wild cluster bootstrap remain the next test.",
            "required_panel_count": 2,
        },
        {
            "page_id": "medical_image_aligned_comparison",
            "page_job": "MEDICAL_IMAGE_COMPARISON",
            "section": "Medical Image",
            "title": "Same-case panels keep the segmentation error interpretable",
            "query": {
                "page_function": "MEDICAL_IMAGE_COMPARISON",
                "scientific_object": "medical image lesion samples task applications visual comparison same case overlay error",
                "domain_family": "medical_imaging",
                "dominant_object_type": "medical_image",
                "evidence_type": "representative image comparison",
                "density": "high",
                "panel_count": 4,
            },
            "content_kind": "image_panel",
            "dominant_object": "same_case_medical_panels",
            "assets": [
                f"{med_assets}/failure_input.png",
                f"{med_assets}/failure_gt.png",
                f"{med_assets}/failure_pred.png",
                f"{med_assets}/failure_error.png",
            ],
            "panel_labels": ["Input", "GT", "Prediction", "Error"],
            "annotation": "All four panels come from the same case; the error panel binds the failure explanation.",
            "required_panel_count": 4,
        },
        {
            "page_id": "discussion_next_experiment",
            "page_job": "NEXT_EXPERIMENT",
            "section": "Next",
            "title": "Next experiment tests whether batch selection reduces fragile coverage",
            "query": {
                "page_function": "NEXT_EXPERIMENT",
                "scientific_object": "discussion next experiment batch query bayesian optimization active learning DPP Mondrian diverse selection partition",
                "domain_family": "statistics",
                "dominant_object_type": "diagram plot comparison",
                "evidence_type": "next-query experimental design",
                "density": "moderate",
                "panel_count": 4,
            },
            "content_kind": "next_experiment",
            "dominant_object": "next_experiment_reasoning",
            "nodes": ["Small-G limit", "DPP batch query", "Mondrian partition", "CR2 / wild bootstrap"],
            "current_limit": "G=8, ICC=.5 and imbalanced clusters remain below nominal coverage.",
            "strategy_variation": [
                "DPP diverse batch",
                "independent random batch",
                "Mondrian-partition batch",
            ],
            "comparator_setup": [
                "CR2 small-sample correction",
                "wild cluster bootstrap",
            ],
            "decision_criterion": "PASS if coverage >= .94 and width inflation is controlled; otherwise stratify by Mondrian cell and recheck leverage.",
            "annotation": "Coverage evidence determines which batch-query strategy to validate next; CR2 and wild bootstrap remain proposed comparators.",
            "required_panel_count": 4,
        },
    ]


def resolve_layout(spec: dict[str, Any], *, recipe_override: dict[str, Any] | None = None) -> dict[str, Any]:
    recipe = recipe_override or build_gold_composition_recipe.build_recipe(spec["query"])
    constraints = recipe["composition_constraints"]
    primary, transforms = fit_bbox(constraints["primary_bbox"], constraints["content_capacity"])
    primary = expand_bbox_for_content(primary, spec["content_kind"], transforms)
    primary = job_primary_geometry(spec, primary, transforms)
    supporting = support_geometry(spec, primary)
    annotation = {key: round(value, 4) for key, value in supporting["annotation"].items()}
    caption = {key: round(value, 4) for key, value in supporting["caption"].items()}
    capacity = capacity_status(spec, recipe)
    emitted_text_regions = [annotation]
    if spec.get("caption"):
        emitted_text_regions.append(caption)
    text_overlap_free = all(
        not bbox_overlap(left, right)
        for idx, left in enumerate(emitted_text_regions)
        for right in emitted_text_regions[idx + 1 :]
    )
    objects = [
        {
            "object_id": f"{spec['page_id']}_primary",
            "role": "primary_scientific_object",
            "native_type": {
                "equation": "equation",
                "figure": "figure",
                "flow": "tikz_connector_diagram",
                "image_panel": "image_panel",
                "next_experiment": "tikz_reasoning_diagram",
            }[spec["content_kind"]],
            "bbox": primary,
        },
        {
            "object_id": f"{spec['page_id']}_annotation",
            "role": "annotation",
            "native_type": "text_callout",
            "bbox": annotation,
        },
        {
            "object_id": f"{spec['page_id']}_caption",
            "role": "caption",
            "native_type": "text_caption",
            "bbox": caption,
        },
    ]
    consumed = [
        "primary_bbox",
        "primary_object_area_ratio",
        "visual_hierarchy",
        "alignment_groups",
        "reading_flow",
        "annotation_legend_caption_panel_relations",
        "content_capacity",
    ]
    resolved = {
        "schema": "RESEARCH_CUHK_SCIENTIFIC_RESOLVED_LAYOUT_V1",
        "task_key": TASK_KEY,
        "page_id": spec["page_id"],
        "page_job": spec["page_job"],
        "dominant_scientific_object": spec["dominant_object"],
        "selected_gold_id": recipe["selected_gold_id"],
        "selected_reference_id": recipe["selected_reference_id"],
        "recipe_sha256": recipe["recipe_sha256"],
        "compatibility_trace": recipe["runtime_trace"]["selection"]["matches"][0]["compatibility_reasons"],
        "exact_cuhk_content_safe_region": SAFE_REGION,
        "source_recipe_fields_consumed": consumed,
        "source_to_cuhk_transform": transforms,
        "resolved_primary_object_geometry": primary,
        "resolved_supporting_object_geometry": {
            "annotation": annotation,
            "caption": caption,
        },
        "visual_hierarchy_mapping": constraints["visual_hierarchy"],
        "alignment_mapping": constraints["alignment_groups"],
        "reading_flow_mapping": constraints["reading_flow"],
        "annotation_legend_caption_panel_mapping": constraints["annotation_legend_caption_panel_relations"],
        "content_capacity_check": capacity,
        "text_region_packing": {
            "emitted_text_region_count": len(emitted_text_regions),
            "non_overlapping": text_overlap_free,
        },
        "native_objects": objects,
        "audience_safe_output_contract": {
            "internal_ids_exposed": False,
            "source_pixels_or_branding_reused": False,
            "forbidden_terms": FORBIDDEN_AUDIENCE_TERMS,
        },
    }
    resolved["resolved_layout_sha256"] = stable_sha(resolved)
    return resolved


def tex_node(x: float, y: float, w: float, body: str, *, align: str = "left") -> str:
    return rf"\StageThreeNode{{{x:.4f}}}{{{y:.4f}}}{{{w:.4f}}}{{{align}}}{{{body}}};"


def emit_equation(spec: dict[str, Any], layout: dict[str, Any]) -> str:
    primary = layout["resolved_primary_object_geometry"]
    annotation = layout["resolved_supporting_object_geometry"]["annotation"]
    return "\n".join([
        tex_node(primary["x"], primary["y"], primary["w"], rf"\Large \[\displaystyle {spec['math']}\]", align="center"),
        tex_node(annotation["x"], annotation["y"], annotation["w"], rf"\small {spec['annotation']}"),
    ])


def emit_figure(spec: dict[str, Any], layout: dict[str, Any], asset_map: dict[str, str]) -> str:
    primary = layout["resolved_primary_object_geometry"]
    annotation = layout["resolved_supporting_object_geometry"]["annotation"]
    caption = layout["resolved_supporting_object_geometry"]["caption"]
    asset = asset_map[spec["asset"]]
    trim = f",trim={spec['image_trim']},clip" if spec.get("image_trim") else ""
    return "\n".join([
        tex_node(primary["x"], primary["y"], primary["w"], rf"\includegraphics[width={primary['w']:.4f}\paperwidth,height={primary['h']:.4f}\paperheight,keepaspectratio{trim}]{{{asset}}}", align="center"),
        tex_node(annotation["x"], annotation["y"], annotation["w"], rf"\footnotesize {tex_escape(spec['annotation'])}"),
        tex_node(caption["x"], caption["y"], caption["w"], rf"\scriptsize {tex_escape(spec['caption'])}"),
    ])


def emit_flow(spec: dict[str, Any], layout: dict[str, Any]) -> str:
    if spec["page_job"] == "EXPERIMENT_DESIGN":
        return emit_experiment_design(spec, layout)
    if spec["page_job"] == "NEXT_EXPERIMENT":
        return emit_next_experiment(spec, layout)
    primary = layout["resolved_primary_object_geometry"]
    nodes = spec["nodes"]
    gap = 0.018
    node_w = (primary["w"] - gap * (len(nodes) - 1)) / len(nodes)
    node_h = min(primary["h"] * 0.42, 0.105)
    y = primary["y"] + primary["h"] * 0.20
    parts = []
    centers: list[tuple[float, float]] = []
    for idx, label in enumerate(nodes):
        x = primary["x"] + idx * (node_w + gap)
        centers.append((x + node_w, y + node_h / 2))
        parts.append(rf"\StageThreeBox{{{x:.4f}}}{{{y:.4f}}}{{{x+node_w:.4f}}}{{{y+node_h:.4f}}};")
        parts.append(tex_node(x + 0.008, y + 0.027, node_w - 0.016, rf"\footnotesize {tex_escape(label)}", align="center"))
    for idx in range(len(centers) - 1):
        x1 = centers[idx][0] + 0.004
        y1 = centers[idx][1]
        x2 = primary["x"] + (idx + 1) * (node_w + gap) - 0.006
        parts.append(rf"\StageThreeArrow{{{x1:.4f}}}{{{y1:.4f}}}{{{x2:.4f}}}{{{y1:.4f}}};")
    annotation = layout["resolved_supporting_object_geometry"]["annotation"]
    parts.append(tex_node(annotation["x"], annotation["y"], annotation["w"], rf"\small {tex_escape(spec['annotation'])}"))
    return "\n".join(parts)


def emit_experiment_design(spec: dict[str, Any], layout: dict[str, Any]) -> str:
    primary = layout["resolved_primary_object_geometry"]
    x = primary["x"]
    y = primary["y"]
    w = primary["w"]
    h = primary["h"]
    factor_w = w * 0.25
    data_w = w * 0.21
    proc_w = w * 0.22
    endpoint_w = w * 0.22
    gap = w * 0.035
    top_h = h * 0.84
    data_x = x + factor_w + gap
    proc_x = data_x + data_w + gap
    endpoint_x = proc_x + proc_w + gap
    parts = [
        rf"\StageThreePanel{{{x:.4f}}}{{{y:.4f}}}{{{x+factor_w:.4f}}}{{{y+top_h:.4f}}};",
        rf"\StageThreePanel{{{data_x:.4f}}}{{{y+0.060:.4f}}}{{{data_x+data_w:.4f}}}{{{y+top_h-0.035:.4f}}};",
        rf"\StageThreePanel{{{proc_x:.4f}}}{{{y:.4f}}}{{{proc_x+proc_w:.4f}}}{{{y+top_h:.4f}}};",
        rf"\StageThreePanel{{{endpoint_x:.4f}}}{{{y+0.030:.4f}}}{{{endpoint_x+endpoint_w:.4f}}}{{{y+top_h-0.010:.4f}}};",
        tex_node(x + 0.012, y + 0.020, factor_w - 0.024, r"\scriptsize\textbf{DGP stress grid}", align="center"),
        tex_node(data_x + 0.012, y + 0.088, data_w - 0.024, r"\scriptsize\textbf{Generated units}\\centers -> subjects\\treatment shares", align="center"),
        tex_node(proc_x + 0.012, y + 0.020, proc_w - 0.024, r"\scriptsize\textbf{Interval procedures}", align="center"),
        tex_node(endpoint_x + 0.012, y + 0.055, endpoint_w - 0.024, r"\scriptsize\textbf{Evaluation endpoints}", align="center"),
    ]
    for idx, factor in enumerate(spec["design_factors"]):
        parts.append(tex_node(x + 0.018, y + 0.092 + idx * 0.078, factor_w - 0.036, rf"\scriptsize {factor}", align="left"))
    parts.append(tex_node(data_x + 0.018, y + 0.230, data_w - 0.036, r"\tiny 400 reps/cell\\records: \(Y_{ij},T_{ij},j\)", align="center"))
    for idx, procedure in enumerate(spec["procedures"]):
        py = y + 0.115 + idx * 0.130
        parts.append(rf"\StageThreeSubPanel{{{proc_x+0.018:.4f}}}{{{py:.4f}}}{{{proc_x+proc_w-0.018:.4f}}}{{{py+0.090:.4f}}};")
        parts.append(tex_node(proc_x + 0.026, py + 0.020, proc_w - 0.052, rf"\tiny {tex_escape(procedure)}", align="center"))
    for idx, endpoint in enumerate(spec["endpoints"]):
        parts.append(tex_node(endpoint_x + 0.018, y + 0.125 + idx * 0.080, endpoint_w - 0.036, rf"\tiny {tex_escape(endpoint)}", align="left"))
    mid_y = y + top_h * 0.50
    parts.extend([
        rf"\StageThreeConnector{{{x+factor_w+0.006:.4f}}}{{{mid_y:.4f}}}{{{data_x-0.008:.4f}}}{{{mid_y:.4f}}};",
        rf"\StageThreeConnector{{{data_x+data_w+0.006:.4f}}}{{{mid_y:.4f}}}{{{proc_x-0.008:.4f}}}{{{mid_y:.4f}}};",
        rf"\StageThreeConnector{{{proc_x+proc_w+0.006:.4f}}}{{{mid_y:.4f}}}{{{endpoint_x-0.008:.4f}}}{{{mid_y:.4f}}};",
    ])
    annotation = layout["resolved_supporting_object_geometry"]["annotation"]
    parts.append(tex_node(annotation["x"], annotation["y"], annotation["w"], rf"\footnotesize {tex_escape(spec['annotation'])}", align="left"))
    return "\n".join(parts)


def emit_next_experiment(spec: dict[str, Any], layout: dict[str, Any]) -> str:
    primary = layout["resolved_primary_object_geometry"]
    x = primary["x"]
    y = primary["y"]
    w = primary["w"]
    h = primary["h"]
    col_w = (w - 0.05) / 3
    x2 = x + col_w + 0.025
    x3 = x2 + col_w + 0.025
    panel_h = h * 0.78
    parts = [
        rf"\StageThreePanel{{{x:.4f}}}{{{y:.4f}}}{{{x+col_w:.4f}}}{{{y+panel_h:.4f}}};",
        rf"\StageThreePanel{{{x2:.4f}}}{{{y:.4f}}}{{{x2+col_w:.4f}}}{{{y+panel_h:.4f}}};",
        rf"\StageThreePanel{{{x3:.4f}}}{{{y:.4f}}}{{{x3+col_w:.4f}}}{{{y+panel_h:.4f}}};",
        tex_node(x + 0.014, y + 0.020, col_w - 0.028, r"\scriptsize\textbf{Current limit}", align="center"),
        tex_node(x + 0.018, y + 0.088, col_w - 0.036, rf"\scriptsize {tex_escape(spec['current_limit'])}", align="left"),
        tex_node(x2 + 0.014, y + 0.020, col_w - 0.028, r"\scriptsize\textbf{Batch-query factor}", align="center"),
        tex_node(x3 + 0.014, y + 0.020, col_w - 0.028, r"\scriptsize\textbf{Comparator and criterion}", align="center"),
    ]
    for idx, strategy in enumerate(spec["strategy_variation"]):
        sy = y + 0.082 + idx * 0.072
        parts.append(rf"\StageThreeSubPanel{{{x2+0.018:.4f}}}{{{sy:.4f}}}{{{x2+col_w-0.018:.4f}}}{{{sy+0.048:.4f}}};")
        parts.append(tex_node(x2 + 0.026, sy + 0.011, col_w - 0.052, rf"\scriptsize {tex_escape(strategy)}", align="center"))
    for idx, comparator in enumerate(spec["comparator_setup"]):
        parts.append(tex_node(x3 + 0.022, y + 0.090 + idx * 0.058, col_w - 0.044, rf"\scriptsize {tex_escape(comparator)}", align="left"))
    parts.append(tex_node(x3 + 0.022, y + 0.215, col_w - 0.044, rf"\tiny {tex_escape(spec['decision_criterion'])}", align="left"))
    mid_y = y + panel_h * 0.47
    parts.extend([
        rf"\StageThreeConnector{{{x+col_w+0.008:.4f}}}{{{mid_y:.4f}}}{{{x2-0.010:.4f}}}{{{mid_y:.4f}}};",
        rf"\StageThreeConnector{{{x2+col_w+0.008:.4f}}}{{{mid_y:.4f}}}{{{x3-0.010:.4f}}}{{{mid_y:.4f}}};",
    ])
    annotation = layout["resolved_supporting_object_geometry"]["annotation"]
    parts.append(tex_node(annotation["x"], annotation["y"], annotation["w"], rf"\footnotesize {tex_escape(spec['annotation'])}", align="left"))
    return "\n".join(parts)


def emit_image_panel(spec: dict[str, Any], layout: dict[str, Any], asset_map: dict[str, str]) -> str:
    primary = layout["resolved_primary_object_geometry"]
    labels = spec["panel_labels"]
    assets = [asset_map[item] for item in spec["assets"]]
    gap = 0.010
    panel_w = (primary["w"] - gap * 3) / 4
    panel_h = min(primary["h"] * 0.72, panel_w * SLIDE_W / SLIDE_H)
    y = primary["y"] + 0.050
    parts = []
    for idx, (label, asset) in enumerate(zip(labels, assets)):
        x = primary["x"] + idx * (panel_w + gap)
        parts.append(tex_node(x, y - 0.037, panel_w, rf"\footnotesize\textbf{{{tex_escape(label)}}}", align="center"))
        parts.append(tex_node(x, y, panel_w, rf"\includegraphics[width={panel_w:.4f}\paperwidth,height={panel_h:.4f}\paperheight,keepaspectratio]{{{asset}}}", align="center"))
    zoom_x = primary["x"] + primary["w"] * 0.34
    zoom_y = y + panel_h + 0.020
    zoom_w = primary["w"] * 0.32
    zoom_h = min(0.135, primary["y"] + primary["h"] - zoom_y)
    parts.append(rf"\StageThreeSubPanel{{{zoom_x:.4f}}}{{{zoom_y:.4f}}}{{{zoom_x+zoom_w:.4f}}}{{{zoom_y+zoom_h:.4f}}};")
    parts.append(tex_node(zoom_x + 0.010, zoom_y + 0.012, zoom_w - 0.020, r"\scriptsize\textbf{Error zoom: TP / FP / FN colors remain bound to the same case}", align="center"))
    annotation = layout["resolved_supporting_object_geometry"]["caption"]
    parts.append(tex_node(annotation["x"], annotation["y"], annotation["w"], rf"\scriptsize {tex_escape(spec['annotation'])}", align="center"))
    return "\n".join(parts)


def emit_frame(spec: dict[str, Any], layout: dict[str, Any], asset_map: dict[str, str]) -> str:
    if spec["content_kind"] == "equation":
        body = emit_equation(spec, layout)
    elif spec["content_kind"] == "figure":
        body = emit_figure(spec, layout, asset_map)
    elif spec["content_kind"] == "image_panel":
        body = emit_image_panel(spec, layout, asset_map)
    else:
        body = emit_flow(spec, layout)
    return rf"""\section{{{tex_escape(spec['section'])}}}
\begin{{frame}}[t]{{{tex_escape(spec['title'])}}}
\begin{{tikzpicture}}[x=\paperwidth,y=-\paperheight]
\path[use as bounding box] (0,0.12) rectangle (1,0.82);
{body}
\end{{tikzpicture}}
\end{{frame}}
"""


def scientific_layout_macros() -> str:
    return r"""\usepackage{tikz}
\usetikzlibrary{arrows.meta,positioning,calc}
\newcommand{\StageThreeNode}[5]{\node[anchor=north west,align=#4,text width=#3\paperwidth,inner sep=0pt] at (#1,#2) {#5}}
\newcommand{\StageThreeBox}[4]{\draw[rounded corners=1.5pt,line width=0.7pt,draw=maincolor!75,fill=white] (#1,#2) rectangle (#3,#4)}
\newcommand{\StageThreeArrow}[4]{\draw[-{Latex[length=2mm]},line width=0.8pt,draw=maincolor!75] (#1,#2) -- (#3,#4)}
\newcommand{\StageThreePanel}[4]{\draw[rounded corners=1pt,line width=0.7pt,draw=maincolor!70,fill=maincolor!3] (#1,#2) rectangle (#3,#4)}
\newcommand{\StageThreeSubPanel}[4]{\draw[rounded corners=0.8pt,line width=0.55pt,draw=maincolor!45,fill=white] (#1,#2) rectangle (#3,#4)}
\newcommand{\StageThreeConnector}[4]{\draw[-{Latex[length=2.2mm]},line width=0.9pt,draw=maincolor!80] (#1,#2) -- (#3,#4)}
"""


def build_main_tex(specs: list[dict[str, Any]], layouts: list[dict[str, Any]], asset_map: dict[str, str]) -> str:
    frames = "\n".join(emit_frame(spec, layout, asset_map) for spec, layout in zip(specs, layouts))
    return rf"""% Generated Stage 3 integration deck.
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

\title{{CUHK Scientific Layout Families}}
\subtitle{{Model, evidence, imaging, and next-experiment pages}}
\author{{Research Presentation Program}}
\institute{{Department of Statistics \& Data Science}}
\date{{\today}}

\begin{{document}}
\maketitle
{frames}
\end{{document}}
"""


def copy_assets(specs: list[dict[str, Any]], build_dir: Path) -> dict[str, str]:
    asset_dir = build_dir / "stage3_assets"
    asset_dir.mkdir(parents=True, exist_ok=True)
    asset_map: dict[str, str] = {}
    for spec in specs:
        paths = []
        if spec.get("asset"):
            paths.append(spec["asset"])
        paths.extend(spec.get("assets", []))
        for raw in paths:
            source = REPO_ROOT / raw
            target = asset_dir / source.name
            shutil.copy2(source, target)
            asset_map[raw] = f"stage3_assets/{target.name}"
    return asset_map


def find_tex_engine() -> dict[str, Any] | None:
    for command in ["xelatex", "lualatex", "pdflatex", "tectonic"]:
        probe = find_command(command)
        if probe["available"]:
            return {"command": command, **probe}
    return None


def dependency_probe() -> dict[str, Any]:
    commands = {command: find_command(command) for command in ["xelatex", "lualatex", "pdflatex", "tectonic", "pdftoppm", "pdfinfo", "pdftotext", "pdffonts"]}
    tex_engine_available = any(commands[command]["available"] for command in ["xelatex", "lualatex", "pdflatex", "tectonic"])
    return {
        "schema": "RESEARCH_CUHK_STAGE3_BUILD_DEPENDENCY_PROBE_V1",
        "task_key": TASK_KEY,
        "commands": commands,
        "local_render_resources": {
            "source": "render-chinese-math-pdf probe / host-local render resources",
            "resource_dir": str(LOCAL_RENDER_RESOURCE_DIR),
            "resource_dir_exists": LOCAL_RENDER_RESOURCE_DIR.exists(),
            "texmf": str(LOCAL_RENDER_TEXMF),
            "texmf_exists": LOCAL_RENDER_TEXMF.exists(),
            "fandol_dir": str(LOCAL_FANDOL_DIR),
            "fandol_dir_exists": LOCAL_FANDOL_DIR.exists(),
            "noto_cjk_dir": str(LOCAL_NOTO_CJK_DIR),
            "noto_cjk_dir_exists": LOCAL_NOTO_CJK_DIR.exists(),
            "times_font_dir": str(TRACE_TIMES_FONT_DIR),
            "times_font_dir_exists": TRACE_TIMES_FONT_DIR.exists(),
            "tinytex_bin": str(LOCAL_TINYTEX_BIN),
            "tinytex_bin_exists": LOCAL_TINYTEX_BIN.exists(),
            "tex_cache_env": tex_cache_env(),
        },
        "tex_engine_available": tex_engine_available,
        "pdf_renderer_available": commands["pdftoppm"]["available"],
        "preferred_route": "latex_to_pdf_to_png" if tex_engine_available else "blocked_missing_dependency",
    }


def compile_pdf(build_dir: Path) -> dict[str, Any]:
    engine = find_tex_engine()
    pdf = build_dir / "main.pdf"
    fontconfig = write_fontconfig(build_dir)
    if not engine:
        return {
            "status": "BLOCKED_MISSING_TEX_ENGINE",
            "engine": None,
            "engine_path": None,
            "fontconfig": fontconfig,
            "pdf": None,
            "log": None,
            "message": "No xelatex, lualatex, pdflatex, or tectonic executable is available through PATH.",
        }
    if engine["command"] == "tectonic":
        cmd = [engine["path"], "main.tex"]
    else:
        cmd = [engine["path"], "-interaction=nonstopmode", "-halt-on-error", "main.tex"]
    env = os.environ.copy()
    env["PATH"] = render_search_path()
    env["FONTCONFIG_FILE"] = fontconfig["fontconfig_file"]
    env["XDG_CACHE_HOME"] = fontconfig["font_cache_dir"]
    env["OSFONTDIR"] = fontconfig["times_font_dir"]
    env.update(tex_cache_env())
    runs = []
    pass_count = 1 if engine["command"] == "tectonic" else 2
    for pass_index in range(pass_count):
        run = subprocess.run(cmd, cwd=build_dir, check=False, capture_output=True, text=True, env=env)
        runs.append((pass_index + 1, run))
        if run.returncode != 0:
            break
    log_path = build_dir / "compile.log"
    log_path.write_text(
        "\n".join(
            f"===== pass {pass_index} stdout =====\n{run.stdout}\n===== pass {pass_index} stderr =====\n{run.stderr}"
            for pass_index, run in runs
        ),
        encoding="utf-8",
    )
    final_run = runs[-1][1]
    if final_run.returncode != 0 or not pdf.exists():
        return {
            "status": "COMPILE_FAILED",
            "engine": engine["command"],
            "engine_path": engine["path"],
            "compile_passes": len(runs),
            "fontconfig": fontconfig,
            "pdf": rel(pdf) if pdf.exists() else None,
            "log": rel(log_path),
            "message": "LaTeX compilation failed.",
        }
    return {
        "status": "COMPILED",
        "engine": engine["command"],
        "engine_path": engine["path"],
        "compile_passes": len(runs),
        "fontconfig": fontconfig,
        "pdf": rel(pdf),
        "pdf_sha256": file_sha(pdf),
        "log": rel(log_path),
    }


def render_pdf(build_dir: Path, compile_status: dict[str, Any]) -> dict[str, Any]:
    if compile_status.get("status") != "COMPILED":
        return {
            "status": compile_status["status"],
            "png_count": 0,
            "rendered_png": [],
            "message": compile_status.get("message"),
        }
    if not shutil.which("pdftoppm"):
        return {
            "status": "BLOCKED_MISSING_PDF_RENDERER",
            "png_count": 0,
            "rendered_png": [],
            "message": "pdftoppm is not available.",
        }
    rendered_dir = build_dir / "rendered"
    rendered_dir.mkdir(exist_ok=True)
    prefix = rendered_dir / "slide"
    run = subprocess.run(["pdftoppm", "-png", "-r", "160", "main.pdf", str(prefix)], cwd=build_dir, check=False, capture_output=True, text=True)
    if run.returncode != 0:
        return {
            "status": "RENDER_FAILED",
            "png_count": 0,
            "rendered_png": [],
            "message": run.stderr or run.stdout,
        }
    pngs = sorted(rendered_dir.glob("slide-*.png"))
    return {
        "status": "ok",
        "png_count": len(pngs),
        "rendered_png": [{"path": rel(path), "sha256": file_sha(path)} for path in pngs],
    }


def clean_latex_intermediates(build_dir: Path) -> list[str]:
    removed: list[str] = []
    for suffix in [".aux", ".nav", ".out", ".snm", ".toc"]:
        path = build_dir / f"main{suffix}"
        if path.exists():
            path.unlink()
            removed.append(rel(path))
    return removed


def normalize_generated_logs(build_dir: Path) -> list[str]:
    normalized: list[str] = []
    for name in ["compile.log", "main.log"]:
        path = build_dir / name
        if not path.exists():
            continue
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
        path.write_text("\n".join(line.rstrip() for line in lines) + "\n", encoding="utf-8")
        normalized.append(rel(path))
    return normalized


def mutation_regression(spec: dict[str, Any], baseline_layout: dict[str, Any]) -> dict[str, Any]:
    baseline_recipe = build_gold_composition_recipe.build_recipe(spec["query"])
    mutated_recipe = json.loads(json.dumps(baseline_recipe))
    bbox = mutated_recipe["composition_constraints"]["primary_bbox"]
    bbox["x"] = clamp(float(bbox["x"]) + 0.08, 0.02, 0.72)
    bbox["w"] = clamp(float(bbox["w"]) * 0.86, 0.18, 0.86)
    mutated_recipe["recipe_sha256"] = stable_sha(mutated_recipe)
    mutated_layout = resolve_layout(spec, recipe_override=mutated_recipe)
    return {
        "schema": "RESEARCH_CUHK_STAGE3_MUTATION_REGRESSION_V1",
        "task_key": TASK_KEY,
        "status": "PASS" if baseline_layout["resolved_primary_object_geometry"] != mutated_layout["resolved_primary_object_geometry"] else "FAIL",
        "mutated_field": "composition_constraints.primary_bbox",
        "baseline_gold_id": baseline_layout["selected_gold_id"],
        "baseline_recipe_sha256": baseline_layout["recipe_sha256"],
        "mutated_recipe_sha256": mutated_layout["recipe_sha256"],
        "baseline_geometry_signature": bbox_signature(baseline_layout["resolved_primary_object_geometry"]),
        "mutated_geometry_signature": bbox_signature(mutated_layout["resolved_primary_object_geometry"]),
        "checks": {
            "source_geometry_changed": True,
            "resolved_geometry_changed": baseline_layout["resolved_primary_object_geometry"] != mutated_layout["resolved_primary_object_geometry"],
            "emitted_geometry_changes_with_recipe": baseline_layout["resolved_primary_object_geometry"] != mutated_layout["resolved_primary_object_geometry"],
            "page_job_unchanged": baseline_layout["page_job"] == mutated_layout["page_job"],
        },
    }


def capacity_failure_contract(spec: dict[str, Any]) -> dict[str, Any]:
    overloaded = json.loads(json.dumps(spec))
    overloaded["required_panel_count"] = int(spec.get("required_panel_count") or 0) + 8
    recipe = build_gold_composition_recipe.build_recipe(spec["query"])
    status = capacity_status(overloaded, recipe)
    return {
        "schema": "RESEARCH_CUHK_STAGE3_CAPACITY_FAILURE_CONTRACT_V1",
        "task_key": TASK_KEY,
        "page_id": spec["page_id"],
        "selected_gold_id": recipe["selected_gold_id"],
        "requested_panel_count": overloaded["required_panel_count"],
        "selected_layout_panel_capacity": recipe["composition_constraints"]["content_capacity"]["panel_count"],
        "status": status["status"],
        "reason": status["reason"],
        "fallback_used": "SPLIT_REQUIRED" if status["status"] == "SPLIT_REQUIRED" else "UNEXPECTED",
        "generic_layout_fallback_used": False,
    }


def visual_review_manifest(
    *,
    render_status: dict[str, Any],
    specs: list[dict[str, Any]],
    layouts: list[dict[str, Any]],
    build_manifest: dict[str, Any],
    build_manifest_path: Path,
) -> dict[str, Any]:
    rendered = render_status.get("rendered_png", [])
    inputs = []
    page_jobs: dict[str, str] = {}
    dominant_objects: dict[str, str] = {}
    selected_gold: dict[str, str] = {}
    png_sha: dict[str, str] = {}
    for idx, item in enumerate(rendered, start=1):
        if idx < 2 or idx - 2 >= len(specs):
            continue
        spec = specs[idx - 2]
        layout = layouts[idx - 2]
        logical_id = f"slide_{idx}_{spec['page_job'].lower()}"
        inputs.append(
            {
                "logical_id": logical_id,
                "path": item["path"],
                "mime_type": "image/png",
                "sha256": item["sha256"],
                "description": f"Rendered exact-CUHK content page for {spec['page_job']} with {spec['dominant_object']} as the main scientific object.",
            }
        )
        page_jobs[logical_id] = spec["page_job"]
        dominant_objects[logical_id] = spec["dominant_object"]
        selected_gold[logical_id] = layout["selected_gold_id"]
        png_sha[logical_id] = item["sha256"]
    return {
        "schema": "AI_BRIDGE_VISUAL_INPUT_MANIFEST_V1",
        "task_key": TASK_KEY,
        "workflow_type": "reviewed_handoff",
        "review_kind": "027-stage3-cuhk-scientific-layout-item-page-review",
        "privacy_policy": "PUBLIC_SAFE_ONLY",
        "prompt_version": "ai-bridge.visual-review.v1",
        "external_upload_authorization": "",
        "rubric": {
            "instructions": (
                "You are reviewing rendered pixels from the 027 Stage 3 exact-CUHK scientific layout integration deck. "
                "Judge each content page independently at item/page level. PASS for an item only if the visible page reaches a mature doctoral research-group meeting or strong conference-talk bar for its page job. "
                "Check that the CUHK Beamer identity is visible; the main scientific object is prominent and projection-readable; math is genuinely typeset rather than source-like text; figures, negative evidence, and medical panels are large enough to inspect; panel labels, captions, legends, and annotations are readable and directly tied to the scientific object; discussion/next-experiment content shows concrete research reasoning rather than generic future-work boxes. "
                "Mark REVISE for any page that looks like a generic card/dashboard/box-arrow fixture, has internal provenance or QA language, has source-like math, hides the evidence in a tiny figure, clips content, uses meaningless whitespace, or repeats one template face without scientific specificity. "
                "Top-level PASS means all six content items pass; top-level REVISE if any item has a blocking visual maturity issue. Do not infer quality from filenames, hashes, metadata, or presumed provenance; inspect the actual pixels."
            ),
            "source_contracts": [
                "Stage 2 gold/reference pixels are evidence only and are not runtime assets.",
                "This is a Stage 3 engineering integration deck, not a final real-paper holdout.",
            ],
        },
        "identity_bindings": {
            "task_key": TASK_KEY,
            "build_manifest": rel(build_manifest_path),
            "build_manifest_sha256": file_sha(build_manifest_path),
            "pdf_sha256": build_manifest.get("compile_status", {}).get("pdf_sha256"),
            "page_job_by_logical_id": page_jobs,
            "dominant_object_by_logical_id": dominant_objects,
            "selected_gold_id_by_logical_id": selected_gold,
            "rendered_png_sha256_by_logical_id": png_sha,
        },
        "inputs": inputs,
    }


def generate(out_dir: Path, *, write_result_visual_inputs: bool = False) -> dict[str, Any]:
    out_dir.mkdir(parents=True, exist_ok=True)
    build_dir = out_dir / "cuhk_stage3_build"
    if build_dir.exists():
        shutil.rmtree(build_dir)
    shutil.copytree(CANONICAL_CUHK, build_dir)
    specs = page_specs()
    asset_map = copy_assets(specs, build_dir)
    layouts = [resolve_layout(spec) for spec in specs]
    (build_dir / "scientific_layouts.tex").write_text(scientific_layout_macros(), encoding="utf-8")
    (build_dir / "main.tex").write_text(build_main_tex(specs, layouts, asset_map), encoding="utf-8")
    trace = {
        "schema": "RESEARCH_CUHK_STAGE3_TRACE_V1",
        "task_key": TASK_KEY,
        "fixture_boundary": "Stage 3 engineering integration fixture; not a real-paper holdout and not ONE_SHOT_QUALITY_PASS.",
        "canonical_cuhk_source": rel(CANONICAL_CUHK),
        "build_workspace": rel(build_dir),
        "slides": [
            {
                "page_id": spec["page_id"],
                "page_job": spec["page_job"],
                "selector_query": spec["query"],
                "selected_gold_id": layout["selected_gold_id"],
                "recipe_sha256": layout["recipe_sha256"],
                "resolved_layout_sha256": layout["resolved_layout_sha256"],
                "emitted_tex_object_ids": [item["object_id"] for item in layout["native_objects"]],
                "content_capacity_check": layout["content_capacity_check"],
            }
            for spec, layout in zip(specs, layouts)
        ],
    }
    (out_dir / "resolved_layouts.json").write_text(json.dumps({"schema": "RESEARCH_CUHK_STAGE3_RESOLVED_LAYOUTS_V1", "task_key": TASK_KEY, "layouts": layouts}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (out_dir / "runtime_trace.json").write_text(json.dumps(trace, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    mutation = mutation_regression(specs[0], layouts[0])
    (out_dir / "mutation_regression.json").write_text(json.dumps(mutation, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    capacity_failure = capacity_failure_contract(specs[4])
    (out_dir / "capacity_failure_contract.json").write_text(json.dumps(capacity_failure, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    dependencies = dependency_probe()
    (out_dir / "dependency_probe.json").write_text(json.dumps(dependencies, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    render_probe = render_skill_probe()
    (out_dir / "render_chinese_math_pdf_probe.json").write_text(json.dumps(render_probe, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    compile_status = compile_pdf(build_dir)
    render_status = render_pdf(build_dir, compile_status)
    cleaned_intermediates = clean_latex_intermediates(build_dir)
    normalized_logs = normalize_generated_logs(build_dir)
    manifest = {
        "schema": "RESEARCH_CUHK_STAGE3_BUILD_MANIFEST_V1",
        "task_key": TASK_KEY,
        "canonical_cuhk_source": rel(CANONICAL_CUHK),
        "canonical_files": {
            rel(path): file_sha(path)
            for path in sorted(CANONICAL_CUHK.rglob("*"))
            if path.is_file()
        },
        "build_workspace": rel(build_dir),
        "tex": rel(build_dir / "main.tex"),
        "scientific_layout_include": rel(build_dir / "scientific_layouts.tex"),
        "compile_status": compile_status,
        "render_status": render_status,
        "mechanical_qa": {
            "status": "MECHANICAL_PASS" if render_status.get("status") == "ok" and render_status.get("png_count", 0) >= 7 else "BLOCKED_RENDER_QA",
            "checks": {
                "canonical_source_copied": True,
                "scientific_layout_include_loaded": True,
                "six_content_page_jobs": len(specs) == 6,
                "title_plus_content_pages_expected": 7,
                "rendered_pages_available": render_status.get("status") == "ok",
            },
        },
        "cleaned_latex_intermediates": cleaned_intermediates,
        "normalized_generated_logs": normalized_logs,
        "resolved_layouts": rel(out_dir / "resolved_layouts.json"),
        "runtime_trace": rel(out_dir / "runtime_trace.json"),
        "mutation_regression": rel(out_dir / "mutation_regression.json"),
        "capacity_failure_contract": rel(out_dir / "capacity_failure_contract.json"),
        "dependency_probe": rel(out_dir / "dependency_probe.json"),
        "render_chinese_math_pdf_probe": rel(out_dir / "render_chinese_math_pdf_probe.json"),
    }
    build_manifest_path = out_dir / "BUILD_MANIFEST.json"
    build_manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    visual_inputs = visual_review_manifest(
        render_status=render_status,
        specs=specs,
        layouts=layouts,
        build_manifest=manifest,
        build_manifest_path=build_manifest_path,
    )
    (out_dir / "visual_inputs.json").write_text(json.dumps(visual_inputs, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    if write_result_visual_inputs:
        RESULT_VISUAL_REVIEW_DIR.mkdir(parents=True, exist_ok=True)
        (RESULT_VISUAL_REVIEW_DIR / "visual_inputs.json").write_text(json.dumps(visual_inputs, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out-dir", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--write-result-visual-inputs", action="store_true")
    args = parser.parse_args()
    manifest = generate(args.out_dir, write_result_visual_inputs=args.write_result_visual_inputs)
    print(json.dumps({"status": manifest["mechanical_qa"]["status"], "out_dir": rel(args.out_dir), "render_status": manifest["render_status"]["status"]}, indent=2))
    return 0 if manifest["mechanical_qa"]["status"] == "MECHANICAL_PASS" else 2


if __name__ == "__main__":
    raise SystemExit(main())
