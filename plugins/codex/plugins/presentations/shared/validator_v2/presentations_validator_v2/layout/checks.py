import math
import re

from ..io import EvidenceMissing, InputError, records, unique_ids
from ..render import Rect, union
from .model import EPS, MM, TEX, check, number, route


def compact_font(name):
    return re.sub(r"[^a-z0-9]", "", re.sub(r"^[A-Z]{6}\+", "", name).lower())


TYPE_ROLES = {
    "paragraph": "body", "list_item": "body", "interpretation": "body",
    "question_label": "subhead", "question_body": "body", "answer_label": "subhead",
    "answer_body": "body", "table_cell": "table", "table_header": "table",
    "table_note": "caption", "source_credit": "footer", "footer_credit": "footer",
    "slide_number": "footer", "closing_headline": "subhead", "closing_takeaway": "body",
    "section_label": "section_nav", "diagram_label": "body", "display_math": "body",
}
BODY_ROLES = {"body", "subhead", "paragraph", "list_item", "interpretation", "code",
              "table", "table_cell", "table_header", "table_note", "caption", "figure",
              "display_math", "question_label", "question_body", "question_rule",
              "answer_label", "answer_body", "answer_rule", "diagram_label", "node",
              "connector", "closing_headline", "closing_takeaway", "closing_question"}
CHROME_ROLES = {"frame_title", "footer_divider", "footer_credit", "source_credit",
                "slide_nav", "section_nav", "section_label", "slide_number",
                "brand", "background"}


def typography(page, contract):
    rows = []
    for key, obj in page.objects.items():
        if not obj.lines:
            continue
        role = TYPE_ROLES.get(obj.role, obj.role)
        if obj.role in {"brand", "slide_nav"}:
            continue
        tokens = contract["typography"]
        if role not in tokens:
            rows.append(route("TYPE", "NOT_VERIFIED", key, "Rendered text has no type token"))
            continue
        token = tokens[role]
        fonts = contract["fonts"]
        bad = []
        for line in obj.lines:
            for span in line.spans:
                flags = span["flags"]
                if role == "code":
                    names = ("code",)
                elif obj.role == "display_math":
                    names = ("math", "math_cal")
                elif re.search(r"[\u3400-\u9fff\uf900-\ufaff]", span["text"]):
                    names = ("cjk_serif", "cjk_sans")
                else:
                    names = ("latin",)
                font = compact_font(span["font"])
                size_ok = abs(span["size"] - token["pdf_pt"]) <= token["tolerance_pdf_pt"] + EPS
                weight_ok = token.get("weight") != "bold" or flags & 16
                if not (size_ok and weight_ok
                        and any(font.startswith(compact_font(fonts[name])) for name in names)):
                    bad.append({"font": span["font"], "size": span["size"], "flags": flags})
        rows.append(check("TYPE", not bad, key, "Font family, size and weight", mismatches=bad))
        if role in {"body", "caption", "table", "code"} and len(obj.lines) > 1:
            baselines = sorted(line.baseline for line in obj.lines)
            gaps = [b - a for a, b in zip(baselines, baselines[1:])]
            expected = token["leading_pt"] * TEX
            rows.append(check("TYPE", min(gaps) + token["tolerance_pdf_pt"] >= expected - EPS,
                              key, "Multiline leading is not compressed", gaps_pdf_pt=gaps))
    return rows


def rail(page, contract):
    bounds = page.render.bounds
    geometry = contract["geometry"]
    rail_box = Rect(bounds.x0 + geometry["body_margin_left_mm"] * MM, bounds.y0,
                    bounds.x1 - geometry["body_margin_right_mm"] * MM, bounds.y1)
    results = [check("RAIL", abs(bounds.width / bounds.height - 16 / 9) <= 0.002,
                     page.id, "PDF page follows the 16:9 geometry")]
    body = [obj for obj in page.objects.values() if obj.role in BODY_ROLES]
    footer = page.by_role("footer_divider")
    if footer:
        rail_box = Rect(rail_box.x0, rail_box.y0, rail_box.x1, footer[0].box.y0)
    for obj in body:
        results.append(check("RAIL", rail_box.contains(obj.box, 2 * page.px), obj.spec["id"],
                             "Body stays inside the protected rail and footer boundary"))
    for obj in page.objects.values():
        if obj.role not in BODY_ROLES | CHROME_ROLES:
            results.append(route("RAIL", "NOT_VERIFIED", obj.spec["id"], "Unknown semantic role"))
    return results


