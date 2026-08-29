from __future__ import annotations

import json
import csv
import copy
import re
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
import generate_cuhk_scientific_layout_stage3 as stage3  # noqa: E402
import generate_research_presentation_production_entry as production_entry  # noqa: E402
import deck_quality_loop  # noqa: E402


class PresentationSharedTests(unittest.TestCase):
    def test_markdown_adapter_matches_deidentified_fixture(self) -> None:
        markdown = (SHARED / "fixtures" / "deidentified_markdown.md").read_text(encoding="utf-8")
        expected = json.loads((SHARED / "fixtures" / "expected_deck_plan.json").read_text(encoding="utf-8"))
        actual = markdown_to_deck_plan.markdown_to_deck_plan(markdown, "Deidentified Research Update")
        self.assertEqual(actual, expected)

    def test_research_markdown_defaults_to_exact_cuhk_beamer_output(self) -> None:
        actual = markdown_to_deck_plan.markdown_to_deck_plan("# One\nBody", "Research Update")
        self.assertEqual(actual["metadata"]["output"], "tex")
        self.assertEqual(actual["metadata"]["editability"], "source-editable")
        self.assertEqual(actual["slides"][0]["slide_purpose"], "communicate one research update message")
        self.assertIn("evidence-bearing visual", actual["slides"][0]["visual_intent"])

    def test_explicit_pptx_still_routes_to_editable_output(self) -> None:
        actual = markdown_to_deck_plan.markdown_to_deck_plan("# One\nBody", "Research Update", output="pptx")
        self.assertEqual(actual["metadata"]["output"], "pptx")
        self.assertEqual(actual["metadata"]["editability"], "editable")

    def test_explicit_tex_still_routes_to_source_editable_latex(self) -> None:
        actual = markdown_to_deck_plan.markdown_to_deck_plan("# One\nBody", "Research Update", output="tex")
        self.assertEqual(actual["metadata"]["output"], "tex")
        self.assertEqual(actual["metadata"]["editability"], "source-editable")

    def test_research_routing_defaults_to_exact_cuhk_beamer_with_editable_override(self) -> None:
        research_skill = (REPO_ROOT / "skills/tools/documents-media/presentations/research-presentations/SKILL.md").read_text(encoding="utf-8")
        ppt_routing = (SHARED / "ppt-skill-routing.md").read_text(encoding="utf-8")
        template_routing = (SHARED / "template-routing.md").read_text(encoding="utf-8")
        latex_notes = (SHARED / "compatibility/openai-latex.md").read_text(encoding="utf-8")
        cuhk_readme = (SHARED / "templates/cuhk/README.md").read_text(encoding="utf-8")
        visual_qa = (SHARED / "visual-qa.md").read_text(encoding="utf-8")

        self.assertIn("defaults to the exact CUHK Beamer route", research_skill)
        self.assertIn("source-editable `.tex`", research_skill)
        self.assertIn("PPT, PowerPoint, `.pptx`, editable, Slides, or later manual editing", ppt_routing)
        self.assertIn("PPTX/Slides/editable manual editing is explicitly requested", ppt_routing)
        self.assertIn("Explicit Beamer, LaTeX slides, `.tex`, academic PDF", ppt_routing)
        self.assertIn("exact CUHK Beamer route by default", template_routing)
        self.assertIn("explicitly requested editable PPTX/Slides", template_routing)
        self.assertIn("file exists", research_skill)
        self.assertIn("file existence alone is not completion", visual_qa)
        self.assertNotIn("Do not default academic or research decks to Beamer", research_skill)
        self.assertNotIn("editable Presentation/Slides route by default", research_skill)
        self.assertNotIn("editable Presentation/Slides route by default", template_routing)
        self.assertIn("If the local skill is not installed", research_skill)
        self.assertIn("Academic presentation compilation must first use", latex_notes)
        self.assertIn("render-chinese-math-pdf", latex_notes)
        self.assertIn("beamer/source/` is the canonical CUHK Beamer template", cuhk_readme)
        self.assertIn("derived scaffolds for non-exact workflows only", cuhk_readme)
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
        style_text = (source / "styles/beamerthemesintef.sty").read_text(encoding="utf-8")
        self.assertIn(r"\usetheme{sintef}", text)
        self.assertIn(r"\titlebackground*{assets/background}", text)
        self.assertIn(r"\usepackage{tcolorbox}", text)
        self.assertIn(r"\setbeamertemplate{headline}", style_text)
        self.assertIn(r"\includegraphics[height=4.0ex", style_text)
        self.assertIn(r"\insertsectionnavigationhorizontal", style_text)

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

    def test_research_slide_composition_representation(self) -> None:
        references = SHARED / "references"
        schema = references / "research_slide_composition.schema.json"
        families = references / "RESEARCH_COMPOSITION_FAMILIES.md"
        composition_index = references / "research_slide_composition_index.json"
        debug_montage = REPO_ROOT / "docs/audits/research_presentation_composition_debug_montage.svg"
        for path in [schema, families, composition_index, debug_montage]:
            self.assertTrue(path.exists(), path)

        validator = SHARED / "scripts/validate_reference_compositions.py"
        result = subprocess.run([sys.executable, str(validator)], check=False, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertRegex(result.stdout, r"validated 1[2-9] research slide composition records")

        rows = {
            row["reference_id"]: row
            for row in csv.DictReader((references / "research_slide_reference_index.csv").read_text(encoding="utf-8").splitlines())
        }
        index = json.loads(composition_index.read_text(encoding="utf-8"))
        records = index["records"]
        self.assertGreaterEqual(len(records), 12)
        self.assertGreaterEqual(len({record["source_id"] for record in records}), 4)
        self.assertGreaterEqual(len({record["page_function"] for record in records}), 6)
        self.assertTrue(any(record["page_function"] in {"STATISTICAL_MODEL", "ESTIMATOR", "THEOREM"} for record in records))
        self.assertGreaterEqual(len([record for record in records if record["page_function"] in {"RESULT_FIGURE", "CONFIDENCE_INTERVAL", "REAL_DATA_APPLICATION"}]), 2)
        self.assertGreaterEqual(len([record for record in records if record["page_function"] == "MEDICAL_IMAGE_COMPARISON"]), 2)
        self.assertTrue(any(record["layout_family"] == "model-check-or-negative" for record in records))
        self.assertTrue(any(any(region["role"] == "decision_or_next_step" for region in record["regions"]) for record in records))
        for record in records:
            row = rows[record["reference_id"]]
            self.assertEqual(row["verification_status"], "inspected")
            self.assertEqual(record["source_id"], row["source_id"])
            self.assertEqual(str(record["actual_page_number"]), row["actual_page_number"])
            self.assertEqual(record["page_function"], row["page_function"])
            self.assertEqual(record["rendered_page_sha256"], row["rendered_page_sha256"])
            primary = next(region for region in record["regions"] if region["region_id"] == record["primary_scientific_object_region_id"])
            self.assertAlmostEqual(primary["bbox"]["w"] * primary["bbox"]["h"], record["primary_object_area_ratio"], places=3)

        selector = SHARED / "scripts/select_reference_compositions.py"
        queries = [
            ["--page-function", "RESULT_FIGURE", "--limit", "2"],
            ["--page-function", "ESTIMATOR", "--scientific-object", "equation formula", "--limit", "2"],
            ["--page-function", "MEDICAL_IMAGE_COMPARISON", "--scientific-object", "aligned panel medical image", "--limit", "2"],
        ]
        for query in queries:
            selected = subprocess.run([sys.executable, str(selector), *query], check=False, capture_output=True, text=True)
            self.assertEqual(selected.returncode, 0, selected.stderr)
            payload = json.loads(selected.stdout)
            self.assertTrue(payload["matches"], query)
            self.assertIn("layout_family", payload["matches"][0])
            self.assertIn("primary_bbox", payload["matches"][0])

        montage_text = debug_montage.read_text(encoding="utf-8")
        self.assertIn("<svg", montage_text)
        self.assertIn("primary_scientific_object", montage_text)
        for forbidden in ["<image", "data:image", "base64,", ".png", ".jpg", ".jpeg", ".pdf", "/home/", ".cache/"]:
            self.assertNotIn(forbidden, montage_text)

    def test_gold_scientific_composition_library_and_runtime_recipe(self) -> None:
        references = SHARED / "references"
        for name in [
            "research_gold_composition.schema.json",
            "research_gold_composition_index.json",
        ]:
            self.assertTrue((references / name).exists(), name)

        validator = SHARED / "scripts/validate_gold_compositions.py"
        result = subprocess.run([sys.executable, str(validator)], check=False, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        self.assertIn("validated 10 gold scientific composition records", result.stdout)

        index = json.loads((references / "research_gold_composition_index.json").read_text(encoding="utf-8"))
        records = index["records"]
        self.assertLess(len(records), 13)
        self.assertGreaterEqual(len({record["source_id"] for record in records}), 3)
        jobs = {job for record in records for job in record["scientific_jobs"]}
        for required in [
            "motivation",
            "estimator",
            "method",
            "quantitative_result",
            "negative_result",
            "medical_image_comparison",
            "discussion",
            "next_experiment",
        ]:
            self.assertTrue(any(required in job for job in jobs), required)
        for record in records:
            self.assertIn(record["rights_reuse_boundary"], {"COMPOSITION_ONLY", "COMPARATIVE_GOLD"})
            self.assertTrue(record["gold_admission_evidence"]["evidence_paths"])
            self.assertEqual(record["gold_admission_evidence"]["item_level_judgement"], "PASS")
            self.assertTrue(record["gold_admission_evidence"]["visual_review_item_id"].startswith("item_"))
            self.assertTrue(record["gold_admission_evidence"]["visual_review_path"].endswith("VISUAL_REVIEW.json"))
            self.assertNotIn("metadata-only", record["gold_admission_evidence"]["basis"].lower())
            self.assertGreater(record["primary_object_area_ratio"], 0)
            self.assertTrue(record["annotation_legend_caption_panel_relations"])
            audience_contract = record["portable_composition_lesson"] + " " + " ".join(record["scientific_jobs"])
            for forbidden in ["RRL-", "SRC-", "GSC-", "QA", "provenance"]:
                self.assertNotIn(forbidden, audience_contract)
        report = json.loads((REPO_ROOT / "docs/audits/research_presentation_gold_composition_library/gold_admission_report.json").read_text(encoding="utf-8"))
        self.assertEqual(set(report["admitted_gold_ids"]), {record["gold_id"] for record in records})
        self.assertIn("discussion / next experiment", report["coverage_summary"])
        self.assertNotIn("no discussion", " ".join(report["coverage_limitations"]).lower())
        self.assertGreaterEqual(len(report["rejected_candidate_examples"]), 20)

        selector = SHARED / "scripts/select_gold_compositions.py"
        stat_selected = subprocess.run(
            [
                sys.executable,
                str(selector),
                "--page-function", "REAL_DATA_APPLICATION",
                "--scientific-object", "biostatistics quantitative model comparison result table figure",
                "--domain-family", "biostatistics",
                "--dominant-object-type", "plot table",
                "--evidence-type", "quantitative comparison result",
                "--density", "moderate",
                "--panel-count", "1",
                "--limit", "2",
            ],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(stat_selected.returncode, 0, stat_selected.stderr)
        stat_payload = json.loads(stat_selected.stdout)
        self.assertEqual(stat_payload["matches"][0]["gold_id"], "GSC-014")
        self.assertEqual(stat_payload["matches"][1]["gold_id"], "GSC-015")
        self.assertTrue(any(item["exclusion_reasons"] for item in stat_payload["excluded"]))

        med_selected = subprocess.run(
            [
                sys.executable,
                str(selector),
                "--page-function", "MEDICAL_IMAGE_COMPARISON",
                "--scientific-object", "medical image lesion samples task applications visual comparison",
                "--domain-family", "medical_imaging",
                "--dominant-object-type", "medical_image",
                "--evidence-type", "representative image comparison",
                "--density", "high",
                "--panel-count", "4",
                "--limit", "2",
            ],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(med_selected.returncode, 0, med_selected.stderr)
        med_payload = json.loads(med_selected.stdout)
        self.assertEqual(med_payload["matches"][0]["gold_id"], "GSC-008")
        self.assertEqual(med_payload["matches"][1]["gold_id"], "GSC-004")
        self.assertFalse(any(item["gold_id"] == "GSC-014" for item in med_payload["matches"]))

        discussion_selected = subprocess.run(
            [
                sys.executable,
                str(selector),
                "--page-function", "NEXT_EXPERIMENT",
                "--scientific-object", "discussion next experiment batch query bayesian optimization active learning DPP Mondrian diverse selection partition",
                "--domain-family", "statistics",
                "--dominant-object-type", "diagram plot comparison",
                "--evidence-type", "next-query experimental design",
                "--density", "moderate",
                "--panel-count", "4",
                "--limit", "2",
            ],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(discussion_selected.returncode, 0, discussion_selected.stderr)
        discussion_payload = json.loads(discussion_selected.stdout)
        self.assertEqual(discussion_payload["matches"][0]["gold_id"], "GSC-018")
        self.assertTrue(discussion_payload["matches"][0]["compatibility_reasons"])

        recipe_builder = SHARED / "scripts/build_gold_composition_recipe.py"
        incompatible_force = subprocess.run(
            [
                sys.executable,
                str(recipe_builder),
                "--page-function", "MEDICAL_IMAGE_COMPARISON",
                "--scientific-object", "medical image lesion samples",
                "--domain-family", "medical_imaging",
                "--dominant-object-type", "medical_image",
                "--force-gold-id", "GSC-014",
            ],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertNotEqual(incompatible_force.returncode, 0)
        self.assertIn("not compatible", incompatible_force.stderr + incompatible_force.stdout)

        probe_generator = SHARED / "scripts/generate_gold_composition_probe_artifacts.py"
        probe_result = subprocess.run([sys.executable, str(probe_generator)], check=False, capture_output=True, text=True)
        self.assertEqual(probe_result.returncode, 0, probe_result.stderr + probe_result.stdout)
        probes = json.loads((REPO_ROOT / "docs/audits/research_presentation_gold_composition_library/runtime_probe_traces.json").read_text(encoding="utf-8"))
        self.assertEqual(probes["status"], "PASS")
        self.assertEqual(len(probes["probes"]), 3)
        for probe in probes["probes"]:
            checks = probe["checks"]
            self.assertTrue(checks["runtime_selected"])
            if probe["alternate_error"] == "no compatible gold composition record":
                self.assertFalse(checks["alternate_runtime_selected"])
                self.assertTrue(checks["exclusion_changes_behavior"])
            else:
                self.assertTrue(checks["alternate_runtime_selected"])
                self.assertTrue(checks["alternate_is_distinct"])
                self.assertTrue(checks["alternate_has_compatibility_reasons"])
                self.assertTrue(checks["primary_bbox_changed"])
            self.assertTrue(checks["actually_consumed"])
            self.assertTrue(checks["output_affected"])
            if probe["alternate_recipe"]:
                self.assertNotEqual(probe["baseline_recipe"]["recipe_sha256"], probe["alternate_recipe"]["recipe_sha256"])
            self.assertNotIn("forced compatible probe", json.dumps(probe, ensure_ascii=False))
            consumed = set(probe["baseline_recipe"]["runtime_trace"]["actually_consumed_fields"])
            self.assertTrue({"primary_bbox", "visual_hierarchy", "alignment_groups"}.issubset(consumed))
        discussion_probe = next(item for item in probes["probes"] if item["probe_id"] == "discussion_next_experiment_batch_query")
        self.assertEqual(discussion_probe["baseline_recipe"]["selected_gold_id"], "GSC-018")
        self.assertEqual(discussion_probe["alternate_error"], "no compatible gold composition record")

    def test_cuhk_scientific_layout_stage3_contract(self) -> None:
        generator = SHARED / "scripts/generate_cuhk_scientific_layout_stage3.py"
        validator = SHARED / "scripts/validate_cuhk_scientific_layout_stage3.py"
        with tempfile.TemporaryDirectory() as tmp:
            generated = Path(tmp) / "stage3"
            implementation_commit = "a" * 40
            result = subprocess.run(
                [
                    sys.executable,
                    str(generator),
                    "--out-dir",
                    str(generated),
                    "--task-key",
                    "030_stage3_visual_recovery",
                    "--implementation-commit",
                    implementation_commit,
                ],
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertIn(result.returncode, {0, 2}, result.stderr + result.stdout)

            validation = subprocess.run(
                [
                    sys.executable,
                    str(validator),
                    "--out-dir",
                    str(generated),
                    "--allow-missing-render",
                    "--task-key",
                    "030_stage3_visual_recovery",
                ],
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertEqual(validation.returncode, 0, validation.stderr + validation.stdout)

            manifest = json.loads((generated / "BUILD_MANIFEST.json").read_text(encoding="utf-8"))
            self.assertEqual(manifest["schema"], "RESEARCH_CUHK_STAGE3_BUILD_MANIFEST_V1")
            self.assertEqual(manifest["task_key"], "030_stage3_visual_recovery")
            self.assertEqual(manifest["implementation_commit"], implementation_commit)
            self.assertIn("templates/cuhk/beamer/source", manifest["canonical_cuhk_source"])
            self.assertTrue(manifest["canonical_files"])
            self.assertTrue((REPO_ROOT / manifest["tex"]).exists())
            self.assertTrue((REPO_ROOT / manifest["scientific_layout_include"]).exists())

            layouts = json.loads((generated / "resolved_layouts.json").read_text(encoding="utf-8"))["layouts"]
            self.assertEqual(len(layouts), 6)
            self.assertEqual(
                {layout["page_job"] for layout in layouts},
                {
                    "STATISTICAL_MODEL",
                    "REAL_DATA_APPLICATION",
                    "EXPERIMENT_DESIGN",
                    "NEGATIVE_RESULT",
                    "MEDICAL_IMAGE_COMPARISON",
                    "NEXT_EXPERIMENT",
                },
            )
            self.assertIn("GSC-018", {layout["selected_gold_id"] for layout in layouts})
            for layout in layouts:
                consumed = set(layout["source_recipe_fields_consumed"])
                self.assertTrue(
                    {
                        "primary_bbox",
                        "primary_object_area_ratio",
                        "visual_hierarchy",
                        "alignment_groups",
                        "reading_flow",
                        "annotation_legend_caption_panel_relations",
                        "content_capacity",
                    }.issubset(consumed)
                )
                self.assertFalse(layout["audience_safe_output_contract"]["internal_ids_exposed"])
                self.assertTrue(layout["text_region_packing"]["non_overlapping"])
                safe = layout["exact_cuhk_content_safe_region"]
                bbox = layout["resolved_primary_object_geometry"]
                self.assertGreaterEqual(bbox["x"], safe["x"])
                self.assertGreaterEqual(bbox["y"], safe["y"])
                self.assertLessEqual(bbox["x"] + bbox["w"], safe["x"] + safe["w"] + 0.0001)
                self.assertLessEqual(bbox["y"] + bbox["h"], safe["y"] + safe["h"] + 0.0001)
                for support in layout["resolved_supporting_object_geometry"].values():
                    self.assertGreaterEqual(support["x"], safe["x"] - 0.0001)
                    self.assertGreaterEqual(support["y"], safe["y"] - 0.0001)
                    self.assertLessEqual(support["x"] + support["w"], safe["x"] + safe["w"] + 0.0001)
                    self.assertLessEqual(support["y"] + support["h"], safe["y"] + safe["h"] + 0.0001)
                if layout["page_job"] == "REAL_DATA_APPLICATION":
                    self.assertGreaterEqual(bbox["w"] * bbox["h"], 0.34)
                    self.assertEqual(layout["executable_layout_family"], "presentation_native_quantitative_result")
                    self.assertEqual(layout["job_specific_runtime_contract"]["primitive"], "csv_driven_tikz_result_figure")
                    self.assertIn(
                        "presentation_native_result_figure",
                        {item["native_type"] for item in layout["native_objects"]},
                    )
                if layout["page_job"] == "MEDICAL_IMAGE_COMPARISON":
                    self.assertGreaterEqual(bbox["w"], 0.84)
                    self.assertGreaterEqual(bbox["h"], 0.48)
                    self.assertEqual(layout["executable_layout_family"], "same_case_medical_roi_zoom")
                    zoom = layout["job_specific_runtime_contract"]["same_case_roi_zoom"]
                    self.assertEqual(len(zoom["crop_records"]), 3)
                    semantic_records = {Path(record["source_asset"]).stem: record for record in zoom["crop_records"]}
                    self.assertEqual(semantic_records["failure_gt"]["visible_error_classes"], ["fn"])
                    self.assertEqual(semantic_records["failure_pred"]["visible_error_classes"], ["fp"])
                    self.assertEqual(sorted(semantic_records["failure_error"]["visible_error_classes"]), ["fn", "fp"])
                    for record in zoom["crop_records"]:
                        self.assertTrue(record["same_case_coordinate_space"])
                        self.assertTrue(record["semantic_overlay"])
                        self.assertTrue((generated / "cuhk_stage3_build" / record["display_asset"]).exists())
                        self.assertTrue((generated / "cuhk_stage3_build" / record["zoom_asset"]).exists())
                if layout["page_job"] in {"EXPERIMENT_DESIGN", "NEXT_EXPERIMENT"}:
                    self.assertGreaterEqual(bbox["w"], 0.87)
                    self.assertGreaterEqual(bbox["h"], 0.55)
                    self.assertGreaterEqual(bbox["w"] * bbox["h"], 0.49)
                    support = layout["resolved_supporting_object_geometry"]["annotation"]
                    self.assertGreaterEqual(support["w"], 0.87)
                    self.assertGreaterEqual(support["y"], bbox["y"] + bbox["h"])
                if layout["page_job"] == "EXPERIMENT_DESIGN":
                    self.assertEqual(layout["executable_layout_family"], "typed_experiment_design_hierarchy")
                    self.assertEqual(layout["job_specific_runtime_contract"]["primitive"], "typed_scientific_hierarchy_relation_map")
                if layout["page_job"] == "NEXT_EXPERIMENT":
                    self.assertEqual(layout["executable_layout_family"], "evidence_to_decision_next_experiment")
                    self.assertEqual(layout["job_specific_runtime_contract"]["primitive"], "evidence_manipulation_comparator_decision_map")

            trace = json.loads((generated / "runtime_trace.json").read_text(encoding="utf-8"))
            self.assertEqual(len(trace["slides"]), 6)
            for slide in trace["slides"]:
                self.assertTrue(slide["selected_gold_id"])
                self.assertTrue(slide["emitted_tex_object_ids"])

            mutation = json.loads((generated / "mutation_regression.json").read_text(encoding="utf-8"))
            self.assertEqual(mutation["status"], "PASS")
            self.assertTrue(mutation["checks"]["resolved_geometry_changed"])
            self.assertNotEqual(mutation["baseline_geometry_signature"], mutation["mutated_geometry_signature"])

            capacity_failure = json.loads((generated / "capacity_failure_contract.json").read_text(encoding="utf-8"))
            self.assertEqual(capacity_failure["status"], "SPLIT_REQUIRED")
            self.assertFalse(capacity_failure["generic_layout_fallback_used"])

            dependency_probe = json.loads((generated / "dependency_probe.json").read_text(encoding="utf-8"))
            self.assertEqual(dependency_probe["schema"], "RESEARCH_CUHK_STAGE3_BUILD_DEPENDENCY_PROBE_V1")
            self.assertIn("pdftoppm", dependency_probe["commands"])
            self.assertEqual(
                manifest["compile_status"]["status"] == "COMPILED",
                dependency_probe["tex_engine_available"],
            )
            visual_inputs = json.loads((generated / "visual_inputs.json").read_text(encoding="utf-8"))
            self.assertEqual(visual_inputs["schema"], "AI_BRIDGE_VISUAL_INPUT_MANIFEST_V1")
            self.assertEqual(visual_inputs["task_key"], "030_stage3_visual_recovery")
            self.assertEqual(visual_inputs["workflow_type"], "reviewed_handoff")
            self.assertEqual(visual_inputs["identity_bindings"]["implementation_commit"], implementation_commit)
            if manifest["render_status"]["status"] == "ok":
                self.assertEqual(len(visual_inputs["inputs"]), 6)
            else:
                self.assertEqual(len(visual_inputs["inputs"]), 0)
            self.assertIn("build_manifest_sha256", visual_inputs["identity_bindings"])

            tex = (REPO_ROOT / manifest["tex"]).read_text(encoding="utf-8")
            self.assertIn(r"\usetheme{sintef}", tex)
            self.assertIn(r"\input{scientific_layouts.tex}", tex)
            self.assertIn(r"\StageThreeNode", tex)
            self.assertIn(r"\displaystyle", tex)
            self.assertIn(r"\includegraphics", tex)
            self.assertIn("Coverage by ICC under imbalanced clusters", tex)
            self.assertNotIn("coverage_by_icc.png", tex)
            self.assertIn("Small-G, high-ICC imbalance still suppresses coverage", tex)
            self.assertNotIn("Native axes, facets, method key, nominal line, and interval callout", tex)
            self.assertIn(r"centers \(G=8,20,50\)", tex)
            self.assertIn(r"ICC \(\rho=0,.1,.3,.5\)", tex)
            self.assertIn("naive iid OLS z interval", tex)
            self.assertIn("The connector direction encodes data generation before interval estimation", tex)
            self.assertNotIn("centers -> subjects", tex)
            self.assertIn("Coverage target 0.95", tex)
            self.assertIn(r"\scriptsize coverage", tex)
            self.assertIn("DPP diverse batch", tex)
            self.assertIn("random batch", tex)
            self.assertIn("coverage >= .94", tex)
            self.assertIn("Same-case ROI zoom", tex)
            self.assertIn("Overlay legend", tex)
            self.assertIn("Decision rule", tex)
            process_tex = "\n".join(
                stage3.emit_flow(spec, stage3.resolve_layout(spec))
                for spec in stage3.page_specs()
                if spec["page_job"] in {"EXPERIMENT_DESIGN", "NEXT_EXPERIMENT"}
            )
            self.assertNotIn(r"\tiny", process_tex)
            self.assertNotIn(r"\scriptsize", process_tex)
            self.assertIn(r"\footnotesize", process_tex)
            self.assertNotIn("Error zoom:", tex)
            for forbidden in ["RRL-", "SRC-", "GSC-", "Reference retrieval", "EVIDENCE_MANIFEST", "Diagram contract", "run ID", "fixture", "workflow"]:
                self.assertNotIn(forbidden, tex)
            plugin_generator = REPO_ROOT / "plugins/codex/plugins/presentations/shared/scripts/generate_cuhk_scientific_layout_stage3.py"
            plugin_validator = REPO_ROOT / "plugins/codex/plugins/presentations/shared/scripts/validate_cuhk_scientific_layout_stage3.py"
            self.assertEqual(generator.read_text(encoding="utf-8"), plugin_generator.read_text(encoding="utf-8"))
            self.assertEqual(validator.read_text(encoding="utf-8"), plugin_validator.read_text(encoding="utf-8"))

            strict = subprocess.run(
                [
                    sys.executable,
                    str(validator),
                    "--out-dir",
                    str(generated),
                    "--task-key",
                    "030_stage3_visual_recovery",
                ],
                check=False,
                capture_output=True,
                text=True,
            )
            if manifest["render_status"]["status"] == "ok":
                self.assertEqual(strict.returncode, 0, strict.stderr + strict.stdout)
                self.assertEqual(manifest["mechanical_qa"]["status"], "MECHANICAL_PASS")
                self.assertGreaterEqual(manifest["render_status"]["png_count"], 7)
            else:
                self.assertNotEqual(strict.returncode, 0)
                self.assertIn(manifest["render_status"]["status"], strict.stderr + strict.stdout)
                self.assertNotEqual(manifest["mechanical_qa"]["status"], "MECHANICAL_PASS")

    def test_process_page_projection_scale_is_page_job_generic(self) -> None:
        experiment_spec = {
            "page_id": "agnostic_design_map",
            "page_job": "EXPERIMENT_DESIGN",
            "section": "Design",
            "title": "Acquisition design links perturbations to endpoint checks",
            "query": {
                "page_function": "EXPERIMENT_DESIGN",
                "scientific_object": "acquisition design perturbation procedure endpoint hierarchy",
                "domain_family": "method_evaluation",
                "dominant_object_type": "diagram",
                "evidence_type": "experiment design",
                "density": "moderate",
                "panel_count": 4,
            },
            "content_kind": "flow",
            "dominant_object": "scientific_relation_diagram",
            "nodes": ["Input factors", "Nested samples", "Procedures", "Endpoint checks"],
            "design_factors": ["site count", "measurement noise", "held-out calibration"],
            "procedures": ["baseline estimator", "regularized estimator"],
            "endpoints": ["coverage floor", "width budget", "bias check"],
            "annotation": "Perturbations feed nested samples before procedures and endpoint checks.",
            "required_panel_count": 4,
        }
        next_spec = {
            "page_id": "agnostic_next_decision",
            "page_job": "NEXT_EXPERIMENT",
            "section": "Next",
            "title": "Next acquisition tests whether design choices reduce failure",
            "query": {
                "page_function": "NEXT_EXPERIMENT",
                "scientific_object": "next experiment evidence manipulation comparator decision",
                "domain_family": "method_evaluation",
                "dominant_object_type": "diagram plot comparison",
                "evidence_type": "next-query experimental design",
                "density": "moderate",
                "panel_count": 4,
            },
            "content_kind": "next_experiment",
            "dominant_object": "next_experiment_reasoning",
            "nodes": ["Failure case", "Sampling choice", "Comparator", "Decision"],
            "current_limit": "The current acquisition leaves one endpoint unstable under shift.",
            "strategy_variation": ["diverse batch", "uncertainty batch", "stratified batch"],
            "comparator_setup": ["small-sample correction", "resampling baseline"],
            "decision_criterion": "Go if the unstable endpoint clears the prespecified floor.",
            "annotation": "Failure evidence determines the next manipulation and comparator choice.",
            "required_panel_count": 4,
        }
        for spec in [experiment_spec, next_spec]:
            layout = stage3.resolve_layout(spec)
            bbox = layout["resolved_primary_object_geometry"]
            safe = layout["exact_cuhk_content_safe_region"]
            self.assertEqual(bbox["x"], safe["x"])
            self.assertGreaterEqual(bbox["w"], 0.87)
            self.assertGreaterEqual(bbox["h"], 0.55)
            self.assertGreaterEqual(bbox["w"] * bbox["h"], 0.49)
            tex = stage3.emit_flow(spec, layout)
            self.assertNotIn(r"\tiny", tex)
            self.assertNotIn(r"\scriptsize", tex)
            self.assertIn(r"\footnotesize", tex)
            for x1, x2 in re.findall(r"\\StageThreeConnector\{([0-9.]+)\}\{[0-9.]+\}\{([0-9.]+)\}\{[0-9.]+\};", tex):
                self.assertGreater(float(x2), float(x1))
        experiment_tex = stage3.emit_flow(experiment_spec, stage3.resolve_layout(experiment_spec))
        self.assertIn("site count", experiment_tex)
        self.assertIn("Nested samples", experiment_tex)
        self.assertIn("regularized estimator", experiment_tex)
        self.assertIn("bias check", experiment_tex)
        next_tex = stage3.emit_flow(next_spec, stage3.resolve_layout(next_spec))
        self.assertIn("unstable endpoint", next_tex)
        self.assertIn("stratified batch", next_tex)
        self.assertIn("resampling baseline", next_tex)
        for unrelated_tex in [experiment_tex, next_tex]:
            for fixture_only in [
                "DGP stress grid",
                "Center hierarchy",
                "Interval procedures",
                "Subject records nested inside each center",
                "400 reps per cell",
                "coverage shortfall at high ICC",
                "G=8",
                "ICC=.5",
                "CR2",
                "wild cluster bootstrap",
            ]:
                self.assertNotIn(fixture_only, unrelated_tex)

    def test_research_presentation_one_call_production_entry(self) -> None:
        generator = SHARED / "scripts/generate_research_presentation_production_entry.py"
        validator = SHARED / "scripts/validate_research_presentation_production_entry.py"
        bundle = SHARED / "fixtures/stage4_engineering_research_bundle/bundle.json"
        implementation_commit = "b" * 40
        with tempfile.TemporaryDirectory() as tmp:
            generated = Path(tmp) / "production"
            result = subprocess.run(
                [
                    sys.executable,
                    str(generator),
                    "--input-bundle",
                    str(bundle),
                    "--out-dir",
                    str(generated),
                    "--implementation-commit",
                    implementation_commit,
                ],
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertIn(result.returncode, {0, 2}, result.stderr + result.stdout)

            validation = subprocess.run(
                [sys.executable, str(validator), "--out-dir", str(generated), "--allow-missing-render"],
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertEqual(validation.returncode, 0, validation.stderr + validation.stdout)

            manifest = json.loads((generated / "BUILD_MANIFEST.json").read_text(encoding="utf-8"))
            self.assertEqual(manifest["schema"], "RESEARCH_PRESENTATION_PRODUCTION_BUILD_MANIFEST_V1")
            self.assertEqual(manifest["task_key"], "031_research_presentation_one_call_production_entry")
            self.assertEqual(manifest["implementation_commit"], implementation_commit)
            self.assertRegex(manifest["render_input_identity_sha256"], r"^[0-9a-f]{64}$")
            self.assertEqual(manifest["render_input_identity"]["sha256"], manifest["render_input_identity_sha256"])
            self.assertIn("templates/cuhk/beamer/source", manifest["canonical_cuhk_source"])
            self.assertEqual(manifest["quality_loop_handoff"]["status"], "WAITING_FOR_DECK_VISUAL_REVIEW")
            self.assertIn("Stage 4 PASS", manifest["stage4_boundary"])
            if manifest["render_status"]["status"] == "ok":
                self.assertEqual(manifest["deck_contact_sheet"]["status"], "GENERATED")
                self.assertTrue((REPO_ROOT / manifest["deck_contact_sheet"]["path"]).exists())
                self.assertTrue(manifest["mechanical_qa"]["checks"]["deck_contact_sheet_generated"])
            self.assertTrue(manifest["mechanical_qa"]["checks"]["quality_loop_budget_enforced"])

            deck_plan = json.loads((generated / "deck_plan.json").read_text(encoding="utf-8"))
            self.assertEqual(deck_plan["metadata"]["production_entry"], "research-presentations one-call production")
            self.assertEqual(deck_plan["metadata"]["output"], "tex")
            self.assertEqual(deck_plan["metadata"]["editability"], "source-editable")
            self.assertEqual(len(deck_plan["slides"]), 6)
            self.assertFalse(any("UNKNOWN" in json.dumps(slide, ensure_ascii=False) for slide in deck_plan["slides"]))
            self.assertEqual(
                [slide["page_function"] for slide in deck_plan["slides"]],
                [
                    "STATISTICAL_MODEL",
                    "REAL_DATA_APPLICATION",
                    "EXPERIMENT_DESIGN",
                    "NEGATIVE_RESULT",
                    "NEXT_EXPERIMENT",
                    "MEDICAL_IMAGE_COMPARISON",
                ],
            )

            fidelity = json.loads((generated / "source_fidelity_map.json").read_text(encoding="utf-8"))
            self.assertFalse(fidelity["stage5_holdout_eligible"])
            self.assertIn("not a final Stage 5", fidelity["holdout_exclusion_reason"])
            self.assertEqual(len(fidelity["pages"]), 6)
            for page in fidelity["pages"]:
                self.assertTrue(page["anchors"])
                self.assertTrue(page["source_recipe_fields_consumed"])
                self.assertTrue(page["selected_gold_id"])

            trace = json.loads((generated / "runtime_trace.json").read_text(encoding="utf-8"))
            self.assertEqual(trace["entrypoint"], "research-presentations one-call production")
            self.assertEqual(trace["benchmark_generators_called_as_entrypoint"], [])
            self.assertEqual(
                [slide["page_job"] for slide in trace["slides"]],
                [
                    "STATISTICAL_MODEL",
                    "REAL_DATA_APPLICATION",
                    "EXPERIMENT_DESIGN",
                    "NEGATIVE_RESULT",
                    "NEXT_EXPERIMENT",
                    "MEDICAL_IMAGE_COMPARISON",
                ],
            )
            jobs = {slide["page_job"] for slide in trace["slides"]}
            self.assertEqual(
                jobs,
                {
                    "STATISTICAL_MODEL",
                    "REAL_DATA_APPLICATION",
                    "EXPERIMENT_DESIGN",
                    "NEGATIVE_RESULT",
                    "MEDICAL_IMAGE_COMPARISON",
                    "NEXT_EXPERIMENT",
                },
            )
            for slide in trace["slides"]:
                self.assertFalse(slide["benchmark_helper_orchestration_surface_used"])
                self.assertFalse(slide["force_gold_id_used"])
                self.assertFalse(slide["score_override_used"])
                self.assertTrue(slide["normal_selector_matches"])
                self.assertTrue(slide["source_derived_composition_fields_consumed"])

            storyline = json.loads((generated / "storyline_trace.json").read_text(encoding="utf-8"))
            self.assertEqual(storyline["schema"], "RESEARCH_PRESENTATION_STORYLINE_TRACE_V1")
            self.assertIn("domain token profiles", storyline["source_derivation"])
            self.assertEqual(
                storyline["storyline_order"],
                [
                    "STATISTICAL_MODEL",
                    "REAL_DATA_APPLICATION",
                    "EXPERIMENT_DESIGN",
                    "NEGATIVE_RESULT",
                    "NEXT_EXPERIMENT",
                    "MEDICAL_IMAGE_COMPARISON",
                ],
            )
            medical_assignment = next(item for item in storyline["page_assignments"] if item["page_job"] == "MEDICAL_IMAGE_COMPARISON")
            self.assertEqual(medical_assignment["workstream_order"], 2)
            self.assertEqual(medical_assignment["workstream_label"], "Segmentation robustness")
            second_workstream = next(item for item in storyline["workstreams"] if item["workstream_order"] == 2)
            self.assertFalse(second_workstream["source_supported_cross_workstream_relation_to_previous"])
            self.assertIn("independent workstream", second_workstream["relation_to_previous"])

            layouts = json.loads((generated / "resolved_layouts.json").read_text(encoding="utf-8"))["layouts"]
            model_layout = next(layout for layout in layouts if layout["page_job"] == "STATISTICAL_MODEL")
            self.assertGreaterEqual(len(model_layout["native_objects"]), 5)
            self.assertIn("key_message", model_layout["job_specific_runtime_contract"]["source_fields_consumed"])
            self.assertIn("scientific_objects", model_layout["job_specific_runtime_contract"]["source_fields_consumed"])
            self.assertIn("source-grounded supporting roles", " ".join(model_layout["source_to_cuhk_transform"]))
            medical_layout = next(layout for layout in layouts if layout["page_job"] == "MEDICAL_IMAGE_COMPARISON")
            semantic_records = {
                Path(record["source_asset"]).stem: record
                for record in medical_layout["job_specific_runtime_contract"]["same_case_roi_zoom"]["crop_records"]
            }
            self.assertEqual(semantic_records["failure_gt"]["visible_error_classes"], ["fn"])
            self.assertEqual(semantic_records["failure_pred"]["visible_error_classes"], ["fp"])
            self.assertEqual(sorted(semantic_records["failure_error"]["visible_error_classes"]), ["fn", "fp"])
            for record in semantic_records.values():
                self.assertTrue(record["semantic_overlay"])
                self.assertTrue((generated / "cuhk_production_build" / record["display_asset"]).exists())
                self.assertTrue((generated / "cuhk_production_build" / record["zoom_asset"]).exists())

            visual_inputs = json.loads((generated / "visual_inputs.json").read_text(encoding="utf-8"))
            self.assertEqual(visual_inputs["schema"], "AI_BRIDGE_VISUAL_INPUT_MANIFEST_V1")
            self.assertEqual(visual_inputs["task_key"], "031_research_presentation_one_call_production_entry")
            self.assertEqual(visual_inputs["identity_bindings"]["implementation_commit"], implementation_commit)
            self.assertIn("deck_sequence_summary", visual_inputs["identity_bindings"])
            self.assertIn("quality_loop_state", visual_inputs["identity_bindings"])
            self.assertEqual(visual_inputs["identity_bindings"]["render_input_identity_sha256"], manifest["render_input_identity_sha256"])
            if manifest["render_status"]["status"] == "ok":
                self.assertEqual(visual_inputs["identity_bindings"]["deck_contact_sheet_sha256"], manifest["deck_contact_sheet"]["sha256"])
                self.assertRegex(visual_inputs["identity_bindings"]["rendered_pixel_identity_sha256"], r"^[0-9a-f]{64}$")
            else:
                self.assertIsNone(visual_inputs["identity_bindings"]["rendered_pixel_identity_sha256"])
            self.assertIn("source-specific content", visual_inputs["rubric"]["instructions"])
            self.assertIn("coherent research update", visual_inputs["rubric"]["instructions"])
            self.assertIn("deck_contact_sheet", visual_inputs["rubric"]["instructions"])
            self.assertIn("top-level package PASS is not enough", visual_inputs["rubric"]["instructions"])
            if manifest["render_status"]["status"] == "ok":
                self.assertEqual(len(visual_inputs["inputs"]), 7)
                self.assertEqual(visual_inputs["inputs"][-1]["logical_id"], "deck_contact_sheet")

            deck_sequence = json.loads((generated / "deck_sequence_summary.json").read_text(encoding="utf-8"))
            self.assertEqual(deck_sequence["schema"], "RESEARCH_PRESENTATION_DECK_SEQUENCE_SUMMARY_V1")
            self.assertEqual(deck_sequence["page_count"], 6)
            self.assertRegex(deck_sequence["render_input_identity_sha256"], r"^[0-9a-f]{64}$")
            self.assertEqual(deck_sequence["render_input_manifest"]["sha256"], deck_sequence["render_input_identity_sha256"])
            render_input_roles = {item["role"] for item in deck_sequence["render_input_manifest"]["files"]}
            self.assertTrue({"main_tex", "scientific_layout_include", "copied_scientific_asset"}.issubset(render_input_roles))
            if manifest["render_status"]["status"] == "ok":
                self.assertEqual(deck_sequence["deck_contact_sheet"]["sha256"], manifest["deck_contact_sheet"]["sha256"])
                self.assertEqual(deck_sequence["pixel_evidence_status"]["status"], "AVAILABLE")
                self.assertRegex(deck_sequence["rendered_pixel_identity_sha256"], r"^[0-9a-f]{64}$")
            else:
                self.assertEqual(deck_sequence["pixel_evidence_status"]["status"], "UNAVAILABLE_RENDER_NOT_OK")
                self.assertIsNone(deck_sequence["rendered_pixel_identity_sha256"])
                self.assertIsNone(deck_sequence["deck_contact_sheet"]["path"])
                self.assertIsNone(deck_sequence["deck_contact_sheet"]["sha256"])
            self.assertEqual(
                deck_sequence["page_order"],
                [
                    "slide_2_statistical_model",
                    "slide_3_real_data_application",
                    "slide_4_experiment_design",
                    "slide_5_negative_result",
                    "slide_6_next_experiment",
                    "slide_7_medical_image_comparison",
                ],
            )
            self.assertEqual(len(deck_sequence["title_sequence"]), 6)
            for page in deck_sequence["pages"]:
                self.assertIn(page["visual_density"]["machine_density"], {"low", "moderate", "high"})
                if manifest["render_status"]["status"] == "ok":
                    self.assertEqual(page["rendered_pixel_status"], "AVAILABLE")
                    self.assertRegex(page["rendered_page_sha256"], r"^[0-9a-f]{64}$")
                else:
                    self.assertEqual(page["rendered_pixel_status"], "UNAVAILABLE_RENDER_NOT_OK")
                    self.assertIsNone(page["rendered_page_sha256"])
                    self.assertIsNone(page["rendered_page_path"])
                self.assertTrue(page["primary_scientific_object_type"])

            quality_loop = json.loads((generated / "quality_loop_state.json").read_text(encoding="utf-8"))
            self.assertEqual(quality_loop["schema"], "RESEARCH_PRESENTATION_DECK_QUALITY_LOOP_STATE_V1")
            self.assertEqual(quality_loop["max_repair_cycles"], 1)
            self.assertEqual(quality_loop["repair_cycle_count"], 0)
            self.assertEqual(quality_loop["render_identity_kind"], "render_input_identity_sha256")
            self.assertEqual(quality_loop["initial_render_identity"], quality_loop["initial_render_input_identity"])
            self.assertRegex(quality_loop["initial_render_input_identity"], r"^[0-9a-f]{64}$")
            self.assertEqual(quality_loop["initial_render_input_manifest"]["sha256"], quality_loop["initial_render_input_identity"])
            self.assertEqual(quality_loop["deck_level_decision"], "WAITING_FOR_DECK_VISUAL_REVIEW")
            self.assertIsNone(quality_loop["final_decision"])

            tex = (REPO_ROOT / manifest["tex"]).read_text(encoding="utf-8")
            self.assertIn(r"\usetheme{sintef}", tex)
            self.assertIn("Clustered Interval Calibration And Synthetic Segmentation Robustness", tex)
            self.assertIn("Uncertainty calibration across clustered data and segmentation stress cases", tex)
            self.assertIn("Coverage by ICC under imbalanced clusters", tex)
            self.assertIn("Model components", tex)
            self.assertIn("Interpretation", tex)
            self.assertIn("center random effect", tex)
            self.assertIn("The source model makes center-level dependence explicit before interval comparison.", tex)
            self.assertNotIn("Calibration link", tex)
            self.assertNotIn("Source-grounded terms", tex)
            self.assertNotIn("Center variation and individual variation define the ICC before the interval comparison.", tex)
            self.assertIn("Same-case ROI zoom", tex)
            self.assertLess(tex.index("Small-G settings remain anti-conservative"), tex.index("Next experiment tests whether batch selection"))
            self.assertLess(tex.index("Next experiment tests whether batch selection"), tex.index("Same-case panels keep the segmentation error interpretable"))
            self.assertIn("Research direction", tex)
            self.assertIn("Segmentation robustness", tex)
            self.assertIn("independent visual failure analysis", tex)
            self.assertNotIn("Workstream transition", tex)
            self.assertNotIn("independent workstream", tex)
            self.assertNotIn("no causal bridge asserted", tex)
            for forbidden in ["RRL-", "SRC-", "GSC-", "Reference retrieval", "EVIDENCE_MANIFEST", "Diagram contract", "run ID", "fixture", "workflow", "production regression", "source bundle"]:
                self.assertNotIn(forbidden, tex)

            source = generator.read_text(encoding="utf-8")
            self.assertNotIn("WORKSTREAM_PROFILES", source)
            self.assertNotIn("clustered_interval_calibration", source)
            self.assertNotIn("segmentation_robustness", source)
            self.assertNotIn("generate_cuhk_scientific_layout_stage3.generate(", source)
            self.assertNotIn("stage3.page_specs(", source)
            self.assertNotIn("Clustered Interval Calibration And Synthetic Segmentation Robustness", source)
            self.assertNotIn("force_gold_id=", source)

            plugin_generator = REPO_ROOT / "plugins/codex/plugins/presentations/shared/scripts/generate_research_presentation_production_entry.py"
            plugin_validator = REPO_ROOT / "plugins/codex/plugins/presentations/shared/scripts/validate_research_presentation_production_entry.py"
            self.assertEqual(generator.read_text(encoding="utf-8"), plugin_generator.read_text(encoding="utf-8"))
            self.assertEqual(validator.read_text(encoding="utf-8"), plugin_validator.read_text(encoding="utf-8"))
            plugin_quality_loop = REPO_ROOT / "plugins/codex/plugins/presentations/shared/scripts/deck_quality_loop.py"
            self.assertEqual((SHARED / "scripts/deck_quality_loop.py").read_text(encoding="utf-8"), plugin_quality_loop.read_text(encoding="utf-8"))

            blocked_bundle = json.loads(bundle.read_text(encoding="utf-8"))
            blocked_bundle["metadata"]["subtitle"] = "Production regression from source bundle"
            blocked_path = Path(tmp) / "blocked_bundle.json"
            blocked_path.write_text(json.dumps(blocked_bundle, indent=2) + "\n", encoding="utf-8")
            blocked = subprocess.run(
                [
                    sys.executable,
                    str(generator),
                    "--input-bundle",
                    str(blocked_path),
                    "--out-dir",
                    str(Path(tmp) / "blocked"),
                    "--implementation-commit",
                    implementation_commit,
                ],
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertNotEqual(blocked.returncode, 0)
            self.assertIn("metadata.subtitle leaks audience-facing internal term", blocked.stderr)

            strict = subprocess.run(
                [sys.executable, str(validator), "--out-dir", str(generated)],
                check=False,
                capture_output=True,
                text=True,
            )
            if manifest["render_status"]["status"] == "ok":
                self.assertEqual(strict.returncode, 0, strict.stderr + strict.stdout)
                self.assertEqual(manifest["mechanical_qa"]["status"], "MECHANICAL_PASS")
            else:
                self.assertNotEqual(strict.returncode, 0)
                self.assertIn(manifest["render_status"]["status"], strict.stderr + strict.stdout)

    def test_statistical_model_support_copy_is_source_driven_for_unrelated_model(self) -> None:
        spec = {
            "page_id": "synthetic_cox_model",
            "page_job": "STATISTICAL_MODEL",
            "section": "Model",
            "title": "Time-to-event model separates baseline risk from covariate effects",
            "query": {
                "page_function": "STATISTICAL_MODEL",
                "scientific_object": "survival analysis cox proportional hazards equation",
                "domain_family": "survival_analysis",
                "dominant_object_type": "equation",
                "evidence_type": "mathematical model",
                "density": "low",
                "panel_count": 0,
            },
            "content_kind": "equation",
            "dominant_object": "native_latex_math",
            "math": r"h(t\mid x)=h_0(t)\exp(x^\top\beta)",
            "annotation": "Hazard ratios are multiplicative shifts from the baseline hazard.",
            "key_message": "Partial likelihood estimates covariate effects without specifying the baseline hazard.",
            "scientific_objects": [
                "baseline hazard",
                "covariate log hazard ratio",
                "risk set partial likelihood",
            ],
            "required_panel_count": 0,
        }
        layout = stage3.resolve_layout(spec)
        tex = stage3.emit_equation(spec, layout)

        self.assertIn(r"\displaystyle h(t\mid x)=h_0(t)\exp(x^\top\beta)", tex)
        self.assertIn("Model components", tex)
        self.assertIn("baseline hazard", tex)
        self.assertIn("covariate log hazard ratio", tex)
        self.assertIn("Partial likelihood estimates covariate effects", tex)
        for forbidden in [
            "ICC",
            "center variation",
            "interval comparison",
            "Calibration link",
            "Source-grounded terms",
        ]:
            self.assertNotIn(forbidden, tex)
        self.assertIn(
            "scientific_objects",
            next(item for item in layout["native_objects"] if item["role"] == "source_field_model_components")["source_fields"],
        )
        self.assertIn(
            "key_message",
            next(item for item in layout["native_objects"] if item["role"] == "source_field_model_interpretation")["source_fields"],
        )

        minimal_spec = dict(spec)
        minimal_spec.pop("scientific_objects")
        minimal_spec.pop("key_message")
        minimal_tex = stage3.emit_equation(minimal_spec, stage3.resolve_layout(minimal_spec))
        self.assertIn("Hazard ratios are multiplicative shifts", minimal_tex)
        self.assertNotIn("Model components", minimal_tex)
        self.assertNotIn("Interpretation", minimal_tex)
        self.assertNotIn("Source-grounded terms", minimal_tex)

        source = (SHARED / "scripts/generate_cuhk_scientific_layout_stage3.py").read_text(encoding="utf-8")
        self.assertNotIn("baseline hazard", source)
        self.assertNotIn("covariate log hazard ratio", source)

    def test_research_presentation_deck_quality_loop_consumes_review_and_fails_closed(self) -> None:
        generator = SHARED / "scripts/generate_research_presentation_production_entry.py"
        validator = SHARED / "scripts/validate_research_presentation_production_entry.py"
        bundle = SHARED / "fixtures/stage4_engineering_research_bundle/bundle.json"
        fixtures = SHARED / "fixtures/deck_quality_loop"
        with tempfile.TemporaryDirectory() as tmp:
            repaired = Path(tmp) / "repaired"
            result = subprocess.run(
                [
                    sys.executable,
                    str(generator),
                    "--input-bundle",
                    str(bundle),
                    "--out-dir",
                    str(repaired),
                    "--implementation-commit",
                    "c" * 40,
                    "--review-evidence",
                    str(fixtures / "transition_blocker_review.json"),
                    "--rereview-evidence",
                    str(fixtures / "pass_review.json"),
                ],
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertIn(result.returncode, {0, 2}, result.stderr + result.stdout)
            validation = subprocess.run(
                [sys.executable, str(validator), "--out-dir", str(repaired), "--allow-missing-render"],
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertEqual(validation.returncode, 0, validation.stderr + validation.stdout)
            state = json.loads((repaired / "quality_loop_state.json").read_text(encoding="utf-8"))
            self.assertEqual(state["repair_cycle_count"], 1)
            self.assertEqual(state["final_decision"], "READY_TO_DELIVER")
            self.assertEqual(len(state["selected_repair_directives"]), 1)
            self.assertEqual(state["selected_repair_directives"][0]["intent"], "ADJUST_TRANSITION_CUE")
            self.assertNotEqual(state["initial_render_identity"], state["repaired_render_identity"])
            self.assertEqual(state["initial_render_identity"], state["initial_render_input_identity"])
            self.assertEqual(state["repaired_render_identity"], state["repaired_render_input_identity"])
            self.assertNotEqual(state["initial_render_input_identity"], state["repaired_render_input_identity"])
            initial_main = next(item for item in state["initial_render_input_manifest"]["files"] if item["role"] == "main_tex")
            repaired_main = next(item for item in state["repaired_render_input_manifest"]["files"] if item["role"] == "main_tex")
            self.assertNotEqual(initial_main["sha256"], repaired_main["sha256"])
            deck_plan = json.loads((repaired / "deck_plan.json").read_text(encoding="utf-8"))
            transition_slide = next(slide for slide in deck_plan["slides"] if slide["page_function"] == "MEDICAL_IMAGE_COMPARISON")
            self.assertEqual(transition_slide["storyline_transition"]["cue_variant"], "compact")
            tex = (repaired / "cuhk_production_build/main.tex").read_text(encoding="utf-8")
            self.assertIn(r"\StageThreePanel{0.0600}{0.1450}{0.9400}{0.2020}", tex)
            self.assertIn("Research direction", tex)
            self.assertIn("Segmentation robustness", tex)
            self.assertNotIn("Workstream transition", tex)
            self.assertNotIn("independent workstream", tex)
            self.assertNotIn("no causal bridge asserted", tex)
            self.assertNotIn("deck-transition-too-heavy", tex)

            sequence = json.loads((repaired / "deck_sequence_summary.json").read_text(encoding="utf-8"))
            unsafe_review, unsafe_sha = deck_quality_loop.load_review_evidence(fixtures / "unknown_blocker_review.json")
            unsafe = deck_quality_loop.consume_review_evidence(
                review_evidence=unsafe_review,
                review_evidence_sha256=unsafe_sha,
                sequence_summary=sequence,
                initial_render_identity=sequence["render_input_identity_sha256"],
                initial_rendered_pixel_identity=sequence["rendered_pixel_identity_sha256"],
                initial_render_input_manifest=sequence["render_input_manifest"],
            )
            self.assertEqual(unsafe["final_decision"], "QUALITY_LOOP_FAIL_NO_WINNER")
            self.assertIn("unsupported repair intent", unsafe["fail_closed_reason"])

    def test_research_presentation_quality_loop_normalizes_terra_style_findings(self) -> None:
        bundle_path = SHARED / "fixtures/stage4_quality_loop_repair_stress_bundle/bundle.json"
        bundle = production_entry.load_bundle(bundle_path)
        plugin_bundle_path = REPO_ROOT / "plugins/codex/plugins/presentations/shared/fixtures/stage4_quality_loop_repair_stress_bundle/bundle.json"
        self.assertEqual(bundle_path.read_text(encoding="utf-8"), plugin_bundle_path.read_text(encoding="utf-8"))
        metadata_audience = " ".join(
            str(bundle["metadata"][field])
            for field in ["title", "subtitle"]
        ).lower()
        for forbidden in ["stage", "quality loop", "qa", "workflow", "fixture", "production regression", "source bundle"]:
            self.assertNotIn(forbidden, metadata_audience)

        deck_jobs, storyline_trace = production_entry.build_storyline(bundle)
        specs = production_entry.build_specs(deck_jobs)
        layouts = [stage3.resolve_layout(spec) for spec in specs]
        rendered = [
            {},
            *[
                {"path": f"synthetic/slide-{idx + 1}.png", "sha256": f"{idx:064x}"}
                for idx in range(1, len(specs) + 1)
            ],
        ]
        sequence = deck_quality_loop.build_sequence_summary(
            specs=specs,
            layouts=layouts,
            render_status={"status": "ok", "rendered_png": rendered, "png_count": len(rendered)},
            storyline_trace=storyline_trace,
            render_input_identity={"sha256": "initial-render-input", "files": []},
            contact_sheet_path="synthetic/contact_sheet.png",
            contact_sheet_sha256="f" * 64,
        )
        review = {
            "schema": "AI_BRIDGE_VISUAL_REVIEW_V1",
            "overall_decision": "REVISE",
            "item_reviews": [{"item_id": "deck_contact_sheet", "scope": "deck", "decision": "REVISE"}],
            "blocking_findings": [
                {
                    "finding_id": "synthetic-audience-copy",
                    "target_logical_id": "slide_3_real_data_application",
                    "requirement_id": "AUDIENCE_FACING_NO_WORKFLOW_PROVENANCE",
                    "summary": "Audience body leaks internal workflow/source bundle copy.",
                    "recommendation": "Remove production meta language using same-page source-grounded copy.",
                },
                {
                    "finding_id": "synthetic-caption-collision",
                    "target_logical_id": "slide_5_negative_result",
                    "requirement_id": "FIGURE_CAPTION_SUPPORTING_COPY_COLLISION",
                    "evidence": "The figure caption and supporting copy overlap near the bottom support band.",
                    "recommendation": "Reserve a separate caption/support region.",
                },
                {
                    "finding_id": "synthetic-small-primary",
                    "target_logical_id": "slide_3_real_data_application",
                    "requirement_id": "READABLE_SCIENTIFIC_OBJECTS",
                    "evidence": "The primary plot is undersized for projection readability.",
                    "recommendation": "Scale the primary scientific object while preserving caption space.",
                },
                {
                    "finding_id": "synthetic-process-collision",
                    "target_logical_id": "slide_6_next_experiment",
                    "requirement_id": "NEXT_EXPERIMENT_DIAGRAM_READABILITY",
                    "evidence": "The process diagram labels overlap and crowd the decision node.",
                    "recommendation": "Use a compatible source-faithful reflow.",
                },
                {
                    "finding_id": "synthetic-medical-legend",
                    "target_logical_id": "slide_7_medical_image_comparison",
                    "requirement_id": "MEDICAL_LEGEND_CALLOUT_OBSTRUCTION",
                    "evidence": "The overlay legend covers the crop/panel region.",
                    "recommendation": "Reserve a legend area without modifying medical pixels.",
                },
            ],
        }
        state = deck_quality_loop.consume_review_evidence(
            review_evidence=review,
            review_evidence_sha256=deck_quality_loop.stable_sha(review),
            sequence_summary=sequence,
            initial_render_identity=sequence["render_input_identity_sha256"],
            initial_rendered_pixel_identity=sequence["rendered_pixel_identity_sha256"],
            initial_render_input_manifest=sequence["render_input_manifest"],
        )
        self.assertTrue(state["repair_allowed"])
        self.assertEqual(state["deck_level_decision"], "REPAIR_SELECTED")
        self.assertEqual(
            [directive["intent"] for directive in state["selected_repair_directives"]],
            [
                "SANITIZE_AUDIENCE_COPY",
                "REPAIR_ANNOTATION_LEGEND",
                "RESCALE_PRIMARY_OBJECT",
                "SWAP_COMPATIBLE_GOLD_LAYOUT",
                "REPAIR_ANNOTATION_LEGEND",
            ],
        )
        for directive in state["selected_repair_directives"]:
            self.assertIn("normalized_repair_mapping", directive)

        ambiguous = {
            "schema": "AI_BRIDGE_VISUAL_REVIEW_V1",
            "overall_decision": "REVISE",
            "item_reviews": [{"item_id": "deck_contact_sheet", "scope": "deck", "decision": "REVISE"}],
            "blocking_findings": [
                {
                    "finding_id": "synthetic-ambiguous",
                    "target_logical_id": "slide_3_real_data_application",
                    "requirement_id": "MATURE_DOCTORAL_GROUP_MEETING_BAR",
                    "summary": "The page needs a better overall visual treatment.",
                }
            ],
        }
        unsafe = deck_quality_loop.consume_review_evidence(
            review_evidence=ambiguous,
            review_evidence_sha256=deck_quality_loop.stable_sha(ambiguous),
            sequence_summary=sequence,
            initial_render_identity=sequence["render_input_identity_sha256"],
            initial_rendered_pixel_identity=sequence["rendered_pixel_identity_sha256"],
            initial_render_input_manifest=sequence["render_input_manifest"],
        )
        self.assertEqual(unsafe["final_decision"], "QUALITY_LOOP_FAIL_NO_WINNER")
        self.assertIn("does not uniquely map", unsafe["fail_closed_reason"])

    def test_research_presentation_quality_loop_repair_directives_affect_render_inputs(self) -> None:
        bundle = production_entry.load_bundle(SHARED / "fixtures/stage4_quality_loop_repair_stress_bundle/bundle.json")
        deck_jobs, _ = production_entry.build_storyline(bundle)
        specs = production_entry.build_specs(deck_jobs)
        real_data = next(spec for spec in specs if spec["page_job"] == "REAL_DATA_APPLICATION")
        negative = next(spec for spec in specs if spec["page_job"] == "NEGATIVE_RESULT")
        next_experiment = next(spec for spec in specs if spec["page_job"] == "NEXT_EXPERIMENT")
        medical = next(spec for spec in specs if spec["page_job"] == "MEDICAL_IMAGE_COMPARISON")

        repaired = deck_quality_loop.apply_repair_directives(
            specs,
            [
                {
                    "directive_id": "repair-audience",
                    "intent": "SANITIZE_AUDIENCE_COPY",
                    "target_logical_ids": ["slide_3_real_data_application"],
                },
                {
                    "directive_id": "repair-scale",
                    "intent": "RESCALE_PRIMARY_OBJECT",
                    "target_logical_ids": ["slide_3_real_data_application"],
                },
                {
                    "directive_id": "repair-figure-support",
                    "intent": "REPAIR_ANNOTATION_LEGEND",
                    "target_logical_ids": ["slide_5_negative_result"],
                },
                {
                    "directive_id": "repair-diagram",
                    "intent": "SWAP_COMPATIBLE_GOLD_LAYOUT",
                    "target_logical_ids": ["slide_6_next_experiment"],
                },
                {
                    "directive_id": "repair-medical-legend",
                    "intent": "REPAIR_ANNOTATION_LEGEND",
                    "target_logical_ids": ["slide_7_medical_image_comparison"],
                },
            ],
        )
        repaired_real_data = next(spec for spec in repaired if spec["page_job"] == "REAL_DATA_APPLICATION")
        self.assertEqual(repaired_real_data["annotation"], real_data["key_message"])
        self.assertTrue(repaired_real_data["audience_copy_repair_trace"])
        self.assertNotIn("workflow", repaired_real_data["annotation"].lower())

        initial_real_layout = stage3.resolve_layout(real_data)
        repaired_real_layout = stage3.resolve_layout(repaired_real_data)
        self.assertNotEqual(initial_real_layout["resolved_primary_object_geometry"], repaired_real_layout["resolved_primary_object_geometry"])
        self.assertIn("primary_object_scale_hint", repaired_real_layout["source_recipe_fields_consumed"])

        initial_negative_layout = stage3.resolve_layout(negative)
        repaired_negative = next(spec for spec in repaired if spec["page_job"] == "NEGATIVE_RESULT")
        repaired_negative_layout = stage3.resolve_layout(repaired_negative)
        self.assertNotEqual(
            initial_negative_layout["resolved_supporting_object_geometry"],
            repaired_negative_layout["resolved_supporting_object_geometry"],
        )
        self.assertIn("legend_repair_hint", repaired_negative_layout["source_recipe_fields_consumed"])

        initial_next_layout = stage3.resolve_layout(next_experiment)
        repaired_next = next(spec for spec in repaired if spec["page_job"] == "NEXT_EXPERIMENT")
        repaired_next_layout = stage3.resolve_layout(repaired_next)
        self.assertNotEqual(initial_next_layout["resolved_primary_object_geometry"], repaired_next_layout["resolved_primary_object_geometry"])
        self.assertIn("compatible_layout_reflow_hint", repaired_next_layout["source_recipe_fields_consumed"])

        repaired_medical = next(spec for spec in repaired if spec["page_job"] == "MEDICAL_IMAGE_COMPARISON")
        with tempfile.TemporaryDirectory() as tmp:
            build_dir = Path(tmp)
            initial_medical = copy.deepcopy(medical)
            initial_asset_map = stage3.copy_assets([initial_medical], build_dir / "initial")
            repaired_asset_map = stage3.copy_assets([repaired_medical], build_dir / "repaired")
            initial_tex = stage3.emit_image_panel(initial_medical, stage3.resolve_layout(initial_medical), initial_asset_map)
            repaired_tex = stage3.emit_image_panel(repaired_medical, stage3.resolve_layout(repaired_medical), repaired_asset_map)
        self.assertNotEqual(initial_tex, repaired_tex)
        self.assertIn("legend_repair_hint", stage3.resolve_layout(repaired_medical)["source_recipe_fields_consumed"])

    def test_research_presentation_storyline_grouping_is_source_derived(self) -> None:
        bundle = json.loads((SHARED / "fixtures/stage4_engineering_research_bundle/bundle.json").read_text(encoding="utf-8"))
        mutated = copy.deepcopy(bundle)
        for index, job in enumerate(mutated["page_jobs"], start=1):
            job["title"] = f"Retitled page {index}"
            job["section"] = f"Retitled section {index}"
        ordered_jobs, storyline = production_entry.build_storyline(mutated)
        self.assertEqual(
            [job["page_job"] for job in ordered_jobs],
            [
                "STATISTICAL_MODEL",
                "REAL_DATA_APPLICATION",
                "EXPERIMENT_DESIGN",
                "NEGATIVE_RESULT",
                "NEXT_EXPERIMENT",
                "MEDICAL_IMAGE_COMPARISON",
            ],
        )
        for assignment in storyline["page_assignments"]:
            self.assertTrue(assignment["assignment_basis"])
            self.assertNotIn("Retitled", " ".join(assignment["assignment_basis"]))
        self.assertIn("domain token profiles", storyline["source_derivation"])

    def test_research_presentation_storyline_grouping_uses_generic_workstream_metadata(self) -> None:
        generic = {
            "evidence": [
                {"id": "EV-A1", "board": "analysis_block"},
                {"id": "EV-A2", "board": "decision_block"},
                {"id": "EV-B1", "board": "audit_block"},
            ],
            "page_jobs": [
                {
                    "page_id": "alpha_model",
                    "page_job": "STATISTICAL_MODEL",
                    "source_evidence_ids": ["EV-A1"],
                    "workstream": {"id": "alpha_path", "label": "Alpha pathway", "scope": "model, failure, and next decision"},
                },
                {
                    "page_id": "beta_result",
                    "page_job": "REAL_DATA_APPLICATION",
                    "source_evidence_ids": ["EV-B1"],
                    "workstream": {"id": "beta_audit", "label": "Beta audit", "scope": "measurement audit and next decision"},
                },
                {
                    "page_id": "alpha_failure",
                    "page_job": "NEGATIVE_RESULT",
                    "source_evidence_ids": ["EV-A2"],
                    "workstream": {"id": "alpha_path", "label": "Alpha pathway", "scope": "model, failure, and next decision"},
                },
                {
                    "page_id": "beta_next",
                    "page_job": "NEXT_EXPERIMENT",
                    "source_evidence_ids": ["EV-B1"],
                    "workstream": {"id": "beta_audit", "label": "Beta audit", "scope": "measurement audit and next decision"},
                },
                {
                    "page_id": "alpha_next",
                    "page_job": "NEXT_EXPERIMENT",
                    "source_evidence_ids": ["EV-A2"],
                    "workstream": {"id": "alpha_path", "label": "Alpha pathway", "scope": "model, failure, and next decision"},
                },
            ],
        }
        self.assertNotRegex(json.dumps(generic, ensure_ascii=False).lower(), r"cluster|coverage|segmentation|medical|lesion|roi")

        ordered_jobs, storyline = production_entry.build_storyline(generic)
        self.assertEqual(
            [job["page_id"] for job in ordered_jobs],
            ["alpha_model", "alpha_failure", "alpha_next", "beta_result", "beta_next"],
        )
        self.assertEqual([item["workstream_id"] for item in storyline["workstreams"]], ["alpha_path", "beta_audit"])
        beta_result = next(job for job in ordered_jobs if job["page_id"] == "beta_result")
        self.assertEqual(beta_result["storyline_transition"]["label"], "Beta audit")
        self.assertEqual(beta_result["storyline_transition"]["audience_text"], "measurement audit and next decision")
        transition_payload = json.dumps(beta_result["storyline_transition"], ensure_ascii=False).lower()
        for forbidden in ["workstream transition", "independent workstream", "no causal bridge asserted", "segmentation robustness"]:
            self.assertNotIn(forbidden, transition_payload)
        for causal_connector in ["therefore", "because", "causes", "applies to", "derived from"]:
            self.assertNotIn(causal_connector, transition_payload)
        for assignment in storyline["page_assignments"]:
            self.assertEqual(assignment["assignment_basis"], ["explicit source workstream metadata"])

    def test_research_presentation_single_workstream_has_no_forced_transition(self) -> None:
        bundle = json.loads((SHARED / "fixtures/stage4_engineering_research_bundle/bundle.json").read_text(encoding="utf-8"))
        bundle["page_jobs"] = [job for job in bundle["page_jobs"] if job["page_job"] != "MEDICAL_IMAGE_COMPARISON"]
        ordered_jobs, storyline = production_entry.build_storyline(bundle)
        self.assertEqual(len(storyline["workstreams"]), 1)
        self.assertFalse(any("storyline_transition" in job for job in ordered_jobs))
        self.assertEqual(
            [job["page_job"] for job in ordered_jobs],
            [
                "STATISTICAL_MODEL",
                "REAL_DATA_APPLICATION",
                "EXPERIMENT_DESIGN",
                "NEGATIVE_RESULT",
                "NEXT_EXPERIMENT",
            ],
        )

    def test_reference_calibrated_candidate_search(self) -> None:
        references = SHARED / "references"
        for name in [
            "research_slide_candidate_request.schema.json",
            "research_slide_candidate_manifest.schema.json",
        ]:
            self.assertTrue((references / name).exists(), name)

        generator = SHARED / "scripts/generate_reference_calibrated_candidates.py"
        validator = SHARED / "scripts/validate_reference_candidate_manifests.py"
        generator_text = generator.read_text(encoding="utf-8")
        self.assertIn("select_reference_compositions.select", generator_text)
        self.assertNotRegex(generator_text, r"RRL-\d{3}")
        import generate_reference_calibrated_candidates as candidate_generator

        output_root = REPO_ROOT / "docs/audits/research_presentation_candidate_search/generated"
        manifests = [
            output_root / "statistical_estimator_cluster_robust_variance/candidate_manifest.json",
            output_root / "medical_image_lesion_overlay_comparison/candidate_manifest.json",
        ]
        for manifest in manifests:
            self.assertTrue(manifest.exists(), manifest)
        validation = subprocess.run([sys.executable, str(validator), *[str(path) for path in manifests]], check=False, capture_output=True, text=True)
        self.assertEqual(validation.returncode, 0, validation.stderr)
        self.assertIn("validated 2 candidate manifest(s)", validation.stdout)

        for manifest_path in manifests:
            payload = json.loads(manifest_path.read_text(encoding="utf-8"))
            self.assertEqual(payload["schema"], "RESEARCH_SLIDE_CANDIDATE_MANIFEST_V1")
            self.assertEqual(payload["request"]["candidate_count"], 3)
            candidates = payload["candidates"]
            self.assertEqual(len(candidates), 3)
            self.assertEqual(
                {candidate["strategy"] for candidate in candidates},
                {"reference_faithful", "alternative_composition", "controlled_wildcard"},
            )
            self.assertEqual(len({candidate["preview_sha256"] for candidate in candidates}), 3)
            self.assertGreaterEqual(len({candidate["layout_family"] for candidate in candidates}), 2)
            self.assertTrue(payload["retrieved_composition_records"])
            for candidate in candidates:
                self.assertFalse(candidate["source_reference_pixels_used"])
                self.assertTrue(candidate["geometry_transfer"])
                self.assertTrue(candidate["content_bindings"])
                preview = REPO_ROOT / candidate["preview_artifact"]["path"]
                self.assertTrue(preview.exists(), preview)
                self.assertGreater(preview.stat().st_size, 10_000)
                audience = "\n".join(candidate["audience_text"])
                for forbidden in ["reference_faithful", "alternative_composition", "controlled_wildcard", "RRL-", "Reference retrieval", "EVIDENCE_MANIFEST"]:
                    self.assertNotIn(forbidden, audience)
            if payload["request"]["page_function"] == "ESTIMATOR":
                self.assertTrue(any(region["content_mode"] == "equation" for candidate in candidates for region in candidate["regions"]))
                for candidate in candidates:
                    for reference_id in candidate["source_reference_ids"]:
                        source = candidate_generator.by_reference_id()[reference_id]
                        self.assertEqual(source["page_function"], "ESTIMATOR")
                        self.assertIn("equation", {region["content_mode"] for region in source["regions"]})
            if payload["request"]["page_function"] == "MEDICAL_IMAGE_COMPARISON":
                self.assertTrue(any(region["content_mode"] == "medical_image" for candidate in candidates for region in candidate["regions"]))
                for candidate in candidates:
                    for reference_id in candidate["source_reference_ids"]:
                        source = candidate_generator.by_reference_id()[reference_id]
                        self.assertEqual(source["page_function"], "MEDICAL_IMAGE_COMPARISON")
                        self.assertIn("medical_image", {region["content_mode"] for region in source["regions"]})
                self.assertNotIn("RRL-034", {reference_id for candidate in candidates for reference_id in candidate["source_reference_ids"]})

        records = candidate_generator.by_reference_id()
        medical_request = json.loads((REPO_ROOT / "docs/audits/research_presentation_candidate_search/requests/medical_image_comparison_request.json").read_text(encoding="utf-8"))
        rrl022_regions, _, _, _ = candidate_generator.candidate_regions(medical_request, "reference_faithful", records["RRL-022"])
        rrl013_regions, _, _, _ = candidate_generator.candidate_regions(medical_request, "reference_faithful", records["RRL-013"])
        rrl022_bboxes = [region["bbox"] for region in rrl022_regions if region["role"] == "primary_scientific_object"]
        rrl013_bboxes = [region["bbox"] for region in rrl013_regions if region["role"] == "primary_scientific_object"]
        self.assertNotEqual(rrl022_bboxes, rrl013_bboxes)

    def test_candidate_visual_finish_repair_manifests(self) -> None:
        validator = SHARED / "scripts/validate_reference_candidate_manifests.py"
        output_root = REPO_ROOT / "docs/audits/research_presentation_candidate_visual_finish_repair/generated"
        manifests = [
            output_root / "statistical_estimator_cluster_robust_variance/candidate_manifest.json",
            output_root / "medical_image_lesion_overlay_comparison/candidate_manifest.json",
        ]
        for manifest in manifests:
            self.assertTrue(manifest.exists(), manifest)
        validation = subprocess.run([sys.executable, str(validator), *[str(path) for path in manifests]], check=False, capture_output=True, text=True)
        self.assertEqual(validation.returncode, 0, validation.stderr)
        for manifest_path in manifests:
            payload = json.loads(manifest_path.read_text(encoding="utf-8"))
            visual_tokens = [candidate["visual_finish"]["visual_tokens"] for candidate in payload["candidates"]]
            self.assertEqual({tokens["token_set_id"] for tokens in visual_tokens}, {"research-presentation-visual-finish-v1"})
            self.assertEqual(len({json.dumps(tokens, sort_keys=True) for tokens in visual_tokens}), 1)
            for candidate in payload["candidates"]:
                finish = candidate["visual_finish"]
                self.assertFalse(finish["primary_object_treatment"]["decorative_card_used"])
                self.assertEqual(finish["primary_object_treatment"]["container_role"], "none")
                self.assertNotIn("RRL-", "\n".join(candidate["audience_text"]))
                old_root = "docs/audits/research_presentation_candidate_search/generated"
                self.assertNotIn(old_root, candidate["preview_artifact"]["path"])
            if payload["request"]["page_function"] == "ESTIMATOR":
                for candidate in payload["candidates"]:
                    self.assertEqual(candidate["visual_finish"]["equation_rendering"]["contrast"], "high")
                    self.assertTrue(candidate["visual_finish"]["annotation_targets"])
            if payload["request"]["page_function"] == "MEDICAL_IMAGE_COMPARISON":
                for candidate in payload["candidates"]:
                    self.assertTrue(candidate["visual_finish"]["panel_correspondence"]["panel_region_ids"])
                    self.assertTrue(candidate["visual_finish"]["legend_binding"]["legend_region_id"])

    def test_comparative_reference_calibrated_visual_review_inputs(self) -> None:
        scripts = SHARED / "scripts"
        for name in [
            "prepare_comparative_visual_review.py",
            "validate_comparative_visual_review.py",
        ]:
            self.assertTrue((scripts / name).exists(), name)
        root = REPO_ROOT / "results/021_research_presentation_comparative_reference_calibrated_visual_review/visual_review"
        for case in ["statistical", "medical"]:
            manifest_path = root / case / "visual_inputs.json"
            map_path = root / case / "review_identity_map.json"
            identity_path = root / case / "review_identity.json"
            self.assertTrue(manifest_path.exists(), manifest_path)
            self.assertTrue(map_path.exists(), map_path)
            self.assertTrue(identity_path.exists(), identity_path)
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            identity_map = json.loads(map_path.read_text(encoding="utf-8"))
            self.assertEqual(manifest["schema"], "AI_BRIDGE_VISUAL_INPUT_MANIFEST_V1")
            self.assertEqual(manifest["task_key"], "021_visual_comparison")
            self.assertEqual(manifest["workflow_type"], "generic")
            self.assertEqual(len(manifest["inputs"]), 5)
            self.assertEqual(len([item for item in identity_map["items"] if item["item_class"] == "candidate"]), 3)
            self.assertGreaterEqual(len([item for item in identity_map["items"] if item["item_class"] == "reference"]), 2)
            visible_text = json.dumps(manifest, sort_keys=True)
            for forbidden in ["RRL-", "SRC-", "candidate", "reference", "generated", "gold", "baseline", "reference_faithful", "alternative_composition", "controlled_wildcard"]:
                self.assertNotIn(forbidden, visible_text)
            self.assertEqual([item["logical_id"] for item in manifest["inputs"]], ["item_A", "item_B", "item_C", "item_D", "item_E"])
        validator = scripts / "validate_comparative_visual_review.py"
        validation = subprocess.run([sys.executable, str(validator)], check=False, capture_output=True, text=True)
        self.assertEqual(validation.returncode, 0, validation.stderr)
        self.assertIn("validated 2 comparative visual-review case(s)", validation.stdout)

    def test_candidate_visual_finish_comparative_inputs(self) -> None:
        root = REPO_ROOT / "results/022_research_presentation_candidate_visual_finish_repair/visual_review"
        for case in ["statistical", "medical"]:
            manifest_path = root / case / "visual_inputs.json"
            map_path = root / case / "review_identity_map.json"
            self.assertTrue(manifest_path.exists(), manifest_path)
            self.assertTrue(map_path.exists(), map_path)
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            identity_map = json.loads(map_path.read_text(encoding="utf-8"))
            self.assertEqual(manifest["task_key"], "022_visual_finish_comparison")
            self.assertEqual(manifest["workflow_type"], "generic")
            self.assertEqual(len(manifest["inputs"]), 5)
            self.assertEqual(len([item for item in identity_map["items"] if item["item_class"] == "candidate"]), 3)
            self.assertEqual(len([item for item in identity_map["items"] if item["item_class"] == "reference"]), 2)
            visible_text = json.dumps(manifest, sort_keys=True)
            for forbidden in ["RRL-", "SRC-", "candidate", "reference", "generated", "gold", "baseline", "reference_faithful", "alternative_composition", "controlled_wildcard"]:
                self.assertNotIn(forbidden, visible_text)
            for item in identity_map["items"]:
                if item["item_class"] == "candidate":
                    self.assertIn("research_presentation_candidate_visual_finish_repair", item["source_path"])
        validator = SHARED / "scripts/validate_comparative_visual_review.py"
        validation = subprocess.run([
            sys.executable,
            str(validator),
            "--task-key",
            "022_research_presentation_candidate_visual_finish_repair",
            "--visible-task-key",
            "022_visual_finish_comparison",
            "--cache-key",
            "022",
        ], check=False, capture_output=True, text=True)
        self.assertEqual(validation.returncode, 0, validation.stderr)
        self.assertIn("validated 2 comparative visual-review case(s)", validation.stdout)

    def test_deck_design_system_integration_artifacts(self) -> None:
        schema = SHARED / "references/research_deck_design_profile.schema.json"
        generator = SHARED / "scripts/generate_deck_design_system_integration.py"
        validator = SHARED / "scripts/validate_deck_design_system_integration.py"
        for path in [schema, generator, validator]:
            self.assertTrue(path.exists(), path)
        mirrors = [
            (
                schema,
                REPO_ROOT / "plugins/codex/plugins/presentations/shared/references/research_deck_design_profile.schema.json",
            ),
            (
                generator,
                REPO_ROOT / "plugins/codex/plugins/presentations/shared/scripts/generate_deck_design_system_integration.py",
            ),
            (
                validator,
                REPO_ROOT / "plugins/codex/plugins/presentations/shared/scripts/validate_deck_design_system_integration.py",
            ),
        ]
        for source, mirror in mirrors:
            self.assertEqual(source.read_text(encoding="utf-8"), mirror.read_text(encoding="utf-8"))

        validation = subprocess.run([sys.executable, str(validator)], check=False, capture_output=True, text=True)
        self.assertEqual(validation.returncode, 0, validation.stderr)
        self.assertIn("validated 2 deck-design-system integration mini-deck(s)", validation.stdout)

        root = REPO_ROOT / "results/023_research_presentation_deck_design_system_integration/generated"
        outputs = json.loads((root / "OUTPUTS.json").read_text(encoding="utf-8"))
        profile = json.loads((root / "deck_design_profile.json").read_text(encoding="utf-8"))
        self.assertEqual(profile["schema"], "RESEARCH_DECK_DESIGN_PROFILE_V1")
        self.assertIn("fonts", profile["locked_properties"])
        self.assertIn("equation", profile["locked_properties"])
        self.assertIn("image_panel", profile["locked_properties"])
        self.assertIn("scientific_object_bbox", profile["page_local_properties"])
        self.assertIn("layout_family", profile["page_local_properties"])
        locked_sha = profile["locked_properties_sha256"]
        self.assertEqual(len(outputs["decks"]), 2)
        review_pack = REPO_ROOT / outputs["review_pack_pdf"]["path"]
        self.assertTrue(review_pack.exists(), review_pack)
        self.assertGreater(review_pack.stat().st_size, 100_000)
        self.assertEqual(len(outputs["review_pack_pdf"]["source_pdfs"]), 2)
        mutation = json.loads((REPO_ROOT / outputs["profile_mutation_regression"]["path"]).read_text(encoding="utf-8"))
        self.assertEqual(mutation["schema"], "RESEARCH_DECK_DESIGN_PROFILE_MUTATION_REGRESSION_V1")
        self.assertEqual(mutation["status"], "PASS")
        self.assertTrue(mutation["checks"]["profile_sha_changed"])
        self.assertTrue(mutation["checks"]["native_pptx_xml_changed"])
        self.assertTrue(mutation["checks"]["page_local_geometry_stable"])
        self.assertNotEqual(mutation["baseline_pptx_xml_sha256"], mutation["mutated_pptx_xml_sha256"])
        self.assertEqual(mutation["baseline_geometry_signature"], mutation["mutated_geometry_signature"])
        for deck in outputs["decks"]:
            manifest = json.loads((REPO_ROOT / deck["manifest"]).read_text(encoding="utf-8"))
            self.assertEqual(manifest["schema"], "RESEARCH_DECK_DESIGN_SYSTEM_INTEGRATION_MANIFEST_V1")
            self.assertEqual(manifest["task_key"], "023_research_presentation_deck_design_system_integration")
            self.assertEqual(manifest["editable_slide_count"], 4)
            self.assertEqual(manifest["render_status"]["status"], "ok")
            self.assertEqual(manifest["render_status"]["png_count"], 4)
            self.assertEqual(manifest["mechanical_qa"]["status"], "MECHANICAL_PASS")
            self.assertGreaterEqual(len(manifest["major_composition_families"]), 3)
            self.assertEqual({slide["locked_properties_sha256"] for slide in manifest["slides"]}, {locked_sha})
            self.assertGreaterEqual(len({tuple(slide["primary_object_roles"]) for slide in manifest["slides"]}), 2)
            with ZipFile(REPO_ROOT / manifest["pptx"]) as deck_zip:
                names = set(deck_zip.namelist())
            self.assertIn("[Content_Types].xml", names)
            self.assertEqual(
                len([name for name in names if name.startswith("ppt/slides/slide") and name.endswith(".xml")]),
                4,
            )
            for slide in manifest["slides"]:
                self.assertTrue(slide["source_reference_ids"])
                self.assertTrue(slide["geometry_transfer"])
                self.assertTrue(slide["primary_bboxes"])
                self.assertTrue(slide["page_local_geometry_preserved"])
                audience = "\n".join(slide["audience_text"])
                for forbidden in ["RRL-", "SRC-", "candidate", "Reference retrieval", "EVIDENCE_MANIFEST", "Diagram contract", "QA"]:
                    self.assertNotIn(forbidden, audience)

    def test_research_presentation_todo_consolidation_and_promotions(self) -> None:
        todo = (REPO_ROOT / "skills/tools/documents-media/presentations/research-presentations/TODO.md").read_text(encoding="utf-8")
        research_skill = (REPO_ROOT / "skills/tools/documents-media/presentations/research-presentations/SKILL.md").read_text(encoding="utf-8")
        visual_qa = (SHARED / "visual-qa.md").read_text(encoding="utf-8")
        archetypes = (SHARED / "references/RESEARCH_SLIDE_ARCHETYPES.md").read_text(encoding="utf-8")

        self.assertNotRegex(todo, r"- \[ \]")
        categories = set(re.findall(r"- \[(ALREADY_IMPLEMENTED|PROMOTE_NOW|KEEP_BACKLOG|DUPLICATE_OR_SUPERSEDED)\]", todo))
        self.assertEqual(categories, {"ALREADY_IMPLEMENTED", "PROMOTE_NOW", "KEEP_BACKLOG", "DUPLICATE_OR_SUPERSEDED"})
        checklist_count = len(re.findall(r"^- \[(?:ALREADY_IMPLEMENTED|PROMOTE_NOW|KEEP_BACKLOG|DUPLICATE_OR_SUPERSEDED)\]", todo, flags=re.MULTILINE))
        basis_count = todo.count("Classification basis:")
        self.assertGreaterEqual(checklist_count, 100)
        self.assertEqual(checklist_count, basis_count)

        for required in [
            "## Classification Legend",
            "`[PROMOTE_NOW]`",
            "`[KEEP_BACKLOG]`",
            "`[DUPLICATE_OR_SUPERSEDED]`",
            "Phase B",
            "statistical/biostatistical benchmark",
            "medical-imaging benchmark",
        ]:
            self.assertIn(required, todo)

        for required in [
            "## Revision Scope",
            "accepted_element_ledger",
            "## Evidence And Concept Grounding",
            "fabricated proxy",
            "## Diagram Gate",
            "connectors must be structural connectors",
        ]:
            self.assertIn(required, research_skill)

        for required in [
            "## Evidence Versus Concept QA",
            "## Diagram Semantic QA",
            "## Revision Scope QA",
            "typed arrow characters",
            "scope creep",
        ]:
            self.assertIn(required, visual_qa)

        for required in [
            "metric semantics, favorable direction, graphical encoding",
            "visually central and large enough to inspect",
            "complete comparison path",
            "every connector represents a true relationship",
        ]:
            self.assertIn(required, archetypes)

        mirrors = [
            (
                REPO_ROOT / "skills/tools/documents-media/presentations/research-presentations/SKILL.md",
                REPO_ROOT / "plugins/codex/plugins/presentations/skills/research/SKILL.md",
            ),
            (
                SHARED / "template-routing.md",
                REPO_ROOT / "plugins/codex/plugins/presentations/shared/template-routing.md",
            ),
            (
                SHARED / "ppt-skill-routing.md",
                REPO_ROOT / "plugins/codex/plugins/presentations/shared/ppt-skill-routing.md",
            ),
            (
                SHARED / "scripts/markdown_to_deck_plan.py",
                REPO_ROOT / "plugins/codex/plugins/presentations/shared/scripts/markdown_to_deck_plan.py",
            ),
            (
                SHARED / "visual-qa.md",
                REPO_ROOT / "plugins/codex/plugins/presentations/shared/visual-qa.md",
            ),
            (
                SHARED / "references/RESEARCH_SLIDE_ARCHETYPES.md",
                REPO_ROOT / "plugins/codex/plugins/presentations/shared/references/RESEARCH_SLIDE_ARCHETYPES.md",
            ),
            (
                SHARED / "references/research_gold_composition.schema.json",
                REPO_ROOT / "plugins/codex/plugins/presentations/shared/references/research_gold_composition.schema.json",
            ),
            (
                SHARED / "references/research_gold_composition_index.json",
                REPO_ROOT / "plugins/codex/plugins/presentations/shared/references/research_gold_composition_index.json",
            ),
            (
                SHARED / "scripts/validate_gold_compositions.py",
                REPO_ROOT / "plugins/codex/plugins/presentations/shared/scripts/validate_gold_compositions.py",
            ),
            (
                SHARED / "scripts/select_gold_compositions.py",
                REPO_ROOT / "plugins/codex/plugins/presentations/shared/scripts/select_gold_compositions.py",
            ),
            (
                SHARED / "scripts/build_gold_composition_recipe.py",
                REPO_ROOT / "plugins/codex/plugins/presentations/shared/scripts/build_gold_composition_recipe.py",
            ),
            (
                SHARED / "scripts/generate_gold_composition_probe_artifacts.py",
                REPO_ROOT / "plugins/codex/plugins/presentations/shared/scripts/generate_gold_composition_probe_artifacts.py",
            ),
            (
                SHARED / "scripts/prepare_discussion_gold_admission_review.py",
                REPO_ROOT / "plugins/codex/plugins/presentations/shared/scripts/prepare_discussion_gold_admission_review.py",
            ),
            (
                SHARED / "scripts/generate_cuhk_scientific_layout_stage3.py",
                REPO_ROOT / "plugins/codex/plugins/presentations/shared/scripts/generate_cuhk_scientific_layout_stage3.py",
            ),
            (
                SHARED / "scripts/validate_cuhk_scientific_layout_stage3.py",
                REPO_ROOT / "plugins/codex/plugins/presentations/shared/scripts/validate_cuhk_scientific_layout_stage3.py",
            ),
            (
                SHARED / "templates/cuhk/beamer/source/styles/beamerthemesintef.sty",
                REPO_ROOT / "plugins/codex/plugins/presentations/shared/templates/cuhk/beamer/source/styles/beamerthemesintef.sty",
            ),
        ]
        for source, mirror in mirrors:
            self.assertEqual(source.read_text(encoding="utf-8"), mirror.read_text(encoding="utf-8"))

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

    def test_research_group_meeting_ai_bridge_visual_inputs_adapter(self) -> None:
        adapter = REPO_ROOT / "tests/fixtures/presentations/research_group_meeting/build_ai_bridge_visual_inputs.py"
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "visual_inputs.json"
            result = subprocess.run(
                [sys.executable, str(adapter), "--output", str(output)],
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            payload = json.loads(result.stdout)
            self.assertEqual(payload["input_count"], 4)
            manifest = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual(manifest["schema"], "AI_BRIDGE_VISUAL_INPUT_MANIFEST_V1")
            self.assertEqual(manifest["task_key"], "012_presentation_visual_adapter")
            self.assertEqual(manifest["workflow_type"], "generic")
            self.assertEqual(manifest["review_kind"], "research-presentation-four-page-smoke")
            self.assertEqual(manifest["privacy_policy"], "PUBLIC_SAFE_ONLY")
            bindings = manifest["identity_bindings"]
            self.assertEqual(bindings["bridge_kit_commit"], "f7c2f97cf44b1a4a52ff188c4a45a7eec57b808e")
            self.assertEqual(bindings["legacy_task_key"], "011_round_handoff")
            self.assertEqual(bindings["source_render_status"], "ok")
            self.assertEqual(bindings["source_mechanical_status"], "MECHANICAL_PASS")
            self.assertEqual(bindings["source_academic_visual_decision"], "NOT_ASSESSED")
            self.assertEqual(len(manifest["inputs"]), 4)
            for index, item in enumerate(manifest["inputs"], start=1):
                self.assertEqual(item["logical_id"], f"slide_{index}")
                self.assertEqual(item["mime_type"], "image/png")
                self.assertEqual(len(item["sha256"]), 64)
                self.assertTrue((REPO_ROOT / item["path"]).is_file())
                self.assertIn(f"slide_{index}", bindings["input_png_sha256_by_slide"])
                self.assertEqual(bindings["input_png_sha256_by_slide"][f"slide_{index}"], item["sha256"])
            rubric = manifest["rubric"]["instructions"]
            self.assertIn("Inspect the actual image pixels page by page", rubric)
            self.assertIn("Do not infer PASS from SHA", rubric)
            self.assertIn("rounded cards, tables, dashboards", rubric)
            self.assertIn("30-90 seconds", rubric)
            self.assertIn("smallest concrete page-specific repair", rubric)
            self.assertIn("skills/tools/documents-media/presentations/shared/visual-qa.md", manifest["rubric"]["source_contracts"])

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
            endpoint_data = manifest["synthetic_endpoint_data"]
            self.assertEqual(endpoint_data["best_by_endpoint"]["Burden error"], "Calibrated")
            self.assertEqual(endpoint_data["burden_error_favorable_direction"], "lower_is_better")
            self.assertEqual(endpoint_data["display_encoding"]["Burden error"], "raw_error_value_lower_is_better")
            self.assertEqual(
                manifest["result_page_evidence_boundary"],
                "Illustrative synthetic results - not completed validation",
            )
            phantom_layout = manifest["synthetic_phantom_metrics"]["layout"]
            self.assertTrue(phantom_layout["same_synthetic_case"])
            self.assertEqual(phantom_layout["source_grid_pixels"], 120)
            self.assertGreaterEqual(phantom_layout["rendered_case_pixels"], 180)
            self.assertGreaterEqual(
                phantom_layout["rendered_case_pixels"] / phantom_layout["panel_pixels"],
                0.75,
            )
            self.assertEqual(
                manifest["phantom_overlay_legend"],
                {"green": "TP/overlap", "red": "FP", "blue": "FN"},
            )
            experiment_paths = manifest["experiment_design_paths"]
            self.assertTrue(experiment_paths["explicit_local_only_comparator_branch"])
            self.assertIn("global_to_endpoint", experiment_paths["structural_connectors"])
            self.assertIn("local_only_to_endpoint", experiment_paths["structural_connectors"])
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
                slide_xml = "\n".join(deck.read(name).decode("utf-8") for name in slide_names)
            self.assertIn("lower-is-better", slide_xml)
            self.assertIn("lowest for Calibrated", slide_xml)
            self.assertIn("illustrative synthetic results", slide_xml)
            self.assertIn("not completed validation", slide_xml)
            self.assertIn("green = TP/overlap", slide_xml)
            self.assertIn("red = FP", slide_xml)
            self.assertIn("blue = FN", slide_xml)
            self.assertIn("Local-only comparator", slide_xml)
            self.assertIn("Endpoint evaluation", slide_xml)
            self.assertEqual(len(slide_names), 4)
            self.assertLess(len(media_names), 5)

    def test_statistical_method_group_meeting_benchmark_generator_outputs_artifacts(self) -> None:
        fixture = REPO_ROOT / "tests/fixtures/presentations/statistical_method_group_meeting"
        script = fixture / "generate_statistical_method_group_meeting_benchmark.py"
        reviewer = fixture / "review_statistical_method_group_meeting_benchmark.py"
        adapter = fixture / "build_ai_bridge_visual_inputs.py"
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
            manifest = json.loads(Path(payload["evidence_manifest"]).read_text(encoding="utf-8"))
            self.assertEqual(manifest["task_key"], "016_statistical_method_group_meeting_benchmark")
            self.assertEqual(manifest["status"], "GENERATED_SOURCE_ARTIFACTS_ONLY")
            self.assertFalse(manifest["generator_may_pass"])
            self.assertEqual(manifest["editable_slide_count"], 5)
            self.assertEqual([slide["archetype"] for slide in manifest["slides"]], [
                "STATISTICAL_MODEL",
                "ESTIMATOR",
                "SIMULATION_DESIGN",
                "RESULT_FIGURE",
                "NEGATIVE_RESULT",
            ])
            summary = manifest["simulation_summary"]
            self.assertEqual(summary["seed"], 20260822)
            self.assertEqual(summary["replicates_per_cell"], 400)
            self.assertEqual(summary["grid"]["center_count"], [8, 20, 50])
            self.assertEqual(summary["grid"]["icc"], [0.0, 0.1, 0.3, 0.5])
            self.assertEqual(summary["grid"]["imbalance"], ["balanced", "imbalanced"])
            self.assertEqual(summary["methods"], ["naive_iid_ols_z", "cluster_robust_z"])
            self.assertIn("95% interval coverage", summary["endpoints"])
            gates = manifest["deterministic_quality_gates"]
            self.assertEqual(gates["status"], "PASS", gates.get("failures"))
            self.assertIn("audience_facing_internal_leak", gates["checked_gates"])
            self.assertIn("math_source_leak", gates["checked_gates"])
            self.assertEqual(set(manifest["math_assets"]), {"slide1_dgp", "slide1_components", "slide1_icc", "slide2_sandwich", "slide2_naive"})
            for asset in manifest["math_assets"].values():
                self.assertEqual(asset["format"], "matplotlib_mathtext_png_transparent")
                self.assertGreater(asset["pixel_width"], 100)
                self.assertGreater(asset["pixel_height"], 40)
                self.assertTrue(Path(asset["path"]).is_file())
            audit_path = Path(tmp) / "reference_design_audit.json"
            self.assertTrue(audit_path.exists())
            reference_audit = json.loads(audit_path.read_text(encoding="utf-8"))
            self.assertEqual(len(reference_audit), 5)
            stress = summary["negative_result"]
            self.assertEqual(stress["condition"], "G=8, rho=0.5, imbalanced cluster sizes and treatment shares")
            self.assertLess(stress["cluster_robust_coverage"], 0.90)
            self.assertLess(stress["naive_iid_coverage"], stress["cluster_robust_coverage"])
            self.assertIn("planned", stress["next_experiment"])
            design = manifest["simulation_design_diagram"]
            self.assertEqual(design["edge_crossing"], "none")
            self.assertEqual(design["reading_direction"], "left_to_right")
            self.assertIn("tailEnd", design["arrowheads"])
            self.assertIn("cluster_to_endpoint", design["structural_connectors"])
            for slide in manifest["slides"]:
                self.assertGreaterEqual(len(slide["reference_ids"]), 2)
                self.assertLessEqual(len(slide["reference_ids"]), 5)
                self.assertEqual(slide["reference_design_audit"]["selected_reference_ids"], slide["reference_ids"])
                self.assertTrue(slide["reference_design_audit"]["adopted_design_decisions"])
                self.assertTrue(slide["audience_text"])
                audience_blob = "\n".join(slide["audience_text"])
                for forbidden in [
                    "RRL-",
                    "Reference retrieval",
                    "EVIDENCE_MANIFEST",
                    "Diagram contract",
                    "style not copied",
                    "Reading target",
                    "Observed in this synthetic run",
                ]:
                    self.assertNotIn(forbidden, audience_blob)
                retrieval = slide["reference_retrieval"]
                self.assertEqual(slide["reference_ids"], retrieval["selected_ids"])
                self.assertGreaterEqual(len(retrieval["candidate_ids"]), len(retrieval["selected_ids"]))
                self.assertIn("intent", retrieval["query"])
                self.assertIn("source_tiers", retrieval)
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
            if render["status"] == "ok":
                self.assertEqual(review["status"], "MECHANICAL_PASS")
                self.assertEqual(review["rendered_png_count"], 5)
            else:
                self.assertEqual(review["status"], "BLOCKED_REAL_PPTX_RENDER")
            with ZipFile(payload["pptx"]) as deck:
                slide_names = [name for name in deck.namelist() if name.startswith("ppt/slides/slide") and name.endswith(".xml")]
                media_names = [name for name in deck.namelist() if name.startswith("ppt/media/")]
                slide_xml = "\n".join(deck.read(name).decode("utf-8") for name in slide_names)
            self.assertEqual(len(slide_names), 5)
            self.assertNotIn("Y_ij = beta_0 + beta_1 T_ij + u_j + epsilon_ij", slide_xml)
            self.assertNotIn("V_CR", slide_xml)
            self.assertNotIn("Reference retrieval", slide_xml)
            self.assertNotIn("Diagram contract", slide_xml)
            self.assertNotIn("Reading target", slide_xml)
            self.assertNotIn("Observed in this synthetic run", slide_xml)
            self.assertNotIn("beta_1", slide_xml)
            self.assertNotIn("epsilon_ij", slide_xml)
            self.assertNotIn("X'X", slide_xml)
            self.assertIn("cluster-robust z interval", slide_xml)
            self.assertIn("coverage, bias, interval", slide_xml)
            self.assertIn("Planned comparison", slide_xml)
            self.assertIn("tailEnd", slide_xml)
            self.assertGreaterEqual(len(media_names), 7)

            committed_source = fixture / "visual_review_packet_source"
            if committed_source.exists():
                output = Path(tmp) / "visual_inputs.json"
                adapter_result = subprocess.run(
                    [sys.executable, str(adapter), "--source-dir", str(committed_source), "--output", str(output)],
                    check=False,
                    capture_output=True,
                    text=True,
                )
                self.assertEqual(adapter_result.returncode, 0, adapter_result.stderr)
                adapter_payload = json.loads(adapter_result.stdout)
                self.assertEqual(adapter_payload["input_count"], 5)
                visual_manifest = json.loads(output.read_text(encoding="utf-8"))
                self.assertEqual(visual_manifest["schema"], "AI_BRIDGE_VISUAL_INPUT_MANIFEST_V1")
                self.assertEqual(visual_manifest["task_key"], "016_statistical_method_group_meeting_benchmark")
                self.assertEqual(visual_manifest["review_kind"], "statistical-method-group-meeting-benchmark")
                self.assertEqual(visual_manifest["privacy_policy"], "PUBLIC_SAFE_ONLY")
                self.assertEqual(len(visual_manifest["inputs"]), 5)
                self.assertEqual(visual_manifest["identity_bindings"]["source_render_status"], "ok")
                self.assertEqual(visual_manifest["identity_bindings"]["source_mechanical_status"], "MECHANICAL_PASS")
                self.assertEqual(visual_manifest["identity_bindings"]["source_academic_visual_decision"], "NOT_ASSESSED")
                self.assertIn("reference_design_audit_sha256", visual_manifest["identity_bindings"])
                rubric = visual_manifest["rubric"]["instructions"]
                self.assertIn("statistical/biostatistical method group meeting benchmark", rubric)
                self.assertIn("coverage near nominal 0.95 is the target", rubric)
                self.assertIn("visible arrowheads", rubric)
                self.assertIn("Mathematical typesetting", rubric)
                self.assertIn("Would this slide look professionally finished", rubric)
                self.assertIn("Reference-informed quality", rubric)

    def test_medical_imaging_group_meeting_benchmark_generator_outputs_artifacts(self) -> None:
        fixture = REPO_ROOT / "tests/fixtures/presentations/medical_imaging_group_meeting"
        script = fixture / "generate_medical_imaging_group_meeting_benchmark.py"
        reviewer = fixture / "review_medical_imaging_group_meeting_benchmark.py"
        adapter = fixture / "build_ai_bridge_visual_inputs.py"
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
            manifest = json.loads(Path(payload["evidence_manifest"]).read_text(encoding="utf-8"))
            self.assertEqual(manifest["task_key"], "017_medical_imaging_group_meeting_benchmark")
            self.assertEqual(manifest["status"], "GENERATED_SOURCE_ARTIFACTS_ONLY")
            self.assertFalse(manifest["generator_may_pass"])
            self.assertEqual(manifest["editable_slide_count"], 5)
            self.assertEqual([slide["archetype"] for slide in manifest["slides"]], [
                "MEDICAL_IMAGE_COMPARISON",
                "EXPERIMENT_DESIGN",
                "RESULT_FIGURE",
                "FAILURE_CASE",
                "NEGATIVE_RESULT",
            ])
            summary = manifest["synthetic_dataset_summary"]
            self.assertEqual(summary["seed"], 20260822)
            self.assertEqual(summary["cases_per_center"], 30)
            self.assertEqual(summary["endpoints"], ["Dice overlap", "lesion-level recall", "false-positive burden"])
            self.assertEqual([row["center"] for row in summary["center_summary"]], ["Center A", "Center B", "Center C"])
            self.assertGreater(summary["negative_result"]["center_c_dice"], 0.40)
            self.assertLess(summary["negative_result"]["small_lesion_recall"], 0.45)
            self.assertIn("planned", summary["negative_result"]["planned_validation"])
            gates = manifest["deterministic_quality_gates"]
            self.assertEqual(gates["status"], "PASS", gates.get("failures"))
            self.assertIn("same_case_failure_panels", gates["checked_gates"])
            self.assertIn("endpoint_disagreement_supported_by_metrics", gates["checked_gates"])
            failure = manifest["failure_case"]
            self.assertTrue(failure["same_slice_geometry"])
            self.assertEqual(failure["center"], "Center C")
            self.assertEqual(failure["lesion_size"], "small")
            self.assertIn("TP / FP / FN", failure["panels"])
            design = manifest["experiment_design_diagram"]
            self.assertEqual(design["edge_crossing"], "none")
            self.assertEqual(design["reading_direction"], "left_to_right")
            self.assertIn("tailEnd", design["arrowheads"])
            audit_path = Path(tmp) / "reference_design_audit.json"
            self.assertTrue(audit_path.exists())
            reference_audit = json.loads(audit_path.read_text(encoding="utf-8"))
            self.assertEqual(len(reference_audit), 5)
            for slide in manifest["slides"]:
                self.assertGreaterEqual(len(slide["reference_ids"]), 2)
                self.assertLessEqual(len(slide["reference_ids"]), 5)
                self.assertEqual(slide["reference_design_audit"]["selected_reference_ids"], slide["reference_ids"])
                self.assertTrue(slide["reference_design_audit"]["adopted_design_decisions"])
                self.assertTrue(slide["audience_text"])
                audience_blob = "\n".join(slide["audience_text"])
                for forbidden in [
                    "RRL-",
                    "Reference retrieval",
                    "EVIDENCE_MANIFEST",
                    "Diagram contract",
                    "style not copied",
                    "Reading target",
                    "Observed in this synthetic run",
                    "evidence boundary",
                ]:
                    self.assertNotIn(forbidden, audience_blob)
                retrieval = slide["reference_retrieval"]
                self.assertEqual(slide["reference_ids"], retrieval["selected_ids"])
                self.assertGreaterEqual(len(retrieval["candidate_ids"]), len(retrieval["selected_ids"]))
                self.assertIn("intent", retrieval["query"])
                for selected_id in retrieval["selected_ids"]:
                    self.assertIn(selected_id, retrieval["candidate_ids"])
                    self.assertIn("source_tier=", retrieval["ranking_relevance_reason"][selected_id])
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
            if render["status"] == "ok":
                self.assertEqual(review["status"], "MECHANICAL_PASS")
                self.assertEqual(review["rendered_png_count"], 5)
            with ZipFile(payload["pptx"]) as deck:
                slide_names = [name for name in deck.namelist() if name.startswith("ppt/slides/slide") and name.endswith(".xml")]
                media_names = [name for name in deck.namelist() if name.startswith("ppt/media/")]
                slide_xml = "\n".join(deck.read(name).decode("utf-8") for name in slide_names)
            self.assertEqual(len(slide_names), 5)
            for forbidden in ["RRL-", "Reference retrieval", "EVIDENCE_MANIFEST", "Diagram contract", "Reading target", "Observed in this synthetic run"]:
                self.assertNotIn(forbidden, slide_xml)
            self.assertIn("Synthetic cardiac-MR-like", slide_xml)
            self.assertIn("lesion recall", slide_xml)
            self.assertIn("Planned validation", slide_xml)
            self.assertIn("tailEnd", slide_xml)
            self.assertGreaterEqual(len(media_names), 8)

            committed_source = fixture / "visual_review_packet_source"
            self.assertTrue(committed_source.exists())
            output = Path(tmp) / "visual_inputs.json"
            adapter_result = subprocess.run(
                [sys.executable, str(adapter), "--source-dir", str(committed_source), "--output", str(output)],
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertEqual(adapter_result.returncode, 0, adapter_result.stderr)
            adapter_payload = json.loads(adapter_result.stdout)
            self.assertEqual(adapter_payload["input_count"], 5)
            visual_manifest = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual(visual_manifest["schema"], "AI_BRIDGE_VISUAL_INPUT_MANIFEST_V1")
            self.assertEqual(visual_manifest["task_key"], "017_medical_imaging_group_meeting_benchmark")
            self.assertEqual(visual_manifest["review_kind"], "medical-imaging-group-meeting-benchmark")
            self.assertEqual(visual_manifest["privacy_policy"], "PUBLIC_SAFE_ONLY")
            self.assertEqual(len(visual_manifest["inputs"]), 5)
            self.assertEqual(visual_manifest["identity_bindings"]["source_render_status"], "ok")
            self.assertEqual(visual_manifest["identity_bindings"]["source_mechanical_status"], "MECHANICAL_PASS")
            self.assertIn("reference_design_audit_sha256", visual_manifest["identity_bindings"])
            rubric = visual_manifest["rubric"]["instructions"]
            self.assertIn("medical-imaging research group meeting benchmark", rubric)
            self.assertIn("actual image pixels", rubric)
            self.assertIn("MICCAI/RSNA-style research talk", rubric)
            self.assertIn("TP/FP/FN legend", rubric)
            self.assertIn("false-positive burden is lower-is-better", rubric)


if __name__ == "__main__":
    unittest.main()
