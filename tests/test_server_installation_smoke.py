from __future__ import annotations

import argparse
import json
import os
import shutil
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import verify_server_installation as smoke  # noqa: E402


class ServerInstallationSmokeTests(unittest.TestCase):
    def test_default_smoke_installs_server_profile_into_temporary_codex_home(self) -> None:
        args = argparse.Namespace(
            profile=[],
            domain=[],
            category=[],
            skill=[],
            mode="copy",
            codex_home=None,
            allow_real_home=False,
            keep=False,
            json=True,
        )
        report = smoke.build_report(args)
        self.assertTrue(report["ok"], report)
        self.assertEqual(report["selection"]["profiles"], ["server-research-baseline"])
        self.assertGreater(report["installed_skill_count"], 0)
        self.assertEqual(Path(report["manifest_path"]).name, smoke.MANIFEST_NAME)

    def test_refuses_current_codex_home_without_explicit_allow(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            previous = os.environ.get("CODEX_HOME")
            os.environ["CODEX_HOME"] = tmp
            try:
                with self.assertRaises(SystemExit):
                    with smoke.temporary_codex_home(tmp, allow_real_home=False, keep=False):
                        pass
            finally:
                if previous is None:
                    os.environ.pop("CODEX_HOME", None)
                else:
                    os.environ["CODEX_HOME"] = previous

    def test_marketplace_payload_paths_are_valid(self) -> None:
        checks: list[dict] = []
        errors = smoke.validate_marketplace_payload(checks)
        self.assertEqual(errors, [])
        self.assertTrue(all(check["ok"] for check in checks))

    def test_presentation_desktop_smoke_installs_required_support_skills(self) -> None:
        args = argparse.Namespace(
            profile=["presentation-desktop"],
            domain=[],
            category=[],
            skill=[],
            mode="copy",
            codex_home=None,
            allow_real_home=False,
            keep=True,
            json=True,
        )
        report = smoke.build_report(args)
        try:
            self.assertTrue(report["ok"], report)
            self.assertEqual(report["installed_skill_count"], 7)
            manifest = json.loads(Path(report["manifest_path"]).read_text(encoding="utf-8"))
            installed_paths = {item["path"] for item in manifest["installed_skills"]}
            self.assertIn("skills/tools/documents-media/render-chinese-math-pdf", installed_paths)
            self.assertIn("skills/writing/research/citation-verification", installed_paths)
        finally:
            shutil.rmtree(report["codex_home"], ignore_errors=True)

    def test_json_report_is_serializable(self) -> None:
        args = argparse.Namespace(
            profile=["global-baseline"],
            domain=[],
            category=[],
            skill=[],
            mode="copy",
            codex_home=None,
            allow_real_home=False,
            keep=False,
            json=True,
        )
        report = smoke.build_report(args)
        json.dumps(report, ensure_ascii=False)
        self.assertTrue(report["ok"], report)


if __name__ == "__main__":
    unittest.main()
