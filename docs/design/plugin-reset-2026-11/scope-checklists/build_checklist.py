#!/usr/bin/env python3
"""Render the shared scope-checklist YAML schema without changing its wording.

Usage: python build_checklist.py INPUT.yaml OUTPUT.pdf
Dependencies: WeasyPrint >= 63, PyYAML, pypdf >= 5, PyMuPDF.
Optional: --font-regular FILE --font-bold FILE (Noto/Source Han SC).
Writes OUTPUT.pdf and previews/page-N.png beside it; prints mechanical QA as JSON.
No HTML, selected test PDF, or other intermediate artifacts are written to disk.
"""

from __future__ import annotations

import argparse
from base64 import b64encode
from collections import Counter
from hashlib import sha256
from html import escape
from io import BytesIO
import json
from pathlib import Path
import re
import subprocess

import pymupdf as fitz
from fontTools import subset
from fontTools.fontBuilder import FontBuilder
from fontTools.pens.cu2quPen import Cu2QuPen
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.ttLib import TTFont
from pypdf import PdfReader, PdfWriter
from pypdf.generic import ArrayObject, BooleanObject, DictionaryObject, NameObject
from weasyprint import HTML
from weasyprint.text.fonts import FontConfiguration
import yaml


OPTIONS = ("0.1", "0.2", "搁置")
PALETTE = {
    "写硬了": ("#1a7f37", "#e6f4ea"),
    "写软了": ("#9a6700", "#fff4d6"),
    "没写": ("#b42318", "#fde8e8"),
    "已有": ("#555", "#eee"),
    "新增": ("#1d4ed8", "#e0ecff"),
}


def norm(value):
    return re.sub(r"\s+", "", str(value))


def font_files(regular=None, bold=None):
    if regular and bold:
        return Path(regular).resolve(), Path(bold).resolve()
    if regular or bold:
        raise ValueError("Specify both --font-regular and --font-bold")
    listing = subprocess.run(
        ["fc-list", "--format", "%{file}\t%{family}\t%{style}\n"],
        check=True, capture_output=True, text=True,
    ).stdout
    found = {}
    for line in listing.splitlines():
        filename, family, style = line.split("\t", 2)
        if any(name in family for name in (
            "Noto Sans CJK SC", "Noto Sans SC", "Source Han Sans SC",
        )):
            if "Bold" in style:
                found.setdefault("bold", Path(filename))
            elif "Regular" in style:
                found.setdefault("regular", Path(filename))
    if len(found) == 2:
        return found["regular"], found["bold"]
    # Existing host resource bundles need not be registered in Fontconfig.
    roots = (Path.home() / "render_resources/chinese_math_pdf",
             Path(__file__).resolve().parent / "fonts")
    for root in roots:
        for regular_path in root.glob("**/NotoSansSC-Regular.otf"):
            bold_path = regular_path.with_name("NotoSansSC-Bold.otf")
            if bold_path.is_file():
                return regular_path, bold_path
    raise FileNotFoundError("Noto/Source Han SC regular and bold fonts not found")


def badge(value):
    foreground, background = PALETTE[value]
    return (f'<span class="badge" style="color:{foreground};'
            f'background:{background}">{escape(value)}</span>')


def choices(item_id):
    return '<td class="choices">' + "".join(
        f'<label><input type="radio" name="item_{escape(str(item_id))}" '
        f'value="{escape(option)}"><span>{escape(option)}</span></label>'
        for option in OPTIONS
    ) + "</td>"


def font_url(path, text):
    """Embed the existing font as portable TrueType outlines, in memory.

    Some readers disagree about CID addressing in subset CFF/OpenType fonts.
    Preserve the existing Noto glyphs and metrics, with <= 0.5 font-unit curve
    approximation error, while avoiding that reader-dependent CFF mapping.
    """
    font = TTFont(path)
    options = subset.Options()
    subsetter = subset.Subsetter(options=options)
    subsetter.populate(text=text)
    subsetter.subset(font)
    if "CFF " in font:
        glyph_set = font.getGlyphSet()
        glyphs = {}
        for name in font.getGlyphOrder():
            pen = TTGlyphPen(glyph_set)
            glyph_set[name].draw(Cu2QuPen(pen, max_err=0.5, reverse_direction=True))
            glyphs[name] = pen.glyph()
        del font["CFF "]
        font.sfntVersion = "\x00\x01\x00\x00"
        builder = FontBuilder(font=font, isTTF=True)
        builder.isTTF = True
        builder.setupGlyf(glyphs)
        builder.setupMaxp()
        builder.setupPost(keepGlyphNames=False)
    data = BytesIO()
    font.save(data)
    return "data:font/ttf;base64," + b64encode(data.getvalue()).decode("ascii")


