from __future__ import annotations

import hashlib
import json
import re
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]

TARGET_ICONS = {
    "presentations": Path("assets/codex/plugin-icons/presentations/composer.svg"),
    "scientific-visualization": Path("assets/codex/plugin-icons/scientific-visualization/composer.svg"),
    "web-development": Path("assets/codex/plugin-icons/web-development/composer.svg"),
    "statistical-modeling": Path("assets/codex/plugin-icons/statistical-modeling/composer.svg"),
    "medical-imaging": Path("assets/codex/plugin-icons/medical-imaging/composer.svg"),
}

TARGET_PLUGIN_VERSIONS = {
    "presentations": "0.3",
    "scientific-visualization": "0.1",
    "web-development": "0.2",
    "statistical-modeling": "0.1",
    "medical-imaging": "0.1",
}

PROTECTED_REFERENCE_ICON_SHA256 = {
    "ai-skills-core": "f00921b5fa304780870501dfe6dead055bf22d4814a578cb62693d53fddb6ea4",
    "presentations": "6bc8ccfe0025d00207610b9f96f50e385afd305634d2681d1d11cf937ae43c94",
    "scientific-visualization": "2f08f6e84d6e449a04c7574351d308c5a4e7dba9f5d67b894f4df84f618fb8df",
    "web-development": "9aef902b4ce9dc8dafa2f7a6eb42e136bc54d016efe41af6446de664b15ca682",
    "workflow-core": "43fa29d8afd649a5f585d4b99f69df7495dd6826e88412beff64dd0d1ac0ccde",
}

UNCHANGED_ICON_SHA256 = {
    "writing-style": "ddd7a6edee8baaae8a5a6212c754fe501e61e5cb0754f522b175127f11f2923a",
    "research-writing": "773b5b9d34c84c330274567ad2c16fecce32b4efd8d80415e4649aa6ebb13c00",
    "bioinformatics": "d69ea796cda5a4f58433e6377c64325bb93de74fe2c149bf87cdfc905449ad48",
}


class CentralPluginIconAssetTests(unittest.TestCase):
    def test_marketplace_keeps_canonical_icon_paths_and_versions(self) -> None:
        config = json.loads((REPO_ROOT / "scripts" / "codex_marketplace_config.json").read_text(encoding="utf-8"))
        plugins = {plugin["name"]: plugin for plugin in config["plugins"]}

        self.assertEqual((REPO_ROOT / "VERSION").read_text(encoding="utf-8").strip(), "5.3.0")
        for slug, version in TARGET_PLUGIN_VERSIONS.items():
            self.assertEqual(plugins[slug]["version"], version)
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
        for slug, expected in (PROTECTED_REFERENCE_ICON_SHA256 | UNCHANGED_ICON_SHA256).items():
            path = REPO_ROOT / "assets" / "codex" / "plugin-icons" / slug / "composer.svg"
            self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), expected, slug)


if __name__ == "__main__":
    unittest.main()
