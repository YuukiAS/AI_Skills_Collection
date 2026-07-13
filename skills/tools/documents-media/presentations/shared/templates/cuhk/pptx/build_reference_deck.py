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


def add_bullets(slide, left, top, width, height, items, size, color):
    box = slide.shapes.add_textbox(left, top, width, height)
    frame = box.text_frame
    frame.clear()
    for index, item in enumerate(items):
        paragraph = frame.paragraphs[0] if index == 0 else frame.add_paragraph()
        paragraph.text = item
        paragraph.level = 0
        paragraph.font.name = TOKENS["typography"]["preferred_sans"][0]
        paragraph.font.size = Pt(size)
        paragraph.font.color.rgb = rgb(color)
    return box


def add_card(slide, left, top, width, height, title: str, body: str):
    colors = TOKENS["colors"]
    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    card.fill.solid()
    card.fill.fore_color.rgb = rgb("#F7F0F6")
    card.line.color.rgb = rgb(colors["muted"])
    add_textbox(slide, left + Inches(0.25), top + Inches(0.25), width - Inches(0.5), Inches(0.35), title, 15, colors["main"], True)
    add_textbox(slide, left + Inches(0.25), top + Inches(0.75), width - Inches(0.5), height - Inches(1.0), body, 12, colors["ink"])


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
    add_header(slide, "Research Question", "Background", "3")
    add_bullets(slide, Inches(0.9), Inches(1.65), Inches(5.6), Inches(3.8), ["Observed gap in the prior workflow", "Primary endpoint and cohort boundary", "Decision that the slide deck should support"], 18, colors["ink"])
    add_card(slide, Inches(7.1), Inches(1.65), Inches(4.7), Inches(2.8), "Source anchor", "Paper page, repo result, notebook cell, or figure id stays attached to the slide plan.")

    slide = prs.slides.add_slide(blank)
    add_header(slide, "Methods Overview", "Method", "4")
    for idx, label in enumerate(["Input", "Model", "Validation", "Decision"]):
        add_card(slide, Inches(0.8 + idx * 3.05), Inches(1.75), Inches(2.55), Inches(2.6), label, "Editable process block with concise evidence.")
    add_textbox(slide, Inches(0.9), Inches(5.2), Inches(11.2), Inches(0.4), "Use this layout for pipelines, study flow, or experiment stages.", 14, colors["ink"])

    slide = prs.slides.add_slide(blank)
    add_header(slide, "Equation or Model", "Method", "5")
    add_textbox(slide, Inches(1.0), Inches(2.0), Inches(5.2), Inches(0.8), "y = f(x; theta) + epsilon", 26, colors["main"], True)
    add_bullets(slide, Inches(7.0), Inches(1.6), Inches(4.8), Inches(3.4), ["Keep equations as text when possible", "Preserve notation from the source", "Explain only the terms needed for the audience"], 16, colors["ink"])

    slide = prs.slides.add_slide(blank)
    add_header(slide, "Results Figure", "Evidence", "6")
    chart = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.9), Inches(1.55), Inches(6.0), Inches(3.7))
    chart.fill.solid()
    chart.fill.fore_color.rgb = rgb("#FFFFFF")
    chart.line.color.rgb = rgb(colors["muted"])
    for idx, height in enumerate([1.2, 2.1, 1.7, 2.8]):
        bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.4 + idx * 1.2), Inches(4.8 - height), Inches(0.55), Inches(height))
        bar.fill.solid()
        bar.fill.fore_color.rgb = rgb(colors["main"] if idx % 2 else colors["gold"])
        bar.line.fill.background()
    add_card(slide, Inches(7.4), Inches(1.65), Inches(4.2), Inches(3.1), "Interpretation", "State what changed, how large it was, and what remains uncertain.")

    slide = prs.slides.add_slide(blank)
    add_header(slide, "Comparison", "Evidence", "7")
    add_card(slide, Inches(0.9), Inches(1.65), Inches(5.1), Inches(3.5), "Baseline", "Strengths, limits, and key metric.")
    add_card(slide, Inches(7.0), Inches(1.65), Inches(5.1), Inches(3.5), "Updated workflow", "Observed gain, tradeoff, and source anchor.")

    slide = prs.slides.add_slide(blank)
    add_header(slide, "Table Layout", "Evidence", "8")
    for row in range(4):
        for col in range(4):
            rect = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.0 + col * 2.6), Inches(1.55 + row * 0.65), Inches(2.55), Inches(0.6))
            rect.fill.solid()
            rect.fill.fore_color.rgb = rgb(colors["light_bar"] if row == 0 else "#FFFFFF")
            rect.line.color.rgb = rgb(colors["muted"])
            add_textbox(slide, Inches(1.1 + col * 2.6), Inches(1.68 + row * 0.65), Inches(2.3), Inches(0.25), "Header" if row == 0 else "Value", 10, colors["ink"], row == 0)

    slide = prs.slides.add_slide(blank)
    add_header(slide, "Limitations and Next Step", "Discussion", "9")
    add_bullets(slide, Inches(0.9), Inches(1.6), Inches(5.4), Inches(3.8), ["What the evidence does not show", "Operational risk or missing validation", "Decision, owner, and next artifact"], 18, colors["ink"])
    add_card(slide, Inches(7.2), Inches(1.65), Inches(4.5), Inches(3.2), "Decision prompt", "The audience should know what response is needed.")

    slide = prs.slides.add_slide(blank)
    add_header(slide, "References", "Appendix", "10")
    add_bullets(slide, Inches(0.9), Inches(1.55), Inches(10.8), Inches(3.8), ["[1] Source paper or dataset", "[2] Repository result artifact", "[3] Review note or issue"], 15, colors["ink"])

    slide = prs.slides.add_slide(blank)
    add_header(slide, "Backup Detail", "Backup", "11")
    add_textbox(slide, Inches(0.9), Inches(1.7), Inches(10.4), Inches(1.2), "Use backup slides for sensitivity analysis, extra tables, or reproducibility details that should not interrupt the main talk.", 18, colors["ink"])

    slide = prs.slides.add_slide(blank)
    add_header(slide, "Thank You", "Closing", "12")
    add_textbox(slide, Inches(0.9), Inches(2.4), Inches(7.0), Inches(0.8), "Discussion", 34, colors["main"], True)
    add_textbox(slide, Inches(0.92), Inches(3.35), Inches(8.0), Inches(0.5), "Questions, next decisions, or contact information.", 18, colors["ink"])
    prs.save(path)


if __name__ == "__main__":
    build(Path(__file__).with_name("cuhk-reference-deck.pptx"))
