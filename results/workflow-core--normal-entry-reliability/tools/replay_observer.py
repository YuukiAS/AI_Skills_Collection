#!/usr/bin/env python3
from __future__ import annotations

import argparse
import contextlib
import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import candidate_plugin_replay as replay  # noqa: E402


def run_child_exec_with_env(
    codex: Path,
    marketplace_root: Path,
    plugin_ids: list[str],
    workspace: Path,
    output_dir: Path,
    prompt: str,
    stdout_path: Path,
    stderr_path: Path,
    writable_dirs: list[Path],
    extra_env: dict[str, str],
) -> replay.CommandResult:
    args = [
        str(codex),
        "exec",
        "--ignore-user-config",
        "--json",
        *replay.codex_config_args(marketplace_root),
    ]
    for plugin_id in plugin_ids:
        args.extend(["-c", f"plugins.{plugin_id}.enabled=true"])
    args.extend(
        [
            "-s",
            "workspace-write",
            "-C",
            str(workspace),
            "--add-dir",
            str(output_dir),
        ]
    )
    for writable_dir in writable_dirs:
        args.extend(["--add-dir", str(writable_dir)])
    args.extend(["--skip-git-repo-check", "--ephemeral", "-"])

    stdout_path.parent.mkdir(parents=True, exist_ok=True)
    stderr_path.parent.mkdir(parents=True, exist_ok=True)
    env = os.environ.copy()
    env.update(extra_env)
    with stdout_path.open("w", encoding="utf-8") as stdout_fh:
        with stderr_path.open("w", encoding="utf-8") as stderr_fh:
            proc = subprocess.Popen(
                args,
                stdin=subprocess.PIPE,
                stdout=stdout_fh,
                stderr=stderr_fh,
                text=True,
                start_new_session=os.name == "posix",
                env=env,
            )
            proc.communicate(input=prompt, timeout=replay.DEFAULT_CHILD_TIMEOUT_SECONDS)
    return replay.CommandResult(
        tuple(args),
        proc.returncode,
        stdout_path.read_text(encoding="utf-8"),
        stderr_path.read_text(encoding="utf-8"),
    )


def collect_command_events(stdout: str) -> list[str]:
    commands: list[str] = []
    for line in stdout.splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        commands.extend(replay.command_execution_evidence_strings(event))
    return commands


def copy_tree_contents(source: Path, dest: Path) -> None:
    if dest.exists():
        shutil.rmtree(dest)
    dest.mkdir(parents=True)
    for item in source.iterdir():
        target = dest / item.name
        if item.is_dir():
            shutil.copytree(item, target)
        else:
            shutil.copy2(item, target)


