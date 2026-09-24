from __future__ import annotations

import hashlib
import json
import re
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]

TARGET_ICONS = {
    "workflow-core": Path("assets/codex/plugin-icons/workflow-core/composer.svg"),
    "ai-skills-core": Path("assets/codex/plugin-icons/ai-skills-core/composer.svg"),
}

UNCHANGED_ICON_SHA256 = {
    "writing-style": "ddd7a6edee8baaae8a5a6212c754fe501e61e5cb0754f522b175127f11f2923a",
    "research-writing": "773b5b9d34c84c330274567ad2c16fecce32b4efd8d80415e4649aa6ebb13c00",
    "presentations": "7d5be5041991117fdad0ddb55a2cfb586c66d4080a0459fd5e54b153476ddc56",
    "web-development": "543f95478e439bf87e1faf59d1b5eae02871058eac1d07a74ca9a862245a90fd",
    "statistical-modeling": "22853e8681b4a8d0ce419200a4daf8b982399a8cbb54bdad7b806b6be4d84228",
    "scientific-visualization": "050c3bc2e40c41e95b639ddaea4686c31e86916fb54faf4d106d354a02aac8d4",
    "bioinformatics": "d69ea796cda5a4f58433e6377c64325bb93de74fe2c149bf87cdfc905449ad48",
    "medical-imaging": "be41dbfa376a47969786a787bde7815b6fc87977d5779c0b3a185ae9b69c999b",
}


class CentralPluginIconAssetTests(unittest.TestCase):
    def test_marketplace_keeps_canonical_icon_paths_and_versions(self) -> None:
        config = json.loads((REPO_ROOT / "scripts" / "codex_marketplace_config.json").read_text(encoding="utf-8"))
        plugins = {plugin["name"]: plugin for plugin in config["plugins"]}

        self.assertEqual((REPO_ROOT / "VERSION").read_text(encoding="utf-8").strip(), "5.1.1")
        self.assertEqual(plugins["workflow-core"]["version"], "0.4")
        self.assertEqual(plugins["ai-skills-core"]["version"], "0.4")
        for slug, path in TARGET_ICONS.items():
            canonical = f"./{path.as_posix()}"
            self.assertEqual(plugins[slug]["composerIcon"], canonical)
            self.assertEqual(plugins[slug]["logo"], canonical)

    def test_target_svgs_are_self_contained_64px_icons(self) -> None:
        for path in TARGET_ICONS.values():
            icon = REPO_ROOT / path
            root = ET.parse(icon).getroot()
            raw = icon.read_text(encoding="utf-8")

            self.assertEqual(root.tag.rsplit("}", 1)[-1], "svg")
            self.assertEqual(root.attrib.get("viewBox"), "0 0 64 64")
            self.assertNotIn("<text", raw)
            self.assertNotIn("<image", raw)
            self.assertNotIn("href=", raw)
            self.assertNotIn("font", raw)

    def test_readme_and_contact_sheet_reference_target_icons(self) -> None:
        readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
        sheet = (REPO_ROOT / "docs" / "audits" / "ICON_CONTACT_SHEET.svg").read_text(encoding="utf-8")

        for path in TARGET_ICONS.values():
            readme_path = f"./{path.as_posix()}"
            sheet_path = f"../../{path.as_posix()}"
            self.assertIn(readme_path, readme)
            self.assertRegex(sheet, rf'href="{re.escape(sheet_path)}"[^>]*width="56"')
            self.assertRegex(sheet, rf'href="{re.escape(sheet_path)}"[^>]*width="40"')

    def test_other_central_plugin_icons_are_unchanged(self) -> None:
        for slug, expected in UNCHANGED_ICON_SHA256.items():
            path = REPO_ROOT / "assets" / "codex" / "plugin-icons" / slug / "composer.svg"
            self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), expected, slug)


if __name__ == "__main__":
    unittest.main()
