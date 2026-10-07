"""PDF and rendered-PNG feature extraction for presentation pages."""

from __future__ import annotations

import hashlib
import math
import subprocess
from collections import deque
from pathlib import Path
from typing import Any

import numpy as np
from lxml import etree
from PIL import Image


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def extract_pdf_text_pages(pdf_path: Path) -> dict[int, dict[str, Any]]:
    """Extract word boxes with pdftotext -bbox-layout.

    PyMuPDF is not always available in Codex runtimes; pdftotext bbox XML is an
    equivalent source for text-span geometry in this pilot.
    """

    proc = subprocess.run(
        ["pdftotext", "-bbox-layout", str(pdf_path), "-"],
        check=True,
        capture_output=True,
    )
    parser = etree.HTMLParser(recover=True)
    root = etree.fromstring(proc.stdout, parser=parser)
    pages: dict[int, dict[str, Any]] = {}
    for idx, page in enumerate(root.xpath("//page"), start=1):
        width = float(page.get("width", "0") or 0)
        height = float(page.get("height", "0") or 0)
        words = []
        for word in page.xpath(".//word"):
            text = "".join(word.itertext()).strip()
            if not text:
                continue
            words.append(
                {
                    "text": text,
                    "x0": float(word.get("xmin") or word.get("xMin") or 0),
                    "y0": float(word.get("ymin") or word.get("yMin") or 0),
                    "x1": float(word.get("xmax") or word.get("xMax") or 0),
                    "y1": float(word.get("ymax") or word.get("yMax") or 0),
                }
            )
        pages[idx] = {"pdf_width": width, "pdf_height": height, "words": words}
    return pages


def _scaled_components(mask: np.ndarray, scale_x: float, scale_y: float) -> list[dict[str, Any]]:
    height, width = mask.shape
    seen = np.zeros_like(mask, dtype=bool)
    components: list[dict[str, Any]] = []
    for y in range(height):
        xs = np.flatnonzero(mask[y] & ~seen[y])
        for start_x in xs:
            if seen[y, start_x]:
                continue
            queue: deque[tuple[int, int]] = deque([(y, int(start_x))])
            seen[y, start_x] = True
            count = 0
            min_x = max_x = int(start_x)
            min_y = max_y = y
            while queue:
                cy, cx = queue.popleft()
                count += 1
                min_x = min(min_x, cx)
                max_x = max(max_x, cx)
                min_y = min(min_y, cy)
                max_y = max(max_y, cy)
                for ny in (cy - 1, cy, cy + 1):
                    if ny < 0 or ny >= height:
                        continue
                    for nx in (cx - 1, cx, cx + 1):
                        if nx < 0 or nx >= width or seen[ny, nx] or not mask[ny, nx]:
                            continue
                        seen[ny, nx] = True
                        queue.append((ny, nx))
            if count < 6:
                continue
            components.append(
                {
                    "x0": round(min_x * scale_x, 2),
                    "y0": round(min_y * scale_y, 2),
                    "x1": round((max_x + 1) * scale_x, 2),
                    "y1": round((max_y + 1) * scale_y, 2),
                    "area_px": int(count * scale_x * scale_y),
                }
            )
    components.sort(key=lambda c: c["area_px"], reverse=True)
    return components