def spacing(page, contract):
    thresholds = contract["spacing_pdf_pt"]
    rows = []
    pairs = set()
    relations = records(page.spec["spacing"])
    for rel in relations.values():
        first, second = page.get(rel["from"]), page.get(rel["to"])
        key = rel["relation"]
        if key in thresholds:
            token = thresholds[key]
        elif key == "title_to_question" and "title_to_question" in page.spec.get("extra_spacing", {}):
            token = page.spec["extra_spacing"][key]
        else:
            raise InputError(f"Unknown spacing relation {key}")
        pair = (first.spec["id"], second.spec["id"])
        if pair in pairs:
            raise InputError("Repeated spacing relation for object pair")
        pairs.add(pair)
        gap = second.box.y0 - first.box.y1
        low, high = token["target"]
        status = ("FAIL" if gap < token["fail_below"] - EPS else
                  "PASS" if low - EPS <= gap <= high + EPS else "REVIEW")
        rows.append(route("SPACE", status, rel["id"], key, measured_pdf_pt=gap,
                          fail_below=token["fail_below"], target_pdf_pt=token["target"]))
    return rows


def columns(page, contract):
    rows = []
    tolerance = contract["columns"]["optical_anchor_tolerance_px"] * page.px
    geometry = contract["geometry"]
    available = page.render.bounds.width - (geometry["body_margin_left_mm"]
                                             + geometry["body_margin_right_mm"]) * MM
    for column_id, spec in records(page.spec.get("columns", [])).items():
        ordered = spec["groups"]
        groups = [union(page.get(name).box for name in unique_ids(group)) for group in ordered]
        if len(groups) < 2:
            raise InputError("Column group must contain at least two columns")
        preset = spec.get("preset")
        approved = contract["columns"].get(preset)
        resolved = isinstance(approved, list) and len(approved) == len(groups)
        gaps = [right.x0 - left.x1 for left, right in zip(groups, groups[1:])]
        rows.append(check("COLUMN", min(gaps) > 0, column_id, "Visible gutter", gaps_pdf_pt=gaps))
        if not resolved:
            rows.append(route("COLUMN", "REVIEW", column_id, "Custom columns require visual review"))
            continue
        rows.append(check("COLUMN", all(group.width <= fraction * available + tolerance
                                        for group, fraction in zip(groups, approved)),
                          column_id, "Content fits approved column preset"))
        if spec.get("anchor") == "baseline":
            anchors = [min(line.baseline for name in group for line in page.get(name).lines)
                       for group in ordered]
        elif spec.get("anchor") == "top":
            anchors = [group.y0 for group in groups]
        else:
            raise EvidenceMissing("Peer columns lack an optical anchor")
        rows.append(check("COLUMN", max(anchors) - min(anchors) <= tolerance + EPS,
                          column_id, "Optical peer anchors"))
        bottoms = [group.y1 for group in groups]
        if max(bottoms) - min(bottoms) > tolerance:
            rows.append(route("COLUMN", "REVIEW", column_id, "Review peer column bottom balance"))
        if spec.get("following_full_width"):
            page.get(spec["following_full_width"])
            rows.append(route("COLUMN", "REVIEW", column_id, "Review prose below columns"))
    return rows


