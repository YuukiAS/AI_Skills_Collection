from __future__ import annotations

import json
import csv
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
                    for record in zoom["crop_records"]:
                        self.assertTrue(record["same_case_coordinate_space"])
                        self.assertTrue((generated / "cuhk_stage3_build" / record["zoom_asset"]).exists())
                if layout["page_job"] in {"EXPERIMENT_DESIGN", "NEXT_EXPERIMENT"}:
                    self.assertGreaterEqual(bbox["w"] * bbox["h"], 0.36)
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
            self.assertIn(r"centers \(G=8,20,50\)", tex)
            self.assertIn(r"ICC \(\rho=0,.1,.3,.5\)", tex)
            self.assertIn("naive iid OLS z interval", tex)
            self.assertIn("Subject records nested inside each center", tex)
            self.assertNotIn("centers -> subjects", tex)
            self.assertIn("Coverage target 0.95", tex)
            self.assertIn("DPP diverse batch", tex)
            self.assertIn("random batch", tex)
            self.assertIn("coverage >= .94", tex)
            self.assertIn("Same-case ROI zoom", tex)
            self.assertIn("Overlay legend", tex)
            self.assertIn("Decision rule", tex)
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
