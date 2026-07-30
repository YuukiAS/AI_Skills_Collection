from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path
from unittest import mock

REPO_ROOT = Path(__file__).resolve().parents[1]
PROBE_PATH = REPO_ROOT / "skills/tools/documents-media/render-chinese-math-pdf/scripts/probe_pdf_render_env.py"
QA_PATH = REPO_ROOT / "skills/tools/documents-media/render-chinese-math-pdf/scripts/validate_pdf_layout.py"
RENDER_CHROMIUM_PATH = REPO_ROOT / "skills/tools/documents-media/render-chinese-math-pdf/scripts/render_markdown_pdf_chromium.py"
HEADER_PATH = REPO_ROOT / "skills/tools/documents-media/render-chinese-math-pdf/scripts/build_chinese_math_header.py"


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


probe = load_module(PROBE_PATH, "probe_pdf_render_env")
qa = load_module(QA_PATH, "validate_pdf_layout")
render_chromium = load_module(RENDER_CHROMIUM_PATH, "render_markdown_pdf_chromium")
header_builder = load_module(HEADER_PATH, "build_chinese_math_header")


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


    def test_resource_bundle_detected_from_shared_roots(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            shared = root / "shared/chinese_math_pdf"
            (shared / "texmf/tex/xelatex/xecjk").mkdir(parents=True)
            (shared / "texmf/tex/latex/ctex").mkdir(parents=True)
            (shared / "texmf/fonts/opentype/public/fandol").mkdir(parents=True)
            (shared / "texmf/tex/xelatex/xecjk/xeCJK.sty").write_text("", encoding="utf-8")
            (shared / "texmf/tex/latex/ctex/ctexart.cls").write_text("", encoding="utf-8")
            (shared / "texmf/fonts/opentype/public/fandol/FandolSong-Regular.otf").write_text("", encoding="utf-8")
            with mock.patch.object(probe, "SHARED_RESOURCE_ROOTS", [shared]):
                bundles = probe.find_project_resource_bundles(root / "project")
        self.assertTrue(any(item["path"] == str(shared) for item in bundles))



    def test_resource_bundle_detected_from_local_override(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            override_root = root / "override/chinese_math_pdf"
            (override_root / "texmf/tex/xelatex/xecjk").mkdir(parents=True)
            (override_root / "texmf/tex/latex/ctex").mkdir(parents=True)
            (override_root / "texmf/fonts/opentype/public/fandol").mkdir(parents=True)
            (override_root / "texmf/tex/xelatex/xecjk/xeCJK.sty").write_text("", encoding="utf-8")
            (override_root / "texmf/tex/latex/ctex/ctexart.cls").write_text("", encoding="utf-8")
            (override_root / "texmf/fonts/opentype/public/fandol/FandolSong-Regular.otf").write_text("", encoding="utf-8")
            override = root / "local-overrides.toml"
            override.write_text(f'[sites.local]\nrender_resource_dirs = "{override_root}"\n', encoding="utf-8")
            bundles = probe.find_project_resource_bundles(root / "project", local_override=override)
        self.assertTrue(any(item["path"] == str(override_root) for item in bundles))

    def test_resource_bundle_detected_from_environment_variable(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            env_root = root / "env/chinese_math_pdf"
            (env_root / "texmf/tex/xelatex/xecjk").mkdir(parents=True)
            (env_root / "texmf/tex/latex/ctex").mkdir(parents=True)
            (env_root / "texmf/fonts/opentype/public/fandol").mkdir(parents=True)
            (env_root / "texmf/tex/xelatex/xecjk/xeCJK.sty").write_text("", encoding="utf-8")
            (env_root / "texmf/tex/latex/ctex/ctexart.cls").write_text("", encoding="utf-8")
            (env_root / "texmf/fonts/opentype/public/fandol/FandolSong-Regular.otf").write_text("", encoding="utf-8")
            with mock.patch.dict(probe.os.environ, {"CHINESE_MATH_PDF_RESOURCE_DIRS": str(env_root)}):
                bundles = probe.find_project_resource_bundles(root / "project")
        self.assertTrue(any(item["path"] == str(env_root) for item in bundles))

    def test_fontconfig_rejects_fallback_family(self) -> None:
        class Proc:
            returncode = 0
            stdout = "/usr/share/fonts/dejavu/DejaVuSans.ttf\tDejaVu Sans\n"
            stderr = ""

        with mock.patch.object(probe.shutil, "which", return_value="/usr/bin/fc-match"), mock.patch.object(
            probe.subprocess, "run", return_value=Proc()
        ):
            info = probe.fontconfig_match("Noto Serif CJK SC")
        self.assertFalse(info["available"])
        self.assertIn("fallback family", info["reason"])

    def test_chromium_css_embeds_resource_fonts(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            font_dir = root / "texmf/fonts/opentype/public/fandol"
            font_dir.mkdir(parents=True)
            (font_dir / "FandolSong-Regular.otf").write_text("font", encoding="utf-8")
            css = render_chromium.css_text(root)
        self.assertIn("FandolSongLocal", css)
        self.assertIn("@font-face", css)

    def test_validate_pdf_defaults_preview_dir(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            pdf = Path(tmp) / "out.pdf"
            pdf.write_bytes(b"%PDF-1.4\n%fake\n")

            def fake_run(args: list[str], timeout: int = 30):
                if args[0] == "pdfinfo":
                    return 0, "Pages: 1\n"
                if args[0] == "pdffonts":
                    return 0, "name type encoding emb sub uni object ID\nFake TrueType yes yes yes 1 0\n"
                if args[0] == "pdftotext":
                    Path(args[-1]).write_text("中文测试内容足够长，表格和公式上下文正常。", encoding="utf-8")
                    return 0, ""
                if args[0] == "pdftoppm":
                    prefix = Path(args[-1])
                    prefix.parent.mkdir(parents=True, exist_ok=True)
                    (prefix.parent / f"{prefix.name}-1.png").write_bytes(b"png")
                    return 0, ""
                raise AssertionError(args)

            with mock.patch.object(qa, "run_command", side_effect=fake_run):
                result = qa.validate_pdf(pdf)
        self.assertFalse(result["errors"])
        self.assertTrue(result["preview_paths"][0].endswith("out-1.png"))

    def test_validate_pdf_rejects_cjk_font_without_unicode_mapping(self) -> None:
        pdffonts = (
            "name type encoding emb sub uni object ID\n"
            "FandolSong-Regular CID Type 0C Identity-H yes yes no 9 0\n"
        )
        result = qa.validate_font_compatibility(pdffonts, "中文测试内容")
        self.assertIn("CJK font(s) lack ToUnicode mapping", result["errors"][0])

    def test_header_prefers_system_cjk_font_over_resource_fandol(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            resource = root / "render_resources/chinese_math_pdf/texmf/fonts/opentype/public/fandol"
            resource.mkdir(parents=True)
            (resource / "FandolSong-Regular.otf").write_text("font", encoding="utf-8")
            system_font = root / "fonts/DroidSansFallbackFull.ttf"
            system_font.parent.mkdir(parents=True)
            system_font.write_text("font", encoding="utf-8")

            def fake_fc_match(font_name: str):
                return system_font if font_name == "Droid Sans Fallback" else None

            args = type(
                "Args",
                (),
                {
                    "root": root,
                    "resource_dir": root / "render_resources/chinese_math_pdf",
                    "cjk_font": "Noto Serif CJK SC",
                    "main_font": "TeX Gyre Termes",
                    "mono_font": "TeX Gyre Cursor",
                    "prefer_resource_cjk": False,
                },
            )()

            with mock.patch.object(header_builder, "fc_match_font", side_effect=fake_fc_match):
                header = header_builder.build_header(args)

        self.assertIn("DroidSansFallbackFull.ttf", header)
        self.assertNotIn("FandolSong-Regular.otf", header)

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
