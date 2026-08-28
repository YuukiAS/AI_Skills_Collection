#!/usr/bin/env python3
"""Generate Stage 3 CUHK scientific-layout integration artifacts."""

from __future__ import annotations

import argparse
import csv
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
DEFAULT_TASK_KEY = "027_research_presentation_executable_cuhk_scientific_layout_system"
RECOVERY_TASK_KEY = "030_stage3_visual_recovery"
TASK_KEY = DEFAULT_TASK_KEY
CANONICAL_CUHK = SHARED / "templates" / "cuhk" / "beamer" / "source"
DEFAULT_OUT = REPO_ROOT / "docs" / "audits" / "research_presentation_cuhk_scientific_layout_stage3" / "generated"

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
MEDICAL_ERROR_COLORS = {
    "tp": (0, 120, 112),
    "fp": (205, 20, 20),
    "fn": (225, 126, 0),
}


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
        "result_figure": (0.82, 0.46),
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
        target = {"w": safe["w"], "h": 0.58, "x": safe["x"], "y": 0.235}
        transforms.append("four-panel medical comparison receives full-width projection-scale image band")
    elif page_job == "EXPERIMENT_DESIGN":
        target = {"w": 0.86, "h": 0.49, "x": 0.07, "y": 0.270}
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
            "annotation": {"x": safe["x"], "y": 0.832, "w": safe["w"], "h": 0.024},
            "caption": {"x": safe["x"], "y": 0.832, "w": safe["w"], "h": 0.024},
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
        "fontconfig_file": str(config.resolve()),
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
    stat_simulation = "tests/fixtures/presentations/statistical_method_group_meeting/visual_review_packet_source/simulation/simulation_summary.csv"
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
            "content_kind": "result_figure",
            "dominant_object": "presentation_native_coverage_figure",
            "data_source": stat_simulation,
            "figure_filter": {"imbalance": "imbalanced"},
            "methods": [
                {"id": "naive_iid_ols_z", "label": "naive iid", "color": "red!72!black"},
                {"id": "cluster_robust_z", "label": "cluster-robust", "color": "teal!70!black"},
            ],
            "nominal_coverage": 0.95,
            "callout": {"G": 8, "rho": 0.5, "label": "small-G stress"},
            "annotation": "Small-G, high-ICC imbalance still suppresses coverage; center-robust intervals recover toward nominal as clusters increase.",
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
                "Coverage target 0.95",
                "mean interval width",
                "treatment-effect bias",
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
            "roi_source_asset": f"{med_assets}/failure_error.png",
            "roi_crop_assets": [
                f"{med_assets}/failure_gt.png",
                f"{med_assets}/failure_pred.png",
                f"{med_assets}/failure_error.png",
            ],
            "roi_crop_labels": ["GT crop", "Prediction crop", "Error crop"],
            "annotation": "All panels and zoom crops come from one case and one ROI; TP/FP/FN colors remain adjacent to the error crop.",
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
                "random batch",
                "Mondrian partition",
            ],
            "comparator_setup": [
                "CR2 small-sample correction",
                "wild cluster bootstrap",
            ],
            "decision_criterion": "Go if coverage >= .94 with controlled width; no-go stratifies by Mondrian cell.",
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
                "result_figure": "presentation_native_result_figure",
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
    if spec.get("same_case_roi_zoom"):
        objects.append(
            {
                "object_id": f"{spec['page_id']}_same_case_roi_zoom",
                "role": "same_case_error_roi_zoom",
                "native_type": "same_case_roi_crop_image",
                "source_assets": spec.get("roi_crop_assets", []),
                "roi_source_asset": spec.get("roi_source_asset"),
                "roi_xywh": spec["same_case_roi_zoom"]["roi_xywh"],
                "crop_records": spec["same_case_roi_zoom"]["crop_records"],
                "same_case_coordinate_space": True,
                "bbox": {
                    "x": round(primary["x"] + primary["w"] * 0.42, 4),
                    "y": round(primary["y"] + primary["h"] * 0.56, 4),
                    "w": round(primary["w"] * 0.42, 4),
                    "h": round(primary["h"] * 0.32, 4),
                },
            }
        )
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
        "executable_layout_family": {
            "REAL_DATA_APPLICATION": "presentation_native_quantitative_result",
            "EXPERIMENT_DESIGN": "typed_experiment_design_hierarchy",
            "MEDICAL_IMAGE_COMPARISON": "same_case_medical_roi_zoom",
            "NEXT_EXPERIMENT": "evidence_to_decision_next_experiment",
        }.get(spec["page_job"], "accepted_stage3_foundation"),
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
        "job_specific_runtime_contract": {
            "primitive": {
                "REAL_DATA_APPLICATION": "csv_driven_tikz_result_figure",
                "EXPERIMENT_DESIGN": "typed_scientific_hierarchy_relation_map",
                "MEDICAL_IMAGE_COMPARISON": "same_case_roi_crop_zoom",
                "NEXT_EXPERIMENT": "evidence_manipulation_comparator_decision_map",
            }.get(spec["page_job"], "accepted_foundation"),
            "source_fields_consumed": [key for key in ["data_source", "figure_filter", "roi_source_asset", "same_case_roi_zoom"] if key in spec],
            "same_case_roi_zoom": spec.get("same_case_roi_zoom"),
        },
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


