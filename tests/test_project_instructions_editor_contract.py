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
            "No-Op Eligibility",
            "Semantic Invariants",
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
