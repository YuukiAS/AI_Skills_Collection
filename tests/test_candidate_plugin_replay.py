from __future__ import annotations

import io
import json
import os
import stat
import subprocess
import sys
import tarfile
import tempfile
import unittest
from contextlib import redirect_stderr
from pathlib import Path
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import candidate_plugin_replay as replay  # noqa: E402


def run(args: list[str], cwd: Path) -> subprocess.CompletedProcess:
    return subprocess.run(args, cwd=str(cwd), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)


def make_repo(marketplace_plugin: dict | None = None) -> tuple[tempfile.TemporaryDirectory[str], Path, str]:
    tmp = tempfile.TemporaryDirectory()
    root = Path(tmp.name)
    (root / ".agents" / "plugins").mkdir(parents=True)
    plugin_dir = root / "plugins" / "codex" / "plugins" / "writing-style"
    (plugin_dir / ".codex-plugin").mkdir(parents=True)
    (plugin_dir / ".codex-plugin" / "plugin.json").write_text('{"name":"writing-style"}\n', encoding="utf-8")
    plugin_entry = marketplace_plugin or {
        "name": "writing-style",
        "source": {"source": "local", "path": "./plugins/codex/plugins/writing-style"},
    }
    (root / ".agents" / "plugins" / "marketplace.json").write_text(
        json.dumps({"plugins": [plugin_entry]}, indent=2) + "\n",
        encoding="utf-8",
    )
    run(["git", "init"], root)
    run(["git", "add", "."], root)
    run(["git", "-c", "user.name=Test", "-c", "user.email=test@example.com", "commit", "-m", "fixture"], root)
    commit = run(["git", "rev-parse", "HEAD"], root).stdout.strip()
    return tmp, root, commit


class CandidateSourceTests(unittest.TestCase):
    def test_unknown_candidate_commit_fails(self) -> None:
        tmp, root, _commit = make_repo()
        self.addCleanup(tmp.cleanup)
        with self.assertRaisesRegex(replay.ReplayError, "unknown candidate commit"):
            replay.resolve_candidate_plugin(root, "deadbeef", "writing-style")

    def test_plugin_missing_from_committed_marketplace_fails(self) -> None:
        tmp, root, commit = make_repo({"name": "other", "source": {"source": "local", "path": "./plugins/other"}})
        self.addCleanup(tmp.cleanup)
        with self.assertRaisesRegex(replay.ReplayError, "exactly once"):
            replay.resolve_candidate_plugin(root, commit, "writing-style")

    def test_non_local_source_fails(self) -> None:
        tmp, root, commit = make_repo({"name": "writing-style", "source": {"source": "github", "path": "x"}})
        self.addCleanup(tmp.cleanup)
        with self.assertRaisesRegex(replay.ReplayError, "source must be local"):
            replay.resolve_candidate_plugin(root, commit, "writing-style")

    def test_escaping_source_fails(self) -> None:
        tmp, root, commit = make_repo({"name": "writing-style", "source": {"source": "local", "path": "../evil"}})
        self.addCleanup(tmp.cleanup)
        with self.assertRaisesRegex(replay.ReplayError, "must not escape"):
            replay.resolve_candidate_plugin(root, commit, "writing-style")

    def test_replay_parser_rejects_arbitrary_runtime_flags(self) -> None:
        parser = replay.build_parser()
        with open(os.devnull, "w", encoding="utf-8") as devnull:
            with redirect_stderr(devnull):
                with self.assertRaises(SystemExit):
                    parser.parse_args(
                        [
                            "replay",
                            "--plugin",
                            "writing-style",
                            "--candidate-commit",
                            "abc",
                            "--task",
                            "task.md",
                            "--input",
                            "input.md",
                            "--codex-executable",
                            "/tmp/codex",
                        ]
                    )
                with self.assertRaises(SystemExit):
                    parser.parse_args(
                        [
                            "replay",
                            "--plugin",
                            "writing-style",
                            "--candidate-commit",
                            "abc",
                            "--task",
                            "task.md",
                            "--input",
                            "input.md",
                            "--codex-home",
                            "/tmp/home",
                        ]
                    )


