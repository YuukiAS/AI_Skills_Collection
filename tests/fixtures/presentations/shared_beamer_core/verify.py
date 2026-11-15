#!/usr/bin/env python3
"""Render both skins and record parity plus V19 geometry on generic slide content."""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
import json
from pathlib import Path
import shutil
import sys
import tempfile

from PIL import Image
import pymupdf as mupdf
import yaml

FIXTURE = Path(__file__).resolve().parent
ROOT = FIXTURE.parents[3]
SOURCE = ROOT / "skills/tools/documents-media/presentations/shared"
PAYLOAD = ROOT / "plugins/codex/plugins/presentations/shared"

sys.path.insert(0, str((SOURCE if "--source" in sys.argv else PAYLOAD) / "scripts"))
import build_beamer_template as builder
import compare_beamer_template_parity as parity

BEAMER_DOCUMENT = r"\documentclass[aspectratio=169,t]{beamer}" + "\n"
IMPORTS = {
    "course-standard": r"\input{template.tex}" + "\n",
    "cuhk": r"\makeatletter\def\input@path{{styles/}}\makeatother\usetheme{sintef}" + "\n",
}


def write_json(path: Path, report: dict) -> None:
    path.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def read_spans(page) -> list[dict]:
    return [span for line in parity.text_lines(page) for span in line["spans"] if span["text"].strip()]


def find_span(page, prefix: str) -> dict:
    matching = [span for span in read_spans(page) if span["text"].startswith(prefix)]
    if len(matching) != 1:
        raise ValueError(f"Page {page.number + 1}: expected one span starting with {prefix!r}, got {len(matching)}")
    return matching[0]


def ink_box(page, bounds) -> mupdf.Rect:
    """Use real 1920px glyph ink for optical alignment rather than font em boxes."""
    scale = 1920 / page.rect.width
    pix = page.get_pixmap(matrix=mupdf.Matrix(scale, scale), clip=mupdf.Rect(bounds), colorspace=mupdf.csGRAY)
    mask = Image.frombytes("L", (pix.width, pix.height), pix.samples).point(lambda gray: 255 if gray < 208 else 0)
    bbox = mask.getbbox()
    if bbox is None:
        raise ValueError(f"No ink on page {page.number + 1} in {bounds}")
    return mupdf.Rect(
        (pix.x + bbox[0]) / scale, (pix.y + bbox[1]) / scale,
        (pix.x + bbox[2]) / scale, (pix.y + bbox[3]) / scale,
    )


