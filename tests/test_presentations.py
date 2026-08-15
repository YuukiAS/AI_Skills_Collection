from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path
from zipfile import ZipFile


REPO_ROOT = Path(__file__).resolve().parents[1]
SHARED = REPO_ROOT / "skills" / "tools" / "documents-media" / "presentations" / "shared"
sys.path.insert(0, str(SHARED / "scripts"))

import markdown_to_deck_plan  # noqa: E402
import validate_deck_plan  # noqa: E402


class PresentationSharedTests(unittest.TestCase):
    def test_markdown_adapter_matches_deidentified_fixture(self) -> None:
        markdown = (SHARED / "fixtures" / "deidentified_markdown.md").read_text(encoding="utf-8")
        expected = json.loads((SHARED / "fixtures" / "expected_deck_plan.json").read_text(encoding="utf-8"))
        actual = markdown_to_deck_plan.markdown_to_deck_plan(markdown, "Deidentified Research Update")
        self.assertEqual(actual, expected)

    def test_research_markdown_defaults_to_latex_beamer_output(self) -> None:
        actual = markdown_to_deck_plan.markdown_to_deck_plan("# One\nBody", "Research Update")
        self.assertEqual(actual["metadata"]["output"], "tex")

    def test_academic_routing_blocks_pptx_and_requires_render_skill(self) -> None:
        research_skill = (REPO_ROOT / "skills/tools/documents-media/presentations/research-presentations/SKILL.md").read_text(encoding="utf-8")
        template_routing = (SHARED / "template-routing.md").read_text(encoding="utf-8")
        latex_notes = (SHARED / "compatibility/openai-latex.md").read_text(encoding="utf-8")
        cuhk_readme = (SHARED / "templates/cuhk/README.md").read_text(encoding="utf-8")

        self.assertIn("LaTeX plus Beamer by default", research_skill)
        self.assertIn("Do not use `python-pptx`, python-ppt", research_skill)
        self.assertIn("If the local skill is not installed", research_skill)
        self.assertIn("Do not route academic decks to `python-pptx`", template_routing)
        self.assertIn("Academic presentation compilation must first use", latex_notes)
        self.assertIn("render-chinese-math-pdf", latex_notes)
        self.assertIn("Preserve the first/title slide layout", cuhk_readme)
        self.assertIn("Times New Roman Regular, Bold, Italic, and Bold Italic", cuhk_readme)

    def test_cuhk_template_payload_is_complete_and_reference_deck_is_valid(self) -> None:
        root = SHARED / "templates/cuhk"
        source = root / "beamer/source"
        required = [
            source / "main.tex",
            source / "styles/beamerthemesintef.sty",
            source / "styles/sintefcolor.sty",
            source / "assets/background.png",
            source / "assets/background_negative.png",
            source / "assets/logo_RGB.png",
            source / "assets/logo_RGB_negative.png",
            source / "bibliography.bib",
            root / "design-tokens.json",
            root / "pptx/build_reference_deck.py",
            root / "pptx/cuhk-reference-deck.pptx",
            root / "scripts/import-local-assets.ps1",
        ]
        for path in required:
            self.assertTrue(path.exists(), path)

        text = (source / "main.tex").read_text(encoding="utf-8")
        self.assertIn(r"\usetheme{sintef}", text)
        self.assertIn(r"\titlebackground*{assets/background}", text)
        self.assertIn(r"\usepackage{tcolorbox}", text)

        tokens = json.loads((root / "design-tokens.json").read_text(encoding="utf-8"))
        self.assertEqual(tokens["slide"]["width_in"], 13.333)
        self.assertEqual(tokens["slide"]["height_in"], 7.5)

        with ZipFile(root / "pptx/cuhk-reference-deck.pptx") as deck:
            names = set(deck.namelist())
        self.assertIn("[Content_Types].xml", names)
        self.assertTrue(any(name.startswith("ppt/slides/slide") for name in names))

    def test_deck_plan_validator_accepts_fixture(self) -> None:
        expected = json.loads((SHARED / "fixtures" / "expected_deck_plan.json").read_text(encoding="utf-8"))
        self.assertEqual(validate_deck_plan.validate_deck_plan(expected), [])

    def test_deck_plan_validator_rejects_missing_anchor_basics(self) -> None:
        errors = validate_deck_plan.validate_deck_plan({"schema_version": 1, "metadata": {}, "slides": [{}]})
        self.assertTrue(any("metadata missing required fields" in error for error in errors))
        self.assertTrue(any("missing id" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
