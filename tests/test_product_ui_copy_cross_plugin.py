from __future__ import annotations

import json
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


class ProductUiCopyCrossPluginTests(unittest.TestCase):
    def test_product_ui_copy_skill_defines_protected_handoff_and_boundaries(self) -> None:
        text = (REPO_ROOT / "skills/writing/core/product-ui-copy/SKILL.md").read_text(encoding="utf-8")

        for field in [
            "SURFACE",
            "UI_ROLE",
            "PRODUCT_STATE",
            "USER_CONSEQUENCE_OR_NEXT_ACTION",
            "NEIGHBORING_VISIBLE_COPY",
            "LOCALE",
            "PROTECTED_MEANING",
            "DISCLOSURE_LEVEL",
            "LENGTH_OR_VIEWPORT_CONSTRAINT",
        ]:
            self.assertIn(field, text)

        for decision in [
            "KEEP",
            "WORDING/NATURALNESS",
            "LOCALE/REGISTER",
            "CONTENT ARCHITECTURE",
            "PRODUCT SEMANTICS",
            "LEGAL/TRUST/SAFETY",
        ]:
            self.assertIn(decision, text)

        self.assertIn("zh-Hans", text)
        self.assertIn("zh-Hant-HK", text)
        self.assertIn("Character conversion alone is not localization", text)
        self.assertIn("Do not turn this handoff into a schema", text)

    def test_chinese_prose_frontmatter_routes_ui_microcopy_away(self) -> None:
        text = (REPO_ROOT / "skills/writing/core/chinese-prose/SKILL.md").read_text(encoding="utf-8")
        frontmatter = text.split("---", 2)[1]

        self.assertIn("文档型中文内容", frontmatter)
        self.assertIn("product-ui-copy", frontmatter)
        self.assertIn("UI microcopy", frontmatter)
        self.assertIn("报告、README", frontmatter)
        self.assertIn("不要因为文本是中文就留在 `chinese-prose`", text)

    def test_writing_fidelity_protects_product_ui_semantics(self) -> None:
        text = (REPO_ROOT / "skills/writing/core/writing-fidelity/SKILL.md").read_text(encoding="utf-8")

        self.assertIn("Use `product-ui-copy`", text)
        self.assertIn("Product UI Copy Handoff", text)
        self.assertIn("PRODUCT SEMANTICS", text)
        self.assertIn("LEGAL/TRUST/SAFETY", text)
        self.assertIn("Do not launder uncertainty into polished copy", text)
        self.assertIn("Frontend Design owns content architecture", text)

    def test_frontend_design_exposes_product_interface_handoff_and_negatives(self) -> None:
        coordinator = (REPO_ROOT / "skills/tools/frontend/frontend-visual-systems/SKILL.md").read_text(
            encoding="utf-8"
        )
        ux = (REPO_ROOT / "skills/tools/frontend/product-ux-planning/SKILL.md").read_text(encoding="utf-8")
        responsive = (REPO_ROOT / "skills/tools/frontend/responsive-accessibility-review/SKILL.md").read_text(
            encoding="utf-8"
        )

        for surface in ["browser extension", "Tauri", "Electron", "native-WebView", "Android", "Compose"]:
            self.assertIn(surface, coordinator)

        self.assertIn("Send that handoff to Clear Writing `product-ui-copy`", coordinator)
        self.assertIn("backend/API/math tasks", coordinator)
        self.assertIn("Room/WorkManager/data-layer changes", coordinator)
        self.assertIn("local platform authority intact", coordinator)

        self.assertIn("Product surfaces include browser extensions", ux)
        self.assertIn("PRODUCT_STATE", ux)
        self.assertIn("Escalate missing product/legal/trust facts", ux)

        self.assertIn("Product UI Copy is validated in the rendered surface", responsive)
        self.assertIn("Do not claim native desktop/mobile runtime behavior", responsive)
        self.assertIn("browser-only", responsive)

    def test_marketplace_source_exposes_product_ui_copy_without_version_bump(self) -> None:
        config = json.loads((REPO_ROOT / "scripts/codex_marketplace_config.json").read_text(encoding="utf-8"))
        plugins = {plugin["name"]: plugin for plugin in config["plugins"]}

        writing = plugins["writing-style"]
        self.assertEqual(writing["version"], "0.3")
        self.assertIn("Product UI Copy", writing["description"])
        writing_sources = {skill["artifact_id"]: skill["source"] for skill in writing["skills"]}
        self.assertEqual(writing_sources["product-ui-copy"], "skills/writing/core/product-ui-copy")

        frontend = plugins["web-development"]
        self.assertEqual(frontend["version"], "0.3")
        self.assertIn("browser extension", frontend["description"])
        self.assertIn("Product UI Copy handoff", frontend["skills"][1]["description"])

    def test_product_ui_copy_trigger_evals_cover_positive_near_miss_and_negative(self) -> None:
        data = json.loads(
            (REPO_ROOT / "skills/writing/core/product-ui-copy/evals/trigger_queries.json").read_text(
                encoding="utf-8"
            )
        )

        self.assertIn("positive", data)
        self.assertIn("indirect", data)
        self.assertIn("near_miss", data)
        self.assertIn("negative", data)
        self.assertTrue(any("浏览器插件 popup" in item for item in data["positive"]))
        self.assertTrue(any("README" in item for item in data["near_miss"]))
        self.assertTrue(any("WorkManager" in item for item in data["negative"]))


if __name__ == "__main__":
    unittest.main()
