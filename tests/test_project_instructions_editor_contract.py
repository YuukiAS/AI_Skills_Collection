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
    def test_frontmatter_matches_frozen_capability_contract(self) -> None:
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
        self.assertEqual(meta.get("metadata", {}).get("skill-author"), "AI Skills Collection maintainers")

        description = meta.get("description", "")
        self.assertLess(len(description), 350)
        for phrase in [
            "ChatGPT Project instructions",
            "live settings",
            "canonical sources",
            "generic system/agent prompts",
            "global Custom Instructions",
        ]:
            self.assertIn(phrase, description)

        self.assertIn("preservation-sensitive", body)
        self.assertIn("greenfield", body)
        self.assertIn("explicit reset", body)
        self.assertIn("Protected Absence", body)
        self.assertIn("semantic ownership", body)
        self.assertIn("effective enforcement", body)

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

    def test_openai_yaml_allows_natural_implicit_entry(self) -> None:
        text = (SKILL_DIR / "agents" / "openai.yaml").read_text(encoding="utf-8")
        self.assertIn('display_name: "Project Instructions Editor"', text)
        self.assertIn("allow_implicit_invocation: true", text)
        self.assertNotIn("allow_implicit_invocation: false", text)
        self.assertIn("$project-instructions-editor", text)

    def test_reference_preserves_non_substitutable_semantics(self) -> None:
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
        ]
        for phrase in required:
            self.assertIn(phrase, contract)

        rejected_mechanics = [
            "English ratios",
            "keyword scorers",
            "fixed paragraph counts",
            "fixed heading counts",
            "fixed formula counts",
        ]
        for phrase in rejected_mechanics:
            self.assertIn(phrase, contract)

    def test_trigger_queries_cover_positive_and_near_miss_boundaries(self) -> None:
        data = json.loads((SKILL_DIR / "evals" / "trigger_queries.json").read_text(encoding="utf-8"))
        positives = " ".join(data["positive"])
        negatives = " ".join(data["negative"] + data["near_miss"])

        for phrase in ["Project instructions", "Compress", "Create initial", "Reset", "Sync"]:
            self.assertIn(phrase, positives)
        for phrase in ["中文", "technical report", "AI_Skills_Collection", "Planner/Critic", "global Custom Instructions"]:
            self.assertIn(phrase, negatives)

        self.assertNotIn("Use project-instructions-editor", positives)
        self.assertNotIn("$project-instructions-editor", positives)

    def test_icon_is_valid_svg_with_expected_viewbox(self) -> None:
        icon = SKILL_DIR / "assets" / "app-facing.svg"
        root = ET.parse(icon).getroot()
        self.assertEqual(root.tag.rsplit("}", 1)[-1], "svg")
        self.assertEqual(root.attrib.get("viewBox"), "0 0 64 64")


if __name__ == "__main__":
    unittest.main()
