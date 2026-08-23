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
INK = (24, 31, 42)
MUTED = (85, 96, 111)
LINE = (200, 208, 218)
ACCENT = (0, 108, 112)
SECONDARY = (67, 56, 202)
WARNING = (171, 91, 28)


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


def paste_contain(canvas: Image.Image, source: Image.Image, box: tuple[int, int, int, int], bg=(255, 255, 255)) -> None:
    x1, y1, x2, y2 = box
    w, h = x2 - x1, y2 - y1
    region = Image.new("RGB", (w, h), bg)
    image = source.convert("RGBA")
    image.thumbnail((w, h), Image.Resampling.LANCZOS)
    px = (w - image.width) // 2
    py = (h - image.height) // 2
    region.paste(image.convert("RGB"), (px, py))
    canvas.paste(region, (x1, y1))


def load_composition_records() -> list[dict[str, Any]]:
    return json.loads(COMPOSITION_INDEX.read_text(encoding="utf-8"))["records"]


def by_reference_id() -> dict[str, dict[str, Any]]:
    return {record["reference_id"]: record for record in load_composition_records()}


def tokens(value: str) -> set[str]:
    return {part.lower() for part in value.replace("/", " ").replace("-", " ").replace("_", " ").split() if len(part) > 2}


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


def compatible_records(request: dict[str, Any], initial_ids: list[str]) -> list[dict[str, Any]]:
    records_by_id = by_reference_id()
    selected = [records_by_id[reference_id] for reference_id in initial_ids if reference_id in records_by_id]
    seen = {record["reference_id"] for record in selected}
    query_terms = tokens(" ".join([request["page_function"], request["scientific_object"], request.get("evidence_type", "")]))
    scored: list[tuple[int, str, dict[str, Any]]] = []
    for record in load_composition_records():
        if record["reference_id"] in seen:
            continue
        score = 0
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
        content_modes = {region["content_mode"] for region in record["regions"]}
        if request["page_function"] in {"ESTIMATOR", "STATISTICAL_MODEL", "THEOREM"} and "equation" in content_modes:
            score += 6
        if request["page_function"] == "ESTIMATOR" and record["page_function"] in {"STATISTICAL_MODEL", "BAYESIAN_MODEL"}:
            score += 4
        if request["page_function"] == "ESTIMATOR" and record["page_function"] in {"RESULT_FIGURE", "CONFIDENCE_INTERVAL", "REAL_DATA_APPLICATION"}:
            score += 2
        if request["page_function"] == "MEDICAL_IMAGE_COMPARISON" and "medical_image" in content_modes:
            score += 6
        if score > 0:
            scored.append((score, record["reference_id"], record))
    scored.sort(key=lambda item: (-item[0], item[1]))
    selected.extend(record for _, _, record in scored)
    return selected


def choose_sources(request: dict[str, Any]) -> tuple[list[dict[str, Any]], dict[str, dict[str, Any]]]:
    retrieved = select_reference_compositions.select(
        request.get("page_function"),
        request.get("evidence_type"),
        request.get("scientific_object"),
        8,
    )
    initial_ids = [item["reference_id"] for item in retrieved]
    pool = compatible_records(request, initial_ids)
    if len(pool) < 3:
        raise RuntimeError(f"{request['request_id']}: fewer than three compatible composition records")
    first = pool[0]
    second = next((record for record in pool[1:] if record["layout_family"] != first["layout_family"]), pool[1])
    third = max(
        (record for record in pool if record["reference_id"] not in {first["reference_id"], second["reference_id"]}),
        key=lambda record: composition_distance(first, record) + composition_distance(second, record),
    )
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