def make_html(source, regular, bold):
    all_characters = json.dumps(source, ensure_ascii=False) + "案例：现在：0.10.2搁置0123456789 / "
    css = """
    @font-face {font-family: Checklist; src: url(REGULAR); font-weight: 400}
    @font-face {font-family: Checklist; src: url(BOLD); font-weight: 700}
    @page {
      size: A4 portrait; margin: 14mm;
      @bottom-center {content: counter(page) " / " counter(pages);
        font: 9pt Checklist; color: #555; vertical-align: middle}
    }
    * {box-sizing: border-box}
    html {font: 10.5pt/1.45 Checklist; color: #000}
    body {margin: 0}
    h1 {font-size: 20pt; line-height: 1.3; margin: 0 0 2mm; font-weight: 700}
    .subtitle {color: #555; margin: 0 0 2mm}
    .legend {font-size: 9.5pt; margin: 0 0 2.5mm; line-height: 1.6}
    .legend-entry {display: inline; margin-right: 3mm}
    h2 {font-size: 13pt; font-weight: 700; line-height: 1.35;
        margin: 3mm 0 0; padding: 0 0 1.5mm;
        border-bottom: .5pt solid #555; break-after: avoid}
    .section:first-of-type h2 {margin-top: 0}
    .regression-note {font-size: 10pt; color: #555; margin: 1.5mm 0 0;
        break-after: avoid}
    table {width: 100%; border-collapse: collapse; table-layout: fixed}
    col.number {width: 7mm} col.choice {width: 26mm}
    tr {break-inside: avoid}
    td {vertical-align: top; padding: 3mm 0; border-bottom: .5pt solid #ddd}
    td.number {font-size: 9.5pt; color: #777; padding-right: 1mm}
    td.content {padding-right: 3mm; overflow-wrap: anywhere}
    .need {font-size: 11pt; font-weight: 700; margin: 0; line-height: 1.45}
    .case {font-size: 10pt; color: #444; margin: 1mm 0 0; line-height: 1.45}
    .status {font-size: 9.5pt; color: #555; margin: 1mm 0 0; line-height: 1.45}
    .badge {font-size: 9pt; font-weight: 400; line-height: 1.45;
        border-radius: 3mm; padding: .25mm 1.4mm; white-space: nowrap}
    .regression-name {font-size: 11pt; font-weight: 700; margin: 0; line-height: 1.45}
    .tests {font-size: 10.5pt; margin: 1mm 0 0; line-height: 1.45}
    td.choices {padding-left: 3mm; vertical-align: middle; color: #000}
    label {display: flex; align-items: center; font-size: 9.5pt;
        line-height: 1.45; margin: 0 0 1.5mm; white-space: nowrap}
    label:last-child {margin-bottom: 0}
    input[type=radio] {appearance: auto; display: inline-block;
        box-sizing: content-box; width: 5.5pt; height: 5.5pt; padding: 1.5pt;
        border: .65pt solid #555; border-radius: 0; margin: 0 2mm 0 0;
        color: #000; background: transparent; flex-shrink: 0}
    """.replace("REGULAR", json.dumps(font_url(regular, all_characters))).replace(
        "BOLD", json.dumps(font_url(bold, all_characters)))
    output = [f'<html lang="zh-CN"><head><meta charset="utf-8"><style>{css}</style>'
              '</head><body>', f'<h1>{escape(source["title"])}</h1>',
              f'<p class="subtitle">{escape(source["subtitle"])}</p>', '<div class="legend">']
    for state, meaning in source["status_legend"].items():
        output.append(f'<span class="legend-entry">{badge(state)} {escape(meaning)}</span>')
    output.append('</div><form>')
    columns = '<colgroup><col class="number"><col><col class="choice"></colgroup>'
    for section in source["sections"]:
        output.append(f'<section class="section"><h2>{escape(section["heading"])}</h2>'
                      f'<table>{columns}<tbody>')
        for item in section["items"]:
            output.append(
                f'<tr id="row-{item["id"]}"><td class="number">{item["id"]}</td>'
                f'<td class="content"><p class="need">{escape(item["need"])}</p>'
                f'<p class="case">案例：{escape(item["case"])}</p>'
                f'<p class="status">现在：{badge(item["status"])} '
                f'{escape(item["status_note"])}</p></td>{choices(item["id"])}</tr>')
        output.append('</tbody></table></section>')
    regression = source["regressions"]
    output.append(f'<section><h2>{escape(regression["heading"])}</h2>'
                  f'<p class="regression-note">{escape(regression["note"])}</p>'
                  f'<table>{columns}<tbody>')
    for item in regression["items"]:
        output.append(
            f'<tr id="row-{item["id"]}"><td class="number">{item["id"]}</td>'
            f'<td class="content"><p class="regression-name">{escape(item["name"])} '
            f'{badge(item["origin"])}</p><p class="tests">{escape(item["tests"])}</p>'
            f'</td>{choices(item["id"])}</tr>')
    output.append('</tbody></table></section></form></body></html>')
    return "".join(output)


