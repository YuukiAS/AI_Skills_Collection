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

    def test_environment_detects_public_site_profile(self) -> None:
        args = argparse.Namespace(site=None, hostname="login01.cuhk.example", path="/project/demo")
        profile, matches = skills.environment_detect_profile(args, skills.load_site_profiles())
        self.assertIsNotNone(profile)
        self.assertEqual(profile["id"], "cuhk-central-cluster")
        self.assertEqual([item["id"] for item in matches], ["cuhk-central-cluster"])

    def test_environment_plan_is_read_only(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp)
            args = argparse.Namespace(
                site="unc-longleaf",
                target="repo",
                project=str(project),
                hostname=None,
                path=None,
                local_override=str(project / "local-overrides.toml"),
            )
            plan = skills.environment_plan_payload(args)
            self.assertEqual(plan["site_id"], "unc-longleaf")
            self.assertFalse((project / ".agents").exists())
            self.assertEqual([action["action"] for action in plan["actions"]], ["materialize-skill", "materialize-skill"])

    def test_environment_apply_is_idempotent_and_manifest_managed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp)
            args = argparse.Namespace(
                site="cuhk-central-cluster",
                target="repo",
                project=str(project),
                hostname=None,
                path=None,
                local_override=str(project / "local-overrides.toml"),
                dry_run=False,
                json=True,
            )
            first = skills.environment_apply_plan(args, skills.environment_plan_payload(args))
            second = skills.environment_apply_plan(args, skills.environment_plan_payload(args))
            manifest_path = Path(first["target_root"]) / skills.ENV_MANIFEST_NAME
            self.assertTrue(manifest_path.exists())
            self.assertEqual(first["site_id"], "cuhk-central-cluster")
            self.assertEqual(second["site_id"], "cuhk-central-cluster")
            self.assertTrue((Path(first["target_root"]) / "slurm-workflows" / "references" / "_generated" / "site-profile.md").exists())

    def test_environment_init_site_writes_only_selected_section_and_refuses_overwrite(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            override = Path(tmp) / "local-overrides.toml"
            args = argparse.Namespace(site="cuhk-central-cluster", local_override=str(override), dry_run=False, force=False)
            self.assertEqual(skills.command_environment_init(args), 0)
            text = override.read_text(encoding="utf-8")
            self.assertIn("[sites.cuhk-central-cluster]", text)
            self.assertNotIn("[sites.unc-longleaf]", text)
            with self.assertRaises(SystemExit):
                skills.command_environment_init(args)

    def test_environment_doctor_reports_override_diagnostics(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp) / "project"
            override = Path(tmp) / "local-overrides.toml"
            override.write_text(
                "\n".join(
                    [
                        "[sites.cuhk-central-cluster]",
                        'account = ""',
                        'unknown_field = "x"',
                        f'scratch_root = "{Path(tmp) / "missing-scratch"}"',
                        "",
                        "[sites.unknown-site]",
                        'account = "x"',
                    ]
                ),
                encoding="utf-8",
            )
            args = argparse.Namespace(
                site="cuhk-central-cluster",
                target="repo",
                project=str(project),
                hostname=None,
                path=None,
                local_override=str(override),
                submit_smoke_job=False,
                json=True,
            )
            data = skills.environment_doctor_payload(args)
            diagnostics = data["diagnostics"]
            self.assertIn("unknown-site", diagnostics["unknown_sites"])
            self.assertIn("unknown_field", diagnostics["unknown_fields"])
            self.assertIn("account", diagnostics["empty_fields"])
            self.assertIn("partition", diagnostics["missing_required_fields"])
            self.assertIn("scratch_root", diagnostics["inaccessible_paths"])

    def test_environment_doctor_reports_site_mismatch(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            override = Path(tmp) / "local-overrides.toml"
            override.write_text("[sites.unc-longleaf]\naccount = \"abc\"\n", encoding="utf-8")
            args = argparse.Namespace(
                site="cuhk-central-cluster",
                target="user",
                project=None,
                hostname=None,
                path=None,
                local_override=str(override),
                submit_smoke_job=False,
                json=True,
            )
            data = skills.environment_doctor_payload(args)
            self.assertTrue(data["diagnostics"]["site_mismatch"])

    def test_environment_local_override_parser_reports_invalid_lines(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            override = Path(tmp) / "local-overrides.toml"
            override.write_text("account = \"outside\"\n[sites.cuhk-central-cluster]\nnot-a-field\n", encoding="utf-8")
            _data, errors = skills.parse_environment_local_override(override)
            self.assertTrue(any("outside" in error for error in errors))
            self.assertTrue(any("expected key = value" in error for error in errors))

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
