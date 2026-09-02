from __future__ import annotations

import hashlib
import importlib.util
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

REPO_ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = REPO_ROOT / "skills/tools/documents-media/render-chinese-math-pdf"
PROBE_PATH = SKILL_ROOT / "scripts/probe_pdf_render_env.py"
QA_PATH = SKILL_ROOT / "scripts/validate_pdf_layout.py"
HEADER_PATH = SKILL_ROOT / "scripts/build_chinese_math_header.py"
SKILLS_CLI_PATH = REPO_ROOT / "scripts/skills.py"


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


probe = load_module(PROBE_PATH, "probe_pdf_render_env")
qa = load_module(QA_PATH, "validate_pdf_layout")
header_builder = load_module(HEADER_PATH, "build_chinese_math_header")


class RenderChineseMathPdfTests(unittest.TestCase):
    def make_resource(self, root: Path) -> Path:
        resource = root / "render_resources/chinese_math_pdf"
        (resource / "scripts").mkdir(parents=True)
        (resource / "templates").mkdir(parents=True)
        (resource / "fonts/texgyre-termes").mkdir(parents=True)
        (resource / "fonts/texgyre-termes-math").mkdir(parents=True)
        (resource / "texmf/fonts/opentype/public/noto-cjk").mkdir(parents=True)
        (resource / "scripts/render_markdown_pdf.sh").write_text("#!/usr/bin/env bash\n", encoding="utf-8")
        (resource / "templates/chinese_math_pandoc_header.tex.in").write_text("% header\n", encoding="utf-8")
        for rel in probe.FONT_FILES.values():
            (resource / rel).write_text("font", encoding="utf-8")
        return resource

    def test_reusable_source_contains_no_private_resource_paths(self) -> None:
        forbidden = [
            "/" + "home/yuukias/render_resources/chinese_math_pdf",
            "/" + "overflow/htzhu/mingcheng_new/render_resources/chinese_math_pdf",
            "/" + "users/a/e/aereinh/render_resources/chinese_math_pdf",
            "/" + "mnt/c/Windows/Fonts",
            "fc-match " + '"Times New Roman"',
        ]
        offenders: list[str] = []
        for path in [*SKILL_ROOT.rglob("*.md"), *SKILL_ROOT.rglob("*.py")]:
            if "__pycache__" in path.parts:
                continue
            text = path.read_text(encoding="utf-8")
            for bad in forbidden:
                if bad in text:
                    offenders.append(str(path.relative_to(REPO_ROOT)))
                    break
        self.assertEqual([], offenders)

    def test_project_local_resource_precedes_environment_and_overrides(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            project_resource = self.make_resource(root / "project")
            env_resource = self.make_resource(root / "env")
            namespace = root / "namespace"
            override_resource = self.make_resource(root / "override")
            override = namespace / probe.OVERRIDE_REL
            override.parent.mkdir(parents=True)
            override.write_text(f'[sites.local]\nrender_resource_dirs = "{override_resource}"\n', encoding="utf-8")

            with mock.patch.dict(
                probe.os.environ,
                {
                    "CHINESE_MATH_PDF_RESOURCE_DIRS": str(env_resource),
                    "CODEX_NAMESPACE_ROOT": str(namespace),
                    "HOME": str(root / "home"),
                },
                clear=False,
            ):
                found = probe.find_resource(root / "project")

        self.assertEqual(project_resource.resolve(), found)

    def test_environment_precedes_namespace_override(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            env_resource = self.make_resource(root / "env")
            namespace = root / "namespace"
            override_resource = self.make_resource(root / "override")
            override = namespace / probe.OVERRIDE_REL
            override.parent.mkdir(parents=True)
            override.write_text(f'[sites.local]\nrender_resource_dirs = "{override_resource}"\n', encoding="utf-8")

            with mock.patch.dict(
                probe.os.environ,
                {"CHINESE_MATH_PDF_RESOURCE_DIRS": str(env_resource), "CODEX_NAMESPACE_ROOT": str(namespace)},
                clear=False,
            ):
                found = probe.find_resource(root / "no-project-resource")

        self.assertEqual(env_resource.resolve(), found)

    def test_same_canonical_probe_reads_different_namespace_overrides(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            ns_a = root / "namespace-a"
            ns_b = root / "namespace-b"
            resource_a = self.make_resource(root / "resource-a")
            resource_b = self.make_resource(root / "resource-b")
            for namespace, resource in [(ns_a, resource_a), (ns_b, resource_b)]:
                override = namespace / probe.OVERRIDE_REL
                override.parent.mkdir(parents=True)
                override.write_text(f'[sites.local]\nrender_resource_dirs = "{resource}"\n', encoding="utf-8")

            with mock.patch.dict(probe.os.environ, {"CODEX_NAMESPACE_ROOT": str(ns_a)}, clear=True):
                found_a = probe.find_resource(root / "missing-a")
            with mock.patch.dict(probe.os.environ, {"CODEX_NAMESPACE_ROOT": str(ns_b)}, clear=True):
                found_b = probe.find_resource(root / "missing-b")

        self.assertEqual(resource_a.resolve(), found_a)
        self.assertEqual(resource_b.resolve(), found_b)

    def test_explicit_local_override_is_read(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            resource = self.make_resource(root / "resource")
            override = root / "custom-local-overrides.toml"
            override.write_text(f'[sites.local]\nrender_resource_dirs = "{resource}"\n', encoding="utf-8")
            self.assertEqual(resource.resolve(), probe.find_resource(root / "missing", local_override=override))

    def test_header_uses_bundle_local_texgyre_and_noto_files(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            resource = self.make_resource(root / "project")
            args = type("Args", (), {"root": root / "project", "resource_dir": None, "local_override": None})()
            header = header_builder.build_header(args)

        self.assertIn(resource.as_posix() + "/fonts/texgyre-termes/", header)
        self.assertIn("texgyretermes-math", header)
        self.assertIn("NotoSerifSC-Regular", header)
        self.assertIn("NotoSansSC-Bold", header)
        self.assertNotIn("Fandol", header)

    def test_probe_policy_is_xelatex_without_chromium_fallback(self) -> None:
        flags = probe.policy_flags()
        self.assertEqual("pandoc_xelatex", probe.DEFAULT_RENDERER)
        self.assertFalse(flags["chromium_latex_fallback"])

    def test_missing_xelatex_reports_dependency_failure_not_chromium(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.make_resource(root / "project")
            args = type("Args", (), {"root": root / "project", "resource_dir": None, "local_override": None})()

            def fake_run(cmd: list[str], env=None):
                if cmd[0] == "xelatex":
                    return {"available": False, "path": None, "first_line": None}
                if cmd[0] == "kpsewhich":
                    return {"available": False, "path": None, "first_line": None}
                return {"available": True, "path": "/usr/bin/" + cmd[0], "first_line": "ok"}

            with mock.patch.object(probe, "run", side_effect=fake_run):
                result = probe.build_probe_result(args)

        self.assertFalse(result["ready"])
        self.assertEqual("blocked_missing_dependency", result["failure_status"])
        self.assertFalse(result["forbidden_default_dependencies"]["chromium_latex_fallback"])

    def test_managed_copy_install_matches_canonical_source(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            env = os.environ.copy()
            env["CODEX_HOME"] = tmp
            proc = subprocess.run(
                [
                    sys.executable,
                    str(REPO_ROOT / "scripts/skills.py"),
                    "install",
                    "--target",
                    "codex-home",
                    "--skill",
                    "tools/documents-media/render-chinese-math-pdf",
                    "--mode",
                    "copy",
                    "--yes",
                    "--json",
                ],
                cwd=REPO_ROOT,
                env=env,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                timeout=30,
            )
            self.assertEqual(proc.returncode, 0, proc.stderr + proc.stdout)
            deployed = Path(tmp) / "skills/tools-documents-media-render-chinese-math-pdf/SKILL.md"
            self.assertTrue(deployed.exists())
            self.assertEqual(digest(SKILL_ROOT / "SKILL.md"), digest(deployed))

    def test_managed_install_does_not_modify_local_override(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            codex_home = root / "codex-home"
            override = root / ".config/ai-skills/local-overrides.toml"
            override.parent.mkdir(parents=True)
            override.write_text('[sites.local]\nrender_resource_dirs = "/example/resource"\n', encoding="utf-8")
            before = digest(override)
            env = os.environ.copy()
            env["CODEX_HOME"] = str(codex_home)
            env["CODEX_NAMESPACE_ROOT"] = str(root)

            proc = subprocess.run(
                [
                    sys.executable,
                    str(REPO_ROOT / "scripts/skills.py"),
                    "install",
                    "--target",
                    "codex-home",
                    "--skill",
                    "tools/documents-media/render-chinese-math-pdf",
                    "--mode",
                    "copy",
                    "--yes",
                    "--json",
                ],
                cwd=REPO_ROOT,
                env=env,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                timeout=30,
            )
            self.assertEqual(proc.returncode, 0, proc.stderr + proc.stdout)
            self.assertEqual(before, digest(override))

    def test_update_keeps_nas_scan_guard_but_allows_explicit_manifest(self) -> None:
        source = SKILLS_CLI_PATH.read_text(encoding="utf-8")
        self.assertIn("refusing to scan /nas path", source)
        self.assertNotIn("refusing to update /nas manifest", source)
        self.assertNotIn("refusing to update manifest with /nas skills_root", source)

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

    def test_cjk_fragmentation_flags_excessive_short_lines(self) -> None:
        fragmented = "\n".join(["中", "文", "测", "试", "数", "学", "表", "格", "正常 English"])
        result = qa.validate_text(fragmented)
        self.assertIn("abnormal CJK line fragmentation detected", result["errors"])

    def test_markdown_table_survival_accepts_layout_rows(self) -> None:
        source = "| 指标 | 数值 |\n| --- | --- |\n| 左室容积 | 120 mL |\n"
        extracted = "指标        数值\n左室容积    120 mL\n"
        result = qa.validate_text(extracted, source)
        self.assertNotIn("Markdown table rows did not survive in extracted PDF layout text", result["errors"])


if __name__ == "__main__":
    unittest.main()