def captions(page, contract):
    rows = []
    token = contract["caption"]
    tolerance = token["left_anchor_tolerance_px"] * page.px
    for obj in page.by_role("caption", "table_note"):
        owner = page.get(obj.spec.get("owner"))
        acceptable = owner.role in {"figure", "table", "node"}
        aligned = bool(obj.lines) and all(abs(line.box.x0 - owner.box.x0) <= tolerance + EPS
                                          for line in obj.lines)
        rows.append(check("CAPTION", acceptable and aligned and obj.box.y0 >= owner.box.y1 - EPS,
                          obj.spec["id"], "Caption below and left aligned to owned object"))
    for obj in page.by_role("figure", "table"):
        if obj.spec.get("caption_required"):
            rows.append(check("CAPTION", any(cap.spec.get("owner") == obj.spec["id"]
                                              for cap in page.by_role("caption", "table_note")),
                              obj.spec["id"], "Required caption exists with the correct role"))
    return rows


def styled(obj, flag, needed=True):
    return bool(obj.lines) and all(bool(span["flags"] & flag) == needed
                                   for line in obj.lines for span in line.spans)


def qa(page, contract):
    rows = []
    for section_id, spec in records(page.spec.get("qa", [])).items():
        kind = spec["kind"]
        if kind not in {"question", "answer"}:
            raise InputError("Unknown question/answer component")
        label, body, rule = (page.get(spec[key]) for key in ("label", "body", "rule"))
        good_roles = (label.role, body.role, rule.role) == tuple(
            f"{kind}_{role}" for role in ("label", "body", "rule")
        )
        edges = [segment for drawing in rule.drawings for segment in drawing.segments]
        line = edges[0] if len(edges) == 1 else None
        accent = spec.get("accent_rgb")
        if accent is None:
            raise EvidenceMissing("Question/answer accent color lacks a frozen value")
        accent_ok = bool(rule.drawings) and all(
            d.color is not None and math.dist(d.color, accent) <= 0.03 for d in rule.drawings
        )
        relative = rule.box.x1 <= body.box.x0 + EPS and label.box.x0 >= rule.box.x0
        endpoints = False
        if line:
            (ax, ay), (bx, by) = line
            top, bottom = sorted((ay, by))
            target_top = body.box.y0 if kind == "answer" else min(body.box.y0, label.box.y0)
            start = contract["qa"]["answer_rule_top_to_body_tolerance_px"] * page.px
            end = contract["qa"]["answer_rule_bottom_to_body_tolerance_px"] * page.px
            endpoints = (abs(ax - bx) <= start and abs(top - target_top) <= start + EPS
                         and abs(bottom - body.box.y1) <= end + EPS)
        outside = kind != "answer" or label.box.y1 <= rule.box.y0 + EPS
        rows.append(check("QA", good_roles and styled(label, 16)
                          and styled(body, 2, kind == "question")
                          and relative and endpoints and outside and accent_ok,
                          section_id, "Label, body style and continuous accent rule endpoints"))
    declared = {name for spec in page.spec.get("qa", []) for name in
                (spec["label"], spec["body"], spec["rule"])}
    undeclared = {obj.spec["id"] for obj in page.by_role(*(
        f"{kind}_{role}" for kind in ("question", "answer") for role in ("body", "label", "rule")
    ))} - declared
    if undeclared:
        rows.append(route("QA", "NOT_VERIFIED", page.id, "Unbound Q/A objects",
                          objects=sorted(undeclared)))
    return rows


def footer(page, contract):
    if not page.spec.get("footer"):
        if page.spec.get("footer_exempt") and not page.by_role(
            "footer_divider", "footer_credit", "source_credit", "slide_number", "slide_nav"
        ):
            return []
        raise EvidenceMissing("Page lacks footer geometry or an explicit exemption")
    spec = page.spec["footer"]
    band = Rect.from_value(spec["band"])
    credit = page.one(spec["credit_role"])
    divider = page.one("footer_divider")
    nav = page.by_role("slide_nav", "section_nav", "section_label")
    number_obj = page.one("slide_number")
    inset = number(spec["inset_pdf_pt"], "footer inset")
    tolerance = contract["footer"]["left_credit_center_tolerance_px"] * page.px
    good = (spec["credit_role"] in {"footer_credit", "source_credit"} and inset >= 0
            and page.render.bounds.contains(band)
            and bool(divider.drawings) and abs(divider.box.y0 - band.y0) <= 2 * page.px
            and divider.box.height <= 2 * page.px
            and divider.box.x0 <= band.x0 + 2 * page.px
            and divider.box.x1 >= band.x1 - 2 * page.px
            and all(band.contains(obj.box, 2 * page.px) for obj in (credit, number_obj, *nav))
            and abs(credit.box.cy - band.cy) <= tolerance + EPS
            and abs(credit.box.x0 - band.x0 - inset) <= 2 * page.px
            and abs(band.x1 - number_obj.box.x1 - inset) <= 2 * page.px
            and abs(number_obj.box.cy - band.cy) <= 2 * page.px
            and number_obj.texts == [spec["page_label"]])
    if contract["footer"]["native_navigation_required"]:
        good = good and bool(nav) and all(
            credit.box.x1 < item.box.x0 and item.box.x1 < number_obj.box.x0
            and any(link.intersects(item.box) and band.contains(link, 2 * page.px)
                    for link in page.render.links)
            for item in nav
        )
    return [check("FOOTER", good, page.id,
                  "Footer band, source/identity placement, page counter and internal links")]


