from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from skill_utils import read_frontmatter  # noqa: E402


SKILL_DIR = REPO_ROOT / "skills" / "science" / "communication" / "project-thread-handoff"
SKILL_FILE = SKILL_DIR / "SKILL.md"
OPENAI_FILE = SKILL_DIR / "agents" / "openai.yaml"
EVAL_FILE = SKILL_DIR / "evals" / "trigger_queries.json"
REGISTRY_FILE = REPO_ROOT / "registry.json"
G3_FIXTURE = REPO_ROOT / "tests" / "fixtures" / "project_thread_handoff" / "g3_regressions.json"


class ProjectThreadHandoffContractTests(unittest.TestCase):
    def test_skill_frontmatter_freezes_read_only_capability(self) -> None:
        meta, _ = read_frontmatter(SKILL_FILE)

        self.assertEqual(meta.get("name"), "project-thread-handoff")
        self.assertEqual(meta.get("status"), "active")
        self.assertEqual(meta.get("provenance"), "user-authored")
        self.assertIs(meta.get("trusted"), False)
        self.assertIs(meta.get("requires_network"), False)
        self.assertIs(meta.get("writes_files"), False)
        self.assertIs(meta.get("executes_code"), False)
        self.assertEqual(meta.get("secrets_needed"), [])
        self.assertEqual(meta.get("recommended_scope"), "project")
        self.assertEqual(meta.get("metadata", {}).get("skill-author"), "AI Skills Collection maintainers")
        self.assertNotIn("allow_implicit_invocation", meta)

    def test_openai_metadata_keeps_invocation_policy_out_of_skill_frontmatter(self) -> None:
        meta, _ = read_frontmatter(SKILL_FILE)
        openai_meta = yaml.safe_load(OPENAI_FILE.read_text(encoding="utf-8"))

        self.assertNotIn("allow_implicit_invocation", meta)
        self.assertIs(openai_meta["policy"]["allow_implicit_invocation"], False)
        self.assertEqual(openai_meta["interface"]["display_name"], "Project Thread Handoff")

    def test_registry_record_preserves_read_only_identity(self) -> None:
        registry = json.loads(REGISTRY_FILE.read_text(encoding="utf-8"))
        matches = [
            record
            for record in registry["skills"]
            if record.get("name") == "project-thread-handoff"
            and record.get("path") == "skills/science/communication/project-thread-handoff"
        ]
        self.assertEqual(len(matches), 1)
        record = matches[0]

        self.assertEqual(record.get("provenance"), "user-authored")
        self.assertIs(record.get("requires_network"), False)
        self.assertIs(record.get("writes_files"), False)
        self.assertIs(record.get("executes_code"), False)
        self.assertEqual(record.get("secrets_needed"), [])

    def test_body_preserves_authority_locator_and_read_only_contract(self) -> None:
        _, body = read_frontmatter(SKILL_FILE)

        required_phrases = [
            "Later assistant brainstorming does not override",
            "thread-only deltas",
            "never invent unknown paths or SHAs",
            "Output one self-contained prompt and stop",
            "Do not ask for confirmation",
            "No repository writes",
            "no MCP dependency",
            "no Bridge Kit dependency",
        ]
        for phrase in required_phrases:
            self.assertIn(phrase, body)

    def test_chatgpt_normal_entry_is_surface_neutral(self) -> None:
        _, body = read_frontmatter(SKILL_FILE)

        self.assertIn("formal Skill selection, mention, or invocation entry", body)
        self.assertIn("do not require a specific", body)
        self.assertNotIn("must use $", body.lower())
        self.assertNotIn("must use @", body.lower())
        self.assertNotIn("must use /", body.lower())

    def test_trigger_eval_requires_explicit_invocation_and_rejects_near_misses(self) -> None:
        data = json.loads(EVAL_FILE.read_text(encoding="utf-8"))

        self.assertGreaterEqual(len(data["positive"]), 3)
        self.assertGreaterEqual(len(data["negative"]), 4)
        self.assertGreaterEqual(len(data["near_miss"]), 4)
        self.assertTrue(all("handoff" in item.lower() for item in data["positive"]))
        self.assertIn("总结一下当前项目", data["negative"])
        self.assertIn("我们现在做到哪了", data["negative"])
        self.assertIn("帮我继续研究", data["negative"])
        self.assertIn("handoff 是什么意思", data["negative"])
        self.assertIn("explicit installed Skill invocation", data["notes"])

    def test_skill_does_not_add_extra_runtime_surfaces(self) -> None:
        unexpected = [
            SKILL_DIR / "scripts",
            SKILL_DIR / "references",
            SKILL_DIR / "database",
            SKILL_DIR / "CURRENT.json",
            SKILL_DIR / "history",
        ]
        self.assertFalse([path for path in unexpected if path.exists()])
        self.assertEqual(sorted(path.name for path in (SKILL_DIR / "assets").glob("*")), ["app-facing.svg"])

    def test_g3_representative_generalization_is_covered_without_project_hardcoding(self) -> None:
        _, body = read_frontmatter(SKILL_FILE)
        fixture = json.loads(G3_FIXTURE.read_text(encoding="utf-8"))

        self.assertIn("cat_trace", fixture)
        self.assertIn("cardiacnexus", fixture)
        self.assertIn("Later assistant brainstorming does not override", body)
        self.assertIn("short recurrence guard", body)
        self.assertIn("Repositories, artifacts, reports, and generated outputs remain the authority", body)
        self.assertIn("immediate next action", body)
        self.assertIn("never invent unknown paths or SHAs", body)
        self.assertNotIn("DII", body)
        self.assertNotIn("CARE", body)
        self.assertNotIn("CAT-TRACE", body)
        self.assertNotIn("CardiacNexus", body)


if __name__ == "__main__":
    unittest.main()
