#!/usr/bin/env python3
"""Generate reference-calibrated research slide candidate previews."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import sys
from pathlib import Path
from typing import Any

from PIL import Image, ImageDraw, ImageFont

import select_reference_compositions


SHARED = Path(__file__).resolve().parents[1]
REPO_ROOT = Path(__file__).resolve().parents[6]
REFERENCES = SHARED / "references"
COMPOSITION_INDEX = REFERENCES / "research_slide_composition_index.json"

WIDTH = 1600
HEIGHT = 900
CANVAS_BG = (252, 252, 250)
INK = (23, 28, 38)
MUTED = (82, 92, 105)
LINE = (188, 196, 208)
ACCENT = (0, 105, 112)
ACCENT_SOFT = (225, 244, 245)
SECONDARY = (63, 69, 120)
WARNING = (174, 94, 25)
STOPWORDS = {
    "and",
    "are",
    "but",
    "can",
    "for",
    "from",
    "into",
    "the",
    "this",
    "that",
    "with",
    "without",
}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def payload_sha(request: dict[str, Any]) -> str:
    slots = []
    for slot in request["content_slots"]:
        item = dict(slot)
        asset = item.get("asset_path")
        if asset:
            item["asset_sha256"] = sha256(REPO_ROOT / asset)
        slots.append(item)
    return hashlib.sha256(json.dumps(slots, sort_keys=True).encode("utf-8")).hexdigest()


def load_font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/dejavu/DejaVuSans.ttf",
    ]
    for candidate in candidates:
        if Path(candidate).exists():
            return ImageFont.truetype(candidate, size)
    return ImageFont.load_default()


def bbox_px(bbox: dict[str, float]) -> tuple[int, int, int, int]:
    return (round(bbox["x"] * WIDTH), round(bbox["y"] * HEIGHT), round((bbox["x"] + bbox["w"]) * WIDTH), round((bbox["y"] + bbox["h"]) * HEIGHT))


def draw_wrapped(draw: ImageDraw.ImageDraw, text: str, xy: tuple[int, int], max_width: int, font: ImageFont.ImageFont, fill=INK, line_spacing: int = 8) -> None:
    words = text.split()
    lines: list[str] = []
    line = ""
    for word in words:
        trial = f"{line} {word}".strip()
        if draw.textbbox((0, 0), trial, font=font)[2] <= max_width or not line:
            line = trial
        else:
            lines.append(line)
            line = word
    if line:
        lines.append(line)
    x, y = xy
    line_height = draw.textbbox((0, 0), "Ag", font=font)[3] + line_spacing
    for i, value in enumerate(lines):
        draw.text((x, y + i * line_height), value, font=font, fill=fill)


def flatten_on_bg(source: Image.Image, bg=(255, 255, 255)) -> Image.Image:
    image = source.convert("RGBA")
    base = Image.new("RGBA", image.size, bg + (255,))
    base.alpha_composite(image)
    return base.convert("RGB")


def paste_contain(canvas: Image.Image, source: Image.Image, box: tuple[int, int, int, int], bg=(255, 255, 255), crop_top_ratio: float = 0.0) -> None:
    x1, y1, x2, y2 = box
    w, h = x2 - x1, y2 - y1
    region = Image.new("RGB", (w, h), bg)
    image = flatten_on_bg(source, bg)
    if crop_top_ratio > 0:
        top_crop = round(image.height * crop_top_ratio)
        image = image.crop((0, top_crop, image.width, image.height))
    image.thumbnail((w, h), Image.Resampling.LANCZOS)
    px = (w - image.width) // 2
    py = (h - image.height) // 2
    region.paste(image, (px, py))
    canvas.paste(region, (x1, y1))


def paste_cover(canvas: Image.Image, source: Image.Image, box: tuple[int, int, int, int], bg=(255, 255, 255), crop_top_ratio: float = 0.0, anchor_y: float = 0.5) -> None:
    x1, y1, x2, y2 = box
    w, h = x2 - x1, y2 - y1
    image = flatten_on_bg(source, bg)
    if crop_top_ratio > 0:
        top_crop = round(image.height * crop_top_ratio)
        image = image.crop((0, top_crop, image.width, image.height))
    scale = max(w / image.width, h / image.height)
    resized = image.resize((round(image.width * scale), round(image.height * scale)), Image.Resampling.LANCZOS)
    left = max(0, (resized.width - w) // 2)
    top = max(0, round((resized.height - h) * anchor_y))
    cropped = resized.crop((left, top, left + w, top + h))
    canvas.paste(cropped, (x1, y1))


def load_composition_records() -> list[dict[str, Any]]:
    return json.loads(COMPOSITION_INDEX.read_text(encoding="utf-8"))["records"]


def by_reference_id() -> dict[str, dict[str, Any]]:
    return {record["reference_id"]: record for record in load_composition_records()}


def tokens(value: str) -> set[str]:
    return {part.lower() for part in value.replace("/", " ").replace("-", " ").replace("_", " ").split() if len(part) > 2 and part.lower() not in STOPWORDS}


def primary_region(record: dict[str, Any]) -> dict[str, Any]:
    return next(region for region in record["regions"] if region["region_id"] == record["primary_scientific_object_region_id"])


def composition_distance(a: dict[str, Any], b: dict[str, Any]) -> float:
    ap = primary_region(a)["bbox"]
    bp = primary_region(b)["bbox"]
    ac = (ap["x"] + ap["w"] / 2, ap["y"] + ap["h"] / 2)
    bc = (bp["x"] + bp["w"] / 2, bp["y"] + bp["h"] / 2)
    center = abs(ac[0] - bc[0]) + abs(ac[1] - bc[1])
    area = abs(a["primary_object_area_ratio"] - b["primary_object_area_ratio"])
    family = 0.35 if a["layout_family"] != b["layout_family"] else 0
    topology = 0.08 * abs(len(a["regions"]) - len(b["regions"]))
    return round(family + center + area + topology, 4)


def content_modes(record: dict[str, Any]) -> set[str]:
    return {region["content_mode"] for region in record["regions"]}


def is_compatible_source(request: dict[str, Any], record: dict[str, Any]) -> tuple[bool, list[str]]:
    modes = content_modes(record)
    page_function = request["page_function"]
    reasons: list[str] = []
    if page_function == "MEDICAL_IMAGE_COMPARISON":
        if record["page_function"] == "MEDICAL_IMAGE_COMPARISON" and "medical_image" in modes:
            reasons.append("medical_image_comparison_page")
            return True, reasons
        return False, reasons
    if page_function in {"ESTIMATOR", "STATISTICAL_MODEL", "THEOREM", "DERIVATION"}:
        if record["page_function"] in {"ESTIMATOR", "STATISTICAL_MODEL", "THEOREM", "DERIVATION", "BAYESIAN_MODEL"} and "equation" in modes:
            reasons.append("equation_compatible_page")
            return True, reasons
        return False, reasons
    if record["page_function"] == page_function:
        reasons.append("exact_page_function")
        return True, reasons
    requested_modes = {
        "equation"
        if slot["content_type"] == "equation_asset"
        else "medical_image"
        if slot["content_type"] == "image_asset"
        else "figure"
        if slot["content_type"] == "plot_asset"
        else None
        for slot in request["content_slots"]
    }
    requested_modes.discard(None)
    if requested_modes & modes:
        reasons.append("content_mode_overlap")
        return True, reasons
    return False, reasons


def compatible_records(request: dict[str, Any], initial_ids: list[str]) -> list[dict[str, Any]]:
    initial_set = set(initial_ids)
    query_terms = tokens(" ".join([request["page_function"], request["scientific_object"], request.get("evidence_type", "")]))
    scored: list[tuple[int, str, dict[str, Any]]] = []
    for record in load_composition_records():
        compatible, compatibility_reasons = is_compatible_source(request, record)
        if not compatible:
            continue
        score = 0
        if record["reference_id"] in initial_set:
            score += 6
        if record["page_function"] == request["page_function"]:
            score += 20
        if request.get("evidence_type") and str(request["evidence_type"]).lower() in str(record["evidence_type"]).lower():
            score += 8
        record_terms = tokens(" ".join([
            record["page_function"],
            record["scientific_object"],
            record["evidence_type"],
            record["layout_family"],
            " ".join(region["content_mode"] for region in record["regions"]),
        ]))
        score += min(10, len(query_terms & record_terms) * 2)
        modes = content_modes(record)
        if request["page_function"] in {"ESTIMATOR", "STATISTICAL_MODEL", "THEOREM"} and "equation" in modes:
            score += 6
        if request["page_function"] == "MEDICAL_IMAGE_COMPARISON" and "medical_image" in modes:
            score += 6
        score += len(compatibility_reasons)
        if score > 0:
            scored.append((score, record["reference_id"], record))
    scored.sort(key=lambda item: (-item[0], item[1]))
    return [record for _, _, record in scored]


def choose_sources(request: dict[str, Any]) -> tuple[list[dict[str, Any]], dict[str, dict[str, Any]]]:
    raw_retrieved = select_reference_compositions.select(
        request.get("page_function"),
        request.get("evidence_type"),
        request.get("scientific_object"),
        8,
    )
    initial_ids = [item["reference_id"] for item in raw_retrieved]
    pool = compatible_records(request, initial_ids)
    if not pool:
        raise RuntimeError(f"{request['request_id']}: no compatible composition records")
    first = pool[0]
    second = next((record for record in pool[1:] if record["layout_family"] != first["layout_family"]), pool[1] if len(pool) > 1 else first)
    remaining = [record for record in pool if record["reference_id"] not in {first["reference_id"], second["reference_id"]}]
    third = max(remaining, key=lambda record: composition_distance(first, record) + composition_distance(second, record)) if remaining else second
    retrieved = []
    for record in pool[:8]:
        primary = primary_region(record)
        compatible, reasons = is_compatible_source(request, record)
        retrieved.append({
            "reference_id": record["reference_id"],
            "source_id": record["source_id"],
            "page_function": record["page_function"],
            "evidence_type": record["evidence_type"],
            "scientific_object": record["scientific_object"],
            "layout_family": record["layout_family"],
            "reading_flow": record["reading_flow"],
            "primary_object_area_ratio": record["primary_object_area_ratio"],
            "primary_bbox": primary["bbox"],
            "compatible": compatible,
            "compatibility_reasons": reasons,
        })
    return retrieved, {
        "reference_faithful": first,
        "alternative_composition": second,
        "controlled_wildcard": third,
    }


def title_slot(request: dict[str, Any]) -> dict[str, Any]:
    return next(slot for slot in request["content_slots"] if slot["role"] == "title")


def slots_by_type(request: dict[str, Any], *content_types: str) -> list[dict[str, Any]]:
    return [slot for slot in request["content_slots"] if slot["content_type"] in content_types]


def text_slot(request: dict[str, Any], role: str) -> dict[str, Any] | None:
    return next((slot for slot in request["content_slots"] if slot["role"] == role and slot.get("text")), None)


def round_bbox(bbox: dict[str, float]) -> dict[str, float]:
    return {key: round(float(bbox[key]), 4) for key in ["x", "y", "w", "h"]}


def clamp_bbox(bbox: dict[str, float]) -> dict[str, float]:
    x = min(max(float(bbox["x"]), 0.02), 0.96)
    y = min(max(float(bbox["y"]), 0.02), 0.94)
    w = min(max(float(bbox["w"]), 0.04), 0.98 - x)
    h = min(max(float(bbox["h"]), 0.04), 0.98 - y)
    return round_bbox({"x": x, "y": y, "w": w, "h": h})


def bbox_inside(parent: dict[str, float], x: float, y: float, w: float, h: float) -> dict[str, float]:
    return clamp_bbox({
        "x": float(parent["x"]) + float(parent["w"]) * x,
        "y": float(parent["y"]) + float(parent["h"]) * y,
        "w": float(parent["w"]) * w,
        "h": float(parent["h"]) * h,
    })


def expand_around_center(bbox: dict[str, float], min_w: float, min_h: float, max_w: float = 0.88, max_h: float = 0.34) -> dict[str, float]:
    cx = float(bbox["x"]) + float(bbox["w"]) / 2
    cy = float(bbox["y"]) + float(bbox["h"]) / 2
    w = min(max(float(bbox["w"]), min_w), max_w)
    h = min(max(float(bbox["h"]), min_h), max_h)
    return clamp_bbox({"x": cx - w / 2, "y": cy - h / 2, "w": w, "h": h})


def split_horizontal(bbox: dict[str, float], count: int, gap: float | None = None) -> list[dict[str, float]]:
    gap = min(0.026, float(bbox["w"]) * 0.045) if gap is None else gap
    width = (float(bbox["w"]) - gap * (count - 1)) / count
    return [clamp_bbox({"x": float(bbox["x"]) + i * (width + gap), "y": float(bbox["y"]), "w": width, "h": float(bbox["h"])}) for i in range(count)]


def source_region(source: dict[str, Any], *, role: str | None = None, content_mode: str | None = None) -> dict[str, Any] | None:
    for region in source["regions"]:
        if role and region["role"] != role:
            continue
        if content_mode and region["content_mode"] != content_mode:
            continue
        return region
    return None


def slot_mode(slot: dict[str, Any]) -> str:
    if slot["content_type"] == "equation_asset":
        return "equation"
    if slot["content_type"] == "image_asset":
        return "medical_image"
    if slot["content_type"] == "plot_asset":
        return "figure"
    if slot["content_type"] == "legend":
        return "legend"
    if slot["content_type"] == "caption":
        return "caption"
    return "text"


def title_region_from_source(source: dict[str, Any], primary: dict[str, Any]) -> tuple[dict[str, float], dict[str, Any], str, str]:
    title = source_region(source, role="title")
    if title:
        bbox = dict(title["bbox"])
        if float(bbox["w"]) < 0.78:
            bbox["w"] = min(0.90, 0.98 - float(bbox["x"]))
        return clamp_bbox(bbox), title, "scale", "scaled the source title band into a readable presentation title span"
    primary_bbox = primary["bbox"]
    derived = clamp_bbox({
        "x": primary_bbox["x"],
        "y": max(0.04, float(primary_bbox["y"]) - 0.08),
        "w": min(float(primary_bbox["w"]), 0.86),
        "h": 0.08,
    })
    return derived, primary, "translate", "derived a title band from the source primary object top edge because the source record has no title region"


def content_bbox_after_title(primary_bbox: dict[str, float], title_bbox: dict[str, float]) -> dict[str, float]:
    bbox = dict(primary_bbox)
    min_y = float(title_bbox["y"]) + float(title_bbox["h"]) + 0.05
    if float(bbox["y"]) < min_y:
        delta = min_y - float(bbox["y"])
        bbox["y"] = min_y
        bbox["h"] = max(0.16, float(bbox["h"]) - delta)
    return clamp_bbox(bbox)


def add_region(
    regions: list[dict[str, Any]],
    transfers: list[dict[str, Any]],
    source: dict[str, Any],
    source_item: dict[str, Any],
    region_id: str,
    role: str,
    bbox: dict[str, float],
    slot_id: str,
    mode: str,
    adaptation_type: str,
    adaptation_reason: str,
) -> None:
    candidate_bbox = clamp_bbox(bbox)
    regions.append({"region_id": region_id, "role": role, "bbox": candidate_bbox, "content_mode": mode, "content_slot_id": slot_id})
    transfers.append({
        "source_reference_id": source["reference_id"],
        "source_region_id": source_item["region_id"],
        "source_role": source_item["role"],
        "source_bbox": source_item["bbox"],
        "candidate_region_id": region_id,
        "candidate_content_slot_id": slot_id,
        "candidate_bbox": candidate_bbox,
        "adaptation_type": adaptation_type,
        "adaptation_reason": adaptation_reason,
    })


def derived_estimator_regions(request: dict[str, Any], strategy: str, source: dict[str, Any]) -> tuple[list[dict[str, Any]], list[dict[str, Any]], str, str]:
    primary = primary_region(source)
    source_equation = source_region(source, content_mode="equation") or primary
    source_secondary = source_region(source, role="secondary_scientific_object") or primary
    title_bbox, title_source, title_adaptation, title_reason = title_region_from_source(source, primary)
    content_box = content_bbox_after_title(primary["bbox"], title_bbox)
    regions: list[dict[str, Any]] = []
    transfers: list[dict[str, Any]] = []
    add_region(regions, transfers, source, title_source, "title", "title", title_bbox, "title", "text", title_adaptation, title_reason)
    layout_family = source["layout_family"]
    reading_flow = source["reading_flow"]
    if strategy == "reference_faithful":
        equation_bbox = expand_around_center(source_equation["bbox"], 0.52, 0.16)
        annotation_bbox = bbox_inside(equation_bbox, 0.10, 1.32, 0.80, 0.52)
        caption_bbox = bbox_inside(content_box, 0.10, 1.10, 0.80, 0.15)
        add_region(regions, transfers, source, source_equation, "equation", "primary_scientific_object", equation_bbox, "equation", "equation", "scale", "scaled the selected source equation region around its original center for legible preview math")
        add_region(regions, transfers, source, source_equation, "annotation", "annotation", annotation_bbox, "annotation", "text", "translate", "placed annotation below the source-derived equation centerline")
        add_region(regions, transfers, source, primary, "caption", "caption", caption_bbox, "caption", "caption", "translate", "placed caption beneath the source primary object span")
    elif strategy == "alternative_composition":
        equation_bbox = expand_around_center(source_equation["bbox"], 0.50, 0.17)
        annotation_bbox = clamp_bbox({
            "x": max(float(source_secondary["bbox"]["x"]), float(equation_bbox["x"]) + float(equation_bbox["w"]) + 0.04),
            "y": min(float(source_secondary["bbox"]["y"]) + 0.03, 0.62),
            "w": min(max(float(source_secondary["bbox"]["w"]) * 0.78, 0.22), 0.32),
            "h": min(max(float(source_secondary["bbox"]["h"]) * 0.36, 0.14), 0.22),
        })
        caption_bbox = bbox_inside(primary["bbox"], 0.02, 1.03, 0.70, 0.14)
        add_region(regions, transfers, source, source_equation, "equation", "primary_scientific_object", equation_bbox, "equation", "equation", "scale", "scaled the source equation region while preserving its side of the split layout")
        add_region(regions, transfers, source, source_secondary, "annotation", "annotation", annotation_bbox, "annotation", "text", "translate", "translated the source secondary object lane into a compact explanatory annotation")
        add_region(regions, transfers, source, primary, "caption", "caption", caption_bbox, "caption", "caption", "translate", "anchored caption to the lower edge of the source primary composition")
    else:
        layout_family = f"{source['layout_family']}-reordered-callout"
        reading_flow = f"{source['reading_flow']}-reordered-callout"
        equation_bbox = bbox_inside(content_box, 0.12, 0.08, 0.70, 0.34)
        annotation_bbox = bbox_inside(content_box, 0.52, 0.56, 0.38, 0.30)
        caption_bbox = bbox_inside(content_box, 0.12, 0.92, 0.56, 0.16)
        add_region(regions, transfers, source, primary, "equation", "primary_scientific_object", equation_bbox, "equation", "equation", "reorder", "reordered the source primary object into an equation-first focus with a lower-right callout")
        add_region(regions, transfers, source, primary, "annotation", "annotation", annotation_bbox, "annotation", "text", "split", "split the source primary object area to create a secondary explanatory callout")
        add_region(regions, transfers, source, primary, "caption", "caption", caption_bbox, "caption", "caption", "translate", "translated caption to the source primary lower edge after the reorder")
    return regions, transfers, layout_family, reading_flow


def derived_medical_regions(request: dict[str, Any], strategy: str, source: dict[str, Any]) -> tuple[list[dict[str, Any]], list[dict[str, Any]], str, str]:
    primary = primary_region(source)
    legend = source_region(source, role="legend") or primary
    title_bbox, title_source, title_adaptation, title_reason = title_region_from_source(source, primary)
    content_box = content_bbox_after_title(primary["bbox"], title_bbox)
    regions: list[dict[str, Any]] = []
    transfers: list[dict[str, Any]] = []
    add_region(regions, transfers, source, title_source, "title", "title", title_bbox, "title", "text", title_adaptation, title_reason)
    layout_family = source["layout_family"]
    reading_flow = source["reading_flow"]
    evidence_box = content_bbox_after_title(
        expand_around_center(content_box, min_w=min(float(content_box["w"]), 0.72), min_h=0.54, max_w=float(content_box["w"]), max_h=0.68),
        title_bbox,
    )
    evidence_row = clamp_bbox({
        "x": evidence_box["x"],
        "y": evidence_box["y"] + evidence_box["h"] * 0.03,
        "w": evidence_box["w"],
        "h": min(evidence_box["h"] * 0.76, 0.52),
    })
    if strategy == "reference_faithful":
        panels = split_horizontal(evidence_row, 4)
        for region_id, slot_id, role, panel in [
            ("image_input", "input_image", "primary_scientific_object", panels[0]),
            ("image_overlay", "overlay_image", "primary_scientific_object", panels[1]),
            ("image_prediction", "prediction_image", "secondary_scientific_object", panels[2]),
            ("image_error", "error_image", "secondary_scientific_object", panels[3]),
        ]:
            add_region(regions, transfers, source, primary, region_id, role, panel, slot_id, "medical_image", "split", "split the source image-grid bbox into equal evidence panels for the current content slots")
        legend_bbox = clamp_bbox({"x": evidence_box["x"], "y": evidence_row["y"] + evidence_row["h"] + 0.025, "w": evidence_box["w"], "h": 0.07})
        add_region(regions, transfers, source, legend, "legend", "legend", legend_bbox, "legend", "legend", "translate", "translated the source legend band below the derived image grid")
    elif strategy == "alternative_composition":
        panels = split_horizontal(evidence_row, 3)
        for region_id, slot_id, role, panel in [
            ("image_input", "input_image", "primary_scientific_object", panels[0]),
            ("image_overlay", "overlay_image", "primary_scientific_object", panels[1]),
            ("image_error", "error_image", "secondary_scientific_object", panels[2]),
        ]:
            add_region(regions, transfers, source, primary, region_id, role, panel, slot_id, "medical_image", "split", "split the source sample-grid bbox into a three-panel comparison row")
        annotation_bbox = clamp_bbox({"x": panels[1]["x"], "y": evidence_row["y"] + evidence_row["h"] + 0.025, "w": panels[1]["w"] + panels[2]["w"] + 0.026, "h": 0.10})
        legend_bbox = clamp_bbox({"x": evidence_box["x"], "y": annotation_bbox["y"] + annotation_bbox["h"] + 0.022, "w": evidence_box["w"], "h": 0.065})
        add_region(regions, transfers, source, primary, "annotation", "annotation", annotation_bbox, "annotation", "text", "translate", "translated the source grid centerline into a concise failure annotation")
        add_region(regions, transfers, source, legend, "legend", "legend", legend_bbox, "legend", "legend", "translate", "kept the source legend relationship below the evidence row")
    else:
        layout_family = f"{source['layout_family']}-focus-callout"
        reading_flow = f"{source['reading_flow']}-focus-callout"
        main_bbox = bbox_inside(evidence_box, 0.00, 0.02, 0.40, 0.90)
        error_bbox = bbox_inside(evidence_box, 0.52, 0.05, 0.30, 0.46)
        annotation_bbox = bbox_inside(evidence_box, 0.50, 0.55, 0.48, 0.18)
        legend_bbox = bbox_inside(evidence_box, 0.50, 0.78, 0.48, 0.14)
        add_region(regions, transfers, source, primary, "image_overlay", "primary_scientific_object", main_bbox, "overlay_image", "medical_image", "scale", "scaled the source image-grid bbox into a dominant overlay panel")
        add_region(regions, transfers, source, primary, "image_error", "secondary_scientific_object", error_bbox, "error_image", "medical_image", "split", "split a small diagnostic error panel from the source image-grid area")
        add_region(regions, transfers, source, primary, "annotation", "annotation", annotation_bbox, "annotation", "text", "split", "split the source grid side area into a failure annotation")
        add_region(regions, transfers, source, legend, "legend", "legend", legend_bbox, "legend", "legend", "translate", "translated the source legend relationship into the sidecar area")
    return regions, transfers, layout_family, reading_flow


def candidate_regions(request: dict[str, Any], strategy: str, source: dict[str, Any]) -> tuple[list[dict[str, Any]], list[dict[str, Any]], str, str]:
    if request["page_function"] == "MEDICAL_IMAGE_COMPARISON":
        return derived_medical_regions(request, strategy, source)
    return derived_estimator_regions(request, strategy, source)


def slot_label(slot_id: str) -> str:
    labels = {
        "input_image": "Input",
        "overlay_image": "GT / prediction",
        "prediction_image": "Prediction",
        "error_image": "Error map",
    }
    return labels.get(slot_id, slot_id.replace("_", " ").title())


def draw_panel_label(draw: ImageDraw.ImageDraw, label: str, box: tuple[int, int, int, int], font: ImageFont.ImageFont) -> None:
    x1, y1, x2, _ = box
    draw.text((x1, max(8, y1 - 30)), label, font=font, fill=MUTED)
    draw.line((x1, y1 - 6, x2, y1 - 6), fill=LINE, width=1)


def draw_semantic_legend(draw: ImageDraw.ImageDraw, text: str, box: tuple[int, int, int, int], font: ImageFont.ImageFont) -> None:
    x1, y1, x2, _ = box
    swatches = [
        ((45, 140, 83), "overlap"),
        ((202, 74, 74), "false positive"),
        ((72, 116, 196), "false negative"),
    ]
    x = x1
    for color, label in swatches:
        draw.rectangle((x, y1 + 10, x + 18, y1 + 28), fill=color)
        draw.text((x + 28, y1 + 4), label, font=font, fill=MUTED)
        x += max(178, draw.textbbox((0, 0), label, font=font)[2] + 56)
        if x > x2 - 130:
            break
    if x == x1:
        draw_wrapped(draw, text, (x1, y1), x2 - x1, font, fill=MUTED)


def draw_equation_target(draw: ImageDraw.ImageDraw, equation_box: tuple[int, int, int, int]) -> tuple[int, int]:
    x1, y1, x2, y2 = equation_box
    width = x2 - x1
    height = y2 - y1
    hx1 = x1 + round(width * 0.43)
    hx2 = x1 + round(width * 0.77)
    hy = y1 + round(height * 0.82)
    draw.line((hx1, hy, hx2, hy), fill=WARNING, width=5)
    draw.arc((hx1, hy - 20, hx1 + 36, hy + 20), 90, 270, fill=WARNING, width=3)
    draw.arc((hx2 - 36, hy - 20, hx2, hy + 20), -90, 90, fill=WARNING, width=3)
    return ((hx1 + hx2) // 2, hy + 4)


def draw_leader(draw: ImageDraw.ImageDraw, start: tuple[int, int], target: tuple[int, int]) -> None:
    sx, sy = start
    tx, ty = target
    mid = (sx, ty)
    draw.line((sx, sy, mid[0], mid[1], tx, ty), fill=ACCENT, width=3)
    draw.ellipse((tx - 5, ty - 5, tx + 5, ty + 5), fill=ACCENT)


def draw_candidate(request: dict[str, Any], candidate: dict[str, Any], output: Path) -> None:
    canvas = Image.new("RGB", (WIDTH, HEIGHT), CANVAS_BG)
    draw = ImageDraw.Draw(canvas)
    title_font = load_font(39, bold=True)
    text_font = load_font(24)
    small_font = load_font(18)
    label_font = load_font(18, bold=True)
    slot_by_id = {slot["slot_id"]: slot for slot in request["content_slots"]}
    region_by_id = {region["region_id"]: region for region in candidate["regions"]}
    equation_target: tuple[int, int] | None = None
    annotation_start: tuple[int, int] | None = None

    for region in candidate["regions"]:
        slot = slot_by_id[region["content_slot_id"]]
        box = bbox_px(region["bbox"])
        x1, y1, x2, y2 = box
        if region["role"] == "title":
            draw_wrapped(draw, slot["text"], (x1, y1), x2 - x1, title_font, fill=INK, line_spacing=4)
            continue
        if slot["content_type"] == "equation_asset":
            paste_contain(canvas, Image.open(REPO_ROOT / slot["asset_path"]), box, bg=CANVAS_BG)
            equation_target = draw_equation_target(draw, box)
        elif slot["content_type"] == "plot_asset":
            paste_contain(canvas, Image.open(REPO_ROOT / slot["asset_path"]), box, bg=CANVAS_BG)
        elif slot["content_type"] == "image_asset":
            draw_panel_label(draw, slot_label(slot["slot_id"]), box, label_font)
            draw.rectangle((x1, y1, x2, y2), outline=LINE, width=1)
            paste_contain(canvas, Image.open(REPO_ROOT / slot["asset_path"]), (x1 + 2, y1 + 2, x2 - 2, y2 - 2), bg=(248, 248, 246), crop_top_ratio=0.10)
        elif slot["content_type"] == "legend":
            draw_semantic_legend(draw, slot["text"], box, small_font)
        elif slot["content_type"] == "caption":
            draw_wrapped(draw, slot["text"], (x1, y1), x2 - x1, small_font, fill=MUTED)
        else:
            annotation_start = (x1, y1 + 10)
            draw.line((x1, y1 + 2, x1, y2 - 2), fill=ACCENT, width=4)
            draw_wrapped(draw, slot["text"], (x1 + 18, y1), x2 - x1 - 18, text_font, fill=INK, line_spacing=6)

    if equation_target and annotation_start:
        draw_leader(draw, annotation_start, equation_target)

    if candidate["layout_family"] == "horizontal-process-flow":
        y = 405
        draw.line((430, y, 580, y), fill=ACCENT, width=8)
        draw.polygon([(580, y), (552, y - 18), (552, y + 18)], fill=ACCENT)
        draw.line((940, y, 1090, y), fill=ACCENT, width=8)
        draw.polygon([(1090, y), (1062, y - 18), (1062, y + 18)], fill=ACCENT)
    output.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(output)


def transfer_trace(source: dict[str, Any], candidate: dict[str, Any]) -> list[dict[str, Any]]:
    source_primary = primary_region(source)
    trace = []
    for region in candidate["regions"]:
        if region["role"] == "title":
            source_region = next((item for item in source["regions"] if item["role"] == "title"), source_primary)
        elif region["role"] in {"primary_scientific_object", "decision_or_next_step"}:
            source_region = source_primary
        else:
            source_region = next((item for item in source["regions"] if item["role"] == region["role"]), source_primary)
        adaptation = "preserve" if region["bbox"] == source_region["bbox"] else "scale"
        if region["bbox"]["x"] != source_region["bbox"]["x"] or region["bbox"]["y"] != source_region["bbox"]["y"]:
            adaptation = "translate" if adaptation == "preserve" else "scale"
        trace.append({
            "source_reference_id": source["reference_id"],
            "source_region_id": source_region["region_id"],
            "source_role": source_region["role"],
            "source_bbox": source_region["bbox"],
            "candidate_region_id": region["region_id"],
            "candidate_content_slot_id": region["content_slot_id"],
            "candidate_bbox": region["bbox"],
            "adaptation_type": adaptation,
            "adaptation_reason": "fit the same scientific content into a neutral 16:9 regression preview while preserving the source role hierarchy",
        })
    return trace


def content_bindings(regions: list[dict[str, Any]]) -> list[dict[str, str]]:
    return [{"region_id": region["region_id"], "content_slot_id": region["content_slot_id"], "role": region["role"]} for region in regions]


def audience_text(request: dict[str, Any]) -> list[str]:
    return [slot["text"] for slot in request["content_slots"] if slot.get("text")]


def candidate_signature(candidate: dict[str, Any]) -> dict[str, Any]:
    roles = [region["role"] for region in candidate["regions"]]
    primary_regions = [region for region in candidate["regions"] if region["role"] == "primary_scientific_object"]
    return {
        "layout_family": candidate["layout_family"],
        "primary_bbox": primary_regions[0]["bbox"],
        "primary_bboxes": [region["bbox"] for region in primary_regions],
        "region_roles": roles,
        "region_count": len(candidate["regions"]),
        "reading_flow": candidate["reading_flow"],
    }


def visual_finish_metadata(request: dict[str, Any], candidate: dict[str, Any]) -> dict[str, Any]:
    primary_ids = [region["region_id"] for region in candidate["regions"] if region["role"] == "primary_scientific_object"]
    data: dict[str, Any] = {
        "visual_tokens": {
            "token_set_id": "research-presentation-visual-finish-v1",
            "background": "warm-white",
            "ink": "near-black",
            "accent": "teal",
            "secondary_accent": "amber",
            "shared_across_candidates": True,
        },
        "primary_object_treatment": {
            "primary_region_ids": primary_ids,
            "container_role": "none",
            "decorative_card_used": False,
            "scale_policy": "use source-derived candidate region without non-semantic padding",
        },
        "audience_leak_guard": {
            "internal_ids_visible": False,
            "candidate_strategy_visible": False,
            "source_provenance_visible": False,
        },
    }
    if request["page_function"] == "MEDICAL_IMAGE_COMPARISON":
        data.update({
            "panel_correspondence": {
                "panel_region_ids": [region["region_id"] for region in candidate["regions"] if region["content_mode"] == "medical_image"],
                "label_policy": "label adjacent to each panel",
                "image_fill_policy": "cover crop inside semantic panel bounds",
            },
            "legend_binding": {
                "legend_region_id": next((region["region_id"] for region in candidate["regions"] if region["role"] == "legend"), None),
                "binding": "shared legend aligned with image evidence area",
            },
            "synthetic_evidence_boundary": "synthetic regression fixture; not real clinical evidence",
        })
    else:
        data.update({
            "equation_rendering": {
                "region_id": next((region["region_id"] for region in candidate["regions"] if region["content_mode"] == "equation"), None),
                "background": "canvas",
                "contrast": "high",
                "asset_alpha_policy": "flatten transparent pixels onto warm-white background before scaling",
            },
            "annotation_targets": [
                {
                    "annotation_region_id": "annotation",
                    "target_region_id": "equation",
                    "target_relation": "leader_to_middle_term",
                    "target_segment": "middle_term",
                }
            ],
        })
    return data


def build_candidate(request: dict[str, Any], strategy: str, source: dict[str, Any], request_out: Path) -> dict[str, Any]:
    regions, transfers, layout_family, reading_flow = candidate_regions(request, strategy, source)
    primary_regions = [region for region in regions if region["role"] == "primary_scientific_object"]
    candidate_id = f"{request['request_id']}__{strategy}"
    candidate = {
        "candidate_id": candidate_id,
        "strategy": strategy,
        "source_reference_ids": [source["reference_id"]],
        "source_composition_families": [source["layout_family"]],
        "layout_family": layout_family,
        "regions": regions,
        "primary_object_area_ratio": round(sum(region["bbox"]["w"] * region["bbox"]["h"] for region in primary_regions), 4),
        "reading_flow": reading_flow,
        "content_bindings": content_bindings(regions),
        "geometry_transfer": transfers,
        "distinctness_signature": {},
        "preview_artifact": {"path": "", "mime_type": "image/png", "sha256": ""},
        "preview_sha256": "",
        "audience_text": audience_text(request),
        "source_reference_pixels_used": False,
    }
    candidate["visual_finish"] = visual_finish_metadata(request, candidate)
    candidate["distinctness_signature"] = candidate_signature(candidate)
    preview = request_out / "previews" / f"{candidate_id}.png"
    draw_candidate(request, candidate, preview)
    digest = sha256(preview)
    candidate["preview_artifact"] = {"path": str(preview.relative_to(REPO_ROOT)), "mime_type": "image/png", "sha256": digest}
    candidate["preview_sha256"] = digest
    return candidate


def make_comparison_sheet(candidates: list[dict[str, Any]], request_out: Path) -> dict[str, str]:
    previews = [Image.open(REPO_ROOT / candidate["preview_artifact"]["path"]).convert("RGB") for candidate in candidates]
    thumb_w, thumb_h = 500, 281
    sheet = Image.new("RGB", (thumb_w * 3 + 80, thumb_h + 125), (248, 250, 252))
    draw = ImageDraw.Draw(sheet)
    font = load_font(19, bold=True)
    for i, (candidate, image) in enumerate(zip(candidates, previews)):
        image.thumbnail((thumb_w, thumb_h), Image.Resampling.LANCZOS)
        x = 20 + i * (thumb_w + 20)
        y = 75
        sheet.paste(image, (x, y))
        draw_wrapped(draw, f"{i + 1}. {candidate['layout_family']}", (x, 16), thumb_w, font, fill=INK, line_spacing=4)
    out = request_out / "comparison_sheet.png"
    out.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(out)
    return {"path": str(out.relative_to(REPO_ROOT)), "mime_type": "image/png", "sha256": sha256(out)}


def generate_request(request_path: Path, output_root: Path) -> Path:
    request = json.loads(request_path.read_text(encoding="utf-8"))
    retrieved, sources = choose_sources(request)
    request_out = output_root / request["request_id"]
    if request_out.exists():
        shutil.rmtree(request_out)
    request_out.mkdir(parents=True)
    candidates = [build_candidate(request, strategy, sources[strategy], request_out) for strategy in ["reference_faithful", "alternative_composition", "controlled_wildcard"]]
    for candidate in candidates:
        distances = {
            other["candidate_id"]: composition_signature_distance(candidate["distinctness_signature"], other["distinctness_signature"])
            for other in candidates
            if other["candidate_id"] != candidate["candidate_id"]
        }
        candidate["distinctness_signature"]["pairwise_distances"] = distances
    manifest = {
        "schema": "RESEARCH_SLIDE_CANDIDATE_MANIFEST_V1",
        "request": request,
        "retrieved_composition_records": retrieved,
        "content_payload_sha256": payload_sha(request),
        "candidates": candidates,
        "comparison_sheet": make_comparison_sheet(candidates, request_out),
    }
    manifest_path = request_out / "candidate_manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    return manifest_path


def composition_signature_distance(a: dict[str, Any], b: dict[str, Any]) -> float:
    ap = a["primary_bbox"]
    bp = b["primary_bbox"]
    center = abs((ap["x"] + ap["w"] / 2) - (bp["x"] + bp["w"] / 2)) + abs((ap["y"] + ap["h"] / 2) - (bp["y"] + bp["h"] / 2))
    area = abs(ap["w"] * ap["h"] - bp["w"] * bp["h"])
    family = 0.35 if a["layout_family"] != b["layout_family"] else 0
    topology = 0.08 * abs(a["region_count"] - b["region_count"])
    flow = 0.12 if a["reading_flow"] != b["reading_flow"] else 0
    return round(center + area + family + topology + flow, 4)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--request", action="append", required=True, help="Path to a candidate request JSON. Can be repeated.")
    parser.add_argument("--out-dir", default="docs/audits/research_presentation_candidate_search/generated")
    args = parser.parse_args()
    output_root = REPO_ROOT / args.out_dir
    output_root.mkdir(parents=True, exist_ok=True)
    manifest_paths = [generate_request((REPO_ROOT / item).resolve() if not Path(item).is_absolute() else Path(item), output_root) for item in args.request]
    print(json.dumps({"manifests": [str(path.relative_to(REPO_ROOT)) for path in manifest_paths]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