def normalize_forms(raw_pdf):
    """Keep WeasyPrint's native widgets and appearances; fix their field tree.

    WeasyPrint 70 lists both radio parents and children in /Fields and uses
    numeric appearance states. pypdf keeps only the parents there, gives states
    the YAML-independent option names, and supplies explicit blank /Off states.
    Existing generated appearance streams are reused, never drawn from scratch.
    """
    writer = PdfWriter(clone_from=BytesIO(raw_pdf))
    form = writer.root_object["/AcroForm"]
    parents = [reference for reference in form["/Fields"]
               if "/Parent" not in reference.get_object()]
    form[NameObject("/Fields")] = ArrayObject(parents)
    form[NameObject("/NeedAppearances")] = BooleanObject(False)
    for reference in parents:
        group = reference.get_object()
        assert len(group["/Kids"]) == len(OPTIONS)
        group[NameObject("/V")] = NameObject("/Off")
        # /Opt is not needed: appearance names are already the export values.
        # Omitting it avoids a second, viewer-dependent numeric value mapping.
        group.pop("/Opt", None)
        for child, option in zip(group["/Kids"], OPTIONS):
            widget = child.get_object()
            appearances = widget["/AP"]["/N"]
            on = next(value for key, value in appearances.items() if key != "/Off")
            # Obtain a valid empty Form XObject by cloning the generated one.
            off = on.get_object().clone(writer, force_duplicate=True)
            off.set_data(b"")
            widget["/AP"][NameObject("/N")] = DictionaryObject({
                NameObject("/" + option): on,
                NameObject("/Off"): writer._add_object(off),
            })
            widget[NameObject("/AS")] = NameObject("/Off")
            widget.pop("/T", None)  # Only the radio parent owns the field name.
            widget.pop("/FT", None)
    result = BytesIO()
    writer.write(result)
    return result.getvalue()


def source_strings(source):
    values = [("title", source["title"]), ("subtitle", source["subtitle"])]
    values.extend((f"status_legend.{key}", value)
                  for key, value in source["status_legend"].items())
    for index, section in enumerate(source["sections"]):
        values.append((f"sections.{index}.heading", section["heading"]))
        for item in section["items"]:
            values.extend((f'item_{item["id"]}.{key}', item[key])
                          for key in ("need", "case", "status_note"))
    regression = source["regressions"]
    values.extend((f"regressions.{key}", regression[key]) for key in ("heading", "note"))
    for item in regression["items"]:
        values.extend((f'item_{item["id"]}.{key}', item[key]) for key in ("name", "tests"))
    return values


def rows(source):
    return [item for section in source["sections"] for item in section["items"]] + list(
        source["regressions"]["items"])


