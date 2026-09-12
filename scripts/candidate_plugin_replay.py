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
import re
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
ASSET_NAME = "codex-package-x86_64-unknown-linux-musl.tar.gz"
ASSET_URL = f"https://github.com/openai/codex/releases/download/{RELEASE_TAG}/{ASSET_NAME}"
ASSET_SHA256 = "a822187e1a2420c61c5926721bfbd878701ed95547c9bb0d4de4498a16ba1821"

MARKETPLACE_NAME = "ai-skills-candidate-053"
CANDIDATE_MARKETPLACE_PREFIX = "ai-skills-candidate"
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
    code_mode_host: Path
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


@dataclass(frozen=True)
class CachebusterEvidence:
    original_version: str
    updated_version: str
    cachebuster: str


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def runtime_paths(root: Path) -> RuntimePaths:
    runtime_root = root / ".local-runtime" / "codex" / CODEX_VERSION
    return RuntimePaths(
        root=runtime_root,
        archive=runtime_root / "downloads" / ASSET_NAME,
        bin_dir=runtime_root / "bin",
        codex=runtime_root / "bin" / "codex",
        code_mode_host=runtime_root / "bin" / "codex-code-mode-host",
        manifest=runtime_root / "runtime.json",
        state_root=root / ".local-runtime" / "candidate-plugin-replay",
    )


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def skill_hashes(plugin_root: Path) -> dict[str, str]:
    skills_root = plugin_root / "skills"
    if not skills_root.is_dir():
        raise ReplayError("candidate plugin has no skills directory")
    hashes = {}
    for path in sorted(skills_root.glob("**/SKILL.md")):
        hashes[path.relative_to(plugin_root).as_posix()] = sha256_file(path)
    if not hashes:
        raise ReplayError("candidate plugin has no SKILL.md files")
    return hashes


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
    if not os.access(paths.codex, os.X_OK):
        raise ReplayError("runtime bin/codex is not executable")
    if not paths.code_mode_host.exists():
        raise ReplayError("runtime bin/codex-code-mode-host is missing")
    if not os.access(paths.code_mode_host, os.X_OK):
        raise ReplayError("runtime bin/codex-code-mode-host is not executable")
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
        package_root = find_package_root(tmp)
        for child in package_root.iterdir():
            dest = paths.root / child.name
            if child.resolve() == dest.resolve():
                continue
            if dest.exists():
                if dest.is_dir() and not dest.is_symlink():
                    shutil.rmtree(dest)
                else:
                    dest.unlink()
            if child.is_dir():
                shutil.copytree(child, dest, symlinks=True)
            else:
                shutil.copy2(child, dest)


def find_package_root(extracted: Path) -> Path:
    if (extracted / "bin" / "codex").is_file():
        return extracted
    candidates = [path for path in extracted.iterdir() if path.is_dir() and (path / "bin" / "codex").is_file()]
    if len(candidates) == 1:
        return candidates[0]
    raise ReplayError("downloaded archive did not contain the expected Codex package layout")


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
        if plugin_id and is_candidate_plugin_id(plugin_id):
            ids.append(plugin_id)
    return sorted(set(ids))


def is_candidate_plugin_id(plugin_id: str) -> bool:
    if "@" not in plugin_id:
        return False
    marketplace = plugin_id.rsplit("@", 1)[1]
    return marketplace == CANDIDATE_MARKETPLACE_PREFIX or marketplace.startswith(f"{CANDIDATE_MARKETPLACE_PREFIX}-")


def candidate_plugin_id(plugin_name: str) -> str:
    return f"{plugin_name}@{MARKETPLACE_NAME}"


def same_name_installed_snapshot(payload: Any, plugin_name: str) -> list[dict[str, Any]]:
    snapshot = []
    for record in plugin_records(payload):
        plugin_id = record_plugin_id(record)
        name = record_plugin_name(record)
        if not plugin_id or is_candidate_plugin_id(plugin_id):
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