def load_result_series(spec: dict[str, Any]) -> dict[int, dict[str, list[dict[str, float]]]]:
    source = REPO_ROOT / spec["data_source"]
    filtered: dict[int, dict[str, list[dict[str, float]]]] = {}
    with source.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            if row.get("imbalance") != spec["figure_filter"]["imbalance"]:
                continue
            center_count = int(row["G"])
            method = row["method"]
            filtered.setdefault(center_count, {}).setdefault(method, []).append(
                {
                    "rho": float(row["rho"]),
                    "coverage": float(row["coverage"]),
                    "mc_se": float(row["mc_se"]),
                }
            )
    for methods in filtered.values():
        for points in methods.values():
            points.sort(key=lambda item: item["rho"])
    return filtered


def emit_result_figure(spec: dict[str, Any], layout: dict[str, Any]) -> str:
    primary = layout["resolved_primary_object_geometry"]
    annotation = layout["resolved_supporting_object_geometry"]["annotation"]
    caption = layout["resolved_supporting_object_geometry"]["caption"]
    data = load_result_series(spec)
    x = primary["x"]
    y = primary["y"]
    w = primary["w"]
    h = primary["h"]
    plot_x = x + 0.070
    plot_y = y + 0.065
    plot_h = h * 0.58
    legend_x = x + w * 0.805
    legend_w = x + w - legend_x
    gap = 0.026
    facet_w = (legend_x - plot_x - gap * 2 - 0.020) / 3
    ymin = 0.50
    ymax = 1.00
    rho_min = 0.0
    rho_max = 0.5

    def px(facet_index: int, rho: float) -> float:
        fx = plot_x + facet_index * (facet_w + gap)
        return fx + (rho - rho_min) / (rho_max - rho_min) * facet_w

    def py(coverage: float) -> float:
        return plot_y + (1.0 - (coverage - ymin) / (ymax - ymin)) * plot_h

    def point_chain(facet_index: int, points: list[dict[str, float]]) -> str:
        return " -- ".join(f"({px(facet_index, item['rho']):.4f},{py(item['coverage']):.4f})" for item in points)

    parts = [
        tex_node(x, y + 0.005, w, r"\small\textbf{Coverage by ICC under imbalanced clusters}", align="center"),
        tex_node(x, y + h - 0.038, w * 0.62, r"\scriptsize Data source: 400 simulation replicates per cell; y-axis shows 95\% interval coverage.", align="left"),
    ]
    nominal_y = py(float(spec["nominal_coverage"]))
    center_counts = sorted(data)
    for facet_index, center_count in enumerate(center_counts):
        fx = plot_x + facet_index * (facet_w + gap)
        parts.extend(
            [
                rf"\draw[line width=0.55pt,draw=black!55] ({fx:.4f},{plot_y:.4f}) rectangle ({fx+facet_w:.4f},{plot_y+plot_h:.4f});",
                rf"\draw[line width=0.75pt,draw=orange!85!black] ({fx:.4f},{nominal_y:.4f}) -- ({fx+facet_w:.4f},{nominal_y:.4f});",
                tex_node(fx, plot_y - 0.032, facet_w, rf"\footnotesize\textbf{{G={center_count}}}", align="center"),
            ]
        )
        for tick, label in [(0.50, "0.50"), (0.75, "0.75"), (0.95, "0.95"), (1.00, "1.00")]:
            ty = py(tick)
            parts.append(rf"\draw[line width=0.35pt,draw=black!22] ({fx:.4f},{ty:.4f}) -- ({fx+facet_w:.4f},{ty:.4f});")
            if facet_index == 0:
                parts.append(tex_node(fx - 0.038, ty - 0.008, 0.032, rf"\scriptsize {label}", align="right"))
        for rho, label in [(0.0, "0"), (0.1, ".1"), (0.3, ".3"), (0.5, ".5")]:
            tx = px(facet_index, rho)
            parts.extend(
                [
                    rf"\draw[line width=0.4pt,draw=black!45] ({tx:.4f},{plot_y+plot_h:.4f}) -- ({tx:.4f},{plot_y+plot_h+0.008:.4f});",
                    tex_node(tx - 0.011, plot_y + plot_h + 0.014, 0.030, rf"\scriptsize {label}", align="center"),
                ]
            )
        for method in spec["methods"]:
            points = data[center_count][method["id"]]
            parts.append(rf"\draw[line width=1.15pt,draw={method['color']}] {point_chain(facet_index, points)};")
            for item in points:
                parts.append(rf"\fill[fill={method['color']}] ({px(facet_index, item['rho']):.4f},{py(item['coverage']):.4f}) circle (1.45pt);")
                err = item["mc_se"]
                parts.append(
                    rf"\draw[line width=0.45pt,draw={method['color']}] "
                    rf"({px(facet_index, item['rho']):.4f},{py(item['coverage'] - err):.4f}) -- "
                    rf"({px(facet_index, item['rho']):.4f},{py(item['coverage'] + err):.4f});"
                )

    callout = spec["callout"]
    callout_facet = center_counts.index(int(callout["G"]))
    callout_x = px(callout_facet, float(callout["rho"]))
    callout_y = py(data[int(callout["G"])]["cluster_robust_z"][-1]["coverage"])
    label_x = callout_x - 0.122
    label_y = callout_y - 0.125
    parts.extend(
        [
            rf"\draw[-{{Latex[length=2mm]}},line width=0.75pt,draw=maincolor!80] ({label_x+0.114:.4f},{label_y+0.032:.4f}) -- ({callout_x:.4f},{callout_y:.4f});",
            tex_node(label_x, label_y, 0.142, rf"\scriptsize\textbf{{{tex_escape(callout['label'])}}}\\cluster robust = 0.78", align="left"),
            tex_node(legend_x, plot_y + 0.010, legend_w, r"\footnotesize\textbf{Method key}", align="left"),
        ]
    )
    for idx, method in enumerate(spec["methods"]):
        ly = plot_y + 0.064 + idx * 0.054
        parts.append(rf"\draw[line width=1.4pt,draw={method['color']}] ({legend_x:.4f},{ly:.4f}) -- ({legend_x+0.032:.4f},{ly:.4f});")
        parts.append(rf"\fill[fill={method['color']}] ({legend_x+0.016:.4f},{ly:.4f}) circle (1.5pt);")
        parts.append(tex_node(legend_x + 0.041, ly - 0.015, legend_w - 0.045, rf"\footnotesize {tex_escape(method['label'])}", align="left"))
    parts.extend(
        [
            rf"\draw[line width=1.0pt,draw=orange!85!black] ({legend_x:.4f},{plot_y+0.174:.4f}) -- ({legend_x+0.032:.4f},{plot_y+0.174:.4f});",
            tex_node(legend_x + 0.041, plot_y + 0.159, legend_w - 0.045, r"\footnotesize nominal 0.95", align="left"),
            tex_node(plot_x + facet_w * 1.12, plot_y + plot_h + 0.040, facet_w, r"\footnotesize ICC \(\rho\)", align="center"),
            tex_node(annotation["x"], annotation["y"], annotation["w"], rf"\footnotesize {tex_escape(spec['annotation'])}"),
            tex_node(caption["x"], caption["y"], caption["w"], rf"\scriptsize {tex_escape(spec['caption'])}"),
        ]
    )
    return "\n".join(parts)


