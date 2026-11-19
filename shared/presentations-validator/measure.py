"""Identity-free PDF/raster measurements. No labels, filenames or page ordinals.

The caller supplies an already opened Page. All local IDs are extraction indices,
never a hand-authored page/object map. Coordinates are PDF points.
"""

import math
import re
import unicodedata
from itertools import pairwise

import numpy as np
import pymupdf as pdf


def normalized(text):
    return " ".join(unicodedata.normalize("NFKC", text).split())


def union(rects):
    if not rects:
        return None
    return [
        min(r[0] for r in rects),
        min(r[1] for r in rects),
        max(r[2] for r in rects),
        max(r[3] for r in rects),
    ]


def intersection(a, b):
    return max(0, min(a[2], b[2]) - max(a[0], b[0])) * max(
        0, min(a[3], b[3]) - max(a[1], b[1])
    )


def is_color(c, rules):
    return bool(
        c and max(c) - min(c) > rules["_extraction"]["chromatic_color_range_min"]
    )


def geometry(page, rules):
    """Discover template bands and table rectangles from painted PDF geometry."""
    w, h = page.rect.width, page.rect.height
    tol = rules["limits"]["boundary_px"] * w / 1920
    drawings = [
        d
        for d in page.get_drawings()
        if (d["color"] and d.get("stroke_opacity", 1) > 0)
        or (d["fill"] and d.get("fill_opacity", 1) > 0)
    ]
    horizontal, footer_lines, headers = [], [], []
    for item in drawings:
        r = list(item["rect"])
        if (
            r[2] - r[0] >= w - 2 * tol
            and r[3] - r[1] <= tol
            and is_color(item["color"], rules)
            and r[1] > h / 2
        ):
            footer_lines.append(r[1])
        if (
            r[0] <= tol
            and r[2] >= w - tol
            and r[1] <= tol
            and r[3] < h / 2
            and is_color(item["fill"], rules)
        ):
            headers.append(r[3])
        if (
            item["color"]
            and not is_color(item["color"], rules)
            and r[3] - r[1] <= tol
            and r[2] - r[0] > rules["font_pdf_pt"]["body"]
        ):
            horizontal.append(r)
    header = max(headers) if headers else None
    footer = max(footer_lines) if footer_lines else None
    # A table needs at least two aligned horizontal rules. Axes/isolated rules
    # remain unclassified; no semantic ownership is asserted for them.
    groups = []
    for r in sorted(horizontal, key=lambda r: r[1]):
        group = next(
            (
                g
                for g in groups
                if abs(g[0][0] - r[0]) <= tol and abs(g[0][2] - r[2]) <= tol
            ),
            None,
        )
        if group is None:
            groups.append([r])
        else:
            group.append(r)
    tables = [union(g) for g in groups if len(g) >= 2 and g[-1][1] > g[0][1] + tol]
    images = [list(z["bbox"]) for z in page.get_image_info()]
    panels = []
    vectors = []
    for item in drawings:
        r = list(item["rect"])
        # Remove page backgrounds and horizontal template/table rules. Keep
        # visible non-white diagram paths, including objects outside the page.
        white = (
            item["fill"]
            and min(item["fill"]) >= rules["_extraction"]["white_fill_min"]
            and not item["color"]
        )
        if white:
            continue
        if header is not None and r[3] <= header + tol:
            continue
        if footer is not None and r[1] >= footer - tol:
            continue
        if (
            item["fill"]
            and item.get("fill_opacity", 1) > 0
            and not is_color(item["fill"], rules)
            and min(item["fill"]) < rules["_extraction"]["white_fill_min"]
            and r[2] - r[0] > tol
            and r[3] - r[1] > tol
            and all(path[0] == "re" for path in item["items"])
        ):
            panels.append(r)
        vectors.append(r)
    footer_controls = [
        list(d["rect"])
        for d in drawings
        if footer is not None
        and d["rect"].y0 > footer + tol
        and d["rect"].x0 > w / 2
        and (d["color"] or d["fill"] and min(d["fill"]) < 1)
    ]
    return {
        "width": w,
        "height": h,
        "header": header,
        "footer": footer,
        "tables": tables,
        "images": images,
        "vectors": vectors,
        "panels": panels,
        "footer_controls": footer_controls,
    }