def marketplace_records(payload: Any) -> list[dict[str, Any]]:
    records = []
    for item in iter_dicts(payload):
        if any(key in item for key in {"name", "marketplaceName", "source", "path", "root"}):
            records.append(item)
    return records


def record_marketplace_name(record: dict[str, Any]) -> str | None:
    for key in ("name", "marketplaceName", "id"):
        value = record.get(key)
        if isinstance(value, str) and value:
            return value
    return None


def candidate_marketplace_names(payload: Any) -> list[str]:
    names = []
    for record in marketplace_records(payload):
        name = record_marketplace_name(record)
        if name == MARKETPLACE_NAME:
            names.append(name)
    return sorted(set(names))


def cleanup_stale_candidate_marketplace(codex: Path) -> list[str]:
    listed = run_codex_json(codex, ["plugin", "marketplace", "list", "--json"], check=False)
    stale_names = candidate_marketplace_names(listed)
    for name in stale_names:
        run_command([str(codex), "plugin", "marketplace", "remove", "--json", name], check=True)
    return stale_names


def assert_candidate_marketplace_absent(payload: Any) -> None:
    remaining = candidate_marketplace_names(payload)
    if remaining:
        raise ReplayError(f"candidate marketplace still configured: {', '.join(remaining)}")


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
    plugin_manifest = json.loads((plugin_dest / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8"))
    category = plugin_manifest.get("interface", {}).get("category")
    if not isinstance(category, str) or not category:
        category = "Productivity"
    manifest = {
        "name": MARKETPLACE_NAME,
        "interface": {"displayName": "AI Skills Candidate 053"},
        "plugins": [
            {
                "name": candidate.name,
                "source": {"source": "local", "path": f"./plugins/{candidate.name}"},
                "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
                "category": category,
            }
        ],
    }
    (manifest_dir / "marketplace.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return marketplace_root


def cachebuster_version(version: str, cachebuster: str) -> str:
    base_version = version.split("+", 1)[0]
    return f"{base_version}+codex.{cachebuster}"


def apply_cachebuster(plugin_root: Path, cachebuster: str) -> CachebusterEvidence:
    manifest_path = plugin_root / ".codex-plugin" / "plugin.json"
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ReplayError(f"staged plugin manifest is invalid JSON: {exc}") from exc
    version = manifest.get("version")
    if not isinstance(version, str) or not version:
        raise ReplayError("staged plugin manifest is missing version")
    updated = cachebuster_version(version, cachebuster)
    manifest["version"] = updated
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return CachebusterEvidence(original_version=version, updated_version=updated, cachebuster=cachebuster)


def add_candidate_marketplace(codex: Path, marketplace_root: Path) -> Any:
    return run_codex_json(codex, ["plugin", "marketplace", "add", "--json", str(marketplace_root)])


def remove_candidate_marketplace(codex: Path) -> None:
    run_command([str(codex), "plugin", "marketplace", "remove", "--json", MARKETPLACE_NAME], check=True)


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
    installed_skills_path = str(Path(installed_path) / "skills")
    stable_suffix = stable_cache_suffix(installed_path)
    stable_skills_suffix = f"{stable_suffix}/skills/" if stable_suffix else None
    for line_index, line in enumerate(stdout.splitlines(), start=1):
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        strings = list(command_execution_evidence_strings(event))
        if any(points_to_skill(value, installed_skills_path) for value in strings):
            event_type = first_event_type(event)
            return ConsumptionEvidence(line_index=line_index, event_type=event_type)
        if stable_skills_suffix and any(points_to_skill(value, stable_skills_suffix) for value in strings):
            event_type = first_event_type(event)
            return ConsumptionEvidence(line_index=line_index, event_type=event_type)
    return None


def stable_cache_suffix(installed_path: str) -> str | None:
    parts = Path(installed_path).parts
    for index in range(len(parts) - 4):
        if parts[index] == "plugins" and parts[index + 1] == "cache":
            marketplace, plugin, version = parts[index + 2 : index + 5]
            if marketplace and plugin and version:
                return "/".join(("", "plugins", "cache", marketplace, plugin, version))
    return None


def command_execution_evidence_strings(value: Any) -> Iterable[str]:
    if isinstance(value, dict):
        if value.get("type") == "command_execution":
            command = value.get("command")
            if isinstance(command, str):
                yield command
        for child in value.values():
            yield from command_execution_evidence_strings(child)
    elif isinstance(value, list):
        for child in value:
            yield from command_execution_evidence_strings(child)


def points_to_skill(value: str, skills_prefix: str) -> bool:
    return skills_prefix in value and "SKILL.md" in value


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


def candidate_cache_dir_from_path(value: str) -> Path | None:
    try:
        path = Path(value)
    except ValueError:
        return None
    if not path.is_absolute():
        return None
    parts = path.parts
    for index in range(len(parts) - 2):
        if parts[index] == "plugins" and parts[index + 1] == "cache" and parts[index + 2] == MARKETPLACE_NAME:
            return Path(*parts[: index + 3])
    return None


def candidate_cache_dirs_from_text(text: str) -> list[Path]:
    pattern = re.compile(r"(/[^\s'\"\n]*/plugins/cache/" + re.escape(MARKETPLACE_NAME) + r"(?:/[^\s'\"\n]*)?)")
    dirs = []
    for match in pattern.finditer(text):
        candidate = candidate_cache_dir_from_path(match.group(1))
        if candidate is not None:
            dirs.append(candidate)
    return sorted(set(dirs))


def cleanup_candidate_cache_dirs(values: Iterable[str | None]) -> list[str]:
    dirs: set[Path] = set()
    for value in values:
        if not value:
            continue
        direct = candidate_cache_dir_from_path(value)
        if direct is not None:
            dirs.add(direct)
        for found in candidate_cache_dirs_from_text(value):
            dirs.add(found)
    removed = []
    for path in sorted(dirs):
        if path.exists():
            shutil.rmtree(path)
            removed.append(str(path))
    return removed


def add_candidate_plugin(codex: Path, marketplace_root: Path, plugin_name: str) -> tuple[str, str, Any]:
    plugin_id = candidate_plugin_id(plugin_name)
    payload = run_codex_json(
        codex,
        ["plugin", "add", "--json", plugin_id],
    )
    if not isinstance(payload, dict):
        raise ReplayError("candidate plugin add returned non-object JSON payload")
    returned_id = payload.get("pluginId")
    installed_path = payload.get("installedPath")
    if not isinstance(returned_id, str) or not returned_id:
        raise ReplayError("candidate plugin add did not return top-level pluginId")
    if not isinstance(installed_path, str) or not installed_path:
        raise ReplayError("candidate plugin add did not return top-level installedPath")
    if returned_id != plugin_id:
        raise ReplayError(f"candidate plugin add returned unexpected pluginId: {returned_id}")
    if not Path(installed_path).exists():
        raise ReplayError("candidate plugin add did not return an existing installedPath")
    return plugin_id, installed_path, payload


def remove_candidate_plugin(codex: Path, plugin_id: str) -> None:
    run_command([str(codex), "plugin", "remove", plugin_id], check=True)


def run_child_exec(
    codex: Path,
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
            "-c",
            f"plugins.{plugin_id}.enabled=true",
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
    plugin_id = candidate_plugin_id(plugin)
    installed_path: str | None = None
    marketplace_added = False
    child_stdout = ""
    before_snapshot: list[dict[str, Any]] = []
    try:
        with replay_lock(root):
            cleanup_stale_candidates(paths.codex)
            cleanup_stale_candidate_marketplace(paths.codex)
            before_list = run_codex_json(paths.codex, ["plugin", "list", "--json"])
            before_snapshot = same_name_installed_snapshot(before_list, plugin)
            marketplace_root = safe_stage_candidate(root, candidate, run_dir)
            staged_plugin_root = marketplace_root / "plugins" / plugin
            staged_skill_hashes = skill_hashes(staged_plugin_root)
            cachebuster = apply_cachebuster(staged_plugin_root, f"local-{run_id}")
            try:
                marketplace_payload = add_candidate_marketplace(paths.codex, marketplace_root)
                marketplace_added = True
                plugin_id, installed_path, add_payload = add_candidate_plugin(paths.codex, marketplace_root, plugin)
                installed_skill_hashes = skill_hashes(Path(installed_path))
                if installed_skill_hashes != staged_skill_hashes:
                    raise ReplayError("installed candidate skill hashes do not match committed staged source")
                (run_dir / "plugin-add.json").write_text(
                    json.dumps(add_payload, indent=2, sort_keys=True) + "\n",
                    encoding="utf-8",
                )
                (run_dir / "marketplace-add.json").write_text(
                    json.dumps(marketplace_payload, indent=2, sort_keys=True) + "\n",
                    encoding="utf-8",
                )
                workspace, output_dir, prompt = prepare_workspace(root, run_dir, task, inputs)
                child = run_child_exec(paths.codex, plugin_id, workspace, output_dir, prompt)
                child_stdout = child.stdout
                stdout_path = run_dir / "child.stdout.jsonl"
                stderr_path = run_dir / "child.stderr"
                stdout_path.write_text(child.stdout, encoding="utf-8")
                stderr_path.write_text(child.stderr, encoding="utf-8")
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
                    "candidate_marketplace": MARKETPLACE_NAME,
                    "candidate_source_path": candidate.source_path,
                    "committed_plugin_tree": git(root, ["rev-parse", f"{candidate.commit}:{candidate.source_path}"]).stdout.strip(),
                    "cachebuster": {
                        "original_version": cachebuster.original_version,
                        "updated_version": cachebuster.updated_version,
                        "cachebuster": cachebuster.cachebuster,
                    },
                    "staged_skill_hashes": staged_skill_hashes,
                    "actual_consumption": {
                        "proven": True,
                        "event_type": evidence.event_type,
                        "line_index": evidence.line_index,
                    },
                    "add_payload": add_payload,
                    "stdout_path": str(stdout_path),
                    "stderr_path": str(stderr_path),
                }
                (run_dir / "run.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
                return result
            finally:
                with contextlib.suppress(Exception):
                    remove_candidate_plugin(paths.codex, plugin_id)
                if marketplace_added:
                    with contextlib.suppress(Exception):
                        remove_candidate_marketplace(paths.codex)
                cache_cleanup_paths = cleanup_candidate_cache_dirs([installed_path, child_stdout])
                (run_dir / "cleanup.json").write_text(
                    json.dumps({"candidate_cache_dirs_removed": cache_cleanup_paths}, indent=2, sort_keys=True) + "\n",
                    encoding="utf-8",
                )
                with contextlib.suppress(Exception):
                    shutil.rmtree(run_dir / "marketplace")
                with contextlib.suppress(Exception):
                    shutil.rmtree(run_dir / "extract")
                after_list = run_codex_json(paths.codex, ["plugin", "list", "--json"])
                assert_candidate_absent(after_list)
                after_marketplaces = run_codex_json(paths.codex, ["plugin", "marketplace", "list", "--json"], check=False)
                assert_candidate_marketplace_absent(after_marketplaces)
                assert_production_unchanged(before_snapshot, same_name_installed_snapshot(after_list, plugin))
    except Exception:
        with contextlib.suppress(Exception):
            shutil.rmtree(run_dir / "marketplace")
        with contextlib.suppress(Exception):
            shutil.rmtree(run_dir / "extract")
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