def emit_figure(spec: dict[str, Any], layout: dict[str, Any], asset_map: dict[str, str]) -> str:
    if spec.get("dominant_object") == "negative_evidence_plot":
        return emit_negative_evidence_plot(spec, layout, asset_map)
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


def emit_negative_evidence_plot(spec: dict[str, Any], layout: dict[str, Any], asset_map: dict[str, str]) -> str:
    primary = layout["resolved_primary_object_geometry"]
    annotation = layout["resolved_supporting_object_geometry"]["annotation"]
    caption = layout["resolved_supporting_object_geometry"]["caption"]
    asset = asset_map[spec["asset"]]
    plot_x = primary["x"] + 0.148
    plot_y = primary["y"] + 0.078
    plot_h = primary["h"] * 0.642
    ymin = 0.45
    ymax = 1.00

    def py(coverage: float) -> float:
        return plot_y + (1.0 - (coverage - ymin) / (ymax - ymin)) * plot_h

    parts = [
        tex_node(primary["x"], primary["y"], primary["w"], rf"\includegraphics[width={primary['w']:.4f}\paperwidth,height={primary['h']:.4f}\paperheight,keepaspectratio]{{{asset}}}", align="center"),
        rf"\draw[line width=0.7pt,draw=black!62] ({plot_x:.4f},{plot_y:.4f}) -- ({plot_x:.4f},{plot_y+plot_h:.4f});",
    ]
    for tick, label in [(0.50, "0.50"), (0.75, "0.75"), (0.95, "0.95"), (1.00, "1.00")]:
        ty = py(tick)
        parts.extend(
            [
                rf"\draw[line width=0.55pt,draw=black!62] ({plot_x-0.006:.4f},{ty:.4f}) -- ({plot_x+0.006:.4f},{ty:.4f});",
                tex_node(plot_x - 0.050, ty - 0.010, 0.040, rf"\scriptsize {label}", align="right"),
            ]
        )
    parts.extend(
        [
            tex_node(plot_x - 0.072, plot_y + plot_h + 0.012, 0.066, r"\scriptsize coverage", align="right"),
            tex_node(annotation["x"], annotation["y"], annotation["w"], rf"\footnotesize {tex_escape(spec['annotation'])}"),
            tex_node(caption["x"], caption["y"], caption["w"], rf"\scriptsize {tex_escape(spec['caption'])}"),
        ]
    )
    return "\n".join(parts)


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
    factor_x = x + 0.020
    hierarchy_x = x + w * 0.315
    proc_x = x + w * 0.575
    endpoint_x = x + w * 0.785
    top = y + 0.030
    center_y = y + h * 0.430
    parts = [
        tex_node(factor_x, top, 0.205, r"\footnotesize\textbf{DGP stress grid}", align="left"),
        tex_node(hierarchy_x - 0.018, top, 0.205, r"\footnotesize\textbf{Center hierarchy}", align="center"),
        tex_node(proc_x - 0.018, top, 0.195, r"\footnotesize\textbf{Interval procedures}", align="center"),
        tex_node(endpoint_x - 0.006, top, 0.170, r"\footnotesize\textbf{Endpoints}", align="center"),
    ]
    for idx, factor in enumerate(spec["design_factors"]):
        fy = y + 0.112 + idx * 0.078
        parts.extend(
            [
                rf"\fill[fill=maincolor!75] ({factor_x:.4f},{fy+0.006:.4f}) circle (2.1pt);",
                tex_node(factor_x + 0.015, fy - 0.004, 0.205, rf"\scriptsize {factor}", align="left"),
            ]
        )
    parts.extend(
        [
            rf"\draw[line width=0.8pt,draw=maincolor!60] ({hierarchy_x+0.042:.4f},{center_y-0.088:.4f}) ellipse (0.056 and 0.076);",
            rf"\draw[line width=0.8pt,draw=maincolor!60] ({hierarchy_x+0.042:.4f},{center_y+0.086:.4f}) ellipse (0.056 and 0.076);",
            tex_node(hierarchy_x - 0.026, center_y + 0.170, 0.160, r"\scriptsize Subject records nested inside each center; 400 reps per cell", align="center"),
        ]
    )
    for base_y in [center_y - 0.088, center_y + 0.086]:
        for offset in [-0.024, 0.0, 0.024]:
            parts.append(rf"\fill[fill=teal!70!black] ({hierarchy_x+0.042+offset:.4f},{base_y+0.021:.4f}) circle (1.6pt);")
            parts.append(rf"\fill[fill=red!70!black] ({hierarchy_x+0.042+offset:.4f},{base_y-0.020:.4f}) circle (1.6pt);")
    for idx, procedure in enumerate(spec["procedures"]):
        py = y + 0.145 + idx * 0.140
        parts.append(rf"\draw[line width=0.9pt,draw=maincolor!75] ({proc_x:.4f},{py:.4f}) -- ({proc_x+0.148:.4f},{py:.4f});")
        parts.append(rf"\fill[fill=white,draw=maincolor!75,line width=0.8pt] ({proc_x+0.074:.4f},{py:.4f}) circle (8.0pt);")
        parts.append(tex_node(proc_x + 0.006, py + 0.020, 0.142, rf"\scriptsize {tex_escape(procedure)}", align="center"))
    for idx, endpoint in enumerate(spec["endpoints"]):
        ey = y + 0.118 + idx * 0.087
        parts.append(rf"\draw[line width=1.1pt,draw=orange!80!black] ({endpoint_x:.4f},{ey:.4f}) -- ({endpoint_x+0.030:.4f},{ey:.4f});")
        parts.append(rf"\draw[line width=0.55pt,draw=black!50] ({endpoint_x:.4f},{ey-0.012:.4f}) -- ({endpoint_x:.4f},{ey+0.012:.4f});")
        parts.append(tex_node(endpoint_x + 0.036, ey - 0.020, 0.172, rf"\tiny {tex_escape(endpoint)}", align="left"))
    mid_y = center_y
    parts.extend([
        rf"\StageThreeConnector{{{factor_x+0.220:.4f}}}{{{mid_y:.4f}}}{{{hierarchy_x-0.004:.4f}}}{{{mid_y:.4f}}};",
        tex_node(factor_x + 0.224, mid_y + 0.018, 0.078, r"\scriptsize generates", align="center"),
        rf"\StageThreeConnector{{{hierarchy_x+0.185:.4f}}}{{{mid_y:.4f}}}{{{proc_x-0.018:.4f}}}{{{mid_y:.4f}}};",
        tex_node(hierarchy_x + 0.150, mid_y + 0.018, 0.082, r"\scriptsize estimates", align="center"),
        rf"\StageThreeConnector{{{proc_x+0.145:.4f}}}{{{mid_y:.4f}}}{{{endpoint_x-0.010:.4f}}}{{{mid_y:.4f}}};",
        tex_node(proc_x + 0.148, mid_y + 0.018, 0.082, r"\scriptsize evaluates", align="center"),
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
    evidence_x = x + 0.015
    strategy_x = x + w * 0.295
    comparator_x = x + w * 0.630
    decision_x = x + w * 0.855
    mid_y = y + h * 0.395
    parts = [
        tex_node(evidence_x, y + 0.020, 0.210, r"\footnotesize\textbf{Failure evidence}", align="left"),
        tex_node(evidence_x, y + 0.085, 0.218, rf"\scriptsize {tex_escape(spec['current_limit'])}", align="left"),
        rf"\draw[line width=1.1pt,draw=red!70!black] ({evidence_x:.4f},{mid_y+0.055:.4f}) -- ({evidence_x+0.180:.4f},{mid_y+0.055:.4f});",
        rf"\draw[line width=1.1pt,draw=orange!80!black] ({evidence_x:.4f},{mid_y+0.018:.4f}) -- ({evidence_x+0.180:.4f},{mid_y+0.018:.4f});",
        rf"\draw[line width=1.1pt,draw=teal!70!black] ({evidence_x:.4f},{mid_y-0.018:.4f}) -- ({evidence_x+0.180:.4f},{mid_y-0.018:.4f});",
        tex_node(evidence_x + 0.010, mid_y + 0.073, 0.185, r"\scriptsize coverage shortfall at high ICC", align="left"),
        tex_node(strategy_x, y + 0.020, 0.210, r"\footnotesize\textbf{Manipulate sampling}", align="center"),
    ]
    for idx, strategy in enumerate(spec["strategy_variation"]):
        sy = y + 0.110 + idx * 0.076
        parts.append(rf"\draw[line width=0.9pt,draw=maincolor!70] ({strategy_x:.4f},{mid_y:.4f}) -- ({strategy_x+0.080:.4f},{sy+0.010:.4f});")
        parts.append(rf"\fill[fill=white,draw=maincolor!70,line width=0.85pt] ({strategy_x+0.102:.4f},{sy+0.010:.4f}) circle (7.0pt);")
        parts.append(tex_node(strategy_x + 0.122, sy - 0.008, 0.128, rf"\scriptsize {tex_escape(strategy)}", align="left"))
    parts.append(tex_node(comparator_x, y + 0.020, 0.180, r"\footnotesize\textbf{Comparator arms}", align="center"))
    for idx, comparator in enumerate(spec["comparator_setup"]):
        cy = y + 0.148 + idx * 0.112
        parts.append(rf"\draw[line width=0.9pt,draw=teal!65!black] ({comparator_x:.4f},{mid_y:.4f}) -- ({comparator_x+0.060:.4f},{cy:.4f});")
        parts.append(rf"\draw[line width=1.1pt,draw=teal!65!black] ({comparator_x+0.060:.4f},{cy:.4f}) -- ({comparator_x+0.182:.4f},{cy:.4f});")
        parts.append(tex_node(comparator_x + 0.066, cy + 0.010, 0.116, rf"\scriptsize {tex_escape(comparator)}", align="center"))
    parts.extend(
        [
            tex_node(decision_x - 0.005, y + 0.020, 0.150, r"\footnotesize\textbf{Decision rule}", align="center"),
            rf"\draw[line width=0.9pt,draw=orange!85!black] ({decision_x+0.070:.4f},{mid_y-0.070:.4f}) -- ({decision_x+0.140:.4f},{mid_y:.4f}) -- ({decision_x+0.070:.4f},{mid_y+0.070:.4f}) -- ({decision_x:.4f},{mid_y:.4f}) -- cycle;",
            tex_node(decision_x + 0.018, mid_y - 0.018, 0.104, r"\scriptsize go/no-go", align="center"),
            tex_node(decision_x - 0.002, mid_y + 0.090, 0.148, rf"\scriptsize {tex_escape(spec['decision_criterion'])}", align="left"),
        ]
    )
    parts.extend([
        rf"\StageThreeConnector{{{evidence_x+0.198:.4f}}}{{{mid_y:.4f}}}{{{strategy_x-0.020:.4f}}}{{{mid_y:.4f}}};",
        tex_node(evidence_x + 0.204, mid_y - 0.066, 0.075, r"\scriptsize motivates", align="center"),
        rf"\StageThreeConnector{{{strategy_x+0.255:.4f}}}{{{mid_y:.4f}}}{{{comparator_x-0.016:.4f}}}{{{mid_y:.4f}}};",
        rf"\StageThreeConnector{{{comparator_x+0.148:.4f}}}{{{mid_y:.4f}}}{{{decision_x-0.016:.4f}}}{{{mid_y:.4f}}};",
    ])
    annotation = layout["resolved_supporting_object_geometry"]["annotation"]
    parts.append(tex_node(annotation["x"], annotation["y"], annotation["w"], rf"\footnotesize {tex_escape(spec['annotation'])}", align="left"))
    return "\n".join(parts)


def emit_image_panel(spec: dict[str, Any], layout: dict[str, Any], asset_map: dict[str, str]) -> str:
    primary = layout["resolved_primary_object_geometry"]
    labels = spec["panel_labels"]
    assets = [asset_map[item] for item in spec["assets"]]
    gap = 0.010
    panel_w = min((primary["w"] - gap * 3) / 4, 0.170)
    panel_h = panel_w * SLIDE_W / SLIDE_H
    row_x = primary["x"] + (primary["w"] - (panel_w * 4 + gap * 3)) / 2
    y = primary["y"] + 0.048
    parts = []
    for idx, (label, asset) in enumerate(zip(labels, assets)):
        x = row_x + idx * (panel_w + gap)
        parts.append(tex_node(x, y - 0.037, panel_w, rf"\footnotesize\textbf{{{tex_escape(label)}}}", align="center"))
        parts.append(tex_node(x, y, panel_w, rf"\includegraphics[width={panel_w:.4f}\paperwidth,height={panel_h:.4f}\paperheight,keepaspectratio]{{{asset}}}", align="center"))
    roi = spec["same_case_roi_zoom"]["roi_xywh"]
    source_w = spec["same_case_roi_zoom"]["crop_records"][0]["source_image_size"]["w"]
    source_h = spec["same_case_roi_zoom"]["crop_records"][0]["source_image_size"]["h"]
    error_panel_x = row_x + 3 * (panel_w + gap)
    roi_x = error_panel_x + roi["x"] / source_w * panel_w
    roi_y = y + roi["y"] / source_h * panel_h
    roi_w = roi["w"] / source_w * panel_w
    roi_h = roi["h"] / source_h * panel_h
    zoom_y = y + panel_h + 0.030
    zoom_panel_w = 0.098
    zoom_panel_h = zoom_panel_w * SLIDE_W / SLIDE_H
    zoom_gap = 0.020
    zoom_x = primary["x"] + 0.072
    parts.extend(
        [
            rf"\draw[line width=0.9pt,draw=orange!85!black] ({roi_x:.4f},{roi_y:.4f}) rectangle ({roi_x+roi_w:.4f},{roi_y+roi_h:.4f});",
            rf"\StageThreeConnector{{{roi_x+roi_w:.4f}}}{{{roi_y+roi_h:.4f}}}{{{zoom_x+zoom_panel_w*2+zoom_gap*2:.4f}}}{{{zoom_y:.4f}}};",
            tex_node(zoom_x, zoom_y - 0.030, 0.435, r"\footnotesize\textbf{Same-case ROI zoom}", align="left"),
        ]
    )
    for idx, (label, raw) in enumerate(zip(spec["roi_crop_labels"], spec["roi_crop_assets"])):
        zx = zoom_x + idx * (zoom_panel_w + zoom_gap)
        crop_asset = asset_map[f"{raw}#roi_zoom"]
        parts.append(tex_node(zx, zoom_y, zoom_panel_w, rf"\includegraphics[width={zoom_panel_w:.4f}\paperwidth,height={zoom_panel_h:.4f}\paperheight,keepaspectratio]{{{crop_asset}}}", align="center"))
        parts.append(tex_node(zx, zoom_y + zoom_panel_h + 0.008, zoom_panel_w, rf"\scriptsize {tex_escape(label)}", align="center"))
    legend_x = zoom_x + 3 * (zoom_panel_w + zoom_gap) + 0.020
    parts.extend(
        [
            tex_node(legend_x, zoom_y + 0.006, 0.205, r"\footnotesize\textbf{Overlay legend}", align="left"),
            rf"\fill[fill=teal!70!black] ({legend_x+0.010:.4f},{zoom_y+0.060:.4f}) circle (2.4pt);",
            tex_node(legend_x + 0.025, zoom_y + 0.047, 0.145, r"\scriptsize TP: overlap", align="left"),
            rf"\fill[fill=red!70!black] ({legend_x+0.010:.4f},{zoom_y+0.105:.4f}) circle (2.4pt);",
            tex_node(legend_x + 0.025, zoom_y + 0.092, 0.145, r"\scriptsize FP: prediction only", align="left"),
            rf"\fill[fill=orange!85!black] ({legend_x+0.010:.4f},{zoom_y+0.150:.4f}) circle (2.4pt);",
            tex_node(legend_x + 0.025, zoom_y + 0.137, 0.145, r"\scriptsize FN: missed GT", align="left"),
        ]
    )
    annotation = layout["resolved_supporting_object_geometry"]["caption"]
    parts.append(tex_node(annotation["x"], annotation["y"], annotation["w"], rf"\scriptsize {tex_escape(spec['annotation'])}", align="center"))
    return "\n".join(parts)


def emit_frame(spec: dict[str, Any], layout: dict[str, Any], asset_map: dict[str, str]) -> str:
    if spec["content_kind"] == "equation":
        body = emit_equation(spec, layout)
    elif spec["content_kind"] == "result_figure":
        body = emit_result_figure(spec, layout)
    elif spec["content_kind"] == "figure":
        body = emit_figure(spec, layout, asset_map)
    elif spec["content_kind"] == "image_panel":
        body = emit_image_panel(spec, layout, asset_map)
    else:
        body = emit_flow(spec, layout)
    if transition := spec.get("storyline_transition"):
        audience_text = transition.get("audience_text") or transition["relation_to_previous"]
        compact = transition.get("cue_variant") == "compact"
        cue_y = 0.1580 if compact else 0.1580
        cue_y2 = 0.2020 if compact else 0.2140
        label_w = 0.1500 if compact else 0.1850
        text_x = 0.2380 if compact else 0.2700
        text_w = 0.6670 if compact else 0.6350
        cue = (
            rf"\StageThreePanel{{0.0600}}{{0.1450}}{{0.9400}}{{{cue_y2:.4f}}};"
            "\n"
            rf"\StageThreeNode{{0.0780}}{{{cue_y:.4f}}}{{{label_w:.4f}}}{{left}}{{\scriptsize\textbf{{Workstream transition}}}};"
            "\n"
            rf"\StageThreeNode{{{text_x:.4f}}}{{{cue_y:.4f}}}{{{text_w:.4f}}}{{left}}{{\scriptsize\textbf{{{tex_escape(transition['label'])}}}: {tex_escape(audience_text)}.}};"
        )
        body = cue + "\n" + body
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


def detect_colored_roi(path: Path, *, pad: int = 42) -> dict[str, int]:
    from PIL import Image

    image = Image.open(path).convert("RGB")
    xs: list[int] = []
    ys: list[int] = []
    for py in range(image.height):
        for px in range(image.width):
            red, green, blue = image.getpixel((px, py))
            if max(red, green, blue) > 40 and max(red, green, blue) - min(red, green, blue) > 20:
                xs.append(px)
                ys.append(py)
    if not xs or not ys:
        raise RuntimeError(f"cannot locate colored error ROI in {path}")
    left = max(0, min(xs) - pad)
    right = min(image.width, max(xs) + 1 + pad)
    top = max(0, min(ys) - pad)
    bottom = min(image.height, max(ys) + 1 + pad)
    width = right - left
    height = bottom - top
    if width > height:
        extra = width - height
        top = max(0, top - extra // 2)
        bottom = min(image.height, bottom + extra - extra // 2)
    elif height > width:
        extra = height - width
        left = max(0, left - extra // 2)
        right = min(image.width, right + extra - extra // 2)
    return {"x": left, "y": top, "w": right - left, "h": bottom - top, "source_w": image.width, "source_h": image.height}


def classify_medical_error_pixel(pixel: tuple[int, int, int]) -> str | None:
    red, green, blue = pixel
    if max(pixel) < 70 or max(pixel) - min(pixel) <= 18:
        return None
    if green > red + 18 and green > blue + 18:
        return "tp"
    if red > 95 and red > green + 18 and red > blue + 18:
        if green >= 72 and blue <= 105 and red - green <= 88:
            return "fn"
        return "fp"
    return None


def classified_medical_error_points(error_image: Any, roi: dict[str, int]) -> dict[str, set[tuple[int, int]]]:
    points: dict[str, set[tuple[int, int]]] = {"tp": set(), "fp": set(), "fn": set()}
    for py in range(roi["y"], roi["y"] + roi["h"]):
        for px in range(roi["x"], roi["x"] + roi["w"]):
            label = classify_medical_error_pixel(error_image.getpixel((px, py)))
            if label:
                points[label].add((px, py))
    return points


def semantic_medical_overlay(source: Any, points: dict[str, set[tuple[int, int]]], visible_classes: set[str]) -> Any:
    from PIL import Image

    base = source.convert("RGBA")
    overlay = Image.new("RGBA", base.size, (0, 0, 0, 0))
    overlay_pixels = overlay.load()
    radius = 3
    for class_name in visible_classes:
        color = MEDICAL_ERROR_COLORS[class_name]
        for px, py in points[class_name]:
            for dx in range(-radius, radius + 1):
                for dy in range(-radius, radius + 1):
                    if dx * dx + dy * dy > radius * radius:
                        continue
                    tx = px + dx
                    ty = py + dy
                    if 0 <= tx < source.width and 0 <= ty < source.height:
                        overlay_pixels[tx, ty] = (*color, 218)
    return Image.alpha_composite(base, overlay).convert("RGB")


def build_medical_semantic_display_assets(spec: dict[str, Any], asset_dir: Path, asset_map: dict[str, str], roi: dict[str, int]) -> dict[str, dict[str, Any]]:
    from PIL import Image

    assets = spec.get("assets", [])
    labels = [label.lower() for label in spec.get("panel_labels", [])]
    by_label = dict(zip(labels, assets))
    gt_raw = by_label.get("gt")
    pred_raw = by_label.get("prediction")
    error_raw = spec.get("roi_source_asset")
    if not gt_raw or not pred_raw or not error_raw:
        return {}
    error_image = Image.open(REPO_ROOT / error_raw).convert("RGB")
    points = classified_medical_error_points(error_image, roi)
    display_specs = {
        gt_raw: {"classes": {"tp", "fn"}, "role": "gt_with_overlap_and_missed_gt"},
        pred_raw: {"classes": {"tp", "fp"}, "role": "prediction_with_overlap_and_prediction_only"},
        error_raw: {"classes": {"tp", "fp", "fn"}, "role": "error_classification_overlay"},
    }
    display_records: dict[str, dict[str, Any]] = {}
    for raw, contract in display_specs.items():
        visible = {class_name for class_name in contract["classes"] if points[class_name]}
        if not visible:
            continue
        source = Image.open(REPO_ROOT / raw).convert("RGB")
        target = asset_dir / f"{Path(raw).stem}_semantic_overlay.png"
        semantic_medical_overlay(source, points, visible).save(target)
        asset_map[raw] = f"stage3_assets/{target.name}"
        display_records[raw] = {
            "display_asset": asset_map[raw],
            "semantic_overlay": True,
            "overlay_role": contract["role"],
            "visible_error_classes": sorted(visible),
        }
    return display_records


def crop_same_case_roi(spec: dict[str, Any], asset_dir: Path, asset_map: dict[str, str]) -> None:
    from PIL import Image

    roi_source = REPO_ROOT / spec["roi_source_asset"]
    roi = detect_colored_roi(roi_source)
    display_records = build_medical_semantic_display_assets(spec, asset_dir, asset_map, roi)
    crop_records = []
    for raw in spec["roi_crop_assets"]:
        display_source = asset_dir / Path(asset_map[raw]).name
        target = asset_dir / f"{display_source.stem}_roi_zoom.png"
        image = Image.open(display_source).convert("RGB")
        box = (roi["x"], roi["y"], roi["x"] + roi["w"], roi["y"] + roi["h"])
        resampling = getattr(getattr(Image, "Resampling", Image), "BICUBIC")
        image.crop(box).resize((320, 320), resampling).save(target)
        crop_key = f"{raw}#roi_zoom"
        asset_map[crop_key] = f"stage3_assets/{target.name}"
        crop_records.append({
            "source_asset": raw,
            "display_asset": asset_map[raw],
            "zoom_asset": asset_map[crop_key],
            "roi_source_asset": spec["roi_source_asset"],
            "roi_xywh": {key: roi[key] for key in ["x", "y", "w", "h"]},
            "source_image_size": {"w": roi["source_w"], "h": roi["source_h"]},
            "same_case_coordinate_space": True,
            **display_records.get(raw, {}),
        })
    spec["same_case_roi_zoom"] = {
        "roi_source_asset": spec["roi_source_asset"],
        "roi_xywh": {key: roi[key] for key in ["x", "y", "w", "h"]},
        "crop_records": crop_records,
    }


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
        if spec.get("roi_crop_assets"):
            crop_same_case_roi(spec, asset_dir, asset_map)
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
    implementation_commit: str | None = None,
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
        "review_kind": f"{TASK_KEY}-stage3-cuhk-scientific-layout-item-page-review",
        "privacy_policy": "PUBLIC_SAFE_ONLY",
        "prompt_version": "ai-bridge.visual-review.v1",
        "external_upload_authorization": "",
        "rubric": {
            "instructions": (
                "You are reviewing rendered pixels from the Stage 3 exact-CUHK scientific layout integration deck. "
                "Judge each content page independently at item/page level. PASS for an item only if the visible page reaches a mature doctoral research-group meeting or strong conference-talk bar for its page job. "
                "Check that the CUHK Beamer identity is visible; the main scientific object is prominent and projection-readable; math is genuinely typeset rather than source-like text; result figures use readable native axes, ticks, facets, method legend, nominal line, and callout; experiment design shows typed hierarchy, DGP factors, procedures, endpoints, and directional scientific relations; medical comparison uses same-case ROI crop/zoom imagery with adjacent TP/FP/FN legend; discussion/next-experiment content shows evidence-to-decision research reasoning rather than generic future-work boxes. "
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
            "implementation_commit": implementation_commit,
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


def generate(
    out_dir: Path,
    *,
    write_result_visual_inputs: bool = False,
    task_key: str = DEFAULT_TASK_KEY,
    implementation_commit: str | None = None,
) -> dict[str, Any]:
    global TASK_KEY
    TASK_KEY = task_key
    out_dir = out_dir.resolve()
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
                "executable_layout_family": layout["executable_layout_family"],
                "job_specific_runtime_contract": layout["job_specific_runtime_contract"],
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
        "implementation_commit": implementation_commit,
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
        implementation_commit=implementation_commit,
    )
    (out_dir / "visual_inputs.json").write_text(json.dumps(visual_inputs, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    if write_result_visual_inputs:
        result_visual_review_dir = REPO_ROOT / "results" / task_key / "visual_review"
        result_visual_review_dir.mkdir(parents=True, exist_ok=True)
        (result_visual_review_dir / "visual_inputs.json").write_text(json.dumps(visual_inputs, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out-dir", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--write-result-visual-inputs", action="store_true")
    parser.add_argument("--task-key", default=DEFAULT_TASK_KEY)
    parser.add_argument("--implementation-commit")
    args = parser.parse_args()
    manifest = generate(
        args.out_dir,
        write_result_visual_inputs=args.write_result_visual_inputs,
        task_key=args.task_key,
        implementation_commit=args.implementation_commit,
    )
    print(json.dumps({"status": manifest["mechanical_qa"]["status"], "out_dir": rel(args.out_dir), "render_status": manifest["render_status"]["status"]}, indent=2))
    return 0 if manifest["mechanical_qa"]["status"] == "MECHANICAL_PASS" else 2


if __name__ == "__main__":
    raise SystemExit(main())