def extract_lines(page, rules):
    """Use dictionary line structure, discard transparent/invisible PDF text.

    get_text() includes opacity-zero native-link placeholder dots in this
    template. They must not become typography/overflow findings. Trace opacity
    is real PDF rendering state, not a text/content exception.
    """
    traces = page.get_texttrace()
    visible = [z for z in traces if z["opacity"] > 0 and z["type"] != 3]
    origins = {}
    tol = rules["limits"]["boundary_px"] * page.rect.width / 1920
    for z in visible:
        for char in z["chars"]:
            x, y = char[2]
            box = char[3]
            # A single painted ligature can expand to several extracted
            # characters with different origins. Index the whole glyph extent.
            left, right = min(x, box[0]), max(x, box[2])
            for cell in range(math.floor(left / tol), math.floor(right / tol) + 1):
                key = (z["font"], cell, math.floor(y / tol))
                origins.setdefault(key, []).append((left, right, y))
    data = page.get_text(
        "rawdict",
        flags=pdf.TEXT_PRESERVE_WHITESPACE | pdf.TEXT_PRESERVE_LIGATURES,
        clip=pdf.INFINITE_RECT(),
    )
    lines = []
    for bi, block in enumerate(data["blocks"]):
        if block["type"] != 0:
            continue
        for li, line in enumerate(block["lines"]):
            spans = []
            for s in line["spans"]:
                chars = []
                visible_nonspace = False
                for char in s["chars"]:
                    # TeX often positions words with advances instead of drawing
                    # space glyphs. MuPDF reconstructs those spaces; retain them
                    # only when this span also contains real visible glyphs.
                    if char["c"].isspace():
                        chars.append(char)
                        continue
                    x, y = char["origin"]
                    gx, gy = math.floor(x / tol), math.floor(y / tol)
                    matches = [
                        p
                        for dx in (-1, 0, 1)
                        for dy in (-1, 0, 1)
                        for p in origins.get((s["font"], gx + dx, gy + dy), [])
                    ]
                    if any(
                        left - tol <= x <= right + tol and abs(y - py) <= tol
                        for left, right, py in matches
                    ):
                        chars.append(char)
                        visible_nonspace = True
                text = "".join(c["c"] for c in chars)
                if not visible_nonspace or not text.strip():
                    continue
                r = union([c["bbox"] for c in chars])
                spans.append(
                    {
                        "text": normalized(text),
                        "font": s["font"],
                        "size": s["size"],
                        "bbox": list(r),
                        "origin": list(s["origin"]),
                        "flags": s["flags"],
                        "color": s["color"],
                    }
                )
            if spans:
                plain = [s for s in spans if "math" not in s["font"].lower()]
                main = max(plain or spans, key=lambda s: len(s["text"]))
                lines.append(
                    {
                        "block": bi,
                        "line": li,
                        "bbox": union([s["bbox"] for s in spans]),
                        "text": normalized(" ".join(s["text"] for s in spans)),
                        "baseline": main["origin"][1],
                        "size": main["size"],
                        "font": main["font"],
                        "spans": spans,
                        "plain_chars": sum(len(s["text"]) for s in plain),
                        "bullet": bool(
                            re.match(
                                r"^(?:[•‣·–]|\d+[.)])(?:\s|$)",
                                min(spans, key=lambda s: s["bbox"][0])["text"],
                            )
                        ),
                    }
                )
    return lines


def code_lines(lines, geom, rules):
    """Identify monospaced blocks from painted panels or multiline structure.

    A monospaced token within prose inherits its surrounding block's role.
    Table cells and list items retain their own roles, including cells or
    continuation lines set entirely in a monospaced font. An isolated unboxed
    monospaced line supplies insufficient evidence for a code block.
    """
    tol = rules["limits"]["optical_px"] * geom["width"] / 1920
    blocks = {}
    for index, line in enumerate(lines):
        blocks.setdefault(line["block"], []).append((index, line))
    result = set()
    for group in blocks.values():
        mono = [
            all(
                s["flags"] & 8
                or re.search(
                    r"mono|courier|cmtt|lmtt|typewriter", s["font"], re.IGNORECASE
                )
                for s in line["spans"]
            )
            for _, line in group
        ]
        multiline = (
            len(group) >= 2
            and all(mono)
            and not any(line["bullet"] for _, line in group)
            and max(line["baseline"] for _, line in group)
            - min(line["baseline"] for _, line in group)
            > tol
        )
        for (index, line), is_mono in zip(group, mono):
            r = line["bbox"]
            in_table = any(
                intersection(r, table) > 0
                and table[1] - tol <= line["baseline"] <= table[3] + tol
                for table in geom["tables"]
            )
            in_panel = any(
                panel[0] - tol <= r[0]
                and r[2] <= panel[2] + tol
                and panel[1] - tol <= line["baseline"] <= panel[3] + tol
                for panel in geom.get("panels", [])
            )
            if (
                is_mono
                and not line["bullet"]
                and (in_panel or multiline and not in_table)
            ):
                result.add(index)
    return result


