from __future__ import annotations

import json
import csv
import subprocess
import sys
import tempfile
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

    def test_research_markdown_defaults_to_editable_pptx_output(self) -> None:
        actual = markdown_to_deck_plan.markdown_to_deck_plan("# One\nBody", "Research Update")
        self.assertEqual(actual["metadata"]["output"], "pptx")
        self.assertEqual(actual["metadata"]["editability"], "editable")
        self.assertEqual(actual["slides"][0]["slide_purpose"], "communicate one research update message")
        self.assertIn("evidence-bearing visual", actual["slides"][0]["visual_intent"])

    def test_explicit_tex_still_routes_to_source_editable_latex(self) -> None:
        actual = markdown_to_deck_plan.markdown_to_deck_plan("# One\nBody", "Research Update", output="tex")
        self.assertEqual(actual["metadata"]["output"], "tex")
        self.assertEqual(actual["metadata"]["editability"], "source-editable")

    def test_research_routing_prefers_requested_editability_not_academic_default_beamer(self) -> None:
        research_skill = (REPO_ROOT / "skills/tools/documents-media/presentations/research-presentations/SKILL.md").read_text(encoding="utf-8")
        ppt_routing = (SHARED / "ppt-skill-routing.md").read_text(encoding="utf-8")
        template_routing = (SHARED / "template-routing.md").read_text(encoding="utf-8")
        latex_notes = (SHARED / "compatibility/openai-latex.md").read_text(encoding="utf-8")
        cuhk_readme = (SHARED / "templates/cuhk/README.md").read_text(encoding="utf-8")
        visual_qa = (SHARED / "visual-qa.md").read_text(encoding="utf-8")

        self.assertIn("Do not default academic or research decks to Beamer", research_skill)
        self.assertIn("Group meeting, research update, or research slides in a desktop presentation context with no format specified -> editable Presentation/Slides route", research_skill)
        self.assertIn("PPT, PowerPoint, `.pptx`, editable, Slides, or later manual editing", ppt_routing)
        self.assertIn("do not switch to Beamer only because the content is academic", ppt_routing)
        self.assertIn("Explicit Beamer, LaTeX slides, `.tex`, academic PDF", ppt_routing)
        self.assertIn("Group meeting, research update, paper talk", template_routing)
        self.assertIn("Do not route academic decks to Beamer only because they are academic", template_routing)
        self.assertIn("file exists", research_skill)
        self.assertIn("file existence alone is not completion", visual_qa)
        self.assertNotIn("LaTeX plus Beamer by default", research_skill)
        self.assertNotIn("LaTeX plus Beamer by default", template_routing)
        self.assertIn("If the local skill is not installed", research_skill)
        self.assertIn("Academic presentation compilation must first use", latex_notes)
        self.assertIn("render-chinese-math-pdf", latex_notes)
        self.assertIn("Preserve the first/title slide layout", cuhk_readme)
        self.assertIn("Times New Roman Regular, Bold, Italic, and Bold Italic", cuhk_readme)

    def test_business_and_shared_routes_connect_chinese_writing_handoff(self) -> None:
        business_skill = (REPO_ROOT / "skills/tools/documents-media/presentations/business-presentations/SKILL.md").read_text(encoding="utf-8")
        ppt_routing = (SHARED / "ppt-skill-routing.md").read_text(encoding="utf-8")
        profile = json.loads((REPO_ROOT / "profiles/presentation-desktop.json").read_text(encoding="utf-8"))

        self.assertIn("Chinese business, executive, product, strategy, or decision slide text", business_skill)
        self.assertIn("writing-fidelity` plus `chinese-prose", business_skill)
        self.assertIn("Chinese presentation text, including research, business, executive, strategy, product, and teaching decks", ppt_routing)
        self.assertIn("must pass through `writing-fidelity` plus `chinese-prose`", ppt_routing)
        self.assertIn("English scientific slide text can pass through `scientific-prose`", ppt_routing)
        profile_skills = "\n".join(profile["skills"])
        self.assertIn("skills/writing/core/writing-fidelity", profile_skills)
        self.assertIn("skills/writing/core/chinese-prose", profile_skills)
        self.assertIn("skills/writing/core/scientific-prose", profile_skills)
        self.assertIn("skills/tools/documents-media/render-chinese-math-pdf", profile_skills)
        self.assertIn("skills/writing/research/citation-verification", profile_skills)
        self.assertEqual(profile["secondary_skills"], [])

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

    def test_research_group_meeting_mode_requires_evidence_board_and_scientific_fields(self) -> None:
        actual = markdown_to_deck_plan.markdown_to_deck_plan(
            "# Updated Result\nEndpoint-specific ranking changed the interpretation.",
            "Group Meeting Regression",
            mode="research-group-meeting",
        )
        self.assertEqual(actual["metadata"]["mode"], "research-group-meeting")
        self.assertIn("research_state", actual)
        self.assertIn("evidence_board", actual)
        self.assertIn("missing_evidence", actual["evidence_board"])
        slide = actual["slides"][0]
        self.assertEqual(slide["page_function"], "RESEARCH_UPDATE")
        self.assertIn("scientific_objects", slide)
        self.assertEqual(validate_deck_plan.validate_deck_plan(actual), [])

    def test_research_group_meeting_validator_rejects_consulting_or_card_substitutes(self) -> None:
        bad_plan = {
            "schema_version": 1,
            "metadata": {
                "title": "Bad Group Meeting",
                "audience": "specialist",
                "mode": "research-group-meeting",
                "purpose": "group-meeting",
                "duration_minutes": 10,
                "language": "en",
                "template": "cuhk-default",
                "output": "pptx",
                "editability": "editable",
            },
            "research_state": {field: "known" for field in validate_deck_plan.RESEARCH_STATE_FIELDS},
            "evidence_board": {field: [] for field in validate_deck_plan.EVIDENCE_BOARD_FIELDS},
            "slides": [
                {
                    "id": "s01",
                    "title": "Three strategic pillars unlock the roadmap",
                    "key_message": "Use a rounded-card dashboard",
                    "slide_purpose": "present a slogan",
                    "visual_intent": "generic arrows",
                    "layout_hint": "cards",
                    "page_function": "RESULT_FIGURE",
                    "required_evidence": ["real endpoint result"],
                    "source_evidence_ids": [],
                    "scientific_objects": [],
                    "evidence_status": "available",
                    "layout_rationale": "card",
                    "allowed_fallback": "missing evidence or next experiment",
                    "forbidden_fallback": "cards",
                    "qa_criteria": ["real evidence visible"],
                }
            ],
        }
        errors = validate_deck_plan.validate_deck_plan(bad_plan)
        self.assertTrue(any("available evidence requires source_evidence_ids" in error for error in errors))
        self.assertTrue(any("layout_hint cannot be only cards" in error for error in errors))
        self.assertTrue(any("anti-pattern term" in error for error in errors))

    def test_research_group_meeting_references_are_packaged(self) -> None:
        references = SHARED / "references"
        for name in [
            "RESEARCH_GROUP_MEETING_MODE.md",
            "RESEARCH_SLIDE_ARCHETYPES.md",
            "RESEARCH_PRESENTATION_ANTIPATTERNS.md",
            "research_slide_reference_index.csv",
        ]:
            self.assertTrue((references / name).exists(), name)
        index_text = (references / "research_slide_reference_index.csv").read_text(encoding="utf-8")
        self.assertIn("source_url,page_number,page_function,visual_lesson", index_text)
        self.assertIn("RESULT_FIGURE", index_text)
        self.assertIn("SUPERVISOR_DECISION", index_text)
        rows = list(csv.DictReader(index_text.splitlines()))
        self.assertGreaterEqual(len(rows), 20)
        for row in rows:
            self.assertTrue(row["source_url"])
            self.assertTrue(row["page_number"])
            self.assertTrue(row["page_function"])
            self.assertTrue(row["visual_lesson"])
            self.assertTrue(row["what_to_learn"])
            self.assertTrue(row["what_not_to_copy"])
            self.assertTrue(row["rights_note"])

    def test_research_group_meeting_regression_generator_outputs_artifacts(self) -> None:
        script = REPO_ROOT / "tests/fixtures/presentations/research_group_meeting/generate_research_group_meeting_regression.py"
        with tempfile.TemporaryDirectory() as tmp:
            result = subprocess.run(
                [sys.executable, str(script), "--out-dir", tmp],
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            payload = json.loads(result.stdout)
            self.assertTrue(Path(payload["pptx"]).exists())
            self.assertTrue(Path(payload["pdf"]).exists())
            qa = json.loads(Path(payload["qa"]).read_text(encoding="utf-8"))
            self.assertEqual(qa["status"], "PASS")
            self.assertEqual(qa["editable_slide_count"], 4)
            self.assertEqual(len(qa["scientific_qa"]), 4)
            with ZipFile(payload["pptx"]) as deck:
                slide_names = [name for name in deck.namelist() if name.startswith("ppt/slides/slide") and name.endswith(".xml")]
            self.assertEqual(len(slide_names), 4)


if __name__ == "__main__":
    unittest.main()