def style_replay(pdf: Path) -> dict:
    contract_path = SOURCE / "templates/_shared/beamer-core-v1/layout-contract.yaml"
    contract = yaml.safe_load(contract_path.read_text(encoding="utf-8"))
    oracle = json.loads((FIXTURE / "v19-geometry.json").read_text(encoding="utf-8"))
    rows = []

    def near(name, value, expected, tolerance, units):
        rows.append({
            "check": name, "measured": value, "expected": expected, "tolerance": tolerance, "units": units,
            "status": "PASS" if abs(value - expected) <= tolerance + 1e-6 else "FAIL",
        })

    def threshold(name, value, target, hard_minimum, units):
        rows.append({
            "check": name, "measured": value, "target": target, "hard_minimum": hard_minimum, "units": units,
            "status": "PASS" if target[0] <= value <= target[1] else "FAIL" if value < hard_minimum else "REVIEW",
        })

    def truth(name, value):
        rows.append({"check": name, "status": "PASS" if value else "FAIL"})

    with mupdf.open(pdf) as deck:
        truth("Reference is 11 slides", deck.page_count == 11)
        ordinary, question, figure = deck[1], deck[2], deck[3]
        scale = 1920 / ordinary.rect.width
        pt = "PDF pt"
        expected = oracle["values_pdf_pt"]
        near("Page width", ordinary.rect.width, expected["page_width"], 0.02, pt)
        near("Page height", ordinary.rect.height, expected["page_height"], 0.02, pt)

        for role, page, prefix, font in (
            ("frame_title", ordinary, "A repeat is only useful", "TeXGyreTermes-Bold"),
            ("body", ordinary, "Record the instrument", "TeXGyreTermes-Regular"),
            ("subhead", deck[4], "Repeatability", "TeXGyreTermes-Bold"),
            ("table", question, "Reference (mm)", "TeXGyreTermes-Bold"),
            ("caption", figure, "Schematic plot", "TeXGyreTermes-Regular"),
            ("footer", ordinary, "Shared reference", "TeXGyreTermes-Regular"),
            ("section_nav", ordinary, "Calibration procedures", "TeXGyreTermes-Bold"),
            ("code", deck[7], "signed_error", "LMMono10-Regular"),
            ("closing_question", deck[-1], "Questions?", "TeXGyreTermes-Regular"),
        ):
            span = find_span(page, prefix)
            token = contract["typography"][role]
            near(f"{role} font size", span["size"], token["pdf_pt"], token["tolerance_pdf_pt"], pt)
            truth(f"{role} font face and series", span["font"] == font)

        near("Frame title vertical anchor", find_span(ordinary, "A repeat is only useful")["bbox"][1],
             expected["ordinary_frame_title_bbox_top"], 2 / scale, pt)
        rail = contract["geometry"]["body_margin_left_mm"] * 72 / 25.4
        origin = find_span(ordinary, "Record the instrument")["origin"]
        near("Ordinary body rail", origin[0], rail, 2 / scale, pt)
        nav = [find_span(ordinary, prefix) for prefix in ("Setup", "Calibration procedures", "Apply")]
        near("Section label top", nav[0]["bbox"][1], expected["section_label_bbox_top"], 2 / scale, pt)
        near("Section band bottom", ordinary.get_drawings()[1]["rect"].y1, expected["section_band_bottom"], 2 / scale, pt)
        nav_gap = min(b["bbox"][0] - a["bbox"][2] for a, b in zip(nav, nav[1:])) * scale
        truth("Visible section labels are separated by at least 12 px", nav_gap >= contract["section_navigation"]["neighbor_gap_px_min"])
        limits = contract["section_navigation"]["width_cap"]
        utilization = nav[1]["bbox"][4] / (limits["base_pdf_pt"] + limits["page_weight_pdf_pt"])
        threshold("Near-budget label is legal", utilization, [limits["review_utilization"], limits["fail_utilization"]],
                  limits["review_utilization"], "fraction")
        if utilization > limits["fail_utilization"]:
            rows[-1]["status"] = "FAIL"
        dests = {link.get("page") for link in ordinary.get_links() if 8 < link["from"].y0 < 16}
        truth("Clickable miniframes cover all sectional slides", dests == set(range(1, 11)))

        bullet_line_1 = find_span(ordinary, "Repeat the reading")
        bullet_line_2 = find_span(ordinary, "change in the reading")
        bullet_2 = find_span(ordinary, "Keep the raw values")
        leading = contract["typography"]["body"]["leading_pt"] * 72 / 72.27
        near("Wrapped item uses the ordinary baseline", bullet_line_2["origin"][1] - bullet_line_1["origin"][1],
             leading, 0.10, pt)
        itemsep = contract["teaching_list"]["itemsep_tex_pt"] * 72 / 72.27
        near("Inter-item glue stays at the shared token",
             bullet_2["origin"][1] - bullet_line_2["origin"][1] - leading, itemsep, 0.12, pt)

        def spacing(name, measured):
            token = contract["spacing_pdf_pt"][name]
            threshold(name, measured, token["target"], token["fail_below"], pt)

        spacing("list_item_gap", ink_box(ordinary, bullet_2["bbox"][:4]).y0
                - ink_box(ordinary, bullet_line_2["bbox"][:4]).y1)
        spacing("paragraph_to_list", ink_box(ordinary, bullet_line_1["bbox"][:4]).y0
                - ink_box(ordinary, find_span(ordinary, "Record the instrument")["bbox"][:4]).y1)
        q_label, q_copy = find_span(question, "Question"), find_span(question, "Do two nearly")
        truth("Question label bold and body italic", q_label["font"].endswith("Bold") and q_copy["font"].endswith("Italic"))
        q_rule, answer_rule = [
            path["rect"] for path in question.get_drawings()
            if path["type"] == "s" and path["rect"].width < 0.1 and path["rect"].height > 5
            and abs(path["rect"].x0 - (path["width"] or 0) / 2 - rail) < 0.12
        ]
        table_rule = next(path["rect"] for path in question.get_drawings()
                          if 60 < path["rect"].y0 < 110 and 100 < path["rect"].width < 250)
        spacing("question_to_next", table_rule.y0 - q_rule.y1)
        answer = find_span(question, "Answer")
        answer_body = find_span(question, "No.")
        truth("Answer label is above the continuous rule", answer["origin"][1] < answer_rule.y0)
        truth("Answer body face is upright", answer_body["font"] == "TeXGyreTermes-Regular")
        body_ink = ink_box(question, (answer_body["bbox"][0], answer_rule.y0 - 1, 430, answer_rule.y1 + 2))
        near("Answer rule starts at its body ink", answer_rule.y0, body_ink.y0, 2 / scale, pt)
        near("Answer rule ends at its body ink", answer_rule.y1, body_ink.y1, 2 / scale, pt)

        plot = next(path["rect"] for path in figure.get_drawings()
                    if 65 < path["rect"].y0 < 115 and 250 < path["rect"].width < 260)
        caption_y = find_span(figure, "Schematic plot")["bbox"][1]
        interpretation = find_span(figure, "The gap matters")["bbox"]
        caption_size = contract["typography"]["caption"]["pdf_pt"]
        caption = [
            span for span in read_spans(figure)
            if caption_y <= span["bbox"][1] < interpretation[1] and abs(span["size"] - caption_size) < 0.1
        ]
        anchors = sorted({min(span["bbox"][0] for span in caption if abs(span["bbox"][1] - line_y) < 0.1)
                          for line_y in {span["bbox"][1] for span in caption}})
        truth("Caption has multiple lines below its plot", len({span["bbox"][1] for span in caption}) > 1 and caption_y > plot.y1)
        for x in anchors:
            near("Caption line aligns with plot", x, plot.x0, 2 / scale, pt)
        caption_ink = ink_box(figure, (rail - 0.5, caption_y, plot.x1, max(span["bbox"][3] for span in caption)))
        spacing("caption_to_body", ink_box(figure, interpretation[:4]).y0 - caption_ink.y1)

        body_width = ordinary.rect.width - 2 * rail
        for page, left, right, preset in (
            (deck[4], "Repeatability", "Agreement", "equal"),
            (deck[5], "Paired readings", "What the difference", "evidence_left"),
            (deck[9], "If repeats vary", "If the mean shifts", "evidence_right"),
        ):
            a, b = find_span(page, left), find_span(page, right)
            near(f"{preset} left rail", a["origin"][0], rail, 2 / scale, pt)
            near(f"{preset} right anchor", b["origin"][0], rail + body_width * (1 - contract["columns"][preset][1]),
                 2 / scale, pt)
            near(f"{preset} peer top alignment", a["origin"][1], b["origin"][1], 2 / scale, pt)

        truth("Table semantic atoms stay on one line",
              all(find_span(deck[6], name)["text"] == name for name in ("Reference-standard", "Paired-reset")))
        truth("Shared math and CJK bind their fixed file faces",
              any(span["font"].startswith("NewCMMath") for span in read_spans(deck[5]))
              and any(span["font"].startswith("TeXGyreTermesMath") for span in read_spans(deck[5]))
              and find_span(deck[9], "校准")["font"] == "NotoSerifSC-Regular")

        shafts = [
            path["rect"].width * 25.4 / 72 for path in deck[8].get_drawings()
            if path["type"] == "s" and 0.64 < path["width"] < 0.66
            and path["rect"].height < 0.05 and 10 < path["rect"].width < 32
        ]
        truth("The ordered process has three distinct rendered shafts", len(shafts) == 3)
        diagram = contract["diagram"]
        for shaft in shafts:
            threshold("Process shaft in preferred interval", shaft, diagram["preferred_process_shaft_mm"],
                      diagram["shaft_fail_below_mm"], "mm")
        if shafts:
            truth("Peer shafts agree within two pixels",
                  (max(shafts) - min(shafts)) * 72 / 25.4 * scale <= diagram["peer_length_tolerance_px"])

        footer = next(path for path in ordinary.get_drawings() if path["rect"].width > 453 and path["type"] == "s")
        near("Footer divider baseline", footer["rect"].y0, expected["footer_divider_y"], 2 / scale, pt)
        band_top = footer["rect"].y0 - footer["width"] / 2
        band_center = (band_top + ordinary.rect.height) / 2
        for page in (ordinary, deck[9]):
            credit_ink = ink_box(page, (rail - 0.5, band_top + 1.0, 200, page.rect.height))
            near(f"Footer credit optical center on page {page.number + 1}",
                 (credit_ink.y0 + credit_ink.y1) / 2, band_center,
                 contract["footer"]["left_credit_center_tolerance_px"] / scale, pt)
        truth("Frame credit replaces default", find_span(deck[9], "Illustrative lab protocol")["text"] == "Illustrative lab protocol")

        cue = find_span(deck[-1], "Questions?")
        near("Questions horizontal center", (cue["bbox"][0] + cue["bbox"][2]) / 2,
             ordinary.rect.width / 2, 2 / scale, pt)
        near("Questions vertical center", (cue["bbox"][1] + cue["bbox"][3]) / 2,
             expected["closing_cue_bbox_center_y"],
             (band_top - expected["section_band_bottom"]) * contract["closing"]["questions_center_tolerance_fraction"], pt)
        near("Closing frame title shares body rail", find_span(deck[-1], "What a calibration")["origin"][0],
             rail, 2 / scale, pt)

    return {
        "schema": "presentations-v19-generic-style-replay-v1",
        "oracle": oracle,
        "fixture_sha256": parity.sha256(FIXTURE / "content.tex"),
        "pdf_sha256": parity.sha256(pdf),
        "status": "FAIL" if any(row["status"] == "FAIL" for row in rows) else "PASS_WITH_REVIEW" if any(
            row["status"] == "REVIEW" for row in rows) else "PASS",
        "checks": rows,
    }


