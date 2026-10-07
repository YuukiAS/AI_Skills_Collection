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
            "Runtime Kernel",
            "Allowed Durable Meaning Set",
            "semantic spine",
            "No-Op And Degradation",
            "semantic mutation radius",
            "surface reconstruction radius",
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

        required = [
            "live baseline",
            "protected absence",
            "lookup-before-action",
            "Semantic ownership alone is not enough",
            "durable semantic map",
            "direct Project-resident rule",
            "short locator bridge",
            "source-only",
            "task/thread only",
            "semantic coverage and redundancy review",
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
            self.assertIn(phrase, contract)

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
            self.assertIn(phrase, contract + skill_body)

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
        combined = contract + skill_body
        for phrase in removed_claims:
            self.assertNotIn(phrase, combined)

    def test_surface_consolidation_repair_contract_is_structural_not_mechanical(self) -> None:
        skill_body = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")
        contract = (SKILL_DIR / "references" / "editor-contract.md").read_text(encoding="utf-8")
        combined = skill_body + "\n" + contract
        fixture = json.loads((FIXTURE_DIR / "surface_consolidation_repair.json").read_text(encoding="utf-8"))

        for phrase in [
            "long-lived semantic map",
            "same practical trigger and user consequence",
            "Allowed Durable Meaning Set",
            "current semantic support",
            "semantic coverage and redundancy review",
            "source wrapper wording",
            "descriptive prose",
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

        for non_goal in fixture["non_goals"]:
            self.assertIn(non_goal, fixture["non_goals"])
        for prohibited_active_mechanism in [
            "Use a Latin-token score",
            "Use an English ratio",
            "Use a translation dictionary",
            "Use a fixed-section template",
        ]:
            self.assertNotIn(prohibited_active_mechanism, combined)

    def test_semantic_spine_repair_contract_is_structural_and_generic(self) -> None:
        skill_body = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")
        contract = (SKILL_DIR / "references" / "editor-contract.md").read_text(encoding="utf-8")
        combined = skill_body + "\n" + contract
        fixture = json.loads((FIXTURE_DIR / "semantic_spine_repair.json").read_text(encoding="utf-8"))

        for phrase in [
            "two-level semantic spine",
            "atomic durable meanings",
            "semantic families",
            "governed actor or surface",
            "trigger or phase",
            "failure consequence",
            "Structure is not a protected semantic invariant by default",
            "heading count",
            "source grouping",
            "scope dominance",
            "authorization, safety, privacy",
            "narrower special-case rule",
            "Dynamic-Set Abstraction",
            "currently supported items defined by the",
            "same trigger and user consequence",
            "preferred vocabulary",
            "semantic-spine reconciliation",
        ]:
            self.assertIn(phrase, combined)

        expectations = fixture["semantic_spine_expectations"]
        self.assertIn("governed actor/surface", expectations["family_construction"]["clusters_by"])
        self.assertTrue(fixture["expected_final_candidate_properties"]["keeps_broad_authorization_boundary"])
        self.assertTrue(fixture["expected_final_candidate_properties"]["does_not_replace_broad_boundary_with_narrow_special_case"])
        self.assertTrue(fixture["expected_final_candidate_properties"]["abstracts_mutable_source_owned_set"])
        self.assertTrue(fixture["expected_final_candidate_properties"]["merges_overlapping_normal_delivery_rules"])
        self.assertTrue(fixture["expected_final_candidate_properties"]["keeps_distinct_closure_trigger_when_needed"])
        self.assertTrue(fixture["expected_final_candidate_properties"]["has_no_project_resident_deletion_tombstone"])

        fixture_text = json.dumps(fixture, ensure_ascii=False)
        for project_specific_term in ["Server+VPS", "Android", "Windows", "macOS", "iPadOS"]:
            self.assertNotIn(project_specific_term, fixture_text)
        self.assertNotIn("nine-section", combined)
        for prohibited_mechanism in ["Latin-token scan", "blacklist", "translation table", "English ratio"]:
            self.assertIn(prohibited_mechanism, fixture_text)
        self.assertNotIn("fixed nine-section template", combined)

    def test_runtime_kernel_refactor_contract_is_closed_world_and_bidirectional(self) -> None:
        skill_body = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")
        contract = (SKILL_DIR / "references" / "editor-contract.md").read_text(encoding="utf-8")
        combined = skill_body + "\n" + contract
        fixture = json.loads((FIXTURE_DIR / "runtime_kernel_refactor.json").read_text(encoding="utf-8"))

        for phrase in [
            "Runtime Kernel",
            "K1",
            "K2",
            "K3",
            "K4",
            "K5",
            "K6",
            "K7",
            "Allowed Durable Meaning Set",
            "semantic mutation radius",
            "surface reconstruction radius",
            "bidirectional reconciliation",
            "coverage direction",
            "provenance direction",
            "dynamic-set abstraction",
            "protected absence wins",
        ]:
            self.assertIn(phrase, combined)

        cases = fixture["cases"]
        self.assertIn("A_semantic_bounded_surface_global", cases)
        self.assertIn("B_closed_world_no_opportunistic_addition", cases)
        self.assertIn("C_global_dynamic_set_abstraction", cases)
        self.assertIn("D_scope_dominance_and_protected_absence", cases)
        self.assertIn("Old heading count and source order are not protected.", cases["A_semantic_bounded_surface_global"]["expected"])
        self.assertIn(
            "The same mutable set does not survive as an enumeration elsewhere.",
            cases["C_global_dynamic_set_abstraction"]["expected"],
        )
        self.assertIn(
            "The historical-only broad rule is not resurrected; protected absence wins unless current user or authorized source sync re-adopts it.",
            cases["D_scope_dominance_and_protected_absence"]["historical_broad_live_narrow"]["expected"],
        )

        fixture_text = json.dumps(fixture, ensure_ascii=False)
        for project_specific_term in ["Server+VPS", "Android", "Windows", "macOS", "iPadOS", "TOTP"]:
            self.assertNotIn(project_specific_term, fixture_text)
        for prohibited_mechanism in ["Latin-token scan", "language ratio", "blacklist", "translation dictionary"]:
            self.assertIn(prohibited_mechanism, fixture_text)

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
