from __future__ import annotations

import json
import sys
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from skill_utils import read_frontmatter  # noqa: E402


SKILL_DIR = REPO_ROOT / "skills" / "core" / "codex-system" / "project-instructions-editor"
FIXTURE_DIR = REPO_ROOT / "tests" / "fixtures" / "project_instructions_editor"


class ProjectInstructionsEditorContractTests(unittest.TestCase):
    def test_frontmatter_matches_v0_1_editor_scope(self) -> None:
        meta, body = read_frontmatter(SKILL_DIR / "SKILL.md")

        self.assertEqual(meta.get("name"), "project-instructions-editor")
        self.assertEqual(meta.get("status"), "active")
        self.assertEqual(meta.get("version"), "0.1")
        self.assertEqual(meta.get("provenance"), "user-authored")
        self.assertIs(meta.get("trusted"), False)
        self.assertIs(meta.get("requires_network"), False)
        self.assertIs(meta.get("writes_files"), False)
        self.assertIs(meta.get("executes_code"), False)
        self.assertEqual(meta.get("secrets_needed"), [])
        self.assertEqual(meta.get("recommended_scope"), "global")
        self.assertEqual(meta.get("icon_small"), "assets/app-facing.svg")
        self.assertEqual(meta.get("icon_large"), "assets/app-facing.svg")

        description = meta.get("description", "")
        self.assertLess(len(description), 350)
        for phrase in [
            "explicitly asks",
            "ChatGPT Project instructions",
            "live setting is missing",
            "ordinary prose",
            "writing fidelity",
            "scientific rewrite",
            "AI_Skills maintenance",
            "workflow/control",
            "generic agent/system prompts",
            "global Custom Instructions",
        ]:
            self.assertIn(phrase, description)

        for phrase in [
            "preservation-sensitive",
            "greenfield",
            "explicit reset",
            "Protected Absence",
            "Simple Editing Core",
            "No-op",
            "FINAL_ROUTE=`SIMPLE_FORMAL_CORE`",
            "ADVANCED_INDEPENDENT_MULTI_CALL_FINALIZATION=`UNSUPPORTED`",
            "CROSS_TURN_FINAL_READER_LAYER_GUARANTEE=`UNSUPPORTED_IN_PIE_0_1`",
        ]:
            self.assertIn(phrase, body)

    def test_runtime_shape_is_instruction_reference_only(self) -> None:
        expected_files = {
            "SKILL.md",
            "agents/openai.yaml",
            "references/editor-contract.md",
            "evals/trigger_queries.json",
            "assets/app-facing.svg",
        }
        actual_files = {
            path.relative_to(SKILL_DIR).as_posix()
            for path in SKILL_DIR.rglob("*")
            if path.is_file()
        }
        self.assertEqual(actual_files, expected_files)
        self.assertFalse((SKILL_DIR / "scripts").exists())

    def test_openai_yaml_allows_natural_project_entry_only(self) -> None:
        text = (SKILL_DIR / "agents" / "openai.yaml").read_text(encoding="utf-8")
        self.assertIn('display_name: "Project Instructions Editor"', text)
        self.assertIn("allow_implicit_invocation: true", text)
        self.assertIn("$project-instructions-editor", text)
        self.assertIn("Edits long-lived ChatGPT Project instructions", text)
        self.assertNotIn("reader-facing output baseline", text)

    def test_reference_preserves_editor_semantics_without_reader_layer_claim(self) -> None:
        skill_body = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")
        contract = (SKILL_DIR / "references" / "editor-contract.md").read_text(encoding="utf-8")
        combined = contract + "\n" + skill_body

        required = [
            "live baseline",
            "Protected Absence",
            "lookup-before-action",
            "Semantic ownership alone is not enough",
            "durable user-facing rule groups",
            "direct Project-resident rule",
            "short locator bridge",
            "canonical-source only",
            "task/thread only",
            "mandatory versus optional",
            "authorization boundaries",
            "evidence strength",
            "explicit user deletion/correction",
            "No-op is valid",
            "No-op is not eligible",
            "locator",
            "budget",
        ]
        for phrase in required:
            self.assertIn(phrase, combined)

        protected_absence_contract = [
            "omit both the deleted rule and its deletion history",
            "do not emit `do not restore X`",
            "Project-resident tombstone",
            "unless the current user explicitly asks",
        ]
        for phrase in protected_absence_contract:
            self.assertIn(phrase, contract)
            self.assertIn(phrase, skill_body)

        unsupported_runtime_named = [
            "MCP finalizer",
            "OPENAI_API_KEY",
            "external model provider",
            "sibling Skill chain",
            "cross-turn final reader-layer guarantee",
        ]
        for phrase in unsupported_runtime_named:
            self.assertIn(phrase, combined)

        removed_claims = [
            "finalize_project_instructions",
            "Stage B",
            "Stage C",
            "Reader-Facing Baseline",
            "reader-facing baseline presence or equivalence",
            "baseline is materially absent",
            "Server+VPS",
            "English ratio",
            "Latin-token score",
            "translation dictionary",
        ]
        for phrase in removed_claims:
            self.assertNotIn(phrase, combined)

    def test_known_good_core_removed_recent_runtime_machinery(self) -> None:
        skill_body = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")
        contract = (SKILL_DIR / "references" / "editor-contract.md").read_text(encoding="utf-8")
        combined = skill_body + "\n" + contract

        for removed_phrase in [
            "Runtime Kernel",
            "K1",
            "K2",
            "K3",
            "K4",
            "K5",
            "K6",
            "K7",
            "Allowed Durable Meaning Set",
            "bidirectional reconciliation",
            "coverage direction",
            "provenance direction",
            "semantic mutation radius",
            "surface reconstruction radius",
            "two-level semantic spine",
        ]:
            self.assertNotIn(removed_phrase, combined)

        for retained_behavior in [
            "identify durable user-facing rule groups",
            "consolidate duplicate rules",
            "move volatile detail behind stable source bridges",
            "preserve semantic force and exact identities",
            "source headings",
            "not protected by default",
            "same normal trigger and user consequence",
            "A historical-only broad rule",
            "stays absent",
        ]:
            self.assertIn(retained_behavior, combined)

        self.assertLess(len(skill_body.encode("utf-8")), 12000)

    def test_surface_consolidation_repair_contract_is_structural_not_mechanical(self) -> None:
        skill_body = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")
        contract = (SKILL_DIR / "references" / "editor-contract.md").read_text(encoding="utf-8")
        combined = skill_body + "\n" + contract
        fixture = json.loads((FIXTURE_DIR / "surface_consolidation_repair.json").read_text(encoding="utf-8"))

        for phrase in [
            "durable user-facing rule groups",
            "same normal trigger and user consequence",
            "current semantic support",
            "source wrapper wording",
            "does not guarantee that all future ChatGPT turns",
            "should not expose internal labels",
        ]:
            self.assertIn(phrase, combined)

        expected_dispositions = {
            item["disposition"] for item in fixture["expected_semantic_dispositions"]
        }
        self.assertEqual(
            expected_dispositions,
            {
                "direct_project_rule",
                "short_locator_bridge",
                "source_only",
                "omit",
                "task_only",
            },
        )
        self.assertTrue(fixture["expected_final_candidate_properties"]["has_no_project_resident_deletion_tombstone"])
        self.assertTrue(fixture["expected_final_candidate_properties"]["does_not_expose_internal_meaning_map_by_default"])

        for prohibited_active_mechanism in [
            "Use a Latin-token score",
            "Use an English ratio",
            "Use a translation dictionary",
            "Use a fixed-section template",
        ]:
            self.assertNotIn(prohibited_active_mechanism, combined)

    def test_generic_known_good_structure_regression_is_not_domain_specific(self) -> None:
        skill_body = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")
        contract = (SKILL_DIR / "references" / "editor-contract.md").read_text(encoding="utf-8")
        combined = skill_body + "\n" + contract
        fixture = json.loads((FIXTURE_DIR / "known_good_generic_structure_regression.json").read_text(encoding="utf-8"))

        for phrase in [
            "source headings",
            "old section order",
            "not protected by default",
            "same normal trigger and user consequence",
            "stable canonical source owns the current list",
            "Apply this globally",
            "A narrower special-case rule",
            "must not swallow a broader live boundary",
            "historical-only broad rule",
            "remains absent",
        ]:
            self.assertIn(phrase, combined)

        self.assertTrue(fixture["expected_final_candidate_properties"]["keeps_broad_authorization_boundary"])
        self.assertTrue(fixture["expected_final_candidate_properties"]["abstracts_mutable_source_owned_set"])
        self.assertTrue(fixture["expected_final_candidate_properties"]["merges_overlapping_normal_delivery_rules"])
        self.assertTrue(fixture["expected_final_candidate_properties"]["keeps_distinct_closure_trigger_when_needed"])
        self.assertTrue(fixture["expected_final_candidate_properties"]["has_no_project_resident_deletion_tombstone"])
        self.assertTrue(fixture["expected_final_candidate_properties"]["does_not_create_unsupported_durable_rules"])

        fixture_text = json.dumps(fixture, ensure_ascii=False)
        for project_specific_term in ["Server+VPS", "Android", "Windows", "macOS", "iPadOS", "TOTP"]:
            self.assertNotIn(project_specific_term, fixture_text)
            self.assertNotIn(project_specific_term, combined)
        self.assertNotIn("always nine sections", combined)
        self.assertNotIn("fixed nine-section template", combined)

    def test_server_vps_positive_fixture_captures_known_good_without_generic_template(self) -> None:
        skill_body = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")
        contract = (SKILL_DIR / "references" / "editor-contract.md").read_text(encoding="utf-8")
        combined = skill_body + "\n" + contract
        fixture = json.loads((FIXTURE_DIR / "server_vps_known_good_positive_regression.json").read_text(encoding="utf-8"))

        self.assertEqual(
            fixture["positive_reference_families"],
            [
                "权威归属",
                "面向用户的回答",
                "代理客户端与交付",
                "客户端实时网络状态与用户操作",
                "自动验证优先",
                "权威来源与生产修改",
                "保守判定与冗余",
                "完整性与敏感信息",
                "生产任务结束时",
            ],
        )
        self.assertTrue(fixture["fixture_scope"]["domain_specific_positive_regression"])
        self.assertFalse(fixture["fixture_scope"]["generic_template"])

        anti_regressions = fixture["anti_regressions"]
        for expected in [
            "no_overlapping_normal_response_sections",
            "no_source_shaped_12_or_13_headings",
            "no_current_device_or_platform_inventory_as_durable_truth",
            "no_repeated_canonical_lookup_clauses",
            "no_unsupported_history_or_best_practice_security_rules",
        ]:
            self.assertIn(expected, anti_regressions)

        self.assertNotIn("Server+VPS", combined)
        self.assertNotIn("nine sections", combined)

    def test_default_output_contract_hides_internal_edit_mode_labels(self) -> None:
        skill_body = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")
        contract = (SKILL_DIR / "references" / "editor-contract.md").read_text(encoding="utf-8")
        combined = skill_body + "\n" + contract

        self.assertNotIn("state the edit mode", combined)
        self.assertNotIn("Full replacements must include mode", combined)
        self.assertIn("Do not print internal mode labels", skill_body)
        self.assertIn("must not print internal mode labels", contract)
        for label in ["`preservation-sensitive`", "`greenfield`", "`explicit reset`"]:
            self.assertIn(label, combined)
        self.assertIn("only when it affects understanding or safety", combined)
        self.assertIn("based on the existing setting", combined)
        self.assertIn("starts from an empty setting", combined)
        self.assertIn("follows an explicit reset", combined)
        self.assertIn("formal audit", combined)

    def test_trigger_queries_cover_positive_and_near_miss_boundaries(self) -> None:
        data = json.loads((SKILL_DIR / "evals" / "trigger_queries.json").read_text(encoding="utf-8"))
        positives = " ".join(data["positive"])
        negatives = " ".join(data["negative"] + data["near_miss"])

        for phrase in ["Project instructions", "Compress", "Create initial", "Reset", "Sync", "Restructure"]:
            self.assertIn(phrase, positives)
        for phrase in ["中文", "technical report", "AI_Skills_Collection", "Planner/Critic", "global Custom Instructions"]:
            self.assertIn(phrase, negatives)

        self.assertNotIn("reader-facing output baseline", positives)
        self.assertNotIn("Use project-instructions-editor", positives)
        self.assertNotIn("$project-instructions-editor", positives)

    def test_icon_is_valid_svg_with_expected_viewbox(self) -> None:
        icon = SKILL_DIR / "assets" / "app-facing.svg"
        root = ET.parse(icon).getroot()
        self.assertEqual(root.tag.rsplit("}", 1)[-1], "svg")
        self.assertEqual(root.attrib.get("viewBox"), "0 0 64 64")


if __name__ == "__main__":
    unittest.main()