def section_nav(page, contract, section_counts):
    labels = page.by_role("section_label")
    if not labels:
        return []
    config = contract["section_navigation"]
    token = config["width_cap"]
    rows = []
    maximum = max(section_counts.values())
    ids = unique_ids([obj.spec["section"] for obj in labels])
    if ids != section_counts.keys():
        rows.append(check("SECTION_NAV", False, page.id, "Exact sections have one visible label each"))
    for obj in labels:
        if obj.spec["section"] not in section_counts:
            raise InputError("Section label references an unknown section")
        cap = token["base_pdf_pt"] + token["page_weight_pdf_pt"] * section_counts[obj.spec["section"]] / maximum
        ratio = obj.box.width / cap
        status = ("FAIL" if len(obj.lines) != 1 or ratio > token["fail_utilization"] + EPS
                  else "REVIEW" if ratio >= token["review_utilization"] - EPS else "PASS")
        rows.append(route("SECTION_NAV", status, obj.spec["id"], "Single-line width budget",
                          utilization=ratio, cap_pdf_pt=cap))
    ordered = sorted(labels, key=lambda obj: obj.box.x0)
    for left, right in zip(ordered, ordered[1:]):
        px_gap = (right.box.x0 - left.box.x1) / page.px
        rows.append(check("SECTION_NAV", px_gap >= config["neighbor_gap_px_min"] - EPS,
                          left.spec["id"], "Visible neighboring label gap", gap_px=px_gap))
    return rows


def tables(page, contract):
    rows = []
    cells = page.by_role("table_cell", "table_header")
    for cell in cells:
        owner = page.get(cell.spec["owner"])
        region = Rect.from_value(cell.spec["region"])
        atoms = cell.spec["atoms"]
        if not isinstance(atoms, list) or not atoms or any(not isinstance(x, str) or not x for x in atoms):
            raise InputError("Table cell needs nonempty semantic atoms")
        normalized = [" ".join(text.split()) for text in cell.texts]
        approved_header_lines = cell.spec.get("approved_header_lines")
        if cell.role == "table_header" and approved_header_lines is not None:
            wrapping = normalized == approved_header_lines
        else:
            wrapping = all(any(" ".join(atom.split()) in line for line in normalized) for atom in atoms)
        rows.append(check("TABLE", wrapping and owner.role == "table"
                          and owner.box.contains(region, 2 * page.px)
                          and region.contains(cell.box, 2 * page.px),
                          cell.spec["id"], "Intentional wraps, unbroken atoms and cell region"))
    for table in page.by_role("table"):
        owned = [cell for cell in cells if cell.spec.get("owner") == table.spec["id"]]
        if not owned:
            rows.append(route("TABLE", "NOT_VERIFIED", table.spec["id"], "No cell bindings"))
        if table.spec.get("booktabs") is True:
            rows.append(check("TABLE", not any(abs(a[0] - b[0]) < EPS and abs(a[1] - b[1]) > 2 * page.px
                                              for d in table.drawings for a, b in d.segments),
                              table.spec["id"], "Booktabs table has no vertical rules"))
    return rows


