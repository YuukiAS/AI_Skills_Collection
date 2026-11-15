"""Whole-page raster comparison outside immutable, explicit change rectangles."""

from ..io import EvidenceMissing, InputError
from ..render import Rect, Render
from .model import check


def compare(approved, page, old_page, new_page):
    import pymupdf

    if old_page.rect != new_page.rect or old_page.rotation != new_page.rotation:
        return check("PROTECTION", False, page.id, "Protected page geometry changed")
    regions = []
    old_render = Render.extract(old_page)
    for zone in approved:
        rect = Rect.from_value(zone["rect"])
        if (not page.render.bounds.contains(rect) or rect.width <= 0 or rect.height <= 0
                or zone.get("kind") not in {"change", "brand"}):
            raise InputError("Invalid protected comparison mask")
        if zone["kind"] == "brand" and any(
            rect.intersects(line.box) for line in [*old_render.lines, *page.render.lines]
        ):
            raise InputError("Brand masks cannot cover rendered text")
        regions.append(rect)
    scale = 1920 / new_page.rect.width
    transform = pymupdf.Matrix(scale, scale)
    before, after = (item.get_pixmap(matrix=transform, colorspace=pymupdf.csRGB, alpha=False)
                     for item in (old_page, new_page))
    if (before.width, before.height) != (after.width, after.height):
        raise EvidenceMissing("Cannot compare differing raster dimensions")
    first, second = before.samples, after.samples
    if first == second:
        return check("PROTECTION", True, page.id, "Protected pixels unchanged", changed_pixels=0)
    intervals = [[] for _ in range(after.height)]
    for rect in regions:
        x0, y0, x1, y1 = (pymupdf.Rect(rect.x0, rect.y0, rect.x1, rect.y1) * transform).irect
        for y in range(max(0, y0), min(after.height, y1)):
            intervals[y].append((max(0, x0), min(after.width, x1)))
    changed = 0
    for y, allowed in enumerate(intervals):
        left = 0
        base = y * after.stride
        for start, stop in [*sorted(allowed), (after.width, after.width)]:
            if start > left:
                begin, end = base + left * 3, base + start * 3
                if first[begin:end] != second[begin:end]:
                    changed += sum(first[i:i + 3] != second[i:i + 3] for i in range(begin, end, 3))
            left = max(left, stop)
    return check("PROTECTION", changed == 0, page.id, "Pixel diff outside authorized masks",
                 changed_pixels=changed)
