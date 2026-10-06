from __future__ import annotations

import io
import json
import contextlib
import os
import shutil
import signal
import stat
import subprocess
import sys
import tarfile
import tempfile
import time
import unittest
from contextlib import redirect_stderr
from pathlib import Path
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import candidate_plugin_replay as replay  # noqa: E402


def run(args: list[str], cwd: Path) -> subprocess.CompletedProcess:
    return subprocess.run(args, cwd=str(cwd), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)


def write_skill(plugin_root: Path, slug: str, name: str) -> Path:
    skill = plugin_root / "skills" / slug / "SKILL.md"
    skill.parent.mkdir(parents=True, exist_ok=True)
    skill.write_text(f"---\nname: {name}\ndescription: Test skill.\n---\n\nBody.\n", encoding="utf-8")
    return skill


def make_cached_package(
    cache_root: Path,
    marketplace: str,
    plugin: str,
    version: str,
    skill_names: list[str],
) -> Path:
    package = cache_root / marketplace / plugin / version
    (package / ".codex-plugin").mkdir(parents=True, exist_ok=True)
    (package / ".codex-plugin" / "plugin.json").write_text(
        json.dumps({"name": plugin, "version": version}) + "\n",
        encoding="utf-8",
    )
    for index, name in enumerate(skill_names, start=1):
        write_skill(package, f"skill-{index}", name)
    return package


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