def classify(lines, geom, rules, model=None):
    w, h = geom["width"], geom["height"]
    tol = rules["limits"]["optical_px"] * w / 1920
    body_size = rules["font_pdf_pt"]["body"]
    header = (
        geom["header"]
        if geom["header"] is not None
        else (model or {}).get("header_fraction", 0) * h
    )
    footer = (
        geom["footer"]
        if geom["footer"] is not None
        else (model or {}).get("footer_fraction", 1) * h
    )
    candidates = [
        l for l in lines if l["bbox"][1] > header + tol and l["bbox"][3] < footer - tol
    ]
    # A cover is a centered typographic composition with no left-rail title.
    # This test is positional; the title words and font size do not select it.
    first = min(candidates, key=lambda l: l["bbox"][1]) if candidates else None
    cover = bool(
        first
        and abs((first["bbox"][0] + first["bbox"][2]) / 2 - w / 2) <= tol
        and not geom["images"]
        and not geom["tables"]
    )
    if model:
        title_band = [v * h for v in model["title_band_fraction"]]
    else:
        # Calibration bootstrap: first bold line at the left rail is title.
        title_band = (
            [first["bbox"][1] - tol, first["bbox"][3] + tol]
            if first and not cover
            else [0, 0]
        )
    code = code_lines(lines, geom, rules)
    for index, l in enumerate(lines):
        r = l["bbox"]
        if r[1] < header:
            role = "navigation"
        elif l["baseline"] >= footer:
            role = "footer"
        elif cover:
            # Vertical bins are calibrated from the cover composition.
            role = "cover"
        elif (
            title_band[0] - tol <= r[1] <= title_band[1] + tol
            and "bold" in l["font"].lower()
        ):
            role = "frame_title"
        elif index in code:
            role = "code"
        elif any(
            intersection(r, table) > 0
            and table[1] - tol <= l["baseline"] <= table[3] + tol
            for table in geom["tables"]
        ):
            role = "table"
        elif (
            any(
                0
                <= r[1] - obj[3]
                <= rules["semantic_spacing"]["caption_to_body"]["target"][1]
                and r[0] >= obj[0] - tol
                and r[2] <= obj[2] + tol
                for obj in geom["images"] + geom["tables"]
            )
            and l["size"] < (body_size + rules["font_pdf_pt"]["caption"]) / 2
        ):
            role = "caption"
        elif normalized(l["text"]).casefold() == "questions?":
            # Semantic role literal from YAML CLOSE, not page identity.
            role = "closing_question"
        elif l["plain_chars"] < sum(len(s["text"]) for s in l["spans"]) / 2:
            role = "math"
        elif l["plain_chars"] <= rules["limits"]["short_token_chars"]:
            role = "short_label"
        else:
            role = "body"
        l["role"] = role
        # Math glyphs/subscripts use separate metrics and cannot safely be
        # assigned an ordinary body font role by size alone.
        for s in l["spans"]:
            s["role"] = (
                "math"
                if "math" in s["font"].lower() and role not in {"footer", "navigation"}
                else role
            )
    # Multi-line captions continue within the same extracted PDF block and
    # style. Underbrace annotations are mathematical labels, not body prose.
    caption_blocks = {l["block"]: l["size"] for l in lines if l["role"] == "caption"}
    math_blocks = {l["block"] for l in lines if any(c in l["text"] for c in ("⏟", "⏞"))}
    for l in lines:
        if l["role"] in {"body", "short_label"}:
            if l["block"] in math_blocks:
                l["role"] = "math"
            elif (
                l["block"] in caption_blocks
                and abs(l["size"] - caption_blocks[l["block"]])
                <= rules["limits"]["font_tolerance_pt"]
            ):
                l["role"] = "caption"
            for s in l["spans"]:
                if s["role"] != "math":
                    s["role"] = l["role"]
    geom["tables"] = [
        t
        for t in geom["tables"]
        if any(l["role"] == "table" and intersection(l["bbox"], t) > 0 for l in lines)
    ]
    return cover