def parse_env(items: list[str]) -> dict[str, str]:
    env: dict[str, str] = {}
    for item in items:
        if "=" not in item:
            raise replay.ReplayError(f"--env must be KEY=VALUE, got {item!r}")
        key, value = item.split("=", 1)
        if not key:
            raise replay.ReplayError("--env key must not be empty")
        env[key] = value
    return env


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Task-local candidate replay observer.")
    parser.add_argument("--candidate-commit", required=True)
    parser.add_argument("--task", required=True)
    parser.add_argument("--input", action="append", default=[], required=True)
    parser.add_argument("--plugin", action="append", default=[], required=True)
    parser.add_argument("--expect-consumed", action="append", default=[])
    parser.add_argument("--expect-not-consumed", action="append", default=[])
    parser.add_argument("--writable-dir", action="append", default=[])
    parser.add_argument("--env", action="append", default=[])
    parser.add_argument("--copy-run-to", required=True)
    parser.add_argument("--label", required=True)
    args = parser.parse_args(argv)

    root = REPO_ROOT
    runtime = replay.ensure_runtime_available(root)
    paths = replay.runtime_paths(root)
    candidates = [replay.resolve_candidate_plugin(root, args.candidate_commit, item) for item in args.plugin]
    resolved_commit = candidates[0].commit
    if any(candidate.commit != resolved_commit for candidate in candidates):
        raise replay.ReplayError("candidate plugins must resolve to the same commit")

    task = replay.repo_relative_existing_file(root, args.task)
    inputs = [replay.repo_relative_existing_file(root, item) for item in args.input]
    writable_dirs = [replay.repo_relative_existing_dir(root, item) for item in args.writable_dir]
    extra_env = parse_env(args.env)
    run_id = time.strftime("%Y%m%dT%H%M%SZ", time.gmtime()) + f"-{os.getpid()}-{args.label}"
    run_dir = root / ".local-runtime" / "workflow-core--normal-entry-reliability" / "observer-runs" / run_id
    run_dir.mkdir(parents=True, exist_ok=True)

    plugin_ids = [f"{plugin}@ai-skills-candidate" for plugin in args.plugin]
    installed_paths: dict[str, str] = {}
    add_payloads: dict[str, Any] = {}
    before_snapshots: dict[str, list[dict[str, Any]]] = {}
    try:
        with replay.replay_lock(root):
            replay.cleanup_stale_candidates(paths.codex)
            before_list = replay.run_codex_json(paths.codex, ["plugin", "list", "--json"])
            before_snapshots = {
                plugin: replay.same_name_installed_snapshot(before_list, plugin)
                for plugin in args.plugin
            }
            marketplace_root = replay.safe_stage_candidates(root, candidates, run_dir)
            try:
                for plugin in args.plugin:
                    plugin_id, installed_path, add_payload = replay.add_candidate_plugin(paths.codex, marketplace_root, plugin)
                    installed_paths[plugin] = installed_path
                    add_payloads[plugin] = add_payload
                (run_dir / "plugin-add.json").write_text(
                    json.dumps(add_payloads, indent=2, sort_keys=True) + "\n",
                    encoding="utf-8",
                )
                workspace, output_dir, prompt = replay.prepare_workspace(root, run_dir, task, inputs)
                stdout_path = run_dir / "child.stdout.jsonl"
                stderr_path = run_dir / "child.stderr"
                child = run_child_exec_with_env(
                    paths.codex,
                    marketplace_root,
                    plugin_ids,
                    workspace,
                    output_dir,
                    prompt,
                    stdout_path,
                    stderr_path,
                    writable_dirs,
                    extra_env,
                )
                consumption = {
                    plugin: replay.parse_consumption(child.stdout, installed_path)
                    for plugin, installed_path in installed_paths.items()
                }
                consumed = {
                    plugin: (
                        None
                        if evidence is None
                        else {"proven": True, "event_type": evidence.event_type, "line_index": evidence.line_index}
                    )
                    for plugin, evidence in consumption.items()
                }
                missing = [plugin for plugin in args.expect_consumed if consumption.get(plugin) is None]
                unexpected = [plugin for plugin in args.expect_not_consumed if consumption.get(plugin) is not None]
                result = {
                    "label": args.label,
                    "candidate_commit": resolved_commit,
                    "runtime_version": runtime["version"],
                    "plugins": [
                        {
                            "name": plugin,
                            "plugin_id": f"{plugin}@ai-skills-candidate",
                            "installed_path": installed_paths[plugin],
                            "add_payload": add_payloads[plugin],
                            "actual_consumption": consumed[plugin],
                        }
                        for plugin in args.plugin
                    ],
                    "expect_consumed": args.expect_consumed,
                    "expect_not_consumed": args.expect_not_consumed,
                    "expectation_failures": {"missing": missing, "unexpected": unexpected},
                    "command_events": collect_command_events(child.stdout),
                    "stdout_path": str(stdout_path),
                    "stderr_path": str(stderr_path),
                    "extra_env_keys": sorted(extra_env),
                    "writable_dirs": [str(path) for path in writable_dirs],
                    "child_returncode": child.returncode,
                }
                (run_dir / "run.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
                copy_tree_contents(run_dir, root / args.copy_run_to)
                if child.returncode != 0:
                    raise replay.ReplayError(f"child exec failed ({child.returncode}): {child.stderr.strip()}")
                if missing or unexpected:
                    raise replay.ReplayError(f"consumption expectation failed: {result['expectation_failures']}")
            finally:
                for plugin_id in plugin_ids:
                    with contextlib.suppress(Exception):
                        replay.remove_candidate_plugin(paths.codex, plugin_id)
                with contextlib.suppress(Exception):
                    shutil.rmtree(run_dir / "marketplace")
                after_list = replay.run_codex_json(paths.codex, ["plugin", "list", "--json"])
                replay.assert_candidate_absent(after_list)
                for plugin in args.plugin:
                    replay.assert_production_unchanged(
                        before_snapshots[plugin],
                        replay.same_name_installed_snapshot(after_list, plugin),
                    )
        return 0
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        with contextlib.suppress(Exception):
            copy_tree_contents(run_dir, root / args.copy_run_to)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
