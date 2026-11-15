#!/usr/bin/env python3
"""Compare generated PDF objects across two Beamer skins, ignoring approved palette changes."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
import re
from typing import Any

import pymupdf as mupdf

REFERENCE_WIDTH = 1920
REFERENCE_HEIGHT = 1080
MAX_GEOMETRY_PX = 2.0
MAX_FONT_PT = 0.1
MASK_KINDS = {"logo", "title-background", "decorative-brand-image"}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def only_keys(obj: dict, names: tuple[str, ...]) -> dict:
    return {name: obj[name] for name in names if name in obj}


def text_lines(page) -> list[dict]:
    # Preserve page and line boundaries. Compare spaces too: native controls
    # use text spaces to construct parts of their link areas.
    return [
        {
            "direction": tuple(line["dir"]),
            "writing_mode": line["wmode"],
            "bbox": bounds(line["bbox"]),
            "spans": [
                {
                    "text": span["text"],
                    "font": span["font"],
                    "flags": span["flags"],
                    "size": span["size"],
                    "origin": tuple(span["origin"]),
                    "bbox": bounds(span["bbox"]),
                }
                for span in line["spans"]
            ],
        }
        for block in page.get_text("dict", flags=mupdf.TEXTFLAGS_TEXT)["blocks"]
        for line in block.get("lines", [])
    ]


def bounds(rect) -> tuple[float, ...]:
    x0, y0, x1, y1 = rect
    return x0, y0, x1, y1, x1 - x0, y1 - y0


def coordinates(value: Any) -> Any:
    if isinstance(value, mupdf.Rect):
        return bounds(value)
    if isinstance(value, (mupdf.Point, mupdf.Quad, tuple, list)):
        return tuple(coordinates(item) for item in value)
    return value


def drawings(page) -> list[dict]:
    # Paths, paint order, clipping and opacity are compared. Only RGB
    # values are omitted, since the palettes deliberately differ.
    geometry_keys = (
        "type", "rect", "items", "width", "dashes", "lineCap", "lineJoin",
        "even_odd", "closePath", "fill_opacity", "stroke_opacity", "level",
        "scissor", "opacity", "isolated", "knockout", "blendmode",
    )
    return [
        {**{k: coordinates(v) for k, v in only_keys(path, geometry_keys).items()},
         "has_fill": path.get("fill") is not None, "has_stroke": path.get("color") is not None}
        for path in page.get_drawings(extended=True)
    ]


def links(page) -> list[dict]:
    return [
        {key: coordinates(value) for key, value in link.items() if key not in {"xref", "id"}}
        for link in page.get_links()
    ]


def load_masks(path: Path, page_count: int) -> list[dict]:
    manifest = json.loads(path.read_text(encoding="utf-8"))
    if manifest["schema"] != "presentations-beamer-brand-masks-v1" or manifest["coordinate_space"] != "1920x1080":
        raise ValueError("Use the v1 brand mask manifest with 1920x1080 coordinates")
    masks = manifest["cuhk"]
    ids = set()
    for mask in masks:
        pages = mask["pages"]
        if pages != "all" and (
            not isinstance(pages, list) or not pages
            or len(set(pages)) != len(pages)
            or any(type(page) is not int or not 1 <= page <= page_count for page in pages)
        ):
            raise ValueError(f"Invalid mask pages: {mask}")
        x0, y0, x1, y1 = mask["rect"]
        if (
            mask["id"] in ids
            or mask["kind"] not in MASK_KINDS
            or not 0 <= x0 < x1 <= REFERENCE_WIDTH
            or not 0 <= y0 < y1 <= REFERENCE_HEIGHT
            or not re.fullmatch("[0-9a-f]{32}", mask["pixel_md5"])
        ):
            raise ValueError(f"Invalid or repeated brand mask: {mask}")
        ids.add(mask["id"])
    return masks


def scaled_rect(rect, page) -> mupdf.Rect:
    sx = page.rect.width / REFERENCE_WIDTH
    sy = page.rect.height / REFERENCE_HEIGHT
    return mupdf.Rect(rect[0] * sx, rect[1] * sy, rect[2] * sx, rect[3] * sy)


def overlaps_vector_object(region: mupdf.Rect, paths: list[dict], page_width: float) -> bool:
    for path in paths:
        if path["type"] not in {"s", "f", "fs"}:
            continue
        rect = mupdf.Rect(path["rect"][:4])
        if path["type"] == "f" and rect.width >= page_width - 0.02 and all(
            item[0] == "re" for item in path["items"]
        ):
            # The full page canvas and full width chrome fills are behind
            # the decoration. Everything else is generated geometry.
            continue
        stroke = (path.get("width") or 0) / 2
        if region.intersects(rect + (-stroke, -stroke, stroke, stroke)):
            return True
    return False


def compare(course_pdf: Path, cuhk_pdf: Path, mask_path: Path) -> dict:
    report = {
        "schema": "presentations-beamer-template-parity-v1",
        "pdf_sha256": {"course-standard": sha256(course_pdf), "cuhk": sha256(cuhk_pdf)},
        "mask_sha256": sha256(mask_path),
        "tolerance": {"geometry_px_at_1920x1080": MAX_GEOMETRY_PX, "font_pdf_pt": MAX_FONT_PT},
        "max_geometry_delta_px": 0.0,
        "max_font_delta_pdf_pt": 0.0,
        "pages": [],
        "errors": [],
    }
    errors = report["errors"]
    with mupdf.open(course_pdf) as course, mupdf.open(cuhk_pdf) as cuhk:
        if course.page_count != cuhk.page_count or course.page_count == 0:
            errors.append(f"Invalid page counts: course-standard={course.page_count}, cuhk={cuhk.page_count}")
        else:
            masks = load_masks(mask_path, course.page_count)
            report["brand_masks"] = masks
            for left, right in zip(course, cuhk):
                compare_page(left, right, masks, report)
    report["status"] = "PASS" if not errors else "FAIL"
    return report


def compare_page(left, right, masks: list[dict], report: dict) -> None:
    errors = report["errors"]
    number = left.number + 1
    if (
        left.rotation or right.rotation or left.rect != right.rect
        or not math.isclose(left.rect.width / left.rect.height, 16 / 9, abs_tol=0.0001)
    ):
        errors.append(f"Page {number}: both skins must have identical unrotated 16:9 media")
        return
    scale = max(REFERENCE_WIDTH / left.rect.width, REFERENCE_HEIGHT / left.rect.height)

    def same(a, b, name, key=None):
        def fail(reason):
            if len(errors) < 120:
                errors.append(f"Page {number} {name}: {reason}")

        if type(a) != type(b):
            fail(f"type {type(a).__name__} != {type(b).__name__}")
        elif isinstance(a, dict):
            if a.keys() != b.keys():
                fail("different fields")
                return
            for k in a:
                same(a[k], b[k], f"{name}.{k}", k)
        elif isinstance(a, (tuple, list)):
            if len(a) != len(b):
                fail(f"count {len(a)} != {len(b)}")
                return
            for i, (old, new) in enumerate(zip(a, b)):
                same(old, new, f"{name}[{i}]", key)
        elif isinstance(a, float):
            if key == "size":
                metric = "max_font_delta_pdf_pt"
                delta, limit = abs(a - b), MAX_FONT_PT
            elif key in {"fill_opacity", "stroke_opacity", "opacity", "direction"}:
                if abs(a - b) > 1e-6:
                    fail(f"{a} != {b}")
                return
            else:
                metric = "max_geometry_delta_px"
                delta, limit = abs(a - b) * scale, MAX_GEOMETRY_PX
            report[metric] = max(report[metric], delta)
            if delta > limit + 1e-6:
                fail(f"{a} != {b} (delta {delta:.4f}, limit {limit})")
        elif a != b:
            fail(f"{a!r} != {b!r}")

    left_text, right_text = text_lines(left), text_lines(right)
    left_paths, right_paths = drawings(left), drawings(right)
    left_links, right_links = links(left), links(right)
    same(left_text, right_text, "text and line breaks")
    same(left_paths, right_paths, "vector objects")
    same(left_links, right_links, "links and destinations")

    old_images = left.get_image_info(hashes=True)
    new_images = right.get_image_info(hashes=True)
    active = [mask for mask in masks if mask["pages"] == "all" or number in mask["pages"]]
    used = set()
    for mask in active:
        region = scaled_rect(mask["rect"], right)
        for side_text, side_links in ((left_text, left_links), (right_text, right_links)):
            if any(region.intersects(mupdf.Rect(span["bbox"][:4]))
                   for line in side_text for span in line["spans"] if span["text"].strip()):
                errors.append(f"Page {number}: mask {mask['id']} intersects generated text")
            if any(region.intersects(mupdf.Rect(link["from"][:4])) for link in side_links):
                errors.append(f"Page {number}: mask {mask['id']} intersects navigation or a link")
        if any(overlaps_vector_object(region, paths, right.rect.width) for paths in (left_paths, right_paths)):
            errors.append(f"Page {number}: mask {mask['id']} intersects generated vector geometry")
        for image in old_images:
            if region.intersects(mupdf.Rect(image["bbox"])):
                errors.append(f"Page {number}: mask {mask['id']} intersects course-standard image")
        matches = [
            i for i, image in enumerate(new_images)
            if region.contains(mupdf.Rect(image["bbox"])) and image["digest"].hex() == mask["pixel_md5"]
        ]
        if len(matches) != 1 or any(index in used for index in matches):
            errors.append(f"Page {number}: mask {mask['id']} must match one unique approved brand image")
            continue
        used.add(matches[0])
        if any(region.intersects(mupdf.Rect(image["bbox"]))
               for i, image in enumerate(new_images) if i != matches[0]):
            errors.append(f"Page {number}: mask {mask['id']} intersects another image")

    def image_objects(images):
        return [
            {"digest": image["digest"].hex(), "bbox": bounds(image["bbox"]), "matrix": image["transform"]}
            for image in images
        ]

    same(image_objects(old_images), image_objects(
        image for i, image in enumerate(new_images) if i not in used
    ), "unmasked images")
    report["pages"].append({
        "page": number,
        "lines": len(left_text),
        "paths": len(left_paths),
        "links": len(left_links),
        "scientific_or_teaching_images": len(old_images),
        "matched_brand_images": len(used),
    })


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("course_standard", type=Path)
    parser.add_argument("cuhk", type=Path)
    parser.add_argument("--masks", required=True, type=Path)
    parser.add_argument("--report", required=True, type=Path)
    args = parser.parse_args()
    report = compare(args.course_standard, args.cuhk, args.masks)
    args.report.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"{report['status']}: {len(report['pages'])} pages, {len(report['errors'])} differences")
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