def column_measure(lines, geom, body_top, rules):
    """Find central whitespace gutter without a supplied object mapping.

    Presets and nearby object edges seed the search. Complete blocks then
    extend each supported column, including wider, non-preset explanations.
    Shared introductions/transitions stay outside the pair.
    """
    w = geom["width"]
    tol = rules["limits"]["optical_px"] * w / 1920
    footer = geom["footer"] or geom["height"]
    blocks = {}
    for l in lines:
        if l["role"] not in {"footer", "navigation", "frame_title"}:
            blocks.setdefault(l["block"], []).append(l["bbox"])
    # Broad prose/table groups are shared introductions/transitions. A short
    # final line in such a group must not become a spurious left column.
    rails = [
        min(
            [l["bbox"][0] for l in lines if l["role"] not in {"footer", "navigation"}]
            or [0]
        ),
        max(
            [l["bbox"][2] for l in lines if l["role"] not in {"footer", "navigation"}]
            or [w]
        ),
    ]
    body_width = rails[1] - rails[0]
    widest = max(max(p) for p in rules["column_presets"].values()) * body_width
    block_bounds = {key: union(rs) for key, rs in blocks.items()}
    text_objects = [
        (l["bbox"], l["role"], block_bounds[l["block"]])
        for l in lines
        if l["role"] in {"body", "code", "caption", "math", "short_label"}
        and l["bbox"][1] >= body_top
        and l["bbox"][3] < footer
    ]
    tagged = (
        text_objects
        + [(r, "image", r) for r in geom["images"]]
        + [(r, "table", r) for r in geom["tables"]]
    )
    tagged += [(r, "diagram", r) for r in geom["vectors"] if r[3] - r[1] > tol]
    tagged = [
        (r, k, block) for r, k, block in tagged if r[1] >= body_top and r[3] < footer
    ]
    seeds = [
        (r, k, block)
        for r, k, block in tagged
        if r[2] - r[0] <= widest + tol and block[2] - block[0] <= widest + tol
    ]
    candidates = []
    centres = [
        rails[0] + (p[0] + (1 - sum(p)) / 2) * body_width
        for p in rules["column_presets"].values()
    ]
    edges = sorted({r[0] for r, _, _ in seeds} | {r[2] for r, _, _ in seeds})
    centres += [
        (a + b) / 2
        for a, b in pairwise(edges)
        if b - a > 2 * tol and min(centres) - tol <= (a + b) / 2 <= max(centres) + tol
    ]
    for cx in centres:
        left = [r for r, _, block in seeds if block[2] < cx - tol]
        right = [r for r, _, block in seeds if block[0] > cx + tol]
        if not left or not right:
            continue
        lb, rb = union(left), union(right)
        shared_blocks = [
            block
            for _, _, block in tagged
            if block[0] < cx - tol
            and block[2] > cx + tol
            and (
                block[1] > max(lb[3], rb[3]) + tol or block[3] < min(lb[1], rb[1]) - tol
            )
        ]
        # The width preset limits initial inference, never final measurement.
        # Include whole blocks extending a supported side while respecting the
        # opposite side's visible edge. A shared full-width block fits neither.
        left = [
            r
            for r, _, block in tagged
            if block not in shared_blocks
            and block[2] < rb[0] - tol
            and block[0] <= lb[2]
        ]
        right = [
            r
            for r, _, block in tagged
            if block not in shared_blocks
            and block[0] > lb[2] + tol
            and block[2] >= rb[0]
        ]
        lb, rb = union(left), union(right)
        if lb[2] + 2 * tol >= rb[0]:
            continue
        if not lb[2] + tol < cx < rb[0] - tol:
            cx = (lb[2] + rb[0]) / 2
        overlap = min(lb[3], rb[3]) - max(lb[1], rb[1])
        if overlap < rules["font_pdf_pt"]["body"]:
            continue
        # One isolated label is not a column. An image can provide its own
        # support; otherwise require multiple lines (the minimum is two).
        if len(left) < 2 and lb not in geom["images"]:
            continue
        if len(right) < 2 and rb not in geom["images"]:
            continue
        # Gutter persists through the shared vertical interval. Crossing prose
        # inside that interval makes the proposed split ambiguous.
        crossing = [
            r
            for r, _, _ in tagged
            if r[0] < cx - tol
            and r[2] > cx + tol
            and max(lb[1], rb[1]) + tol < (r[1] + r[3]) / 2 < min(lb[3], rb[3]) - tol
        ]
        if crossing:
            continue
        # The frozen exception requires a shared full-width object *below*
        # both columns. Keep its short wrapped lines out of either column and
        # retain the visible transition/gap for role/spacing review.
        shared_objects = list(block_bounds.values()) + geom["images"] + geom["tables"]
        shared_objects += [r for r in geom["vectors"] if r[3] - r[1] > tol]
        shared = [
            r
            for r in shared_objects
            if r[0] < cx - tol
            and r[2] > cx + tol
            and r[1] >= max(lb[3], rb[3]) + tol
            and r[3] < footer
        ]
        full_width = min(shared, key=lambda r: r[1]) if shared else None
        candidates.append(
            {
                "split_fraction": cx / w,
                "left": lb,
                "right": rb,
                "left_count": len(left),
                "right_count": len(right),
                "bottom_delta_px": abs(lb[3] - rb[3]) * 1920 / w,
                "top_delta_px": abs(lb[1] - rb[1]) * 1920 / w,
                "overlap_pt": overlap,
                "full_width_below": full_width,
                "full_width_gap_pt": full_width[1] - max(lb[3], rb[3])
                if full_width
                else None,
                "kind": "/".join(
                    next(
                        (
                            role
                            for role in ("image", "code", "table", "diagram")
                            if any(k == role and r in side for r, k, _ in tagged)
                        ),
                        "text",
                    )
                    for side in (left, right)
                ),
            }
        )
    return max(candidates, key=lambda c: c["overlap_pt"]) if candidates else None