def closing(page, contract):
    archetype = page.spec.get("closing")
    if not archetype:
        if page.by_role("closing_question", "closing_headline", "closing_takeaway"):
            raise EvidenceMissing("Closing roles lack an authorized archetype")
        return []
    if archetype != "substantive":
        return [route("CLOSING", "REVIEW", page.id, "Nonstandard closing archetype")]
    token = contract["closing"]
    body = Rect.from_value(page.spec["body_region"])
    cue = page.one("closing_question")
    upper = page.by_role("closing_headline", "closing_takeaway")
    if body.height <= 0:
        raise InputError("Closing body region is empty")
    fraction = (cue.box.cy - body.y0) / body.height
    split = body.y0 + body.height * token["upper_fraction"]
    margin = token["body_margin_mm"] * MM
    aligned = abs(cue.box.cx - body.cx) <= 2 * page.px + EPS
    margin_ok = (abs(body.x0 - margin) <= 2 * page.px
                 and abs(page.render.bounds.x1 - body.x1 - margin) <= 2 * page.px)
    return [check("CLOSING", abs(fraction - token["questions_center_body_fraction"])
                  <= token["questions_center_tolerance_fraction"] + EPS
                  and bool(upper) and all(obj.box.y1 <= split for obj in upper)
                  and cue.box.y0 >= split and body.contains(cue.box) and aligned and margin_ok,
                  page.id, "Normal rail and split with centered closing cue", center_fraction=fraction)]


def line_crosses_rect(start, end, rect):
    """Whether the open segment traverses the interior of the rectangle."""
    low, high = 0.0, 1.0
    for a, b, left, right in zip(start, end, (rect.x0, rect.y0), (rect.x1, rect.y1)):
        velocity = b - a
        if abs(velocity) <= EPS:
            if not left + EPS < a < right - EPS:
                return False
            continue
        first, last = sorted(((left - a) / velocity, (right - a) / velocity))
        low, high = max(low, first), min(high, last)
    return high - low > EPS


def segments_cross(first, second):
    def orientation(a, b, c):
        return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])

    a, b = first
    c, d = second
    return orientation(a, b, c) * orientation(a, b, d) < -EPS and (
        orientation(c, d, a) * orientation(c, d, b) < -EPS
    )


def diagram(page, contract):
    rows = []
    token = contract["diagram"]
    tolerance = token["boundary_tolerance_px"] * page.px
    nodes = page.by_role("node")
    lines = {}
    lengths = {}
    for obj in page.by_role("connector"):
        start, end = (page.get(obj.spec[name]) for name in ("from", "to"))
        shaft = [segment for drawing in obj.drawings for segment in drawing.segments]
        if not shaft or start.role != "node" or end.role != "node":
            raise EvidenceMissing("Connector lacks measurable shaft or node binding")
        segment = max(shaft, key=lambda line: math.dist(*line))
        lines[obj.spec["id"]] = segment
        a, b = segment
        direct = max(start.box.distance_to_boundary(*a), end.box.distance_to_boundary(*b))
        reverse = max(start.box.distance_to_boundary(*b), end.box.distance_to_boundary(*a))
        length = math.dist(a, b)
        lengths[obj.spec["id"]] = length
        third_party = [other.box for other in nodes if other not in (start, end)]
        text_boxes = [line.box for other in page.objects.values() for line in other.lines]
        obstructed = any(line_crosses_rect(a, b, box) for box in (*third_party, *text_boxes))
        rows.append(check("DIAGRAM", min(direct, reverse) <= tolerance + EPS and not obstructed,
                          obj.spec["id"], "Connector touches node boundaries and avoids content"))
        if obj.spec.get("ordered_process", True):
            mm = length / MM
            status = ("FAIL" if mm < token["shaft_fail_below_mm"] - EPS else
                      "REVIEW" if mm < token["shaft_review_below_mm"] - EPS else "PASS")
            rows.append(route("DIAGRAM", status, obj.spec["id"], "Visible process shaft", shaft_mm=mm))
    for obj in nodes:
        style = obj.spec["style"]
        label = page.get(obj.spec["label"])
        padding = number(style["min_padding_pdf_pt"], "node padding")
        b = obj.box
        inner = Rect(b.x0 + padding, b.y0 + padding, b.x1 - padding, b.y1 - padding)
        color = style["stroke_rgb"]
        valid_style = padding >= 0 and bool(obj.drawings) and all(
            d.color is not None and math.dist(color, d.color) <= 0.03
            and d.width is not None and abs(d.width - style["stroke_pdf_pt"]) <= 0.1
            for d in obj.drawings
        )
        rows.append(check("DIAGRAM", valid_style and inner.contains(label.box, tolerance),
                          obj.spec["id"], "Node style and rendered label padding"))
    connectors = page.by_role("connector")
    for index, first in enumerate(connectors):
        for second in connectors[index + 1:]:
            a, b = first.spec["id"], second.spec["id"]
            if segments_cross(lines[a], lines[b]):
                permitted = b in first.spec.get("intentional_crossings", []) and (
                    a in second.spec.get("intentional_crossings", []))
                rows.append(route("DIAGRAM", "REVIEW" if permitted else "FAIL", f"{a}/{b}",
                                  "Connectors cross"))
            peer = first.spec.get("peer_group")
            if peer is not None and peer == second.spec.get("peer_group"):
                together = abs(lengths[a] - lengths[b]) <= token["peer_length_tolerance_px"] * page.px
                rows.append(check("DIAGRAM", together, f"{a}/{b}", "Peer connector lengths"))
    return rows