class RuntimeTests(unittest.TestCase):
    def test_runtime_missing_replay_fails_with_ensure_runtime_hint(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaisesRegex(replay.ReplayError, "ensure-runtime"):
                replay.ensure_runtime_available(Path(tmp))

    def test_wrong_runtime_digest_or_version_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            paths = replay.runtime_paths(root)
            paths.bin_dir.mkdir(parents=True)
            paths.archive.parent.mkdir(parents=True)
            paths.archive.write_bytes(b"wrong archive")
            paths.codex.write_text("#!/bin/sh\nprintf 'codex-cli 0.153.4\\n'\n", encoding="utf-8")
            paths.codex.chmod(paths.codex.stat().st_mode | stat.S_IXUSR)
            paths.code_mode_host.write_text("#!/bin/sh\nexit 0\n", encoding="utf-8")
            paths.code_mode_host.chmod(paths.code_mode_host.stat().st_mode | stat.S_IXUSR)
            paths.manifest.write_text(
                json.dumps(
                    {
                        "asset_url": replay.ASSET_URL,
                        "asset_sha256": "wrong",
                        "binary_sha256": replay.sha256_file(paths.codex),
                        "version": replay.EXPECTED_CODEX_VERSION,
                    }
                ),
                encoding="utf-8",
            )
            with self.assertRaisesRegex(replay.ReplayError, "SHA256 mismatch"):
                replay.validate_runtime(paths)

            paths.archive.write_bytes(b"archive")
            with mock.patch.object(replay, "ASSET_SHA256", replay.sha256_file(paths.archive)):
                paths.manifest.write_text(
                    json.dumps(
                        {
                            "asset_url": replay.ASSET_URL,
                            "asset_sha256": replay.sha256_file(paths.archive),
                            "binary_sha256": replay.sha256_file(paths.codex),
                            "version": replay.EXPECTED_CODEX_VERSION,
                        }
                    ),
                    encoding="utf-8",
                )
                paths.codex.write_text("#!/bin/sh\nprintf 'codex-cli 0.1.0\\n'\n", encoding="utf-8")
                paths.codex.chmod(paths.codex.stat().st_mode | stat.S_IXUSR)
                paths.manifest.write_text(
                    json.dumps(
                        {
                            "asset_url": replay.ASSET_URL,
                            "asset_sha256": replay.sha256_file(paths.archive),
                            "binary_sha256": replay.sha256_file(paths.codex),
                            "version": replay.EXPECTED_CODEX_VERSION,
                        }
                    ),
                    encoding="utf-8",
                )
                with self.assertRaisesRegex(replay.ReplayError, "version mismatch"):
                    replay.validate_runtime(paths)

    def test_missing_code_mode_host_fails_runtime_validation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            paths = replay.runtime_paths(root)
            paths.bin_dir.mkdir(parents=True)
            paths.archive.parent.mkdir(parents=True)
            paths.archive.write_bytes(b"archive")
            paths.codex.write_text("#!/bin/sh\nprintf 'codex-cli 0.153.4\\n'\n", encoding="utf-8")
            paths.codex.chmod(paths.codex.stat().st_mode | stat.S_IXUSR)
            with mock.patch.object(replay, "ASSET_SHA256", replay.sha256_file(paths.archive)):
                paths.manifest.write_text(
                    json.dumps(
                        {
                            "asset_url": replay.ASSET_URL,
                            "asset_sha256": replay.sha256_file(paths.archive),
                            "binary_sha256": replay.sha256_file(paths.codex),
                            "version": replay.EXPECTED_CODEX_VERSION,
                        }
                    ),
                    encoding="utf-8",
                )
                with self.assertRaisesRegex(replay.ReplayError, "codex-code-mode-host is missing"):
                    replay.validate_runtime(paths)

    def test_safe_archive_extraction_rejects_escape(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            archive = root / "bad.tar.gz"
            data = b"x"
            info = tarfile.TarInfo("../escape")
            info.size = len(data)
            with tarfile.open(archive, "w:gz") as tf:
                tf.addfile(info, io.BytesIO(data))
            with self.assertRaisesRegex(replay.ReplayError, "outside runtime dir"):
                replay.safe_extract_tar(archive, root / "extract")


class ReplayMechanismTests(unittest.TestCase):
    def test_stale_cleanup_only_selects_fixed_candidate_namespace(self) -> None:
        payload = {
            "plugins": [
                {"pluginId": "writing-style@ai-skills-candidate"},
                {"pluginId": "writing-style@yuukias-ai-skills"},
                {"pluginId": "other@ai-bridge-candidate"},
            ]
        }
        self.assertEqual(replay.candidate_plugin_ids(payload), ["writing-style@ai-skills-candidate"])

    def test_actual_consumption_requires_parsed_json_event(self) -> None:
        installed = "/tmp/candidate/plugin"
        raw_only = f"plain text {installed}\n"
        self.assertIsNone(replay.parse_consumption(raw_only, installed))
        structured = json.dumps(
            {
                "type": "item.completed",
                "item": {
                    "type": "command_execution",
                    "command": f"cat {installed}/skills/zh/SKILL.md",
                },
            }
        )
        evidence = replay.parse_consumption(raw_only + structured + "\n", installed)
        self.assertIsNotNone(evidence)
        self.assertEqual(evidence.line_index, 2)

    def test_consumption_accepts_stable_candidate_cache_suffix(self) -> None:
        installed = "/canonical/root/plugins/cache/ai-skills-candidate/writing-style/0.1"
        event = json.dumps(
            {
                "type": "item.completed",
                "item": {
                    "type": "command_execution",
                    "command": (
                        "cat /logical/root/plugins/cache/ai-skills-candidate/"
                        "writing-style/0.1/skills/scientific-rewrite/SKILL.md"
                    ),
                },
            }
        )

        evidence = replay.parse_consumption(event + "\n", installed)

        self.assertIsNotNone(evidence)
        self.assertEqual(evidence.line_index, 1)

    def test_consumption_rejects_other_marketplace_same_plugin(self) -> None:
        installed = "/canonical/root/plugins/cache/ai-skills-candidate/writing-style/0.1"
        event = json.dumps(
            {
                "type": "item.completed",
                "item": {
                    "type": "command_execution",
                    "command": "cat /logical/root/plugins/cache/other-market/writing-style/0.1/skills/zh/SKILL.md",
                },
            }
        )

        self.assertIsNone(replay.parse_consumption(event + "\n", installed))

    def test_consumption_rejects_raw_non_json_candidate_path(self) -> None:
        installed = "/canonical/root/plugins/cache/ai-skills-candidate/writing-style/0.1"
        raw = "/logical/root/plugins/cache/ai-skills-candidate/writing-style/0.1/skills/zh/SKILL.md\n"

        self.assertIsNone(replay.parse_consumption(raw, installed))

    def test_consumption_rejects_assistant_text_candidate_path(self) -> None:
        installed = "/canonical/root/plugins/cache/ai-skills-candidate/writing-style/0.1"
        event = json.dumps(
            {
                "type": "item.completed",
                "item": {
                    "type": "message",
                    "role": "assistant",
                    "content": [
                        {
                            "type": "output_text",
                            "text": (
                                "I used /logical/root/plugins/cache/ai-skills-candidate/"
                                "writing-style/0.1/skills/zh/SKILL.md"
                            ),
                        }
                    ],
                },
            }
        )

        self.assertIsNone(replay.parse_consumption(event + "\n", installed))

    def test_consumption_still_accepts_full_absolute_installed_path(self) -> None:
        installed = "/canonical/root/plugins/cache/ai-skills-candidate/writing-style/0.1"
        event = json.dumps(
            {
                "type": "item.completed",
                "item": {
                    "type": "command_execution",
                    "command": f"cat {installed}/skills/fidelity/SKILL.md",
                },
            }
        )

        self.assertIsNotNone(replay.parse_consumption(event + "\n", installed))

    def test_plugin_add_uses_top_level_installed_path_only(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            wrong = root / "wrong" / "staged" / "source"
            correct = root / "correct" / "codex" / "cache" / "writing-style" / "0.1"
            wrong.mkdir(parents=True)
            correct.mkdir(parents=True)
            payload = {
                "pluginId": "writing-style@ai-skills-candidate",
                "source": {"path": str(wrong)},
                "installedPath": str(correct),
            }

            with mock.patch.object(replay, "run_codex_json", return_value=payload):
                plugin_id, installed_path, returned_payload = replay.add_candidate_plugin(
                    Path("/repo/.local-runtime/codex/0.153.4/bin/codex"),
                    Path("/repo/.local-runtime/candidate-marketplace"),
                    "writing-style",
                )

        self.assertEqual(plugin_id, "writing-style@ai-skills-candidate")
        self.assertEqual(installed_path, str(correct))
        self.assertNotEqual(installed_path, str(wrong))
        self.assertIs(returned_payload, payload)

    def test_candidate_absent_after_normal_completion(self) -> None:
        replay.assert_candidate_absent({"plugins": [{"pluginId": "writing-style@yuukias-ai-skills"}]})
        with self.assertRaisesRegex(replay.ReplayError, "still installed"):
            replay.assert_candidate_absent({"plugins": [{"pluginId": "writing-style@ai-skills-candidate"}]})

    def test_production_same_name_identity_unchanged(self) -> None:
        before = [{"pluginId": "writing-style@yuukias-ai-skills", "enabled": True}]
        replay.assert_production_unchanged(before, [{"pluginId": "writing-style@yuukias-ai-skills", "enabled": True}])
        with self.assertRaisesRegex(replay.ReplayError, "production same-name"):
            replay.assert_production_unchanged(before, [{"pluginId": "writing-style@yuukias-ai-skills", "enabled": False}])

    def test_plugin_add_failure_triggers_cleanup(self) -> None:
        tmp, root, commit = make_repo()
        self.addCleanup(tmp.cleanup)
        (root / "task.md").write_text("Do the task.\n", encoding="utf-8")
        (root / "input.md").write_text("Input.\n", encoding="utf-8")
        remove_calls: list[str] = []

        def fake_stage(_root: Path, _candidate: replay.CandidatePlugin, run_dir: Path) -> Path:
            marketplace = run_dir / "marketplace"
            marketplace.mkdir(parents=True)
            return marketplace

        def fake_run_codex_json(_codex: Path, args: list[str], **_kwargs):
            if args[:3] == ["plugin", "list", "--json"]:
                return {"plugins": [{"pluginId": "writing-style@yuukias-ai-skills", "name": "writing-style", "enabled": True}]}
            if args[-4:] == ["plugin", "add", "--json", "writing-style@ai-skills-candidate"]:
                return {"pluginId": "wrong@ai-skills-candidate", "installedPath": "/tmp/nope"}
            return None

        with mock.patch.object(replay, "ensure_runtime_available", return_value={"version": replay.EXPECTED_CODEX_VERSION}):
            with mock.patch.object(replay, "safe_stage_candidate", side_effect=fake_stage):
                with mock.patch.object(replay, "run_codex_json", side_effect=fake_run_codex_json):
                    with mock.patch.object(replay, "remove_candidate_plugin", side_effect=lambda _c, plugin_id: remove_calls.append(plugin_id)):
                        with self.assertRaisesRegex(replay.ReplayError, "unexpected pluginId"):
                            replay.run_replay(root, "writing-style", commit, "task.md", ["input.md"])
        self.assertEqual(remove_calls, ["writing-style@ai-skills-candidate"])

    def test_child_failure_triggers_cleanup(self) -> None:
        tmp, root, commit = make_repo()
        self.addCleanup(tmp.cleanup)
        (root / "task.md").write_text("Do the task.\n", encoding="utf-8")
        (root / "input.md").write_text("Input.\n", encoding="utf-8")
        installed = root / ".local-runtime" / "installed-candidate"
        installed.mkdir(parents=True)
        remove_calls: list[str] = []

        def fake_stage(_root: Path, _candidate: replay.CandidatePlugin, run_dir: Path) -> Path:
            marketplace = run_dir / "marketplace"
            marketplace.mkdir(parents=True)
            return marketplace

        def fake_run_codex_json(_codex: Path, args: list[str], **_kwargs):
            if args[:3] == ["plugin", "list", "--json"]:
                return {"plugins": [{"pluginId": "writing-style@yuukias-ai-skills", "name": "writing-style", "enabled": True}]}
            return None

        child = replay.CommandResult(
            ("codex", "exec"),
            1,
            json.dumps({"type": "event", "path": str(installed / "skills" / "x")}) + "\n",
            "failed",
        )
        with mock.patch.object(replay, "ensure_runtime_available", return_value={"version": replay.EXPECTED_CODEX_VERSION}):
            with mock.patch.object(replay, "safe_stage_candidate", side_effect=fake_stage):
                with mock.patch.object(replay, "run_codex_json", side_effect=fake_run_codex_json):
                    with mock.patch.object(
                        replay,
                        "add_candidate_plugin",
                        return_value=("writing-style@ai-skills-candidate", str(installed), {}),
                    ):
                        with mock.patch.object(replay, "run_child_exec", return_value=child):
                            with mock.patch.object(
                                replay,
                                "remove_candidate_plugin",
                                side_effect=lambda _c, plugin_id: remove_calls.append(plugin_id),
                            ):
                                with self.assertRaisesRegex(replay.ReplayError, "child exec failed"):
                                    replay.run_replay(root, "writing-style", commit, "task.md", ["input.md"])
        self.assertEqual(remove_calls, ["writing-style@ai-skills-candidate"])

    def test_consumption_proof_failure_still_persists_child_streams(self) -> None:
        tmp, root, commit = make_repo()
        self.addCleanup(tmp.cleanup)
        (root / "task.md").write_text("Do the task.\n", encoding="utf-8")
        (root / "input.md").write_text("Input.\n", encoding="utf-8")
        installed = root / ".local-runtime" / "installed-candidate"
        installed.mkdir(parents=True)

        def fake_stage(_root: Path, _candidate: replay.CandidatePlugin, run_dir: Path) -> Path:
            marketplace = run_dir / "marketplace"
            marketplace.mkdir(parents=True)
            return marketplace

        def fake_run_codex_json(_codex: Path, args: list[str], **_kwargs):
            if args[:3] == ["plugin", "list", "--json"]:
                return {"plugins": [{"pluginId": "writing-style@yuukias-ai-skills", "name": "writing-style", "enabled": True}]}
            return None

        child_stdout = json.dumps({"type": "event", "message": "no candidate installed path here"}) + "\n"
        child_stderr = "diagnostic stderr\n"
        child = replay.CommandResult(("codex", "exec"), 0, child_stdout, child_stderr)
        with mock.patch.object(replay, "ensure_runtime_available", return_value={"version": replay.EXPECTED_CODEX_VERSION}):
            with mock.patch.object(replay, "safe_stage_candidate", side_effect=fake_stage):
                with mock.patch.object(replay, "run_codex_json", side_effect=fake_run_codex_json):
                    with mock.patch.object(
                        replay,
                        "add_candidate_plugin",
                        return_value=("writing-style@ai-skills-candidate", str(installed), {}),
                    ):
                        with mock.patch.object(replay, "run_child_exec", return_value=child):
                            with mock.patch.object(replay, "remove_candidate_plugin"):
                                with self.assertRaisesRegex(replay.ReplayError, "actual consumption"):
                                    replay.run_replay(root, "writing-style", commit, "task.md", ["input.md"])

        stdout_files = list((root / ".local-runtime" / "candidate-plugin-replay" / "runs").glob("*/child.stdout.jsonl"))
        stderr_files = list((root / ".local-runtime" / "candidate-plugin-replay" / "runs").glob("*/child.stderr"))
        add_payload_files = list((root / ".local-runtime" / "candidate-plugin-replay" / "runs").glob("*/plugin-add.json"))
        self.assertEqual(len(stdout_files), 1)
        self.assertEqual(len(stderr_files), 1)
        self.assertEqual(len(add_payload_files), 1)
        self.assertEqual(stdout_files[0].read_text(encoding="utf-8"), child_stdout)
        self.assertEqual(stderr_files[0].read_text(encoding="utf-8"), child_stderr)
        self.assertEqual(json.loads(add_payload_files[0].read_text(encoding="utf-8")), {})

    def test_child_exec_enable_config_uses_unquoted_plugin_id(self) -> None:
        captured: dict[str, list[str]] = {}

        def fake_run_command(args: list[str], **_kwargs):
            captured["args"] = args
            return replay.CommandResult(tuple(args), 0, "", "")

        with mock.patch.object(replay, "run_command", side_effect=fake_run_command):
            replay.run_child_exec(
                Path("/repo/.local-runtime/codex/0.153.4/bin/codex"),
                Path("/repo/.local-runtime/candidate-marketplace"),
                "writing-style@ai-skills-candidate",
                Path("/repo/workspace"),
                Path("/repo/workspace/outputs"),
                "Rewrite this.",
            )

        self.assertIn("plugins.writing-style@ai-skills-candidate.enabled=true", captured["args"])
        self.assertNotIn('plugins."writing-style@ai-skills-candidate".enabled=true', captured["args"])


if __name__ == "__main__":
    unittest.main()