def contact_sheet(pdf: Path, target: Path) -> None:
    with mupdf.open(pdf) as deck:
        width, height, columns, gap = 400, 225, 3, 8
        rows = (deck.page_count + columns - 1) // columns
        sheet = Image.new("RGB", (columns * (width + gap) + gap, rows * (height + gap) + gap), "#d5d9df")
        for page in deck:
            pix = page.get_pixmap(matrix=mupdf.Matrix(width / page.rect.width, height / page.rect.height))
            slide = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
            sheet.paste(slide, (gap + (page.number % columns) * (width + gap),
                                gap + (page.number // columns) * (height + gap)))
        sheet.save(target)


def run(out: Path) -> int:
    out.mkdir(parents=True, exist_ok=True)
    content = (FIXTURE / "content.tex").read_bytes()
    with tempfile.TemporaryDirectory(prefix="beamer-parity-") as temp:
        scratch = Path(temp)

        def build(skin: str) -> None:
            driver = scratch / f"{skin}.tex"
            driver.write_bytes((BEAMER_DOCUMENT + IMPORTS[skin]).encode("ascii") + content)
            source_dir = scratch / skin
            receipt = builder.build(skin, source_dir, document=driver)
            if receipt["status"] != "COMPILED":
                log = (source_dir / "compile.log").read_text(encoding="utf-8") if (source_dir / "compile.log").is_file() else ""
                raise RuntimeError(f"{skin} build failed: {receipt}\n{log[-5000:]}")
            shutil.copy2(source_dir / "main.pdf", out / f"{skin}.pdf")
            write_json(out / f"{skin}-fonts.json", {
                "engine": receipt["engine"], "font_binding": {
                    k: receipt["font_binding"][k] for k in ("resource_dir", "fonts")
                }, "pdffonts": receipt["font_qa"]["stdout"],
                "pdf_sha256": receipt["pdf_sha256"],
            })

        with ThreadPoolExecutor(max_workers=2) as pool:
            list(pool.map(build, IMPORTS))
    report = parity.compare(out / "course-standard.pdf", out / "cuhk.pdf", FIXTURE / "brand-masks.json")
    report["same_content_sha256"] = parity.sha256(FIXTURE / "content.tex")
    write_json(out / "parity.json", report)
    replay = style_replay(out / "course-standard.pdf")
    write_json(out / "v19-style-replay.json", replay)
    for skin in IMPORTS:
        contact_sheet(out / f"{skin}.pdf", out / f"{skin}-contact.png")
    print(f"Parity {report['status']}, V19 geometry replay {replay['status']}")
    return int(report["status"] != "PASS" or replay["status"] == "FAIL")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out-dir", type=Path, required=True)
    parser.add_argument("--source", action="store_true", help="Build from source instead of the generated plugin payload")
    raise SystemExit(run(parser.parse_args().out_dir))
