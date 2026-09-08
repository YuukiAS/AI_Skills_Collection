#!/usr/bin/env python3
from __future__ import annotations

import argparse
import contextlib
import fcntl
import hashlib
import io
import json
import os
import platform
import shutil
import stat
import subprocess
import sys
import tarfile
import tempfile
import time
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable


CODEX_VERSION = "0.153.4"
EXPECTED_CODEX_VERSION = f"codex-cli {CODEX_VERSION}"
RELEASE_TAG = f"rust-v{CODEX_VERSION}"
ASSET_NAME = "codex-x86_64-unknown-linux-musl.tar.gz"
ASSET_URL = f"https://github.com/openai/codex/releases/download/{RELEASE_TAG}/{ASSET_NAME}"
ASSET_SHA256 = "f479424eca092484dc40d87ae28c44f4cc40234a60045d6131e493800d814a30"

MARKETPLACE_NAME = "ai-skills-candidate"
CANDIDATE_NAMESPACE_SUFFIX = f"@{MARKETPLACE_NAME}"
MARKETPLACE_JSON = ".agents/plugins/marketplace.json"


class ReplayError(RuntimeError):
    pass


@dataclass(frozen=True)
class RuntimePaths:
    root: Path
    archive: Path
    bin_dir: Path
    codex: Path
    manifest: Path
    state_root: Path


@dataclass(frozen=True)
class CommandResult:
    args: tuple[str, ...]
    returncode: int
    stdout: str
    stderr: str


@dataclass(frozen=True)
class CandidatePlugin:
    commit: str
    name: str
    source_path: str