def candidate_regions(request: dict[str, Any], strategy: str, source: dict[str, Any]) -> list[dict[str, Any]]:
    family = source["layout_family"]
    if request["page_function"] == "MEDICAL_IMAGE_COMPARISON":
        if family == "aligned-multi-panel" and strategy == "reference_faithful":
            boxes = [
                ("image_input", "primary_scientific_object", {"x": 0.07, "y": 0.22, "w": 0.20, "h": 0.36}, "input_image"),
                ("image_overlay", "primary_scientific_object", {"x": 0.30, "y": 0.22, "w": 0.20, "h": 0.36}, "overlay_image"),
                ("image_prediction", "secondary_scientific_object", {"x": 0.53, "y": 0.22, "w": 0.20, "h": 0.36}, "prediction_image"),
                ("image_error", "secondary_scientific_object", {"x": 0.76, "y": 0.22, "w": 0.17, "h": 0.36}, "error_image"),
                ("legend", "legend", {"x": 0.09, "y": 0.66, "w": 0.80, "h": 0.09}, "legend"),
            ]
        elif family in {"split-visual-explanation", "result-with-callout"}:
            boxes = [
                ("image_overlay", "primary_scientific_object", {"x": 0.07, "y": 0.20, "w": 0.48, "h": 0.56}, "overlay_image"),
                ("image_error", "secondary_scientific_object", {"x": 0.60, "y": 0.23, "w": 0.22, "h": 0.25}, "error_image"),
                ("annotation", "annotation", {"x": 0.60, "y": 0.52, "w": 0.30, "h": 0.18}, "annotation"),
                ("legend", "legend", {"x": 0.60, "y": 0.73, "w": 0.30, "h": 0.10}, "legend"),
            ]
        else:
            boxes = [
                ("image_input", "primary_scientific_object", {"x": 0.06, "y": 0.24, "w": 0.21, "h": 0.34}, "input_image"),
                ("image_overlay", "primary_scientific_object", {"x": 0.38, "y": 0.24, "w": 0.21, "h": 0.34}, "overlay_image"),
                ("image_error", "secondary_scientific_object", {"x": 0.70, "y": 0.24, "w": 0.21, "h": 0.34}, "error_image"),
                ("annotation", "annotation", {"x": 0.30, "y": 0.64, "w": 0.42, "h": 0.14}, "annotation"),
                ("legend", "legend", {"x": 0.21, "y": 0.80, "w": 0.58, "h": 0.08}, "legend"),
            ]
    else:
        if family == "equation-dominant":
            boxes = [
                ("equation", "primary_scientific_object", {"x": 0.10, "y": 0.28, "w": 0.80, "h": 0.22}, "equation"),
                ("annotation", "annotation", {"x": 0.20, "y": 0.56, "w": 0.60, "h": 0.12}, "annotation"),
                ("caption", "caption", {"x": 0.18, "y": 0.76, "w": 0.64, "h": 0.07}, "caption"),
            ]
        elif family == "split-visual-explanation":
            boxes = [
                ("equation", "primary_scientific_object", {"x": 0.07, "y": 0.27, "w": 0.58, "h": 0.20}, "equation"),
                ("annotation", "annotation", {"x": 0.69, "y": 0.25, "w": 0.24, "h": 0.20}, "annotation"),
                ("caption", "caption", {"x": 0.07, "y": 0.62, "w": 0.60, "h": 0.08}, "caption"),
            ]
        elif family == "result-with-callout":
            boxes = [
                ("equation", "primary_scientific_object", {"x": 0.12, "y": 0.23, "w": 0.72, "h": 0.18}, "equation"),
                ("annotation", "annotation", {"x": 0.52, "y": 0.49, "w": 0.34, "h": 0.16}, "annotation"),
                ("caption", "caption", {"x": 0.12, "y": 0.73, "w": 0.50, "h": 0.08}, "caption"),
            ]
        else:
            boxes = [
                ("equation", "primary_scientific_object", {"x": 0.17, "y": 0.22, "w": 0.66, "h": 0.18}, "equation"),
                ("annotation", "annotation", {"x": 0.16, "y": 0.47, "w": 0.68, "h": 0.12}, "annotation"),
                ("caption", "caption", {"x": 0.16, "y": 0.68, "w": 0.68, "h": 0.08}, "caption"),
            ]
    regions = [{"region_id": "title", "role": "title", "bbox": {"x": 0.06, "y": 0.06, "w": 0.82, "h": 0.10}, "content_mode": "text", "content_slot_id": "title"}]
    for region_id, role, bbox, slot_id in boxes:
        slot = next(slot for slot in request["content_slots"] if slot["slot_id"] == slot_id)
        mode = "equation" if slot["content_type"] == "equation_asset" else "medical_image" if slot["content_type"] == "image_asset" else "text"
        if slot["content_type"] == "legend":
            mode = "legend"
        if slot["content_type"] == "caption":
            mode = "caption"
        regions.append({"region_id": region_id, "role": role, "bbox": bbox, "content_mode": mode, "content_slot_id": slot_id})
    return regions