def process_is_running(pid: int) -> bool:
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    proc_stat = Path(f"/proc/{pid}/stat")
    if proc_stat.exists():
        try:
            if proc_stat.read_text(encoding="utf-8").split()[2] == "Z":
                return False
        except (OSError, IndexError):
            pass
    return True


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
    def make_executable(self, root: Path, script: str) -> Path:
        path = root / "codex"
        path.write_text(script, encoding="utf-8")
        path.chmod(path.stat().st_mode | stat.S_IXUSR)
        return path

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

    def test_consumer_isolation_allows_candidate_stable_suffix(self) -> None:
        installed = "/canonical/root/plugins/cache/ai-skills-candidate/writing-style/0.1"
        event = json.dumps(
            {
                "type": "item.completed",
                "item": {
                    "type": "command_execution",
                    "command": (
                        "cat /logical/root/plugins/cache/ai-skills-candidate/"
                        "writing-style/0.1/skills/zh/SKILL.md"
                    ),
                },
            }
        )

        self.assertEqual(replay.parse_consumer_isolation_violations(event + "\n", [installed]), [])

    def test_consumer_isolation_flags_live_plugin_cache_skill_read(self) -> None:
        installed = "/canonical/root/plugins/cache/ai-skills-candidate/writing-style/0.1"
        event = json.dumps(
            {
                "type": "item.completed",
                "item": {
                    "type": "command_execution",
                    "command": (
                        "cat /users/me/.codex/plugins/cache/created-by-me-remote/"
                        "research-authoring/0.3.0/skills/report/SKILL.md"
                    ),
                },
            }
        )

        violations = replay.parse_consumer_isolation_violations(event + "\n", [installed])

        self.assertEqual(len(violations), 1)
        self.assertEqual(violations[0].line_index, 1)
        self.assertIn("created-by-me-remote/research-authoring", violations[0].command)

    def test_consumer_isolation_ignores_non_plugin_cache_skill_read(self) -> None:
        installed = "/canonical/root/plugins/cache/ai-skills-candidate/writing-style/0.1"
        event = json.dumps(
            {
                "type": "item.completed",
                "item": {
                    "type": "command_execution",
                    "command": "cat /repo/skills/writing-style/SKILL.md",
                },
            }
        )

        self.assertEqual(replay.parse_consumer_isolation_violations(event + "\n", [installed]), [])

    def test_writable_dir_must_be_existing_repo_local_directory(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            allowed = root / "private" / "exports" / "task" / "fixtures"
            allowed.mkdir(parents=True)

            self.assertEqual(replay.repo_relative_existing_dir(root, "private/exports/task/fixtures"), allowed.resolve())
            with self.assertRaisesRegex(replay.ReplayError, "directory does not exist"):
                replay.repo_relative_existing_dir(root, "private/exports/task/missing")
            with self.assertRaisesRegex(replay.ReplayError, "inside this repository"):
                replay.repo_relative_existing_dir(root, "../outside")

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

    def test_normalized_plugin_list_can_ignore_exact_current_run_candidates(self) -> None:
        baseline = {
            "plugins": [
                {
                    "pluginId": "writing-style@yuukias-ai-skills",
                    "name": "writing-style",
                    "enabled": True,
                    "marketplaceName": "yuukias-ai-skills",
                    "installedPath": "/cache/yuukias-ai-skills/writing-style/0.4",
                }
            ]
        }
        current = {
            "plugins": baseline["plugins"]
            + [
                {
                    "pluginId": "web-development@ai-skills-candidate",
                    "name": "web-development",
                    "enabled": True,
                    "marketplaceName": "ai-skills-candidate",
                    "installedPath": "/cache/ai-skills-candidate/web-development/0.4",
                },
                {
                    "pluginId": "writing-style@ai-skills-candidate",
                    "name": "writing-style",
                    "enabled": True,
                    "marketplaceName": "ai-skills-candidate",
                    "installedPath": "/cache/ai-skills-candidate/writing-style/0.4",
                },
            ]
        }

        self.assertEqual(
            replay.normalized_plugin_list(
                current,
                ignored_plugin_ids={
                    "web-development@ai-skills-candidate",
                    "writing-style@ai-skills-candidate",
                },
            ),
            replay.normalized_plugin_list(baseline),
        )

    def test_normalized_plugin_list_detects_unrelated_non_candidate_change(self) -> None:
        baseline = {"plugins": [{"pluginId": "writing-style@yuukias-ai-skills", "enabled": True}]}
        current = {
            "plugins": baseline["plugins"]
            + [
                {"pluginId": "writing-style@ai-skills-candidate", "enabled": True},
                {"pluginId": "unrelated@yuukias-ai-skills", "enabled": True},
            ]
        }

        self.assertNotEqual(
            replay.normalized_plugin_list(
                current,
                ignored_plugin_ids={"writing-style@ai-skills-candidate"},
            ),
            replay.normalized_plugin_list(baseline),
        )

    def test_normalized_plugin_list_with_explicit_ignore_keeps_other_candidate_plugins(self) -> None:
        baseline = {"plugins": [{"pluginId": "writing-style@yuukias-ai-skills", "enabled": True}]}
        current = {
            "plugins": baseline["plugins"]
            + [
                {"pluginId": "writing-style@ai-skills-candidate", "enabled": True},
                {"pluginId": "other@ai-skills-candidate", "enabled": True},
            ]
        }

        self.assertNotEqual(
            replay.normalized_plugin_list(
                current,
                ignored_plugin_ids={"writing-style@ai-skills-candidate"},
            ),
            replay.normalized_plugin_list(baseline),
        )

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
        self.assertEqual(json.loads(add_payload_files[0].read_text(encoding="utf-8")), {"writing-style": {}})

    def test_consumer_isolation_failure_still_cleans_candidate(self) -> None:
        tmp, root, commit = make_repo()
        self.addCleanup(tmp.cleanup)
        (root / "task.md").write_text("Do the task.\n", encoding="utf-8")
        (root / "input.md").write_text("Input.\n", encoding="utf-8")
        installed = root / "plugins" / "cache" / "ai-skills-candidate" / "writing-style" / "0.1"
        installed.mkdir(parents=True)
        codex_home = root / ".codex"
        discovery = codex_home / "plugins" / "cache"
        original = make_cached_package(discovery, "live", "writing-style", "0.4", ["chinese-prose"])
        package = replay.cached_plugin_package_from_path(original, discovery)
        self.assertIsNotNone(package)
        assert package is not None
        conflict = replay.QuarantineRecord(
            package=package,
            quarantine_path=Path(),
            overlapping_skill_names=("chinese-prose",),
        )
        remove_calls: list[str] = []

        def fake_stage(_root: Path, _candidate: replay.CandidatePlugin, run_dir: Path) -> Path:
            marketplace = run_dir / "marketplace"
            marketplace.mkdir(parents=True)
            return marketplace

        def fake_run_codex_json(_codex: Path, args: list[str], **_kwargs):
            if args[:3] == ["plugin", "list", "--json"]:
                return {"plugins": [{"pluginId": "writing-style@yuukias-ai-skills", "name": "writing-style", "enabled": True}]}
            return None

        candidate_event = json.dumps(
            {
                "type": "item.completed",
                "item": {
                    "type": "command_execution",
                    "command": f"cat {installed}/skills/zh/SKILL.md",
                },
            }
        )
        live_event = json.dumps(
            {
                "type": "item.completed",
                "item": {
                    "type": "command_execution",
                    "command": f"cat {original}/skills/skill-1/SKILL.md",
                },
            }
        )
        child = replay.CommandResult(("codex", "exec"), 0, candidate_event + "\n" + live_event + "\n", "")
        with mock.patch.object(replay, "ensure_runtime_available", return_value={"version": replay.EXPECTED_CODEX_VERSION}):
            with mock.patch.object(replay, "safe_stage_candidate", side_effect=fake_stage):
                with mock.patch.object(replay, "run_codex_json", side_effect=fake_run_codex_json):
                    with mock.patch.object(
                        replay,
                        "add_candidate_plugin",
                        return_value=("writing-style@ai-skills-candidate", str(installed), {}),
                    ):
                        with mock.patch.object(replay, "effective_codex_home", return_value=codex_home.resolve()):
                            with mock.patch.object(replay, "detect_conflicting_cached_packages", return_value=[conflict]):
                                with mock.patch.object(replay, "assert_no_concurrent_codex_consumers"):
                                    with mock.patch.object(replay, "run_child_exec", return_value=child):
                                        with mock.patch.object(
                                            replay,
                                            "remove_candidate_plugin",
                                            side_effect=lambda _c, plugin_id: remove_calls.append(plugin_id),
                                        ):
                                            with self.assertRaisesRegex(replay.ReplayError, "consumer isolation"):
                                                replay.run_replay(root, "writing-style", commit, "task.md", ["input.md"])

        self.assertEqual(remove_calls, ["writing-style@ai-skills-candidate"])

    def test_child_exec_normal_completion_persists_streams(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            workspace = root / "workspace"
            output_dir = workspace / "outputs"
            workspace.mkdir()
            output_dir.mkdir()
            stdout_path = root / "run" / "child.stdout.jsonl"
            stderr_path = root / "run" / "child.stderr"
            codex = self.make_executable(
                root,
                "#!/usr/bin/env python3\n"
                "import sys\n"
                "sys.stdin.read()\n"
                "print('stdout line', flush=True)\n"
                "print('stderr line', file=sys.stderr, flush=True)\n",
            )

            result = replay.run_child_exec(
                codex,
                root / "marketplace",
                "writing-style@ai-skills-candidate",
                workspace,
                output_dir,
                "prompt text",
                stdout_path=stdout_path,
                stderr_path=stderr_path,
                timeout_seconds=5,
                terminate_grace_seconds=0.1,
            )

            self.assertEqual(result.returncode, 0)
            self.assertEqual(result.stdout, "stdout line\n")
            self.assertEqual(result.stderr, "stderr line\n")
            self.assertEqual(stdout_path.read_text(encoding="utf-8"), "stdout line\n")
            self.assertEqual(stderr_path.read_text(encoding="utf-8"), "stderr line\n")

    def test_child_exec_timeout_preserves_streams_and_kills_process_group(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            workspace = root / "workspace"
            output_dir = workspace / "outputs"
            workspace.mkdir()
            output_dir.mkdir()
            stdout_path = root / "run" / "child.stdout.jsonl"
            stderr_path = root / "run" / "child.stderr"
            run_json = root / "run" / "run.json"
            pid_path = root / "descendant.pid"
            installed = root / "plugins" / "cache" / "ai-skills-candidate" / "writing-style" / "0.1"
            installed.mkdir(parents=True)
            codex = self.make_executable(
                root,
                "#!/usr/bin/env python3\n"
                "import json, pathlib, subprocess, sys, time\n"
                f"pid_path = pathlib.Path({str(pid_path)!r})\n"
                "sys.stdin.read()\n"
                "args = sys.argv[1:]\n"
                "output_dir = pathlib.Path(args[args.index('--add-dir') + 1])\n"
                "output_dir.mkdir(parents=True, exist_ok=True)\n"
                "(output_dir / 'candidate.md').write_text('partial output\\n', encoding='utf-8')\n"
                "child = subprocess.Popen([sys.executable, '-c', 'import time; time.sleep(60)'])\n"
                "pid_path.write_text(str(child.pid), encoding='utf-8')\n"
                f"command = 'cat {installed}/skills/zh/SKILL.md'\n"
                "event = {'type': 'item.completed', 'item': {'type': 'command_execution', 'command': command}}\n"
                "print(json.dumps(event), flush=True)\n"
                "print('diagnostic stderr', file=sys.stderr, flush=True)\n"
                "while True:\n"
                "    time.sleep(1)\n",
            )
            try:
                with self.assertRaisesRegex(replay.ReplayError, "timed out"):
                    replay.run_child_exec(
                        codex,
                        root / "marketplace",
                        "writing-style@ai-skills-candidate",
                        workspace,
                        output_dir,
                        "prompt text",
                        stdout_path=stdout_path,
                        stderr_path=stderr_path,
                        timeout_seconds=3,
                        terminate_grace_seconds=0.2,
                    )

                stdout = stdout_path.read_text(encoding="utf-8")
                self.assertIn(f"{installed}/skills/zh/SKILL.md", stdout)
                self.assertEqual(stderr_path.read_text(encoding="utf-8"), "diagnostic stderr\n")
                self.assertEqual((output_dir / "candidate.md").read_text(encoding="utf-8"), "partial output\n")
                self.assertFalse(run_json.exists())
                descendant_pid = int(pid_path.read_text(encoding="utf-8"))
                deadline = time.time() + 3
                while time.time() < deadline and process_is_running(descendant_pid):
                    time.sleep(0.05)
                self.assertFalse(process_is_running(descendant_pid))
            finally:
                if pid_path.exists():
                    with contextlib.suppress(ProcessLookupError):
                        os.kill(int(pid_path.read_text(encoding="utf-8")), signal.SIGKILL)

    def test_child_exec_timeout_from_run_replay_triggers_cleanup(self) -> None:
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

        with mock.patch.object(replay, "ensure_runtime_available", return_value={"version": replay.EXPECTED_CODEX_VERSION}):
            with mock.patch.object(replay, "safe_stage_candidate", side_effect=fake_stage):
                with mock.patch.object(replay, "run_codex_json", side_effect=fake_run_codex_json):
                    with mock.patch.object(
                        replay,
                        "add_candidate_plugin",
                        return_value=("writing-style@ai-skills-candidate", str(installed), {}),
                    ):
                        with mock.patch.object(
                            replay,
                            "run_child_exec",
                            side_effect=replay.ReplayError("candidate child exec timed out after 0.5s"),
                        ):
                            with mock.patch.object(
                                replay,
                                "remove_candidate_plugin",
                                side_effect=lambda _c, plugin_id: remove_calls.append(plugin_id),
                            ):
                                with self.assertRaisesRegex(replay.ReplayError, "timed out"):
                                    replay.run_replay(root, "writing-style", commit, "task.md", ["input.md"])
        self.assertEqual(remove_calls, ["writing-style@ai-skills-candidate"])
        run_json_files = list((root / ".local-runtime" / "candidate-plugin-replay" / "runs").glob("*/run.json"))
        self.assertEqual(run_json_files, [])

    def test_child_exec_enable_config_uses_unquoted_plugin_id(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            workspace = root / "workspace"
            output_dir = workspace / "outputs"
            workspace.mkdir()
            output_dir.mkdir()
            args_file = root / "args.json"
            codex = self.make_executable(
                root,
                "#!/usr/bin/env python3\n"
                "import json, pathlib, sys\n"
                f"pathlib.Path({str(args_file)!r}).write_text(json.dumps(sys.argv[1:]), encoding='utf-8')\n"
                "sys.stdin.read()\n",
            )
            replay.run_child_exec(
                codex,
                root / "candidate-marketplace",
                "writing-style@ai-skills-candidate",
                workspace,
                output_dir,
                "Rewrite this.",
                stdout_path=root / "run" / "child.stdout.jsonl",
                stderr_path=root / "run" / "child.stderr",
                timeout_seconds=5,
                terminate_grace_seconds=0.1,
            )

            captured = json.loads(args_file.read_text(encoding="utf-8"))

        self.assertIn("plugins.writing-style@ai-skills-candidate.enabled=true", captured)
        self.assertNotIn('plugins."writing-style@ai-skills-candidate".enabled=true', captured)

    def test_child_exec_does_not_inject_candidate_consumer_isolation_prompt(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            workspace = root / "workspace"
            output_dir = workspace / "outputs"
            workspace.mkdir()
            output_dir.mkdir()
            prompt_file = root / "prompt.txt"
            codex = self.make_executable(
                root,
                "#!/usr/bin/env python3\n"
                "import pathlib, sys\n"
                f"pathlib.Path({str(prompt_file)!r}).write_text(sys.stdin.read(), encoding='utf-8')\n",
            )
            installed = "/root/plugins/cache/ai-skills-candidate/writing-style/0.1"

            replay.run_child_exec(
                codex,
                root / "candidate-marketplace",
                "writing-style@ai-skills-candidate",
                workspace,
                output_dir,
                "Rewrite this.",
                stdout_path=root / "run" / "child.stdout.jsonl",
                stderr_path=root / "run" / "child.stderr",
                timeout_seconds=5,
                terminate_grace_seconds=0.1,
            )

            prompt = prompt_file.read_text(encoding="utf-8")

        self.assertEqual(installed, "/root/plugins/cache/ai-skills-candidate/writing-style/0.1")
        self.assertEqual(prompt, "Rewrite this.")

    def test_child_exec_can_add_repo_local_writable_dirs(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            workspace = root / "workspace"
            output_dir = workspace / "outputs"
            fixture_dir = root / "private" / "exports" / "task" / "fixtures"
            workspace.mkdir()
            output_dir.mkdir()
            fixture_dir.mkdir(parents=True)
            args_file = root / "args.json"
            codex = self.make_executable(
                root,
                "#!/usr/bin/env python3\n"
                "import json, pathlib, sys\n"
                f"pathlib.Path({str(args_file)!r}).write_text(json.dumps(sys.argv[1:]), encoding='utf-8')\n"
                "sys.stdin.read()\n",
            )
            replay.run_child_exec(
                codex,
                root / "candidate-marketplace",
                "writing-style@ai-skills-candidate",
                workspace,
                output_dir,
                "Rewrite this.",
                stdout_path=root / "run" / "child.stdout.jsonl",
                stderr_path=root / "run" / "child.stderr",
                writable_dirs=[fixture_dir],
                timeout_seconds=5,
                terminate_grace_seconds=0.1,
            )

            captured = json.loads(args_file.read_text(encoding="utf-8"))

        add_dir_values = [captured[index + 1] for index, value in enumerate(captured) if value == "--add-dir"]
        self.assertIn(str(output_dir), add_dir_values)
        self.assertIn(str(fixture_dir), add_dir_values)

    def test_child_exec_can_enable_multiple_candidate_plugins(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            workspace = root / "workspace"
            output_dir = workspace / "outputs"
            workspace.mkdir()
            output_dir.mkdir()
            args_file = root / "args.json"
            codex = self.make_executable(
                root,
                "#!/usr/bin/env python3\n"
                "import json, pathlib, sys\n"
                f"pathlib.Path({str(args_file)!r}).write_text(json.dumps(sys.argv[1:]), encoding='utf-8')\n"
                "sys.stdin.read()\n",
            )
            replay.run_child_exec(
                codex,
                root / "candidate-marketplace",
                ["web-development@ai-skills-candidate", "writing-style@ai-skills-candidate"],
                workspace,
                output_dir,
                "Plan product interface copy.",
                stdout_path=root / "run" / "child.stdout.jsonl",
                stderr_path=root / "run" / "child.stderr",
                timeout_seconds=5,
                terminate_grace_seconds=0.1,
            )

            captured = json.loads(args_file.read_text(encoding="utf-8"))

        self.assertIn("plugins.web-development@ai-skills-candidate.enabled=true", captured)
        self.assertIn("plugins.writing-style@ai-skills-candidate.enabled=true", captured)

    def test_parser_accepts_repeated_plugin_arguments_for_same_session_replay(self) -> None:
        parser = replay.build_parser()

        args = parser.parse_args(
            [
                "replay",
                "--plugin",
                "web-development",
                "--plugin",
                "writing-style",
                "--candidate-commit",
                "abc",
                "--task",
                "task.md",
                "--input",
                "input.md",
            ]
        )

        self.assertEqual(args.plugin, ["web-development", "writing-style"])


class CandidateConsumerIsolationRecoveryTests(unittest.TestCase):
    def make_equivalent_rehydration_fixture(
        self,
        root: Path,
        *,
        run_id: str = "run",
        before_list: dict | None = None,
    ) -> tuple[Path, Path, Path, replay.QuarantineTransaction, dict]:
        codex_home = root / ".codex"
        discovery = codex_home / "plugins" / "cache"
        original = make_cached_package(
            discovery,
            "created-by-me-remote",
            "research-authoring",
            "0.3.0",
            ["research-reporting"],
        )
        package = replay.cached_plugin_package_from_path(original, discovery)
        self.assertIsNotNone(package)
        assert package is not None
        paths = replay.runtime_paths(root)
        record = replay.QuarantineRecord(
            package=package,
            quarantine_path=(
                replay.quarantine_parent(codex_home, run_id)
                / "created-by-me-remote"
                / "research-authoring"
                / "0.3.0"
            ),
            overlapping_skill_names=("research-reporting",),
        )
        plugin_list = before_list or {
            "plugins": [
                {
                    "pluginId": "research-authoring@created-by-me-remote",
                    "name": "research-authoring",
                    "enabled": True,
                    "marketplaceName": "created-by-me-remote",
                    "installedPath": str(original),
                }
            ]
        }
        with mock.patch.object(replay, "effective_codex_home", return_value=codex_home.resolve()):
            transaction = replay.prepare_quarantine_transaction(paths, run_id, plugin_list, {}, [record])
        self.assertIsNotNone(transaction)
        assert transaction is not None
        replay.activate_quarantine(transaction)
        return codex_home, discovery, original, transaction, plugin_list

    def test_detects_different_plugin_name_same_skill_conflict(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            cache = Path(tmp) / ".codex" / "plugins" / "cache"
            make_cached_package(cache, "created-by-me-remote", "research-authoring", "0.3.0", ["research-reporting"])

            conflicts = replay.detect_conflicting_cached_packages(cache, {"research-reporting"})

        self.assertEqual(len(conflicts), 1)
        self.assertEqual(conflicts[0].package.plugin, "research-authoring")
        self.assertEqual(conflicts[0].overlapping_skill_names, ("research-reporting",))

    def test_no_conflict_path_returns_empty(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            cache = Path(tmp) / ".codex" / "plugins" / "cache"
            make_cached_package(cache, "yuukias-ai-skills", "presentations", "0.4", ["slide-authoring"])

            conflicts = replay.detect_conflicting_cached_packages(cache, {"research-reporting"})

        self.assertEqual(conflicts, [])

    def test_detects_same_name_production_conflict(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            cache = Path(tmp) / ".codex" / "plugins" / "cache"
            make_cached_package(cache, "yuukias-ai-skills", "writing-style", "0.4", ["chinese-prose"])

            conflicts = replay.detect_conflicting_cached_packages(cache, {"chinese-prose"})

        self.assertEqual(len(conflicts), 1)
        self.assertEqual(conflicts[0].package.plugin, "writing-style")

    def test_multi_candidate_duplicate_skill_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            market = root / "marketplace"
            first = market / "plugins" / "alpha"
            second = market / "plugins" / "beta"
            write_skill(first, "one", "shared-skill")
            write_skill(second, "two", "shared-skill")
            candidates = [
                replay.CandidatePlugin(commit="abc", name="alpha", source_path="plugins/alpha"),
                replay.CandidatePlugin(commit="abc", name="beta", source_path="plugins/beta"),
            ]

            with self.assertRaisesRegex(replay.ReplayError, "duplicate top-level skill"):
                replay.candidate_skill_name_union(market, candidates)

    def test_quarantine_destination_is_outside_discovery_root_and_same_filesystem(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            codex_home = Path(tmp) / ".codex"
            discovery = codex_home / "plugins" / "cache"
            original = make_cached_package(discovery, "live", "research-authoring", "0.3.0", ["research-reporting"])
            parent = replay.quarantine_parent(codex_home, "run-1")
            dest = replay.quarantine_destination(
                parent,
                replay.cached_plugin_package_from_path(original, discovery),  # type: ignore[arg-type]
            )

            replay.validate_quarantine_destination(discovery, parent, original, dest)

        self.assertFalse(replay.is_relative_to_path(parent.resolve(), discovery.resolve()))

    def test_cross_filesystem_quarantine_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            codex_home = Path(tmp) / ".codex"
            discovery = codex_home / "plugins" / "cache"
            original = make_cached_package(discovery, "live", "research-authoring", "0.3.0", ["research-reporting"])
            parent = replay.quarantine_parent(codex_home, "run-1")
            real_stat = Path.stat

            def fake_stat(path: Path, *args, **kwargs):
                result = real_stat(path, *args, **kwargs)
                if Path(path) == parent:
                    fake = mock.Mock()
                    fake.st_dev = result.st_dev + 1
                    return fake
                return result

            with mock.patch.object(Path, "stat", fake_stat):
                with self.assertRaisesRegex(replay.ReplayError, "different filesystem"):
                    replay.validate_quarantine_destination(discovery, parent, original, parent / "live" / "x" / "1")

    def test_cache_hidden_quarantine_fallback_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            codex_home = Path(tmp) / ".codex"
            discovery = codex_home / "plugins" / "cache"
            original = make_cached_package(discovery, "live", "research-authoring", "0.3.0", ["research-reporting"])
            parent = discovery / ".candidate-plugin-replay-quarantine" / "run"

            with self.assertRaisesRegex(replay.ReplayError, "inside plugin discovery"):
                replay.validate_quarantine_destination(discovery, parent, original, parent / "live" / "x" / "1")

    def test_symlink_resolve_back_to_discovery_root_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            codex_home = Path(tmp) / ".codex"
            discovery = codex_home / "plugins" / "cache"
            original = make_cached_package(discovery, "live", "research-authoring", "0.3.0", ["research-reporting"])
            link = codex_home / "quarantine-link"
            link.symlink_to(discovery, target_is_directory=True)

            with self.assertRaisesRegex(replay.ReplayError, "inside plugin discovery"):
                replay.validate_quarantine_destination(discovery, link, original, link / "live" / "x" / "1")

    def test_success_restoration_restores_tree_and_removes_manifest(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            codex_home = root / ".codex"
            discovery = codex_home / "plugins" / "cache"
            original = make_cached_package(discovery, "live", "research-authoring", "0.3.0", ["research-reporting"])
            package = replay.cached_plugin_package_from_path(original, discovery)
            self.assertIsNotNone(package)
            paths = replay.runtime_paths(root)
            record = replay.QuarantineRecord(package=package, quarantine_path=replay.quarantine_parent(codex_home, "run") / "live" / "research-authoring" / "0.3.0", overlapping_skill_names=("research-reporting",))
            with mock.patch.object(replay, "effective_codex_home", return_value=codex_home.resolve()):
                transaction = replay.prepare_quarantine_transaction(paths, "run", {"plugins": []}, {}, [record])

            self.assertIsNotNone(transaction)
            assert transaction is not None
            replay.activate_quarantine(transaction)
            self.assertFalse(original.exists())
            self.assertTrue(record.quarantine_path.exists())
            replay.restore_quarantine(transaction)

            self.assertTrue(original.exists())
            self.assertFalse(transaction.manifest_path.exists())

    def test_timeout_or_exception_style_restoration_can_run_after_failure(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            codex_home = root / ".codex"
            discovery = codex_home / "plugins" / "cache"
            original = make_cached_package(discovery, "live", "research-authoring", "0.3.0", ["research-reporting"])
            package = replay.cached_plugin_package_from_path(original, discovery)
            self.assertIsNotNone(package)
            paths = replay.runtime_paths(root)
            record = replay.QuarantineRecord(package=package, quarantine_path=replay.quarantine_parent(codex_home, "run") / "live" / "research-authoring" / "0.3.0", overlapping_skill_names=("research-reporting",))
            with mock.patch.object(replay, "effective_codex_home", return_value=codex_home.resolve()):
                transaction = replay.prepare_quarantine_transaction(paths, "run", {"plugins": []}, {}, [record])
            assert transaction is not None
            replay.activate_quarantine(transaction)
            try:
                raise replay.ReplayError("child timed out")
            except replay.ReplayError:
                replay.restore_quarantine(transaction)

            self.assertTrue(original.exists())

    def test_catchable_sigterm_handler_restores_previous_handler(self) -> None:
        if os.name != "posix":
            self.skipTest("POSIX signal test")
        previous = signal.getsignal(signal.SIGTERM)
        with self.assertRaisesRegex(replay.ReplayError, "SIGTERM"):
            with replay.catch_sigterm_as_error():
                os.kill(os.getpid(), signal.SIGTERM)
        self.assertEqual(signal.getsignal(signal.SIGTERM), previous)

    def test_stale_quarantine_recovery_restores_missing_original(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            codex_home = root / ".codex"
            discovery = codex_home / "plugins" / "cache"
            original = make_cached_package(discovery, "live", "research-authoring", "0.3.0", ["research-reporting"])
            package = replay.cached_plugin_package_from_path(original, discovery)
            self.assertIsNotNone(package)
            paths = replay.runtime_paths(root)
            record = replay.QuarantineRecord(package=package, quarantine_path=replay.quarantine_parent(codex_home, "run") / "live" / "research-authoring" / "0.3.0", overlapping_skill_names=("research-reporting",))
            with mock.patch.object(replay, "effective_codex_home", return_value=codex_home.resolve()):
                transaction = replay.prepare_quarantine_transaction(paths, "run", {"plugins": []}, {}, [record])
            assert transaction is not None
            replay.activate_quarantine(transaction)
            recovered = replay.recover_stale_quarantines(paths)

            self.assertTrue(original.exists())
            self.assertIn(str(original.resolve()), recovered)

    def test_ambiguous_recovery_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            codex_home = root / ".codex"
            discovery = codex_home / "plugins" / "cache"
            original = make_cached_package(discovery, "live", "research-authoring", "0.3.0", ["research-reporting"])
            package = replay.cached_plugin_package_from_path(original, discovery)
            self.assertIsNotNone(package)
            paths = replay.runtime_paths(root)
            record = replay.QuarantineRecord(package=package, quarantine_path=replay.quarantine_parent(codex_home, "run") / "live" / "research-authoring" / "0.3.0", overlapping_skill_names=("research-reporting",))
            with mock.patch.object(replay, "effective_codex_home", return_value=codex_home.resolve()):
                transaction = replay.prepare_quarantine_transaction(paths, "run", {"plugins": []}, {}, [record])
            assert transaction is not None
            replay.activate_quarantine(transaction)
            make_cached_package(discovery, "live", "research-authoring", "0.3.0", ["research-reporting"])

            with self.assertRaisesRegex(replay.ReplayError, "RESTORATION_AMBIGUOUS"):
                replay.recover_stale_quarantines(paths)

    def test_equivalent_rehydration_deletes_only_transaction_owned_quarantine_duplicate(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            codex_home, _discovery, original, transaction, plugin_list = self.make_equivalent_rehydration_fixture(root)
            self.assertFalse(original.exists())
            quarantine = transaction.records[0].quarantine_path
            self.assertTrue(quarantine.exists())
            shutil.copytree(quarantine, original)

            result = replay.restore_quarantine(
                transaction,
                read_proof={
                    "candidate_path_reads": 1,
                    "original_conflict_path_reads": 0,
                    "quarantine_path_reads": 0,
                },
                current_plugin_list=plugin_list,
                codex_home=codex_home.resolve(),
            )

            self.assertTrue(result.verified_equivalent_rehydration)
            self.assertTrue(result.final_persistent_state_equivalent_to_before)
            self.assertTrue(original.exists())
            self.assertFalse(quarantine.exists())
            self.assertFalse(transaction.manifest_path.exists())
            self.assertEqual(replay.tree_sha256(original), transaction.records[0].package.tree_sha256)

    def test_equivalent_rehydration_records_config_drift_without_blocking_cleanup(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            codex_home, _discovery, original, transaction, plugin_list = self.make_equivalent_rehydration_fixture(root)
            quarantine = transaction.records[0].quarantine_path
            shutil.copytree(quarantine, original)
            (codex_home / "config.toml").write_text("changed = true\n", encoding="utf-8")

            result = replay.restore_quarantine(
                transaction,
                read_proof={
                    "candidate_path_reads": 1,
                    "original_conflict_path_reads": 0,
                    "quarantine_path_reads": 0,
                },
                current_plugin_list=plugin_list,
                codex_home=codex_home.resolve(),
            )

            self.assertTrue(result.verified_equivalent_rehydration)
            self.assertTrue(result.final_persistent_state_equivalent_to_before)
            self.assertTrue(original.exists())
            self.assertFalse(quarantine.exists())
            diagnostics = result.diagnostics or {}
            proof = diagnostics[str(original.resolve())]
            self.assertTrue(proof["config_hash_drift_observed"])
            self.assertIsNone(proof["recorded_config_hash_diagnostic"])
            self.assertEqual(proof["current_config_hash_diagnostic"], replay.config_hash(codex_home))
            self.assertEqual(proof["final_config_hash_diagnostic"], replay.config_hash(codex_home))

    def test_equivalent_rehydration_allows_current_run_candidate_ids_during_restore(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            codex_home, _discovery, original, transaction, plugin_list = self.make_equivalent_rehydration_fixture(root)
            quarantine = transaction.records[0].quarantine_path
            shutil.copytree(quarantine, original)
            current_list = {
                "plugins": plugin_list["plugins"]
                + [
                    {
                        "pluginId": "web-development@ai-skills-candidate",
                        "name": "web-development",
                        "enabled": True,
                        "marketplaceName": "ai-skills-candidate",
                    },
                    {
                        "pluginId": "writing-style@ai-skills-candidate",
                        "name": "writing-style",
                        "enabled": True,
                        "marketplaceName": "ai-skills-candidate",
                    },
                ]
            }

            result = replay.restore_quarantine(
                transaction,
                read_proof={
                    "candidate_path_reads": 1,
                    "original_conflict_path_reads": 0,
                    "quarantine_path_reads": 0,
                },
                current_plugin_list=current_list,
                final_plugin_list_reader=lambda: current_list,
                codex_home=codex_home.resolve(),
                ignored_plugin_ids={
                    "web-development@ai-skills-candidate",
                    "writing-style@ai-skills-candidate",
                },
            )

            self.assertTrue(result.verified_equivalent_rehydration)
            self.assertTrue(result.final_persistent_state_equivalent_to_before)
            self.assertFalse(quarantine.exists())

    def test_equivalent_rehydration_rejects_unrelated_state_change_during_restore(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            codex_home, _discovery, original, transaction, plugin_list = self.make_equivalent_rehydration_fixture(root)
            quarantine = transaction.records[0].quarantine_path
            shutil.copytree(quarantine, original)
            current_list = {
                "plugins": plugin_list["plugins"]
                + [
                    {"pluginId": "writing-style@ai-skills-candidate", "enabled": True},
                    {"pluginId": "unrelated@yuukias-ai-skills", "enabled": True},
                ]
            }

            with self.assertRaisesRegex(replay.ReplayError, "normalized plugin state mismatch"):
                replay.restore_quarantine(
                    transaction,
                    read_proof={
                        "candidate_path_reads": 1,
                        "original_conflict_path_reads": 0,
                        "quarantine_path_reads": 0,
                    },
                    current_plugin_list=current_list,
                    codex_home=codex_home.resolve(),
                    ignored_plugin_ids={"writing-style@ai-skills-candidate"},
                )

            self.assertTrue(original.exists())
            self.assertTrue(quarantine.exists())
            self.assertTrue(transaction.manifest_path.exists())

    def test_equivalent_rehydration_rejects_non_current_run_candidate_plugin(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            codex_home, _discovery, original, transaction, plugin_list = self.make_equivalent_rehydration_fixture(root)
            quarantine = transaction.records[0].quarantine_path
            shutil.copytree(quarantine, original)
            current_list = {
                "plugins": plugin_list["plugins"]
                + [
                    {"pluginId": "writing-style@ai-skills-candidate", "enabled": True},
                    {"pluginId": "other@ai-skills-candidate", "enabled": True},
                ]
            }

            with self.assertRaisesRegex(replay.ReplayError, "normalized plugin state mismatch"):
                replay.restore_quarantine(
                    transaction,
                    read_proof={
                        "candidate_path_reads": 1,
                        "original_conflict_path_reads": 0,
                        "quarantine_path_reads": 0,
                    },
                    current_plugin_list=current_list,
                    codex_home=codex_home.resolve(),
                    ignored_plugin_ids={"writing-style@ai-skills-candidate"},
                )

            self.assertTrue(original.exists())
            self.assertTrue(quarantine.exists())
            self.assertTrue(transaction.manifest_path.exists())

    def test_equivalent_rehydration_rechecks_plugin_state_after_prior_normal_restore(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            codex_home = root / ".codex"
            discovery = codex_home / "plugins" / "cache"
            dual_original = make_cached_package(
                discovery,
                "created-by-me-remote",
                "research-authoring",
                "0.3.0",
                ["writing-fidelity"],
            )
            normal_original = make_cached_package(
                discovery,
                "yuukias-ai-skills",
                "writing-style",
                "0.4",
                ["writing-fidelity"],
            )
            dual_package = replay.cached_plugin_package_from_path(dual_original, discovery)
            normal_package = replay.cached_plugin_package_from_path(normal_original, discovery)
            self.assertIsNotNone(dual_package)
            self.assertIsNotNone(normal_package)
            assert dual_package is not None
            assert normal_package is not None
            before_list = {
                "plugins": [
                    {
                        "pluginId": "writing-style@yuukias-ai-skills",
                        "name": "writing-style",
                        "enabled": True,
                        "marketplaceName": "yuukias-ai-skills",
                    },
                    {
                        "pluginId": "research-writing@yuukias-ai-skills",
                        "name": "research-writing",
                        "enabled": True,
                        "marketplaceName": "yuukias-ai-skills",
                    },
                ]
            }
            current_before_restore = {
                "plugins": [
                    before_list["plugins"][1],
                    {
                        "pluginId": "writing-style@ai-skills-candidate",
                        "name": "writing-style",
                        "enabled": True,
                        "marketplaceName": "ai-skills-candidate",
                    },
                ]
            }
            current_after_normal_restore = {
                "plugins": before_list["plugins"]
                + [
                    {
                        "pluginId": "writing-style@ai-skills-candidate",
                        "name": "writing-style",
                        "enabled": True,
                        "marketplaceName": "ai-skills-candidate",
                    }
                ]
            }
            paths = replay.runtime_paths(root)
            records = [
                replay.QuarantineRecord(
                    package=dual_package,
                    quarantine_path=(
                        replay.quarantine_parent(codex_home, "run")
                        / "created-by-me-remote"
                        / "research-authoring"
                        / "0.3.0"
                    ),
                    overlapping_skill_names=("writing-fidelity",),
                ),
                replay.QuarantineRecord(
                    package=normal_package,
                    quarantine_path=(
                        replay.quarantine_parent(codex_home, "run")
                        / "yuukias-ai-skills"
                        / "writing-style"
                        / "0.4"
                    ),
                    overlapping_skill_names=("writing-fidelity",),
                ),
            ]
            with mock.patch.object(replay, "effective_codex_home", return_value=codex_home.resolve()):
                transaction = replay.prepare_quarantine_transaction(paths, "run", before_list, {}, records)
            self.assertIsNotNone(transaction)
            assert transaction is not None
            replay.activate_quarantine(transaction)
            shutil.copytree(transaction.records[0].quarantine_path, dual_original)

            result = replay.restore_quarantine(
                transaction,
                read_proof={
                    "candidate_path_reads": 1,
                    "original_conflict_path_reads": 0,
                    "quarantine_path_reads": 0,
                },
                current_plugin_list=current_before_restore,
                final_plugin_list_reader=lambda: current_after_normal_restore,
                codex_home=codex_home.resolve(),
                ignored_plugin_ids={"writing-style@ai-skills-candidate"},
            )

            self.assertTrue(result.verified_equivalent_rehydration)
            self.assertTrue(result.final_persistent_state_equivalent_to_before)
            self.assertTrue(dual_original.exists())
            self.assertTrue(normal_original.exists())
            self.assertFalse(transaction.records[0].quarantine_path.exists())
            self.assertFalse(transaction.records[1].quarantine_path.exists())

    def test_equivalent_rehydration_without_candidate_proof_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            codex_home, _discovery, original, transaction, plugin_list = self.make_equivalent_rehydration_fixture(root)
            quarantine = transaction.records[0].quarantine_path
            shutil.copytree(quarantine, original)

            with self.assertRaisesRegex(replay.ReplayError, "candidate consumption proof"):
                replay.restore_quarantine(
                    transaction,
                    read_proof={
                        "candidate_path_reads": 0,
                        "original_conflict_path_reads": 0,
                        "quarantine_path_reads": 0,
                    },
                    current_plugin_list=plugin_list,
                    codex_home=codex_home.resolve(),
                )

            self.assertTrue(original.exists())
            self.assertTrue(quarantine.exists())
            self.assertTrue(transaction.manifest_path.exists())

    def test_equivalent_rehydration_with_conflict_read_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            codex_home, _discovery, original, transaction, plugin_list = self.make_equivalent_rehydration_fixture(root)
            quarantine = transaction.records[0].quarantine_path
            shutil.copytree(quarantine, original)

            with self.assertRaisesRegex(replay.ReplayError, "conflict package read proof"):
                replay.restore_quarantine(
                    transaction,
                    read_proof={
                        "candidate_path_reads": 1,
                        "original_conflict_path_reads": 1,
                        "quarantine_path_reads": 0,
                    },
                    current_plugin_list=plugin_list,
                    codex_home=codex_home.resolve(),
                )

            self.assertTrue(original.exists())
            self.assertTrue(quarantine.exists())
            self.assertTrue(transaction.manifest_path.exists())

    def test_equivalent_rehydration_hash_mismatch_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            codex_home, _discovery, original, transaction, plugin_list = self.make_equivalent_rehydration_fixture(root)
            quarantine = transaction.records[0].quarantine_path
            shutil.copytree(quarantine, original)
            (original / "skills" / "skill-1" / "SKILL.md").write_text("changed\n", encoding="utf-8")

            with self.assertRaisesRegex(replay.ReplayError, "tree hash mismatch"):
                replay.restore_quarantine(
                    transaction,
                    read_proof={
                        "candidate_path_reads": 1,
                        "original_conflict_path_reads": 0,
                        "quarantine_path_reads": 0,
                    },
                    current_plugin_list=plugin_list,
                    codex_home=codex_home.resolve(),
                )

            self.assertTrue(original.exists())
            self.assertTrue(quarantine.exists())
            self.assertTrue(transaction.manifest_path.exists())

    def test_run_replay_allows_verified_equivalent_rehydration_without_conflict_reads(self) -> None:
        tmp, root, commit = make_repo()
        self.addCleanup(tmp.cleanup)
        (root / "task.md").write_text("Do the task.\n", encoding="utf-8")
        (root / "input.md").write_text("Input.\n", encoding="utf-8")
        codex_home = root / ".codex"
        discovery = codex_home / "plugins" / "cache"
        original = make_cached_package(
            discovery,
            "created-by-me-remote",
            "research-authoring",
            "0.3.0",
            ["research-reporting"],
        )
        package = replay.cached_plugin_package_from_path(original, discovery)
        self.assertIsNotNone(package)
        assert package is not None
        conflict = replay.QuarantineRecord(
            package=package,
            quarantine_path=Path(),
            overlapping_skill_names=("research-reporting",),
        )
        installed = root / "plugins" / "cache" / "ai-skills-candidate" / "writing-style" / "0.1"
        installed.mkdir(parents=True)
        before_list = {
            "plugins": [
                {
                    "pluginId": "research-authoring@created-by-me-remote",
                    "name": "research-authoring",
                    "enabled": True,
                    "marketplaceName": "created-by-me-remote",
                    "installedPath": str(original),
                }
            ]
        }
        candidate_plugin_list = {
            "plugins": before_list["plugins"]
            + [
                {
                    "pluginId": "writing-style@ai-skills-candidate",
                    "name": "writing-style",
                    "enabled": True,
                    "marketplaceName": "ai-skills-candidate",
                    "installedPath": str(installed),
                }
            ]
        }
        candidate_installed = {"value": False}
        remove_calls: list[str] = []

        def fake_stage(_root: Path, _candidates: list[replay.CandidatePlugin], run_dir: Path) -> Path:
            marketplace = run_dir / "marketplace"
            marketplace.mkdir(parents=True)
            return marketplace

        def fake_run_codex_json(_codex: Path, args: list[str], **_kwargs):
            if args[:3] == ["plugin", "list", "--json"]:
                return candidate_plugin_list if candidate_installed["value"] else before_list
            return None

        def fake_child(*_args, **_kwargs):
            quarantines = list((codex_home / ".candidate-plugin-replay-quarantine").glob("*/*/*/*"))
            self.assertEqual(len(quarantines), 1)
            self.assertFalse(original.exists())
            shutil.copytree(quarantines[0], original)
            event = {
                "type": "item.completed",
                "item": {
                    "type": "command_execution",
                    "command": f"cat {installed}/skills/zh/SKILL.md",
                },
            }
            return replay.CommandResult(("codex", "exec"), 0, json.dumps(event) + "\n", "")

        with mock.patch.object(replay, "ensure_runtime_available", return_value={"version": replay.EXPECTED_CODEX_VERSION}):
            with mock.patch.object(replay, "safe_stage_candidates", side_effect=fake_stage):
                with mock.patch.object(replay, "run_codex_json", side_effect=fake_run_codex_json):
                    with mock.patch.object(
                        replay,
                        "add_candidate_plugin",
                        side_effect=lambda *_args, **_kwargs: (
                            candidate_installed.__setitem__("value", True)
                            or ("writing-style@ai-skills-candidate", str(installed), {})
                        ),
                    ):
                        with mock.patch.object(replay, "effective_codex_home", return_value=codex_home.resolve()):
                            with mock.patch.object(replay, "detect_conflicting_cached_packages", return_value=[conflict]):
                                with mock.patch.object(replay, "assert_no_concurrent_codex_consumers"):
                                    with mock.patch.object(replay, "run_child_exec", side_effect=fake_child):
                                        with mock.patch.object(
                                            replay,
                                            "remove_candidate_plugin",
                                            side_effect=lambda _c, plugin_id: (
                                                remove_calls.append(plugin_id),
                                                candidate_installed.__setitem__("value", False),
                                            ),
                                        ):
                                            result = replay.run_replay(
                                                root,
                                                "writing-style",
                                                commit,
                                                "task.md",
                                                ["input.md"],
                                            )

        self.assertEqual(remove_calls, ["writing-style@ai-skills-candidate"])
        self.assertTrue(result["restoration"]["verified_equivalent_rehydration"])
        self.assertTrue(result["consumer_isolation"]["final_persistent_state_equivalent_to_before"])
        self.assertTrue(original.exists())
        self.assertFalse(any((codex_home / ".candidate-plugin-replay-quarantine").glob("*/*/*/*")))

    def test_three_way_candidate_original_quarantine_read_proof(self) -> None:
        candidate = "/home/me/.codex/plugins/cache/ai-skills-candidate/research-writing/0.3"
        original = "/home/me/.codex/plugins/cache/created-by-me-remote/research-authoring/0.3.0"
        quarantine = "/home/me/.codex/.candidate-plugin-replay-quarantine/run/created-by-me-remote/research-authoring/0.3.0"
        stdout = "\n".join(
            [
                json.dumps({"type": "item.completed", "item": {"type": "command_execution", "command": f"cat {candidate}/skills/report/SKILL.md"}}),
                json.dumps({"type": "item.completed", "item": {"type": "command_execution", "command": f"cat {original}/skills/report/SKILL.md"}}),
                json.dumps({"type": "item.completed", "item": {"type": "command_execution", "command": f"cat {quarantine}/skills/report/SKILL.md"}}),
            ]
        )

        self.assertEqual(len(replay.parse_candidate_read_events(stdout, [candidate])), 1)
        self.assertEqual(len(replay.parse_skill_read_events(stdout, [original])), 1)
        self.assertEqual(len(replay.parse_skill_read_events(stdout, [quarantine])), 1)

    def test_concurrency_preflight_positive_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            codex_home = Path(tmp) / ".codex"
            ps = f"99999 1 S 00:01 codex exec CODEX_HOME={codex_home} --json\n"
            with mock.patch.object(replay, "run_command", return_value=replay.CommandResult(("ps",), 0, ps, "")):
                with mock.patch.object(replay, "ancestor_pids", return_value={os.getpid()}):
                    with self.assertRaisesRegex(replay.ReplayError, "CONCURRENT_SHARED_CODEX_HOME_CONSUMER"):
                        replay.assert_no_concurrent_codex_consumers(codex_home)

    def test_concurrency_preflight_ignores_current_process_tree(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            codex_home = Path(tmp) / ".codex"
            ps = f"{os.getpid()} 1 S 00:01 codex exec CODEX_HOME={codex_home} --json\n"
            with mock.patch.object(replay, "run_command", return_value=replay.CommandResult(("ps",), 0, ps, "")):
                with mock.patch.object(replay, "ancestor_pids", return_value={os.getpid()}):
                    replay.assert_no_concurrent_codex_consumers(codex_home)

    def test_concurrency_preflight_does_not_match_codex_run_substring(self) -> None:
        codex_home = Path("/users/a/e/aereinh/.codex")
        command = "/path/to/codex app-server proxy --sock /users/a/e/aereinh/.codex-run/as/socket"

        self.assertFalse(replay.command_has_explicit_codex_home(command, codex_home))


if __name__ == "__main__":
    unittest.main()