def verify(source, document, pdf_bytes, output):
    pdf = fitz.open(stream=pdf_bytes, filetype="pdf")
    texts = [norm(page.get_text(sort=True)) for page in pdf]
    # Keep text in content-column reading order when searching wrapped strings.
    content_texts = []
    for page in pdf:
        content_texts.append(norm(page.get_text(
            clip=fitz.Rect(20 * 72 / 25.4, 0, (210 - 14 - 26) * 72 / 25.4,
                           page.rect.height), sort=True)))
    # The three top fields are wider than the table's middle column.
    complete = norm("".join(texts))
    middle = norm("".join(content_texts))
    missing = [key for key, value in source_strings(source)
               if norm(value) not in complete and norm(value) not in middle]
    # Exact character multiset, including ALL visible YAML values and every
    # authorized repeated prefix/choice/footer. Detect extras AND duplications.
    expected = []
    expected.extend(value for _, value in source_strings(source))
    expected.extend(source["status_legend"].keys())
    for section in source["sections"]:
        for item in section["items"]:
            expected.extend((str(item["id"]), "案例：", "现在：", item["status"], *OPTIONS))
    for item in source["regressions"]["items"]:
        expected.extend((str(item["id"]), item["origin"], *OPTIONS))
    expected.extend(f"{index + 1} / {len(pdf)}" for index in range(len(pdf)))
    wanted = Counter(norm("".join(expected)))
    actual = Counter(complete)
    extra = dict(actual - wanted)
    missing_characters = dict(wanted - actual)

    reader = PdfReader(BytesIO(pdf_bytes))
    fields = reader.get_fields()
    expected_names = {f'item_{item["id"]}' for item in rows(source)}
    assert set(fields) == expected_names, (set(fields), expected_names)
    assert len(reader.root_object["/AcroForm"]["/Fields"]) == len(expected_names)
    for group in fields.values():
        assert group["/FT"] == "/Btn" and group["/Ff"] & (1 << 15)
        assert group["/V"] == "/Off" and len(group["/Kids"]) == 3
        for child, option in zip(group["/Kids"], OPTIONS):
            widget = child.get_object()
            assert widget["/AS"] == "/Off" and widget["/F"] & 4
            assert set(widget["/AP"]["/N"]) == {"/Off", "/" + option}
    # Update and reread a separate in-memory PDF, keeping the deliverable empty.
    writer = PdfWriter(clone_from=BytesIO(pdf_bytes))
    target = "item_1" if "item_1" in fields else sorted(expected_names)[0]
    writer.update_page_form_field_values(
        None, {target: "/0.2"}, auto_regenerate=False)
    selected = BytesIO()
    writer.write(selected)
    readback = PdfReader(BytesIO(selected.getvalue()))
    group = readback.get_fields()[target]
    states = [str(child.get_object()["/AS"]) for child in group["/Kids"]]
    assert str(group["/V"]) == "/0.2" and states == ["/Off", "/0.2", "/Off"]
    # Independently render the selected appearance and confirm a visible dot.
    selected_pdf = fitz.open(stream=selected.getvalue(), filetype="pdf")
    visible_difference = 0
    for empty_page, selected_page in zip(pdf, selected_pdf):
        a = empty_page.get_pixmap(dpi=150).samples
        b = selected_page.get_pixmap(dpi=150).samples
        visible_difference += sum(x != y for x, y in zip(a, b))
    assert visible_difference > 0

    placements = {}
    content_bottoms = []
    for page_index, page in enumerate(document.pages, 1):
        last_bottom = 0
        for box in page._page_box.descendants():
            if box.element_tag == "tr":
                row_id = box.element.get("id")
                placements.setdefault(row_id, []).append({
                    "page": page_index, "top": box.position_y * .75,
                    "bottom": (box.position_y + box.height) * .75})
                last_bottom = max(last_bottom, (box.position_y + box.height) * .75)
        content_bottoms.append(last_bottom)
    split = {key: value for key, value in placements.items() if len(value) != 1}
    assert len(placements) == len(expected_names)
    # Each complete row's source content must also occur on its recorded PDF page.
    for item in rows(source):
        placement = placements[f'row-{item["id"]}'][0]
        page_index = placement["page"] - 1
        for key in ("need", "case", "status_note") if "need" in item else ("name", "tests"):
            assert norm(item[key]) in content_texts[page_index], (item["id"], key)
    blank = [round((page.rect.height - bottom) / page.rect.height * 100, 2)
             for page, bottom in zip(pdf, content_bottoms)]
    blank_failures = [index + 1 for index, value in enumerate(blank[:-1]) if value > 20]

    preview_dir = output.parent / "previews"
    preview_dir.mkdir(exist_ok=True)
    for old in preview_dir.glob("page-*.png"):
        if re.fullmatch(r"page-\d+\.png", old.name):
            old.unlink()
    for index, page in enumerate(pdf, 1):
        page.get_pixmap(dpi=150).save(str(preview_dir / f"page-{index}.png"))

    report = {
        "pdf": str(output), "pages": len(pdf),
        "text_missing_items": missing, "text_extra_characters": extra,
        "text_missing_characters": missing_characters,
        "radio_groups": len(fields), "options_per_group": 3,
        "selection_readback": {"field": target, "value": str(group["/V"]),
                               "states": states, "changed_render_samples": visible_difference},
        "split_rows": split, "row_placements": placements,
        "bottom_blank_percent_including_margin_excluding_footer": blank,
        "bottom_blank_failures_except_last": blank_failures,
        "previews": len(pdf), "preview_dpi": 150,
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if missing or extra or missing_characters or split or blank_failures:
        raise SystemExit("Mechanical QA failed; see JSON report")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--font-regular", type=Path)
    parser.add_argument("--font-bold", type=Path)
    args = parser.parse_args()
    original = args.input.read_bytes()
    source = yaml.safe_load(original)
    identifiers = [str(item["id"]) for item in rows(source)]
    if len(set(identifiers)) != len(identifiers):
        raise ValueError("Row IDs must be unique")
    regular, bold = font_files(args.font_regular, args.font_bold)
    document = HTML(string=make_html(source, regular, bold)).render(
        font_config=FontConfiguration(), pdf_forms=True)
    pdf_bytes = normalize_forms(document.write_pdf(pdf_forms=True))
    output = args.output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes(pdf_bytes)
    print(json.dumps({"source_sha256": sha256(original).hexdigest(),
                      "fonts": [str(regular), str(bold)]}, ensure_ascii=False))
    verify(source, document, pdf_bytes, output)
    assert args.input.read_bytes() == original, "Source changed during render"


if __name__ == "__main__":
    main()
