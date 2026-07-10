from __future__ import annotations

import argparse
import json
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import skills  # noqa: E402


class SkillUpdateTests(unittest.TestCase):
    def test_install_request_round_trip_uses_manifest_field(self) -> None:
        request, warnings = skills.request_from_manifest(
            {
                "install_request": {
                    "profiles": ["codex-core-global"],
                    "domains": ["medical-imaging"],
                    "categories": [],
                    "skills": ["writing/core/chinese-prose"],
                }
            }
        )
        self.assertEqual(warnings, [])
        self.assertEqual(request["profiles"], ["codex-core-global"])
        self.assertEqual(request["domains"], ["medical-imaging"])
        self.assertEqual(request["skills"], ["writing/core/chinese-prose"])

    def test_legacy_manifest_reconstructs_from_install_kind(self) -> None:
        request, warnings = skills.request_from_manifest(
            {
                "install_kind": "mixed:profile:codex-workflow-core+domain:medical-imaging+skills",
                "installed_skills": [
                    {"path": "skills/writing/core/chinese-prose"},
                    {"path": "skills/tools/documents-media/render-chinese-math-pdf"},
                ],
            }
        )
        self.assertTrue(warnings)
        self.assertEqual(request["profiles"], ["codex-workflow-core"])
        self.assertEqual(request["domains"], ["medical-imaging"])
        self.assertEqual(
            request["skills"],
            ["skills/writing/core/chinese-prose", "skills/tools/documents-media/render-chinese-math-pdf"],
        )

    def test_manifest_to_install_args_sets_codex_home_from_skills_root(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            manifest_path = root / "home" / "skills" / skills.MANIFEST_NAME
            manifest_path.parent.mkdir(parents=True)
            manifest_path.write_text(
                json.dumps(
                    {
                        "target": "codex-home",
                        "install_mode_requested": "copy",
                        "skills_root": str(manifest_path.parent),
                        "agents_md_managed": False,
                        "prune_managed": True,
                        "install_request": {
                            "profiles": ["codex-core-global"],
                            "domains": [],
                            "categories": [],
                            "skills": [],
                        },
                    }
                ),
                encoding="utf-8",
            )
            update_args = argparse.Namespace(dry_run=True)
            install_args, warnings, temporary_codex_home = skills.manifest_to_install_args(manifest_path, update_args)
        self.assertEqual(warnings, [])
        self.assertEqual(install_args.target, "codex-home")
        self.assertEqual(install_args.mode, "copy")
        self.assertTrue(install_args.prune_managed)
        self.assertEqual(temporary_codex_home, str(root / "home"))

    def test_find_manifests_respects_scan_depth(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            shallow = root / "repo" / ".agents" / "skills" / skills.MANIFEST_NAME
            deep = root / "a" / "b" / "c" / "d" / "skills" / skills.MANIFEST_NAME
            shallow.parent.mkdir(parents=True)
            deep.parent.mkdir(parents=True)
            shallow.write_text(json.dumps({"target": "repo", "skills_root": str(shallow.parent)}), encoding="utf-8")
            deep.write_text(json.dumps({"target": "repo", "skills_root": str(deep.parent)}), encoding="utf-8")
            found = skills.find_manifests([str(root)], max_depth=4)
        self.assertEqual(found, [shallow.resolve()])


if __name__ == "__main__":
    unittest.main()
