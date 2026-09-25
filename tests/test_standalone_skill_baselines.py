from __future__ import annotations

import json
import re
import sys
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from skill_utils import read_frontmatter  # noqa: E402


STANDALONE_SKILLS = {
    "project-thread-handoff": {
        "path": Path("skills/science/communication/project-thread-handoff"),
        "display": "Project Thread Handoff",
        "icon": Path("assets/app-facing.svg"),
    },
    "render-chinese-math-pdf": {
        "path": Path("skills/tools/documents-media/render-chinese-math-pdf"),
        "display": "Chinese Math PDF",
        "icon": Path("assets/app-facing.svg"),
    },
    "slurm-workflows": {
        "path": Path("skills/tools/hpc/slurm-workflows"),
        "display": "Slurm Workflows",
        "icon": Path("assets/slurm-workflows.svg"),
    },
}

EXPECTED_PLUGIN_VERSIONS = {
    "workflow-core": "0.4",
    "ai-skills-core": "0.5",
    "writing-style": "0.3",
    "research-writing": "0.2",
    "presentations": "0.3",
    "scientific-visualization": "0.1",
    "web-development": "0.2",
    "statistical-modeling": "0.1",
    "bioinformatics": "0.1",
    "medical-imaging": "0.1",
}


class StandaloneSkillBaselineTests(unittest.TestCase):
    def test_standalone_skills_have_v01_metadata_and_icons(self) -> None:
        for slug, info in STANDALONE_SKILLS.items():
            skill_dir = REPO_ROOT / info["path"]
            meta, _ = read_frontmatter(skill_dir / "SKILL.md")

            self.assertEqual(meta.get("name"), slug)
            self.assertEqual(meta.get("version"), "0.1")
            self.assertEqual(meta.get("icon_small"), info["icon"].as_posix())
            self.assertEqual(meta.get("icon_large"), info["icon"].as_posix())

            icon_path = skill_dir / info["icon"]
            self.assertTrue(icon_path.exists(), icon_path)
            root = ET.parse(icon_path).getroot()
            self.assertEqual(root.tag.rsplit("}", 1)[-1], "svg")
            self.assertEqual(root.attrib.get("viewBox"), "0 0 64 64")

    def test_readme_versions_match_skill_metadata(self) -> None:
        readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("Standalone Skills", readme)
        self.assertIn("不是中央 Marketplace Plugins", readme)

        for slug, info in STANDALONE_SKILLS.items():
            meta, _ = read_frontmatter(REPO_ROOT / info["path"] / "SKILL.md")
            self.assertIn(info["display"], readme)
            self.assertIn(f"<code>{slug}</code> · v`{meta['version']}`", readme)

    def test_standalone_skills_stay_out_of_central_marketplace_topology(self) -> None:
        config = json.loads((REPO_ROOT / "scripts" / "codex_marketplace_config.json").read_text(encoding="utf-8"))
        serialized = json.dumps(config)

        self.assertEqual({plugin["name"]: plugin["version"] for plugin in config["plugins"]}, EXPECTED_PLUGIN_VERSIONS)
        for info in STANDALONE_SKILLS.values():
            self.assertNotIn(info["path"].as_posix(), serialized)

    def test_repository_version_and_contact_sheet_are_stable(self) -> None:
        self.assertEqual((REPO_ROOT / "VERSION").read_text(encoding="utf-8").strip(), "5.2.1")

        sheet = (REPO_ROOT / "docs" / "audits" / "ICON_CONTACT_SHEET.svg").read_text(encoding="utf-8")
        for slug, info in STANDALONE_SKILLS.items():
            self.assertIn((info["path"] / info["icon"]).as_posix(), sheet)
            self.assertRegex(sheet, rf">{re.escape(slug)}<")
        for plugin in ["workflow-core", "ai-skills-core", "writing-style", "presentations"]:
            self.assertIn(f"assets/codex/plugin-icons/{plugin}/composer.svg", sheet)


if __name__ == "__main__":
    unittest.main()