def draw_candidate(request: dict[str, Any], candidate: dict[str, Any], output: Path) -> None:
    canvas = Image.new("RGB", (WIDTH, HEIGHT), (250, 250, 248))
    draw = ImageDraw.Draw(canvas)
    title_font = load_font(42, bold=True)
    text_font = load_font(25)
    small_font = load_font(20)
    draw.rectangle((0, 0, WIDTH, 900), fill=(250, 250, 248))
    draw.line((96, 150, 1504, 150), fill=LINE, width=2)
    slot_by_id = {slot["slot_id"]: slot for slot in request["content_slots"]}
    for region in candidate["regions"]:
        slot = slot_by_id[region["content_slot_id"]]
        box = bbox_px(region["bbox"])
        x1, y1, x2, y2 = box
        if region["role"] == "title":
            draw_wrapped(draw, slot["text"], (x1, y1), x2 - x1, title_font)
            continue
        if slot["content_type"] in {"equation_asset", "plot_asset", "image_asset"}:
            draw.rounded_rectangle((x1, y1, x2, y2), radius=10, fill=(255, 255, 255), outline=LINE, width=2)
            paste_contain(canvas, Image.open(REPO_ROOT / slot["asset_path"]), (x1 + 12, y1 + 12, x2 - 12, y2 - 12))
        elif slot["content_type"] == "legend":
            draw.rounded_rectangle((x1, y1, x2, y2), radius=8, fill=(241, 245, 249), outline=LINE, width=1)
            draw_wrapped(draw, slot["text"], (x1 + 14, y1 + 12), x2 - x1 - 28, small_font, fill=MUTED)
        elif slot["content_type"] == "caption":
            draw_wrapped(draw, slot["text"], (x1, y1), x2 - x1, small_font, fill=MUTED)
        else:
            draw.rounded_rectangle((x1, y1, x2, y2), radius=8, fill=(236, 253, 245), outline=ACCENT, width=2)
            draw_wrapped(draw, slot["text"], (x1 + 16, y1 + 14), x2 - x1 - 32, text_font, fill=INK)
    # Draw structural arrows for flow-like candidates after images.
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
    primary = next(region for region in candidate["regions"] if region["role"] == "primary_scientific_object")
    return {
        "layout_family": candidate["layout_family"],
        "primary_bbox": primary["bbox"],
        "region_roles": roles,
        "region_count": len(candidate["regions"]),
        "reading_flow": candidate["reading_flow"],
    }


def build_candidate(request: dict[str, Any], strategy: str, source: dict[str, Any], request_out: Path) -> dict[str, Any]:
    regions = candidate_regions(request, strategy, source)
    primary = next(region for region in regions if region["role"] == "primary_scientific_object")
    candidate_id = f"{request['request_id']}__{strategy}"
    candidate = {
        "candidate_id": candidate_id,
        "strategy": strategy,
        "source_reference_ids": [source["reference_id"]],
        "source_composition_families": [source["layout_family"]],
        "layout_family": source["layout_family"],
        "regions": regions,
        "primary_object_area_ratio": round(primary["bbox"]["w"] * primary["bbox"]["h"], 4),
        "reading_flow": source["reading_flow"],
        "content_bindings": content_bindings(regions),
        "geometry_transfer": [],
        "distinctness_signature": {},
        "preview_artifact": {"path": "", "mime_type": "image/png", "sha256": ""},
        "preview_sha256": "",
        "audience_text": audience_text(request),
        "source_reference_pixels_used": False,
    }
    candidate["geometry_transfer"] = transfer_trace(source, candidate)
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
    sheet = Image.new("RGB", (thumb_w * 3 + 80, thumb_h + 110), (248, 250, 252))
    draw = ImageDraw.Draw(sheet)
    font = load_font(22, bold=True)
    for i, (candidate, image) in enumerate(zip(candidates, previews)):
        image.thumbnail((thumb_w, thumb_h), Image.Resampling.LANCZOS)
        x = 20 + i * (thumb_w + 20)
        y = 60
        sheet.paste(image, (x, y))
        draw.text((x, 20), f"{i + 1}. {candidate['layout_family']}", font=font, fill=INK)
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