def density(page, contract):
    rows = []
    body = [obj for obj in page.objects.values() if obj.role in BODY_ROLES]
    bounds = page.render.bounds
    for obj in page.objects.values():
        if not bounds.contains(obj.box, page.px):
            rows.append(check("DENSITY_WHITESPACE", False, obj.spec["id"], "Object exceeds page bounds"))
    exclusive_roles = BODY_ROLES - {"table", "node", "connector", "question_rule", "answer_rule"}
    exclusive = [obj for obj in body if obj.role in exclusive_roles]
    for index, a in enumerate(exclusive):
        for b in exclusive[index + 1:]:
            if a.box.intersects(b.box):
                width = min(a.box.x1, b.box.x1) - max(a.box.x0, b.box.x0)
                height = min(a.box.y1, b.box.y1) - max(a.box.y0, b.box.y0)
                if min(width, height) > 2 * page.px:
                    allowed = b.spec["id"] in a.spec.get("intentional_overlap", []) and (
                        a.spec["id"] in b.spec.get("intentional_overlap", []))
                    rows.append(route("DENSITY_WHITESPACE", "REVIEW" if allowed else "FAIL",
                                      f"{a.spec['id']}/{b.spec['id']}", "Rendered objects overlap"))
    if not body:
        return [*rows, route("DENSITY_WHITESPACE", "REVIEW", page.id, "Review page substance")]
    region = Rect.from_value(page.spec.get("body_region", (
        bounds.x0, bounds.y0, bounds.x1, bounds.y1
    )))
    end = region.y0
    largest_gap = 0
    for b in sorted((obj.box for obj in body), key=lambda r: r.y0):
        largest_gap = max(largest_gap, b.y0 - end)
        end = max(end, b.y1)
    lower_void = max(0, region.y1 - end)
    floor = page.spec.get("primary_min_size_pdf_pt")
    primary = [obj for obj in body if obj.spec.get("primary")]
    if floor is not None and not primary:
        raise EvidenceMissing("A primary object minimum was declared without its rendered object")
    undersized = floor is not None and any(
        obj.box.width < floor[0] - EPS or obj.box.height < floor[1] - EPS for obj in primary
    )
    if undersized:
        rows.append(check("DENSITY_WHITESPACE", False, page.id,
                          "Primary object is below the independently declared size floor"))
    rows.append(route("DENSITY_WHITESPACE", "REVIEW", page.id,
                      "Rendered balance and reading load require review",
                      internal_void_pdf_pt=largest_gap, lower_void_pdf_pt=lower_void,
                      semantic_blocks=len(body)))
    return rows