def line_pairs(lines, rules):
    out = []
    merge = rules["limits"]["optical_px"] * 453.54 / 1920
    for role in ("body", "code", "caption"):
        blocks = sorted({l["block"] for l in lines if l["role"] == role})
        for b in blocks:
            group = sorted(
                [l for l in lines if l["role"] == role and l["block"] == b],
                key=lambda l: l["baseline"],
            )
            for a, z in pairwise(group):
                if (
                    min(a["bbox"][2], z["bbox"][2]) - max(a["bbox"][0], z["bbox"][0])
                    <= 0
                ):
                    continue
                dy = z["baseline"] - a["baseline"]
                if dy <= merge:
                    continue
                # Identify wraps using normal leading + maximum list separation
                # from YAML. Larger paragraph/semantic gaps are not leading.
                target = rules["font_tex_baselines_pt"][role] * 72 / 72.27
                if (
                    dy
                    <= target
                    + rules["list_contract"]["teaching_list_itemsep_tex_pt_range"][1]
                ):
                    out.append(
                        {
                            "role": role,
                            "delta_pt": dy,
                            "bullet": z["bullet"],
                            "a": a["bbox"],
                            "b": z["bbox"],
                            "block": b,
                        }
                    )
    return out


def otsu(hist):
    hist = np.asarray(hist, dtype=float)
    total = hist.sum()
    if not total:
        return 128
    p = hist / total
    omega = np.cumsum(p)
    mu = np.cumsum(p * np.arange(256))
    denom = omega * (1 - omega)
    score = np.divide(
        (mu[-1] * omega - mu) ** 2, denom, out=np.zeros(256), where=denom > 0
    )
    return int(np.argmax(score))