@dataclass(frozen=True)
class ConsumptionEvidence:
    line_index: int
    event_type: str


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def runtime_paths(root: Path) -> RuntimePaths:
    runtime_root = root / ".local-runtime" / "codex" / CODEX_VERSION
    return RuntimePaths(
        root=runtime_root,
        archive=runtime_root / "downloads" / ASSET_NAME,
        bin_dir=runtime_root / "bin",
        codex=runtime_root / "bin" / "codex",
        manifest=runtime_root / "runtime.json",
        state_root=root / ".local-runtime" / "candidate-plugin-replay",
    )


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def run_command(
    args: list[str],
    *,
    cwd: Path | None = None,
    input_text: str | None = None,
    input_bytes: bytes | None = None,
    check: bool = True,
) -> CommandResult:
    if input_text is not None and input_bytes is not None:
        raise ValueError("input_text and input_bytes are mutually exclusive")
    proc = subprocess.run(
        args,
        cwd=str(cwd) if cwd else None,
        input=input_bytes if input_bytes is not None else input_text,
        text=input_bytes is None,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    stdout = proc.stdout.decode("utf-8", "replace") if isinstance(proc.stdout, bytes) else proc.stdout
    stderr = proc.stderr.decode("utf-8", "replace") if isinstance(proc.stderr, bytes) else proc.stderr
    result = CommandResult(tuple(args), proc.returncode, stdout, stderr)
    if check and result.returncode != 0:
        raise ReplayError(f"command failed ({result.returncode}): {' '.join(args)}\n{stderr.strip()}")
    return result


def git(root: Path, args: list[str], *, input_bytes: bytes | None = None, check: bool = True) -> CommandResult:
    return run_command(["git", *args], cwd=root, input_bytes=input_bytes, check=check)


def ensure_linux_x86_64() -> None:
    if platform.system() != "Linux" or platform.machine() not in {"x86_64", "AMD64"}:
        raise ReplayError("this tool currently supports only Linux x86_64")


def codex_version(codex: Path) -> str:
    result = run_command([str(codex), "--version"], check=True)
    return result.stdout.strip().splitlines()[-1].strip()


def read_runtime_manifest(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise ReplayError("runtime manifest is missing")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ReplayError(f"runtime manifest is invalid JSON: {exc}") from exc


def validate_runtime(paths: RuntimePaths) -> dict[str, Any]:
    if not paths.codex.exists():
        raise ReplayError("runtime missing; run: python scripts/candidate_plugin_replay.py ensure-runtime")
    if not paths.archive.exists():
        raise ReplayError("runtime archive missing; run: python scripts/candidate_plugin_replay.py ensure-runtime")
    manifest = read_runtime_manifest(paths.manifest)
    archive_sha = sha256_file(paths.archive)
    binary_sha = sha256_file(paths.codex)
    version = codex_version(paths.codex)
    if manifest.get("asset_url") != ASSET_URL:
        raise ReplayError("runtime manifest URL mismatch")
    if manifest.get("asset_sha256") != ASSET_SHA256 or archive_sha != ASSET_SHA256:
        raise ReplayError("runtime archive SHA256 mismatch")
    if manifest.get("binary_sha256") != binary_sha:
        raise ReplayError("runtime binary SHA256 mismatch")
    if manifest.get("version") != EXPECTED_CODEX_VERSION or version != EXPECTED_CODEX_VERSION:
        raise ReplayError(f"runtime version mismatch: expected {EXPECTED_CODEX_VERSION}, got {version}")
    return {
        "version": version,
        "archive_sha256": archive_sha,
        "binary_sha256": binary_sha,
        "path": str(paths.codex),
    }


def safe_extract_tar(archive: Path, dest: Path) -> None:
    dest.mkdir(parents=True, exist_ok=True)
    dest_resolved = dest.resolve()
    with tarfile.open(archive, "r:gz") as tf:
        for member in tf.getmembers():
            target = (dest / member.name).resolve()
            if dest_resolved != target and dest_resolved not in target.parents:
                raise ReplayError(f"refusing archive path outside runtime dir: {member.name}")
        extract_members(tf, dest)


def extract_members(tf: tarfile.TarFile, dest: Path) -> None:
    try:
        tf.extractall(dest, filter="data")
    except TypeError:
        tf.extractall(dest)


def install_codex_from_archive(paths: RuntimePaths) -> None:
    with tempfile.TemporaryDirectory(prefix="codex-runtime-", dir=str(paths.root)) as tmp_name:
        tmp = Path(tmp_name)
        safe_extract_tar(paths.archive, tmp)
        candidates = [p for p in tmp.rglob("*") if p.is_file() and p.name.startswith("codex")]
        if not candidates:
            raise ReplayError("downloaded archive did not contain a codex executable")
        source = candidates[0]
        paths.bin_dir.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, paths.codex)
        mode = paths.codex.stat().st_mode
        paths.codex.chmod(mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)


def ensure_runtime(root: Path) -> dict[str, Any]:
    ensure_linux_x86_64()
    paths = runtime_paths(root)
    if paths.codex.exists() and paths.archive.exists() and paths.manifest.exists():
        return validate_runtime(paths)

    paths.archive.parent.mkdir(parents=True, exist_ok=True)
    paths.root.mkdir(parents=True, exist_ok=True)
    tmp_archive = paths.archive.with_suffix(paths.archive.suffix + ".tmp")
    with urllib.request.urlopen(ASSET_URL, timeout=60) as response:
        with tmp_archive.open("wb") as out:
            shutil.copyfileobj(response, out)
    archive_sha = sha256_file(tmp_archive)
    if archive_sha != ASSET_SHA256:
        tmp_archive.unlink(missing_ok=True)
        raise ReplayError("downloaded runtime archive SHA256 mismatch")
    tmp_archive.replace(paths.archive)
    install_codex_from_archive(paths)
    version = codex_version(paths.codex)
    if version != EXPECTED_CODEX_VERSION:
        raise ReplayError(f"runtime version mismatch: expected {EXPECTED_CODEX_VERSION}, got {version}")
    manifest = {
        "asset_url": ASSET_URL,
        "asset_sha256": ASSET_SHA256,
        "binary_sha256": sha256_file(paths.codex),
        "version": version,
        "installed_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    }
    paths.manifest.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return validate_runtime(paths)


def ensure_runtime_available(root: Path) -> dict[str, Any]:
    ensure_linux_x86_64()
    return validate_runtime(runtime_paths(root))


def resolve_commit(root: Path, candidate_commit: str) -> str:
    result = git(root, ["rev-parse", "--verify", f"{candidate_commit}^{{commit}}"], check=False)
    if result.returncode != 0:
        raise ReplayError(f"unknown candidate commit: {candidate_commit}")
    return result.stdout.strip()


def git_show_text(root: Path, commit: str, rel_path: str) -> str:
    result = git(root, ["show", f"{commit}:{rel_path}"], check=False)
    if result.returncode != 0:
        raise ReplayError(f"candidate commit does not contain {rel_path}")
    return result.stdout


def committed_path_exists(root: Path, commit: str, rel_path: str) -> bool:
    result = git(root, ["cat-file", "-e", f"{commit}:{rel_path}"], check=False)
    return result.returncode == 0


def normalize_local_source_path(path: str) -> str:
    raw = Path(path)
    if raw.is_absolute():
        raise ReplayError("candidate plugin source path must be repository-local")
    parts = raw.parts
    if any(part == ".." for part in parts):
        raise ReplayError("candidate plugin source path must not escape the repository")
    normalized = raw.as_posix()
    if normalized.startswith("./"):
        normalized = normalized[2:]
    if not normalized or normalized == ".":
        raise ReplayError("candidate plugin source path is empty")
    return normalized


def resolve_candidate_plugin(root: Path, candidate_commit: str, plugin_name: str) -> CandidatePlugin:
    commit = resolve_commit(root, candidate_commit)
    try:
        marketplace = json.loads(git_show_text(root, commit, MARKETPLACE_JSON))
    except json.JSONDecodeError as exc:
        raise ReplayError(f"candidate marketplace JSON is invalid: {exc}") from exc
    matches = [item for item in marketplace.get("plugins", []) if item.get("name") == plugin_name]
    if len(matches) != 1:
        raise ReplayError(f"plugin {plugin_name!r} must appear exactly once in committed marketplace")
    source = matches[0].get("source")
    if not isinstance(source, dict) or source.get("source") != "local":
        raise ReplayError("candidate plugin source must be local")
    source_path = source.get("path")
    if not isinstance(source_path, str):
        raise ReplayError("candidate plugin local source path is missing")
    rel_path = normalize_local_source_path(source_path)
    if not committed_path_exists(root, commit, f"{rel_path}/.codex-plugin/plugin.json"):
        raise ReplayError(f"candidate plugin source missing .codex-plugin/plugin.json at {rel_path}")
    return CandidatePlugin(commit=commit, name=plugin_name, source_path=rel_path)


def lock_path(root: Path) -> Path:
    path = runtime_paths(root).state_root / "candidate-plugin-replay.lock"
    path.parent.mkdir(parents=True, exist_ok=True)
    return path


@contextlib.contextmanager
def replay_lock(root: Path):
    path = lock_path(root)
    with path.open("w", encoding="utf-8") as fh:
        fcntl.flock(fh.fileno(), fcntl.LOCK_EX)
        try:
            yield
        finally:
            fcntl.flock(fh.fileno(), fcntl.LOCK_UN)


def codex_config_args(marketplace_root: Path) -> list[str]:
    return [
        "-c",
        f'marketplaces.{MARKETPLACE_NAME}.source_type="local"',
        "-c",
        f'marketplaces.{MARKETPLACE_NAME}.source="{marketplace_root}"',
    ]


def run_codex_json(codex: Path, args: list[str], *, cwd: Path | None = None, check: bool = True) -> Any:
    result = run_command([str(codex), *args], cwd=cwd, check=check)
    text = result.stdout.strip()
    if not text:
        return None
    try:
        return json.loads(text)
    except json.JSONDecodeError as exc:
        raise ReplayError(f"codex command did not return valid JSON: {exc}") from exc


def iter_dicts(value: Any) -> Iterable[dict[str, Any]]:
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from iter_dicts(child)
    elif isinstance(value, list):
        for child in value:
            yield from iter_dicts(child)


def first_string_value(value: Any, keys: set[str]) -> str | None:
    for item in iter_dicts(value):
        for key in keys:
            found = item.get(key)
            if isinstance(found, str) and found:
                return found
    return None


def plugin_records(payload: Any) -> list[dict[str, Any]]:
    records = []
    for item in iter_dicts(payload):
        if any(key in item for key in {"pluginId", "plugin_id", "id", "name", "installedPath"}):
            records.append(item)
    return records


def record_plugin_id(record: dict[str, Any]) -> str | None:
    for key in ("pluginId", "plugin_id", "id"):
        value = record.get(key)
        if isinstance(value, str):
            return value
    return None


def record_plugin_name(record: dict[str, Any]) -> str | None:
    value = record.get("name")
    return value if isinstance(value, str) else None


def record_enabled(record: dict[str, Any]) -> bool | None:
    value = record.get("enabled")
    return value if isinstance(value, bool) else None


def candidate_plugin_ids(payload: Any) -> list[str]:
    ids = []
    for record in plugin_records(payload):
        plugin_id = record_plugin_id(record)
        if plugin_id and plugin_id.endswith(CANDIDATE_NAMESPACE_SUFFIX):
            ids.append(plugin_id)
    return sorted(set(ids))


def same_name_installed_snapshot(payload: Any, plugin_name: str) -> list[dict[str, Any]]:
    snapshot = []
    for record in plugin_records(payload):
        plugin_id = record_plugin_id(record)
        name = record_plugin_name(record)
        if not plugin_id or plugin_id.endswith(CANDIDATE_NAMESPACE_SUFFIX):
            continue
        if name == plugin_name or plugin_id.split("@", 1)[0] == plugin_name:
            snapshot.append(
                {
                    "pluginId": plugin_id,
                    "enabled": record_enabled(record),
                    "marketplaceName": record.get("marketplaceName"),
                    "installedPath": record.get("installedPath"),
                }
            )
    return sorted(snapshot, key=lambda item: item["pluginId"])


def assert_candidate_absent(payload: Any) -> None:
    remaining = candidate_plugin_ids(payload)
    if remaining:
        raise ReplayError(f"candidate plugin identity still installed: {', '.join(remaining)}")


def assert_production_unchanged(before: list[dict[str, Any]], after: list[dict[str, Any]]) -> None:
    if before != after:
        raise ReplayError("production same-name plugin identity changed")


def cleanup_stale_candidates(codex: Path) -> list[str]:
    listed = run_codex_json(codex, ["plugin", "list", "--json"])
    stale_ids = candidate_plugin_ids(listed)
    for plugin_id in stale_ids:
        run_command([str(codex), "plugin", "remove", plugin_id], check=True)
    return stale_ids


def safe_stage_candidate(root: Path, candidate: CandidatePlugin, run_dir: Path) -> Path:
    # git archive stdout is binary; keep the public wrapper above easy to test by
    # using subprocess directly for this one command.
    proc = subprocess.run(
        ["git", "archive", "--format=tar", candidate.commit, candidate.source_path],
        cwd=str(root),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if proc.returncode != 0:
        raise ReplayError(f"failed to archive candidate plugin: {proc.stderr.decode('utf-8', 'replace').strip()}")
    extract_dir = run_dir / "extract"
    extract_dir.mkdir(parents=True, exist_ok=True)
    with tarfile.open(fileobj=io.BytesIO(proc.stdout), mode="r:") as tf:
        extract_members(tf, extract_dir)
    source = extract_dir / candidate.source_path
    if not source.exists():
        raise ReplayError("failed to stage candidate plugin from committed tree")
    marketplace_root = run_dir / "marketplace"
    plugin_dest = marketplace_root / "plugins" / candidate.name
    plugin_dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, plugin_dest)
    manifest_dir = marketplace_root / ".agents" / "plugins"
    manifest_dir.mkdir(parents=True, exist_ok=True)
    manifest = {
        "name": MARKETPLACE_NAME,
        "displayName": "AI Skills Candidate",
        "plugins": [
            {
                "name": candidate.name,
                "source": {"source": "local", "path": f"./plugins/{candidate.name}"},
                "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
            }
        ],
    }
    (manifest_dir / "marketplace.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return marketplace_root


def repo_relative_existing_file(root: Path, path: str) -> Path:
    candidate = (root / path).resolve() if not Path(path).is_absolute() else Path(path).resolve()
    root_resolved = root.resolve()
    if root_resolved != candidate and root_resolved not in candidate.parents:
        raise ReplayError(f"file must be inside this repository: {path}")
    if not candidate.is_file():
        raise ReplayError(f"file does not exist: {path}")
    return candidate


def prepare_workspace(root: Path, run_dir: Path, task: Path, inputs: list[Path]) -> tuple[Path, Path, str]:
    workspace = run_dir / "workspace"
    output_dir = workspace / "outputs"
    input_dir = workspace / "inputs"
    output_dir.mkdir(parents=True, exist_ok=True)
    input_dir.mkdir(parents=True, exist_ok=True)
    task_copy = workspace / task.name
    shutil.copy2(task, task_copy)
    copied_inputs = []
    for index, source in enumerate(inputs, start=1):
        dest = input_dir / f"{index:02d}-{source.name}"
        shutil.copy2(source, dest)
        copied_inputs.append(dest.relative_to(workspace).as_posix())
    prompt = task.read_text(encoding="utf-8").rstrip()
    prompt += "\n\nInput files available in this workspace:\n"
    for copied in copied_inputs:
        prompt += f"- {copied}\n"
    prompt += f"\nWrite all outputs under: {output_dir.relative_to(workspace).as_posix()}\n"
    return workspace, output_dir, prompt


def parse_consumption(stdout: str, installed_path: str) -> ConsumptionEvidence | None:
    skills_path = str(Path(installed_path) / "skills")
    for line_index, line in enumerate(stdout.splitlines(), start=1):
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        strings = list(iter_strings(event))
        if any(installed_path in value or skills_path in value for value in strings):
            event_type = first_event_type(event)
            return ConsumptionEvidence(line_index=line_index, event_type=event_type)
    return None


def iter_strings(value: Any) -> Iterable[str]:
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for child in value.values():
            yield from iter_strings(child)
    elif isinstance(value, list):
        for child in value:
            yield from iter_strings(child)


def first_event_type(value: Any) -> str:
    for item in iter_dicts(value):
        for key in ("type", "event", "event_type"):
            found = item.get(key)
            if isinstance(found, str):
                return found
    return "unknown"


def add_candidate_plugin(codex: Path, marketplace_root: Path, plugin_name: str) -> tuple[str, str, Any]:
    plugin_id = f"{plugin_name}{CANDIDATE_NAMESPACE_SUFFIX}"
    payload = run_codex_json(
        codex,
        [*codex_config_args(marketplace_root), "plugin", "add", "--json", plugin_id],
    )
    returned_id = first_string_value(payload, {"pluginId", "plugin_id", "id"})
    installed_path = first_string_value(payload, {"installedPath", "installed_path", "path"})
    if returned_id != plugin_id:
        raise ReplayError(f"candidate plugin add returned unexpected pluginId: {returned_id}")
    if not installed_path or not Path(installed_path).exists():
        raise ReplayError("candidate plugin add did not return an existing installedPath")
    return plugin_id, installed_path, payload


def remove_candidate_plugin(codex: Path, plugin_id: str) -> None:
    run_command([str(codex), "plugin", "remove", plugin_id], check=True)


def run_child_exec(
    codex: Path,
    marketplace_root: Path,
    plugin_id: str,
    workspace: Path,
    output_dir: Path,
    prompt: str,
) -> CommandResult:
    return run_command(
        [
            str(codex),
            "exec",
            "--ignore-user-config",
            "--json",
            *codex_config_args(marketplace_root),
            "-c",
            f'plugins."{plugin_id}".enabled=true',
            "-s",
            "workspace-write",
            "-C",
            str(workspace),
            "--add-dir",
            str(output_dir),
            "--skip-git-repo-check",
            "--ephemeral",
            "-",
        ],
        input_text=prompt,
        check=False,
    )


def run_replay(root: Path, plugin: str, candidate_commit: str, task_arg: str, input_args: list[str]) -> dict[str, Any]:
    runtime = ensure_runtime_available(root)
    paths = runtime_paths(root)
    task = repo_relative_existing_file(root, task_arg)
    inputs = [repo_relative_existing_file(root, item) for item in input_args]
    candidate = resolve_candidate_plugin(root, candidate_commit, plugin)
    run_id = time.strftime("%Y%m%dT%H%M%SZ", time.gmtime()) + f"-{os.getpid()}"
    run_dir = paths.state_root / "runs" / run_id
    run_dir.mkdir(parents=True, exist_ok=True)
    plugin_id = f"{plugin}{CANDIDATE_NAMESPACE_SUFFIX}"
    installed_path: str | None = None
    before_snapshot: list[dict[str, Any]] = []
    try:
        with replay_lock(root):
            cleanup_stale_candidates(paths.codex)
            before_list = run_codex_json(paths.codex, ["plugin", "list", "--json"])
            before_snapshot = same_name_installed_snapshot(before_list, plugin)
            marketplace_root = safe_stage_candidate(root, candidate, run_dir)
            try:
                plugin_id, installed_path, add_payload = add_candidate_plugin(paths.codex, marketplace_root, plugin)
                workspace, output_dir, prompt = prepare_workspace(root, run_dir, task, inputs)
                child = run_child_exec(paths.codex, marketplace_root, plugin_id, workspace, output_dir, prompt)
                evidence = parse_consumption(child.stdout, installed_path)
                if child.returncode != 0:
                    raise ReplayError(f"candidate child exec failed ({child.returncode}): {child.stderr.strip()}")
                if evidence is None:
                    raise ReplayError("candidate actual consumption was not proven by parsed JSON event")
                result = {
                    "candidate_commit": candidate.commit,
                    "plugin_id": plugin_id,
                    "installed_path": installed_path,
                    "runtime_version": runtime["version"],
                    "actual_consumption": {
                        "proven": True,
                        "event_type": evidence.event_type,
                        "line_index": evidence.line_index,
                    },
                    "add_payload": add_payload,
                    "stdout_path": str(run_dir / "child.stdout.jsonl"),
                    "stderr_path": str(run_dir / "child.stderr"),
                }
                (run_dir / "child.stdout.jsonl").write_text(child.stdout, encoding="utf-8")
                (run_dir / "child.stderr").write_text(child.stderr, encoding="utf-8")
                (run_dir / "run.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
                return result
            finally:
                with contextlib.suppress(Exception):
                    remove_candidate_plugin(paths.codex, plugin_id)
                with contextlib.suppress(Exception):
                    shutil.rmtree(run_dir / "marketplace")
                after_list = run_codex_json(paths.codex, ["plugin", "list", "--json"])
                assert_candidate_absent(after_list)
                assert_production_unchanged(before_snapshot, same_name_installed_snapshot(after_list, plugin))
    except Exception:
        with contextlib.suppress(Exception):
            shutil.rmtree(run_dir / "marketplace")
        raise


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Replay a committed AI_Skills candidate plugin with repo-local Codex.")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("ensure-runtime", help="download and verify the fixed repo-local Codex runtime")
    replay = sub.add_parser("replay", help="run a committed candidate plugin through the fixed repo-local runtime")
    replay.add_argument("--plugin", required=True)
    replay.add_argument("--candidate-commit", required=True)
    replay.add_argument("--task", required=True)
    replay.add_argument("--input", action="append", default=[], required=True)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    root = repo_root()
    try:
        if args.command == "ensure-runtime":
            result = ensure_runtime(root)
        elif args.command == "replay":
            result = run_replay(root, args.plugin, args.candidate_commit, args.task, args.input)
        else:
            raise ReplayError(f"unknown command: {args.command}")
    except ReplayError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