def inspect_rendered_png(png_path: Path, *, max_components: int = 20) -> dict[str, Any]:
    """Open the exact PNG and inspect pixel geometry.

    This function is intentionally named "inspect" because it reads pixels from
    the rendered page. It does not infer semantic acceptance on its own.
    """

    with Image.open(png_path) as image:
        rgb_image = image.convert("RGB")
        rgb = np.asarray(rgb_image)
        small = rgb_image.resize((480, max(1, round(rgb_image.height * 480 / rgb_image.width))))
        small_rgb = np.asarray(small.convert("RGB"))

    height, width = rgb.shape[:2]
    nonwhite = np.any(rgb < 245, axis=2)
    body = nonwhite[int(height * 0.10) : int(height * 0.90), int(width * 0.035) : int(width * 0.965)]
    coords = np.argwhere(body)
    if coords.size:
        y0, x0 = coords.min(axis=0)
        y1, x1 = coords.max(axis=0)
        body_bbox = {
            "x0": int(x0 + width * 0.035),
            "y0": int(y0 + height * 0.10),
            "x1": int(x1 + width * 0.035),
            "y1": int(y1 + height * 0.10),
        }
        bbox_area_ratio = ((x1 - x0 + 1) * (y1 - y0 + 1)) / max(1, body.shape[0] * body.shape[1])
        top_void = y0 / max(1, body.shape[0])
        bottom_void = (body.shape[0] - y1 - 1) / max(1, body.shape[0])
    else:
        body_bbox = None
        bbox_area_ratio = 0.0
        top_void = 1.0
        bottom_void = 1.0

    small_nonwhite = np.any(small_rgb < 245, axis=2)
    components = _scaled_components(
        small_nonwhite,
        scale_x=width / small_nonwhite.shape[1],
        scale_y=height / small_nonwhite.shape[0],
    )[:max_components]
    component_area = sum(c["area_px"] for c in components[:5])
    largest = components[0] if components else None
    row_occ = body.mean(axis=1) if body.size else np.array([])
    col_occ = body.mean(axis=0) if body.size else np.array([])
    left = float(col_occ[: int(len(col_occ) * 0.45)].mean()) if len(col_occ) else 0.0
    center = float(col_occ[int(len(col_occ) * 0.45) : int(len(col_occ) * 0.55)].mean()) if len(col_occ) else 0.0
    right = float(col_occ[int(len(col_occ) * 0.55) :].mean()) if len(col_occ) else 0.0
    return {
        "png_path": str(png_path),
        "png_sha256": sha256_file(png_path),
        "width": width,
        "height": height,
        "body_occupancy_ratio": round(float(body.mean()), 5) if body.size else 0.0,
        "body_bbox": body_bbox,
        "body_bbox_area_ratio": round(float(bbox_area_ratio), 5),
        "top_void_ratio": round(float(top_void), 5),
        "bottom_void_ratio": round(float(bottom_void), 5),
        "content_components": components,
        "largest_component": largest,
        "top_components_area_ratio": round(component_area / max(1, width * height), 5),
        "left_occupancy": round(left, 5),
        "center_occupancy": round(center, 5),
        "right_occupancy": round(right, 5),
        "active_horizontal_band_count": int(np.sum(row_occ > 0.012)) if row_occ.size else 0,
    }


def text_geometry_features(page: dict[str, Any], image_width: int, image_height: int) -> dict[str, Any]:
    words = page.get("words", [])
    pdf_w = page.get("pdf_width") or 1
    pdf_h = page.get("pdf_height") or 1
    spans = []
    heights = []
    for w in words:
        x0 = w["x0"] * image_width / pdf_w
        x1 = w["x1"] * image_width / pdf_w
        y0 = w["y0"] * image_height / pdf_h
        y1 = w["y1"] * image_height / pdf_h
        if x1 <= x0 or y1 <= y0:
            continue
        spans.append({"text": w["text"], "x0": x0, "y0": y0, "x1": x1, "y1": y1, "height": y1 - y0})
        heights.append(y1 - y0)
    body_spans = [s for s in spans if s["y0"] > image_height * 0.10 and s["y1"] < image_height * 0.90]
    left_words = sum(1 for s in body_spans if (s["x0"] + s["x1"]) / 2 < image_width * 0.47)
    right_words = sum(1 for s in body_spans if (s["x0"] + s["x1"]) / 2 > image_width * 0.53)
    return {
        "word_count": len(spans),
        "body_word_count": len(body_spans),
        "median_word_height_px": round(float(np.median(heights)), 3) if heights else 0.0,
        "min_word_height_px": round(float(min(heights)), 3) if heights else 0.0,
        "left_body_words": left_words,
        "right_body_words": right_words,
        "two_column_text_signal": bool(left_words > 25 and right_words > 25),
        "spans": spans[:1200],
        "text_excerpt": " ".join(s["text"] for s in spans)[:2000],
        "question_spans": [s for s in spans if s["text"].lower().strip(":：") in {"question", "q", "问题"}],
        "answer_spans": [s for s in spans if s["text"].lower().strip(":：") in {"answer", "a", "答案"}],
    }


def rect_distance(a: dict[str, float], b: dict[str, float]) -> float:
    dx = max(float(a["x0"]) - float(b["x1"]), float(b["x0"]) - float(a["x1"]), 0.0)
    dy = max(float(a["y0"]) - float(b["y1"]), float(b["y0"]) - float(a["y1"]), 0.0)
    return math.hypot(dx, dy)
