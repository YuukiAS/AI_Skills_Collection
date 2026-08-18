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
            "reference_sources_manifest.json",
        ]:
            self.assertTrue((references / name).exists(), name)
        index_text = (references / "research_slide_reference_index.csv").read_text(encoding="utf-8")
        self.assertIn("source_url,local_cache_file,actual_page_number,page_function,scientific_object,evidence_type", index_text)
        self.assertIn("RESULT_FIGURE", index_text)
        self.assertIn("SUPERVISOR_DECISION", index_text)
        self.assertNotIn("metadata page-function record", index_text)
        rows = list(csv.DictReader(index_text.splitlines()))
        self.assertGreaterEqual(len(rows), 40)
        required_fields = {
            "reference_id",
            "source_id",
            "talk_title",
            "local_cache_file",
            "actual_page_number",
            "scientific_object",
            "evidence_type",
            "approximate_figure_text_ratio",
            "uncertainty_handling",
            "negative_result_handling",
            "why_this_specific_page_works",
            "source_file_sha256",
            "rendered_page_sha256",
            "inspection_date",
            "inspection_means",
            "visible_page_title",
            "short_page_specific_observation",
            "suitable_contexts",
        }
        self.assertTrue(required_fields.issubset(rows[0]))
        for row in rows:
            self.assertTrue(row["source_url"])
            self.assertTrue(row["actual_page_number"].isdigit())
            self.assertTrue(row["page_function"])
            self.assertTrue(row["scientific_object"])
            self.assertTrue(row["evidence_type"])
            self.assertTrue(row["what_to_learn"])
            self.assertTrue(row["what_not_to_copy"])
            self.assertTrue(row["rights_note"])
            self.assertEqual(row["verification_status"], "inspected")
            self.assertEqual(len(row["source_file_sha256"]), 64)
            self.assertEqual(len(row["rendered_page_sha256"]), 64)
            self.assertRegex(row["inspection_date"], r"^20\d\d-\d\d-\d\d$")
            self.assertIn("pdftotext", row["inspection_means"])
        by_id = {row["reference_id"]: row for row in rows}
        self.assertEqual(by_id["RRL-020"]["source_id"], "SRC-006")
        self.assertEqual(by_id["RRL-020"]["actual_page_number"], "17")
        self.assertEqual(by_id["RRL-020"]["visible_page_title"], "Overall objective function")
        self.assertIn("objective", by_id["RRL-020"]["scientific_object"].lower())
        manifest = json.loads((references / "reference_sources_manifest.json").read_text(encoding="utf-8"))
        self.assertGreaterEqual(len(manifest["candidate_sources"]), 50)
        self.assertEqual(
            manifest["retrieval_priority"],
            ["PRIMARY_RESEARCH_PRESENTATION", "SECONDARY_TEACHING_REFERENCE", "PRESENTATION_GUIDANCE", "CANDIDATE_BACKLOG"],
        )
        tiers = {source["source_tier"] for source in manifest["candidate_sources"]}
        self.assertTrue({"PRIMARY_RESEARCH_PRESENTATION", "SECONDARY_TEACHING_REFERENCE", "PRESENTATION_GUIDANCE", "CANDIDATE_BACKLOG"}.issubset(tiers))
        stats_sources = [source for source in manifest["candidate_sources"] if source["domain_family"] in {"statistics", "biostatistics"}]
        self.assertGreaterEqual(len(stats_sources), 30)
        self.assertGreaterEqual(len([source for source in stats_sources if source["verification_status"] == "candidate_backlog"]), 10)

    def test_research_group_meeting_final_validation_rejects_unknown_and_checks_evidence_refs(self) -> None:
        draft = markdown_to_deck_plan.markdown_to_deck_plan(
            "# Updated Result\nEndpoint-specific ranking changed the interpretation.",
            "Group Meeting Regression",
            mode="research-group-meeting",
        )
        self.assertEqual(validate_deck_plan.validate_deck_plan(draft, phase="planning"), [])
        final_errors = validate_deck_plan.validate_deck_plan(draft, phase="final")
        self.assertTrue(any("final validation rejects UNKNOWN" in error for error in final_errors))
        draft["research_state"] = {field: "source-supported value" for field in validate_deck_plan.RESEARCH_STATE_FIELDS}
        draft["slides"][0]["source_evidence_ids"] = ["missing-id"]
        ref_errors = validate_deck_plan.validate_deck_plan(draft, phase="planning")
        self.assertTrue(any("references missing evidence_board item" in error for error in ref_errors))

    def test_research_group_meeting_regression_generator_outputs_artifacts(self) -> None:
        script = REPO_ROOT / "tests/fixtures/presentations/research_group_meeting/generate_research_group_meeting_regression.py"
        reviewer = REPO_ROOT / "tests/fixtures/presentations/research_group_meeting/review_research_group_meeting_regression.py"
        script_text = script.read_text(encoding="utf-8")
        self.assertNotIn('["RRL-003", "RRL-020", "RRL-022", "RRL-029"]', script_text)
        self.assertIn("retrieve_references", script_text)
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
            self.assertFalse((Path(tmp) / "SCIENTIFIC_QA.json").exists())
            manifest = json.loads(Path(payload["evidence_manifest"]).read_text(encoding="utf-8"))
            self.assertEqual(manifest["status"], "GENERATED_SOURCE_ARTIFACTS_ONLY")
            self.assertFalse(manifest["generator_may_pass"])
            self.assertEqual(manifest["editable_slide_count"], 4)
            self.assertEqual(len(manifest["slides"]), 4)
            expected_render = REPO_ROOT / "tests/fixtures/presentations/research_group_meeting/expected_render"
            for slide_number in range(1, 5):
                png = expected_render / f"slide-{slide_number}.png"
                self.assertTrue(png.exists(), png)
                self.assertGreater(png.stat().st_size, 10_000)
            for slide in manifest["slides"]:
                self.assertGreaterEqual(len(slide["reference_ids"]), 2)
                self.assertLessEqual(len(slide["reference_ids"]), 5)
                self.assertTrue(slide["expected_scientific_objects"])
                retrieval = slide["reference_retrieval"]
                self.assertEqual(slide["reference_ids"], retrieval["selected_ids"])
                self.assertGreaterEqual(len(retrieval["candidate_ids"]), len(retrieval["selected_ids"]))
                self.assertIn("intent", retrieval["query"])
                self.assertIn("page_functions", retrieval["query"])
                self.assertIn("evidence_types", retrieval["query"])
                self.assertTrue(retrieval["source_tiers"])
                self.assertEqual(set(retrieval["selected_ids"]), set(retrieval["ranking_relevance_reason"]))
                for selected_id in retrieval["selected_ids"]:
                    self.assertIn(selected_id, retrieval["candidate_ids"])
                    self.assertIn("source_tier=", retrieval["ranking_relevance_reason"][selected_id])
                self.assertIn("No full-slide screenshots", retrieval["what_was_not_copied"])
            render = json.loads(Path(payload["render_status"]).read_text(encoding="utf-8"))
            self.assertIn(render["status"], {"ok", "BLOCKED_REAL_PPTX_RENDER"})
            review_result = subprocess.run(
                [sys.executable, str(reviewer), "--out-dir", tmp],
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertEqual(review_result.returncode, 0, review_result.stderr)
            review_payload = json.loads(review_result.stdout)
            review = json.loads(Path(review_payload["review"]).read_text(encoding="utf-8"))
            self.assertEqual(review["review_type"], "MECHANICAL_VISUAL_REVIEW")
            self.assertEqual(review["academic_visual_decision"], "NOT_ASSESSED")
            self.assertFalse((Path(tmp) / "SCIENTIFIC_VISUAL_REVIEW.json").exists())
            self.assertTrue(review.get("reviewer_independent_from_generator") or review["status"] == "BLOCKED_REAL_PPTX_RENDER")
            if render["status"] == "ok":
                self.assertEqual(review["status"], "MECHANICAL_PASS")
                self.assertEqual(review["rendered_png_count"], 4)
                packet_builder = REPO_ROOT / "tests/fixtures/presentations/research_group_meeting/build_visual_review_packet.py"
                packet_dir = Path(tmp) / "visual-review-packet"
                packet_zip = Path(tmp) / "visual-review-packet.zip"
                packet_result = subprocess.run(
                    [
                        sys.executable,
                        str(packet_builder),
                        "--regression-dir",
                        tmp,
                        "--packet-dir",
                        str(packet_dir),
                        "--zip-path",
                        str(packet_zip),
                        "--implementation-commit",
                        "TEST_IMPLEMENTATION_COMMIT",
                        "--transport-commit",
                        "TEST_TRANSPORT_COMMIT",
                        "--skip-generate",
                    ],
                    check=False,
                    capture_output=True,
                    text=True,
                )
                self.assertEqual(packet_result.returncode, 0, packet_result.stderr)
                packet_payload = json.loads(packet_result.stdout)
                self.assertTrue(Path(packet_payload["packet_manifest"]).exists())
                self.assertTrue(packet_zip.exists())
                packet_manifest = json.loads(Path(packet_payload["packet_manifest"]).read_text(encoding="utf-8"))
                self.assertEqual(packet_manifest["academic_visual_decision"], "NOT_ASSESSED")
                self.assertEqual(len(packet_manifest["golden_render_comparison"]), 4)
                self.assertTrue(all("byte_matches_committed_golden" in item for item in packet_manifest["golden_render_comparison"]))
                packet_paths = {item["path"] for item in packet_manifest["files"]}
                self.assertTrue({f"rendered/slide-{slide}.png" for slide in range(1, 5)}.issubset(packet_paths))
                self.assertTrue({f"expected_render/slide-{slide}.png" for slide in range(1, 5)}.issubset(packet_paths))
                self.assertIn("pdf/research_group_meeting_regression.pdf", packet_paths)
                self.assertIn("research_group_meeting_regression.pptx", packet_paths)
                self.assertIn("EVIDENCE_MANIFEST.json", packet_paths)
                self.assertIn("RENDER_STATUS.json", packet_paths)
                source_packet_dir = Path(tmp) / "visual-review-packet-source"
                source_packet_zip = Path(tmp) / "visual-review-packet-source.zip"
                source_packet_result = subprocess.run(
                    [
                        sys.executable,
                        str(packet_builder),
                        "--source-dir",
                        str(REPO_ROOT / "tests/fixtures/presentations/research_group_meeting/visual_review_packet_source"),
                        "--packet-dir",
                        str(source_packet_dir),
                        "--zip-path",
                        str(source_packet_zip),
                        "--implementation-commit",
                        "TEST_IMPLEMENTATION_COMMIT",
                        "--transport-commit",
                        "TEST_TRANSPORT_COMMIT",
                    ],
                    check=False,
                    capture_output=True,
                    text=True,
                )
                self.assertEqual(source_packet_result.returncode, 0, source_packet_result.stderr)
                self.assertTrue(source_packet_zip.exists())
                pages_builder = REPO_ROOT / "tests/fixtures/presentations/research_group_meeting/build_visual_review_pages.py"
                pages_dir = Path(tmp) / "pages"
                pages_result = subprocess.run(
                    [
                        sys.executable,
                        str(pages_builder),
                        "--source-dir",
                        str(REPO_ROOT / "tests/fixtures/presentations/research_group_meeting/visual_review_packet_source"),
                        "--pages-dir",
                        str(pages_dir),
                        "--implementation-commit",
                        "TEST_IMPLEMENTATION_COMMIT",
                        "--transport-commit",
                        "TEST_TRANSPORT_COMMIT",
                        "--copy-latest",
                    ],
                    check=False,
                    capture_output=True,
                    text=True,
                )
                self.assertEqual(pages_result.returncode, 0, pages_result.stderr)
                pages_payload = json.loads(pages_result.stdout)
                immutable_dir = Path(pages_payload["immutable_dir"])
                self.assertTrue((immutable_dir / "research_group_meeting_regression.pdf").exists())
                self.assertTrue((immutable_dir / "packet_manifest.json").exists())
                pages_manifest = json.loads((immutable_dir / "packet_manifest.json").read_text(encoding="utf-8"))
                self.assertEqual(pages_manifest["transport"], "github_pages_pdf")
                self.assertEqual(pages_manifest["academic_visual_decision"], "NOT_ASSESSED")
                self.assertEqual(pages_manifest["pdf"]["page_count"], 4)
                published_paths = {item["path"] for item in pages_manifest["published_files"]}
                self.assertEqual(
                    published_paths,
                    {
                        "EVIDENCE_MANIFEST.json",
                        "MECHANICAL_VISUAL_REVIEW.json",
                        "RENDER_STATUS.json",
                        "research_group_meeting_regression.pdf",
                    },
                )
                self.assertFalse((immutable_dir / "research_group_meeting_regression.pptx").exists())
                self.assertFalse((immutable_dir / "rendered").exists())
            else:
                self.assertEqual(review["status"], "BLOCKED_REAL_PPTX_RENDER")
            with ZipFile(payload["pptx"]) as deck:
                slide_names = [name for name in deck.namelist() if name.startswith("ppt/slides/slide") and name.endswith(".xml")]
                media_names = [name for name in deck.namelist() if name.startswith("ppt/media/")]
            self.assertEqual(len(slide_names), 4)
            self.assertLess(len(media_names), 5)


if __name__ == "__main__":
    unittest.main()
