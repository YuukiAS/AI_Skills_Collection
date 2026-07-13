from __future__ import annotations

import json
from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.util import Inches, Pt


ROOT = Path(__file__).resolve().parents[1]
TOKENS = json.loads((ROOT / "design-tokens.json").read_text(encoding="utf-8"))


def rgb(hex_value: str) -> RGBColor:
    value = hex_value.lstrip("#")
    return RGBColor(int(value[0:2], 16), int(value[2:4], 16), int(value[4:6], 16))


def add_textbox(slide, left, top, width, height, text, size, color, bold=False):
    box = slide.shapes.add_textbox(left, top, width, height)
    frame = box.text_frame
    frame.clear()
    paragraph = frame.paragraphs[0]
    run = paragraph.add_run()
    run.text = text
    run.font.name = TOKENS["typography"]["preferred_sans"][0]
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.color.rgb = rgb(color)
    return box


def add_header(slide, title: str, section: str, page: str):
    colors = TOKENS["colors"]
    bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(0.42))
    bar.fill.solid()
    bar.fill.fore_color.rgb = rgb(colors["main"])
    bar.line.fill.background()
    add_textbox(slide, Inches(0.45), Inches(0.08), Inches(7.5), Inches(0.25), section, 9, "#FFFFFF")
    add_textbox(slide, Inches(11.6), Inches(0.08), Inches(1.2), Inches(0.25), page, 9, "#FFFFFF")
    add_textbox(slide, Inches(0.65), Inches(0.72), Inches(10.8), Inches(0.55), title, 28, colors["ink"], True)


def build(path: Path) -> None:
    prs = Presentation()
    prs.slide_width = Inches(TOKENS["slide"]["width_in"])
    prs.slide_height = Inches(TOKENS["slide"]["height_in"])
    blank = prs.slide_layouts[6]
    colors = TOKENS["colors"]

    slide = prs.slides.add_slide(blank)
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid()
    bg.fill.fore_color.rgb = rgb(colors["main"])
    bg.line.fill.background()
    facet = slide.shapes.add_shape(MSO_SHAPE.RIGHT_TRIANGLE, Inches(9.2), 0, Inches(4.15), Inches(7.5))
    facet.fill.solid()
    facet.fill.fore_color.rgb = rgb(colors["light_bar"])
    facet.fill.transparency = 35
    facet.line.fill.background()
    add_textbox(slide, Inches(0.75), Inches(1.65), Inches(8.5), Inches(0.75), "Presentation Title", 36, "#FFFFFF", True)
    add_textbox(slide, Inches(0.78), Inches(2.55), Inches(7.2), Inches(0.45), "Subtitle or source paper", 18, "#FFFFFF")
    add_textbox(slide, Inches(0.78), Inches(5.75), Inches(7.5), Inches(0.7), "Author Name\nDepartment of Statistics and Data Science", 13, "#FFFFFF")

    slide = prs.slides.add_slide(blank)
    add_header(slide, "One Main Message", "Introduction", "2")
    add_textbox(slide, Inches(0.85), Inches(1.65), Inches(5.2), Inches(3.8), "Use this area for the claim, context, or interpretation. Keep the slide editable and avoid using a rendered PDF page as the background.", 18, colors["ink"])
    panel = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.0), Inches(1.55), Inches(4.9), Inches(3.6))
    panel.fill.solid()
    panel.fill.fore_color.rgb = rgb(colors["light_bar"])
    panel.line.color.rgb = rgb(colors["muted"])
    add_textbox(slide, Inches(7.35), Inches(2.05), Inches(4.1), Inches(0.6), "Editable visual area", 20, colors["main"], True)
    add_textbox(slide, Inches(7.35), Inches(2.85), Inches(4.0), Inches(1.2), "Insert charts, figures, diagrams, or equations here.", 15, colors["ink"])

    slide = prs.slides.add_slide(blank)
    add_header(slide, "Thank You", "Closing", "3")
    add_textbox(slide, Inches(0.9), Inches(2.4), Inches(7.0), Inches(0.8), "Discussion", 34, colors["main"], True)
    add_textbox(slide, Inches(0.92), Inches(3.35), Inches(8.0), Inches(0.5), "Questions, next decisions, or contact information.", 18, colors["ink"])
    prs.save(path)


if __name__ == "__main__":
    build(Path(__file__).with_name("cuhk-reference-deck.pptx"))