def raster_stats(page, geom, lines, model, rules, render_path=None):
    w, h = geom["width"], geom["height"]
    pix = page.get_pixmap(
        matrix=pdf.Matrix(1920 / w, 1080 / h), alpha=False, colorspace=pdf.csRGB
    )
    if render_path:
        pix.save(str(render_path))
    rgb = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width, 3)
    gray = np.min(rgb, axis=2)
    hist = np.bincount(gray.ravel(), minlength=256)
    threshold = model["ink_threshold"] if model else otsu(hist)
    ink = gray <= threshold
    footer = geom["footer"] or (model or {}).get("footer_fraction", 1) * h
    title = [l["bbox"][3] for l in lines if l["role"] == "frame_title"]
    body = [
        l["bbox"]
        for l in lines
        if l["role"] not in {"frame_title", "navigation", "footer"}
    ]
    top = max(title) if title else (geom["header"] or 0)
    objs = body + geom["images"] + geom["vectors"]
    objs = [r for r in objs if r[1] >= top and r[3] < footer]
    bounds = union(objs)
    y0, y1 = math.ceil(top * 1080 / h), math.floor(footer * 1080 / h)
    crop = ink[y0:y1, :]
    half = len(crop) // 2
    upper, lower = crop[:half], crop[half:]
    occupied_rows = crop.any(axis=1)
    result = {
        "body_top": top,
        "body_bottom": footer,
        "occupancy": (bounds[3] - top) / (footer - top)
        if bounds and footer > top
        else None,
        "top_density": float(upper.mean()) if upper.size else 0,
        "bottom_density": float(lower.mean()) if lower.size else 0,
        "occupied_row_fraction": float(occupied_rows.mean())
        if occupied_rows.size
        else 0,
        "body_bounds": bounds,
        "ink_histogram": hist.tolist(),
    }
    # The concentration ratio distinguishes a top-heavy short composition
    # from a genuinely sparse page. It has no free pixel/ink threshold.
    upper_ink = int(upper.sum())
    total_ink = upper_ink + int(lower.sum())
    result["upper_ink_fraction"] = upper_ink / total_ink if total_ink else None
    # Crop group ink below the divider, excluding the divider itself by its
    # measured half-stroke width + YAML boundary tolerance.
    fy = min(pix.height, math.ceil(footer * 1080 / h) + rules["limits"]["boundary_px"])
    footer_lines = [l for l in lines if l["role"] == "footer"]
    groups = {
        "left": [l for l in footer_lines if l["bbox"][0] < w / 2],
        "counter": [l for l in footer_lines if re.search(r"\d\s*/\s*\d", l["text"])],
        "right": [l for l in footer_lines if l["bbox"][0] >= w / 2],
    }
    if geom["footer_controls"]:
        # Measure the actual vector controls separately from the page counter.
        groups["right"] = [{"bbox": union(geom["footer_controls"])}]
    if geom["footer_controls"]:
        groups["right"] = [{"bbox": r} for r in geom["footer_controls"]]
    centers = {}
    for name, members in groups.items():
        if not members:
            continue
        rect = union([l["bbox"] for l in members])
        x0 = max(0, math.floor(rect[0] * 1920 / w))
        x1 = min(pix.width, math.ceil(rect[2] * 1920 / w))
        sub = ink[fy:, x0:x1]
        yy = np.where(sub.any(axis=1))[0]
        if len(yy):
            centers[name] = (float(yy.min() + yy.max()) / 2 + fy) - (
                footer * 1080 / h + 1080
            ) / 2
    result["footer_center_offsets_px"] = centers
    return result


def measure(page, rules, model=None, render_path=None):
    geom = geometry(page, rules)
    lines = extract_lines(page, rules)
    cover = classify(lines, geom, rules, model)
    raster = raster_stats(page, geom, lines, model, rules, render_path)
    col = None if cover else column_measure(lines, geom, raster["body_top"], rules)
    layout = (
        "cover"
        if cover
        else "columns"
        if col
        else "image"
        if geom["images"]
        else "table"
        if geom["tables"]
        else "text"
    )
    return {
        "geometry": geom,
        "lines": lines,
        "raster": raster,
        "line_pairs": line_pairs(lines, rules),
        "columns": col,
        "layout": layout,
    }


def footer_text(measurement):
    w = measurement["geometry"]["width"]
    ls = sorted(
        [
            l
            for l in measurement["lines"]
            if l["role"] == "footer" and l["bbox"][0] < w / 2
        ],
        key=lambda l: (l["baseline"], l["bbox"][0]),
    )
    return normalized(" ".join(l["text"] for l in ls))


def footer_kind(measurement):
    if measurement["layout"] == "cover":
        return "cover"
    return "source" if footer_text(measurement) else "plain"
