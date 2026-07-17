from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
PROBE_PATH = REPO_ROOT / "skills/tools/documents-media/render-chinese-math-pdf/scripts/probe_pdf_render_env.py"
QA_PATH = REPO_ROOT / "skills/tools/documents-media/render-chinese-math-pdf/scripts/validate_pdf_layout.py"


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


probe = load_module(PROBE_PATH, "probe_pdf_render_env")
qa = load_module(QA_PATH, "validate_pdf_layout")


class RenderChineseMathPdfTests(unittest.TestCase):
    def test_resource_bundle_reports_usable_local_texmf(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            bundle = root / "render_resources/chinese_math_pdf"
            (bundle / "texmf/tex/xelatex/xecjk").mkdir(parents=True)
            (bundle / "texmf/tex/latex/ctex").mkdir(parents=True)
            (bundle / "texmf/fonts/opentype/public/fandol").mkdir(parents=True)
            (bundle / "texmf/tex/xelatex/xecjk/xeCJK.sty").write_text("", encoding="utf-8")
            (bundle / "texmf/tex/latex/ctex/ctexart.cls").write_text("", encoding="utf-8")
            (bundle / "texmf/fonts/opentype/public/fandol/FandolSong-Regular.otf").write_text("", encoding="utf-8")
            bundles = probe.find_project_resource_bundles(root / "project")
        matching = [item for item in bundles if item["path"] == str(bundle)]
        self.assertEqual(len(matching), 1)
        self.assertTrue(matching[0]["usable_chinese_math_bundle"])
        self.assertTrue(matching[0]["tex_files"]["xeCJK.sty"].endswith("xeCJK.sty"))

    def test_cjk_fragmentation_flags_excessive_short_lines(self) -> None:
        fragmented = "\n".join(["中", "文", "测", "试", "数", "学", "表", "格", "正常 English"])
        result = qa.validate_text(fragmented)
        self.assertIn("abnormal CJK line fragmentation detected", result["errors"])

    def test_markdown_table_survival_flags_collapsed_table(self) -> None:
        source = "| 指标 | 数值 |\n| --- | --- |\n| 左室容积 | 120 mL |\n| 射血分数 | 55% |\n"
        extracted = "指标\n数值\n左室容积\n120 mL\n射血分数\n55%\n"
        result = qa.validate_text(extracted, source)
        self.assertIn("Markdown table rows did not survive in extracted PDF layout text", result["errors"])

    def test_markdown_table_survival_accepts_layout_rows(self) -> None:
        source = "| 指标 | 数值 |\n| --- | --- |\n| 左室容积 | 120 mL |\n"
        extracted = "指标        数值\n左室容积    120 mL\n"
        result = qa.validate_text(extracted, source)
        self.assertNotIn("Markdown table rows did not survive in extracted PDF layout text", result["errors"])


if __name__ == "__main__":
    unittest.main()
