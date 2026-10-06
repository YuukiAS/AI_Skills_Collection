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
import shlex
import shutil
import signal
import stat
import subprocess
import sys
import tarfile
import tempfile
import time
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Iterable


CODEX_VERSION = "0.153.4"
EXPECTED_CODEX_VERSION = f"codex-cli {CODEX_VERSION}"
RELEASE_TAG = f"rust-v{CODEX_VERSION}"
ASSET_NAME = "codex-package-x86_64-unknown-linux-musl.tar.gz"
ASSET_URL = f"https://github.com/openai/codex/releases/download/{RELEASE_TAG}/{ASSET_NAME}"
ASSET_SHA256 = "a822187e1a2420c61c5926721bfbd878701ed95547c9bb0d4de4498a16ba1821"

MARKETPLACE_NAME = "ai-skills-candidate"
CANDIDATE_NAMESPACE_SUFFIX = f"@{MARKETPLACE_NAME}"
MARKETPLACE_JSON = ".agents/plugins/marketplace.json"
DEFAULT_CHILD_TIMEOUT_SECONDS = 30 * 60
DEFAULT_CHILD_TERMINATE_GRACE_SECONDS = 10


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
class ConsumerIsolationViolation:
    line_index: int
    event_type: str
    command: str


@dataclass(frozen=True)
class SkillReadEvent:
    line_index: int
    event_type: str
    command: str


@dataclass(frozen=True)
class CachedPluginPackage:
    path: Path
    marketplace: str
    plugin: str
    version: str
    skill_names: tuple[str, ...]
    tree_sha256: str
    plugin_manifest_sha256: str | None


@dataclass(frozen=True)
class QuarantineRecord:
    package: CachedPluginPackage
    quarantine_path: Path
    overlapping_skill_names: tuple[str, ...]


@dataclass(frozen=True)
class QuarantineTransaction:
    manifest_path: Path
    discovery_root: Path
    quarantine_parent: Path
    records: tuple[QuarantineRecord, ...]


@dataclass(frozen=True)
class RestorationResult:
    actions: tuple[str, ...]
    verified_equivalent_rehydration: bool
    final_persistent_state_equivalent_to_before: bool


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
    return safe_stage_candidates(root, [candidate], run_dir)


def safe_stage_candidates(root: Path, candidates: list[CandidatePlugin], run_dir: Path) -> Path:
    if not candidates:
        raise ReplayError("at least one candidate plugin is required")
    seen_names: set[str] = set()
    marketplace_plugins: list[dict[str, Any]] = []
    marketplace_root = run_dir / "marketplace"
    for candidate in candidates:
        if candidate.name in seen_names:
            raise ReplayError(f"duplicate candidate plugin: {candidate.name}")
        seen_names.add(candidate.name)
        stage_one_candidate(root, candidate, run_dir, marketplace_root)
        marketplace_plugins.append(
            {
                "name": candidate.name,
                "source": {"source": "local", "path": f"./plugins/{candidate.name}"},
                "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
            }
        )
    manifest_dir = marketplace_root / ".agents" / "plugins"
    manifest_dir.mkdir(parents=True, exist_ok=True)
    manifest = {
        "name": MARKETPLACE_NAME,
        "displayName": "AI Skills Candidate",
        "plugins": marketplace_plugins,
    }
    (manifest_dir / "marketplace.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return marketplace_root


def parse_skill_frontmatter_name(skill_md: Path) -> str | None:
    try:
        lines = skill_md.read_text(encoding="utf-8").splitlines()
    except UnicodeDecodeError as exc:
        raise ReplayError(f"skill file is not valid UTF-8: {skill_md}") from exc
    if not lines or lines[0].strip() != "---":
        return None
    for line in lines[1:]:
        stripped = line.strip()
        if stripped == "---":
            return None
        if stripped.startswith("name:"):
            value = stripped.split(":", 1)[1].strip().strip('"').strip("'")
            return value or None
    return None


def top_level_skill_names(plugin_root: Path) -> set[str]:
    skills_root = plugin_root / "skills"
    if not skills_root.is_dir():
        return set()
    names: set[str] = set()
    for skill_md in sorted(skills_root.glob("*/SKILL.md")):
        name = parse_skill_frontmatter_name(skill_md)
        if name:
            names.add(name)
    return names


def candidate_skill_name_union(marketplace_root: Path, candidates: list[CandidatePlugin]) -> dict[str, set[str]]:
    by_plugin: dict[str, set[str]] = {}
    owner_by_skill: dict[str, str] = {}
    duplicates: dict[str, list[str]] = {}
    for candidate in candidates:
        names = top_level_skill_names(marketplace_root / "plugins" / candidate.name)
        by_plugin[candidate.name] = names
        for name in names:
            previous = owner_by_skill.get(name)
            if previous and previous != candidate.name:
                duplicates.setdefault(name, [previous]).append(candidate.name)
            else:
                owner_by_skill[name] = candidate.name
    if duplicates:
        detail = ", ".join(f"{name}: {sorted(set(owners))}" for name, owners in sorted(duplicates.items()))
        raise ReplayError(f"candidate-candidate duplicate top-level skill name is ambiguous: {detail}")
    return by_plugin


def effective_codex_home() -> Path:
    return Path(os.environ.get("CODEX_HOME", str(Path.home() / ".codex"))).expanduser().resolve()


def plugin_discovery_root(codex_home: Path | None = None) -> Path:
    return (codex_home or effective_codex_home()) / "plugins" / "cache"


def is_relative_to_path(path: Path, parent: Path) -> bool:
    try:
        path.relative_to(parent)
        return True
    except ValueError:
        return False


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def optional_file_sha256(path: Path) -> str | None:
    return sha256_file(path) if path.is_file() else None


def tree_sha256(path: Path) -> str:
    h = hashlib.sha256()
    root = path.resolve()
    if not root.is_dir():
        raise ReplayError(f"cannot hash missing package tree: {path}")
    for current, dirs, files in os.walk(root):
        dirs.sort()
        files.sort()
        current_path = Path(current)
        for name in dirs:
            item = current_path / name
            rel = item.relative_to(root).as_posix()
            if item.is_symlink():
                h.update(f"L\t{rel}\t{os.readlink(item)}\n".encode("utf-8"))
            else:
                h.update(f"D\t{rel}\n".encode("utf-8"))
        for name in files:
            item = current_path / name
            rel = item.relative_to(root).as_posix()
            if item.is_symlink():
                h.update(f"L\t{rel}\t{os.readlink(item)}\n".encode("utf-8"))
            else:
                h.update(f"F\t{rel}\t".encode("utf-8"))
                with item.open("rb") as fh:
                    for chunk in iter(lambda: fh.read(1024 * 1024), b""):
                        h.update(chunk)
                h.update(b"\n")
    return h.hexdigest()


def cached_plugin_package_from_path(path: Path, discovery_root: Path) -> CachedPluginPackage | None:
    resolved_root = discovery_root.resolve()
    resolved = path.resolve()
    if not is_relative_to_path(resolved, resolved_root):
        return None
    rel_parts = resolved.relative_to(resolved_root).parts
    if len(rel_parts) != 3:
        return None
    if rel_parts[0] == MARKETPLACE_NAME:
        return None
    if not (resolved / ".codex-plugin" / "plugin.json").is_file():
        return None
    skill_names = tuple(sorted(top_level_skill_names(resolved)))
    return CachedPluginPackage(
        path=resolved,
        marketplace=rel_parts[0],
        plugin=rel_parts[1],
        version=rel_parts[2],
        skill_names=skill_names,
        tree_sha256=tree_sha256(resolved),
        plugin_manifest_sha256=optional_file_sha256(resolved / ".codex-plugin" / "plugin.json"),
    )


def discover_cached_plugin_packages(discovery_root: Path) -> list[CachedPluginPackage]:
    if not discovery_root.is_dir():
        return []
    packages: list[CachedPluginPackage] = []
    for manifest in sorted(discovery_root.glob("*/*/*/.codex-plugin/plugin.json")):
        package = cached_plugin_package_from_path(manifest.parents[1], discovery_root)
        if package:
            packages.append(package)
    return packages


def detect_conflicting_cached_packages(
    discovery_root: Path,
    candidate_skill_names: Iterable[str],
) -> list[QuarantineRecord]:
    candidate_names = set(candidate_skill_names)
    if not candidate_names:
        return []
    conflicts: list[QuarantineRecord] = []
    for package in discover_cached_plugin_packages(discovery_root):
        overlap = tuple(sorted(candidate_names.intersection(package.skill_names)))
        if overlap:
            conflicts.append(
                QuarantineRecord(
                    package=package,
                    quarantine_path=Path(),
                    overlapping_skill_names=overlap,
                )
            )
    return conflicts


def fsync_path(path: Path) -> None:
    try:
        fd = os.open(path, os.O_RDONLY)
    except OSError:
        return
    try:
        os.fsync(fd)
    finally:
        os.close(fd)


def write_json_durable(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp")
    with tmp.open("w", encoding="utf-8") as fh:
        json.dump(payload, fh, indent=2, sort_keys=True)
        fh.write("\n")
        fh.flush()
        os.fsync(fh.fileno())
    tmp.replace(path)
    fsync_path(path.parent)


def normalized_plugin_list(payload: Any) -> Any:
    records = []
    for record in plugin_records(payload):
        plugin_id = record_plugin_id(record)
        if plugin_id and plugin_id.endswith(CANDIDATE_NAMESPACE_SUFFIX):
            continue
        records.append(
            {
                "pluginId": plugin_id,
                "name": record_plugin_name(record),
                "enabled": record_enabled(record),
                "marketplaceName": record.get("marketplaceName"),
                "installedPath": record.get("installedPath"),
            }
        )
    return sorted(records, key=lambda item: json.dumps(item, sort_keys=True))


def config_hash(codex_home: Path) -> str | None:
    return optional_file_sha256(codex_home / "config.toml")


def plugin_manifest_path(package_path: Path) -> Path:
    return package_path / ".codex-plugin" / "plugin.json"


def package_identity(path: Path, discovery_root: Path) -> dict[str, str]:
    resolved_root = discovery_root.resolve()
    resolved = path.resolve()
    if not is_relative_to_path(resolved, resolved_root):
        raise ReplayError(f"package path is outside discovery root: {path}")
    parts = resolved.relative_to(resolved_root).parts
    if len(parts) != 3:
        raise ReplayError(f"package path does not have marketplace/plugin/version identity: {path}")
    return {"marketplace": parts[0], "plugin": parts[1], "version": parts[2]}


def read_proof_counts(read_proof: dict[str, Any] | None) -> tuple[int, int, int]:
    if not read_proof:
        return 0, 0, 0
    return (
        int(read_proof.get("candidate_path_reads") or 0),
        int(read_proof.get("original_conflict_path_reads") or 0),
        int(read_proof.get("quarantine_path_reads") or 0),
    )


def quarantine_parent(codex_home: Path, run_id: str) -> Path:
    return (codex_home / ".candidate-plugin-replay-quarantine" / run_id).resolve()


def quarantine_destination(parent: Path, package: CachedPluginPackage) -> Path:
    return parent / package.marketplace / package.plugin / package.version


def validate_quarantine_destination(discovery_root: Path, parent: Path, original: Path, dest: Path) -> None:
    discovery_resolved = discovery_root.resolve()
    parent_resolved = parent.resolve()
    if parent_resolved == discovery_resolved or is_relative_to_path(parent_resolved, discovery_resolved):
        raise ReplayError("SAFE_QUARANTINE_UNAVAILABLE: quarantine parent resolves inside plugin discovery root")
    original_resolved = original.resolve()
    if original_resolved == parent_resolved or is_relative_to_path(parent_resolved, original_resolved):
        raise ReplayError("SAFE_QUARANTINE_UNAVAILABLE: quarantine parent resolves inside original package")
    if dest.exists():
        raise ReplayError(f"SAFE_QUARANTINE_UNAVAILABLE: quarantine destination already exists: {dest}")
    parent.mkdir(parents=True, exist_ok=True)
    if original.stat().st_dev != parent.stat().st_dev:
        raise ReplayError("SAFE_QUARANTINE_UNAVAILABLE: quarantine parent is on a different filesystem")


def prepare_quarantine_transaction(
    paths: RuntimePaths,
    run_id: str,
    before_list: Any,
    installed_paths: dict[str, str],
    conflict_records: list[QuarantineRecord],
) -> QuarantineTransaction | None:
    if not conflict_records:
        return None
    codex_home = effective_codex_home()
    discovery_root = plugin_discovery_root(codex_home).resolve()
    parent = quarantine_parent(codex_home, run_id)
    prepared_records: list[QuarantineRecord] = []
    for record in conflict_records:
        dest = quarantine_destination(parent, record.package)
        validate_quarantine_destination(discovery_root, parent, record.package.path, dest)
        prepared_records.append(
            QuarantineRecord(
                package=record.package,
                quarantine_path=dest,
                overlapping_skill_names=record.overlapping_skill_names,
            )
        )
    manifest_path = paths.state_root / "recovery" / f"{run_id}.json"
    manifest = {
        "run_id": run_id,
        "phase": "prepared",
        "codex_home": str(codex_home),
        "discovery_root": str(discovery_root),
        "quarantine_parent": str(parent),
        "discovery_root_st_dev": discovery_root.stat().st_dev if discovery_root.exists() else None,
        "quarantine_parent_st_dev": parent.stat().st_dev,
        "normalized_before_plugin_list": normalized_plugin_list(before_list),
        "config_hash": config_hash(codex_home),
        "candidate_installed_paths": installed_paths,
        "records": [
            {
                "marketplace": record.package.marketplace,
                "plugin": record.package.plugin,
                "version": record.package.version,
                "original_path": str(record.package.path),
                "quarantine_path": str(record.quarantine_path),
                "original_st_dev": record.package.path.stat().st_dev,
                "quarantine_parent_st_dev": parent.stat().st_dev,
                "tree_sha256": record.package.tree_sha256,
                "plugin_manifest_sha256": record.package.plugin_manifest_sha256,
                "overlapping_skill_names": list(record.overlapping_skill_names),
            }
            for record in prepared_records
        ],
    }
    write_json_durable(manifest_path, manifest)
    return QuarantineTransaction(
        manifest_path=manifest_path,
        discovery_root=discovery_root,
        quarantine_parent=parent,
        records=tuple(prepared_records),
    )


def update_transaction_phase(transaction: QuarantineTransaction, phase: str) -> None:
    payload = json.loads(transaction.manifest_path.read_text(encoding="utf-8"))
    payload["phase"] = phase
    write_json_durable(transaction.manifest_path, payload)


def update_transaction_payload(transaction: QuarantineTransaction, updates: dict[str, Any]) -> None:
    payload = json.loads(transaction.manifest_path.read_text(encoding="utf-8"))
    payload.update(updates)
    write_json_durable(transaction.manifest_path, payload)


def activate_quarantine(transaction: QuarantineTransaction) -> None:
    for record in transaction.records:
        record.quarantine_path.parent.mkdir(parents=True, exist_ok=True)
    update_transaction_phase(transaction, "quarantining")
    for record in transaction.records:
        if not record.package.path.exists():
            raise ReplayError(f"SAFE_QUARANTINE_UNAVAILABLE: original package missing before quarantine: {record.package.path}")
        record.package.path.rename(record.quarantine_path)
        fsync_path(record.package.path.parent)
        fsync_path(record.quarantine_path.parent)
    update_transaction_phase(transaction, "quarantined")


def write_post_child_evidence(
    transaction: QuarantineTransaction,
    *,
    stdout_path: Path,
    stderr_path: Path,
    installed_paths: dict[str, str],
    candidate_read_events: list[SkillReadEvent],
    original_conflict_events: list[SkillReadEvent],
    quarantine_events: list[SkillReadEvent],
) -> dict[str, Any]:
    proof = {
        "stdout_path": str(stdout_path),
        "stdout_sha256": sha256_file(stdout_path) if stdout_path.is_file() else None,
        "stderr_path": str(stderr_path),
        "stderr_sha256": sha256_file(stderr_path) if stderr_path.is_file() else None,
        "candidate_installed_paths": installed_paths,
        "candidate_path_reads": len(candidate_read_events),
        "original_conflict_path_reads": len(original_conflict_events),
        "quarantine_path_reads": len(quarantine_events),
        "candidate_read_events": read_event_payload(candidate_read_events),
        "original_conflict_read_events": read_event_payload(original_conflict_events),
        "quarantine_read_events": read_event_payload(quarantine_events),
        "post_child_original_presence": {
            str(record.package.path): record.package.path.exists()
            for record in transaction.records
        },
        "recovery_manifest_path": str(transaction.manifest_path),
    }
    update_transaction_payload(transaction, {"phase": "post_child_evidence", "post_child_evidence": proof})
    return proof


def verify_equivalent_rehydration_record(
    *,
    manifest: dict[str, Any],
    record_payload: dict[str, Any],
    transaction: QuarantineTransaction,
    record: QuarantineRecord,
    read_proof: dict[str, Any] | None,
    current_plugin_list: Any,
    codex_home: Path,
) -> dict[str, Any]:
    candidate_reads, original_reads, quarantine_reads = read_proof_counts(read_proof)
    original = record.package.path.resolve()
    quarantine = record.quarantine_path.resolve()
    expected_original = Path(record_payload["original_path"]).resolve()
    expected_quarantine = Path(record_payload["quarantine_path"]).resolve()
    if original != expected_original or quarantine != expected_quarantine:
        raise ReplayError("RESTORATION_AMBIGUOUS: package path does not match recovery manifest")
    if not is_relative_to_path(quarantine, transaction.quarantine_parent.resolve()):
        raise ReplayError("RESTORATION_AMBIGUOUS: quarantine path is not owned by this transaction")
    if not original.exists() or not quarantine.exists():
        raise ReplayError("RESTORATION_AMBIGUOUS: equivalent rehydration requires both copies")
    original_tree = tree_sha256(original)
    quarantine_tree = tree_sha256(quarantine)
    expected_tree = record_payload.get("tree_sha256")
    if not expected_tree or original_tree != quarantine_tree or original_tree != expected_tree:
        raise ReplayError("RESTORATION_AMBIGUOUS: equivalent rehydration tree hash mismatch")
    original_manifest_hash = optional_file_sha256(plugin_manifest_path(original))
    quarantine_manifest_hash = optional_file_sha256(plugin_manifest_path(quarantine))
    expected_manifest_hash = record_payload.get("plugin_manifest_sha256")
    if not expected_manifest_hash or original_manifest_hash != quarantine_manifest_hash or original_manifest_hash != expected_manifest_hash:
        raise ReplayError("RESTORATION_AMBIGUOUS: equivalent rehydration plugin manifest hash mismatch")
    identity = package_identity(original, transaction.discovery_root)
    quarantine_identity = {
        "marketplace": record_payload.get("marketplace"),
        "plugin": record_payload.get("plugin"),
        "version": record_payload.get("version"),
    }
    if identity != quarantine_identity:
        raise ReplayError("RESTORATION_AMBIGUOUS: original marketplace/plugin/version identity mismatch")
    quarantine_rel = quarantine.relative_to(transaction.quarantine_parent.resolve()).parts
    if tuple(quarantine_rel) != (identity["marketplace"], identity["plugin"], identity["version"]):
        raise ReplayError("RESTORATION_AMBIGUOUS: quarantine marketplace/plugin/version identity mismatch")
    if config_hash(codex_home) != manifest.get("config_hash"):
        raise ReplayError("RESTORATION_AMBIGUOUS: config hash mismatch")
    if normalized_plugin_list(current_plugin_list) != manifest.get("normalized_before_plugin_list"):
        raise ReplayError("RESTORATION_AMBIGUOUS: normalized plugin state mismatch")
    if candidate_reads <= 0:
        raise ReplayError("RESTORATION_AMBIGUOUS: candidate consumption proof is missing")
    if original_reads != 0 or quarantine_reads != 0:
        raise ReplayError("RESTORATION_AMBIGUOUS: conflict package read proof is nonzero")
    return {
        "classification": "VERIFIED_EQUIVALENT_REHYDRATION",
        "original_path": str(original),
        "quarantine_path": str(quarantine),
        "tree_sha256": original_tree,
        "plugin_manifest_sha256": original_manifest_hash,
        "identity": identity,
        "candidate_path_reads": candidate_reads,
        "original_conflict_path_reads": original_reads,
        "quarantine_path_reads": quarantine_reads,
    }


def remove_equivalent_quarantine_duplicate(record: QuarantineRecord) -> None:
    quarantine = record.quarantine_path.resolve()
    if not quarantine.is_dir():
        raise ReplayError(f"RESTORATION_AMBIGUOUS: quarantine duplicate is missing: {quarantine}")
    shutil.rmtree(quarantine)
    fsync_path(quarantine.parent)


def restore_quarantine(
    transaction: QuarantineTransaction,
    *,
    read_proof: dict[str, Any] | None = None,
    current_plugin_list: Any | None = None,
    final_plugin_list_reader: Callable[[], Any] | None = None,
    codex_home: Path | None = None,
) -> RestorationResult:
    manifest = json.loads(transaction.manifest_path.read_text(encoding="utf-8"))
    record_payloads = manifest.get("records")
    if not isinstance(record_payloads, list) or len(record_payloads) != len(transaction.records):
        raise ReplayError(f"RESTORATION_AMBIGUOUS: invalid recovery manifest {transaction.manifest_path}")
    errors: list[str] = []
    actions: list[str] = []
    verified_equivalent = False
    for record in reversed(transaction.records):
        original = record.package.path
        quarantine = record.quarantine_path
        record_payload = next(
            (
                item for item in record_payloads
                if Path(item.get("original_path", "")).resolve() == original.resolve()
                and Path(item.get("quarantine_path", "")).resolve() == quarantine.resolve()
            ),
            None,
        )
        if not isinstance(record_payload, dict):
            errors.append(f"RESTORATION_AMBIGUOUS: missing manifest record for {original}")
            continue
        if original.exists() and quarantine.exists():
            if current_plugin_list is None or codex_home is None:
                errors.append(f"RESTORATION_AMBIGUOUS: both original and quarantine exist for {original}")
                continue
            try:
                proof = verify_equivalent_rehydration_record(
                    manifest=manifest,
                    record_payload=record_payload,
                    transaction=transaction,
                    record=record,
                    read_proof=read_proof,
                    current_plugin_list=current_plugin_list,
                    codex_home=codex_home,
                )
                remove_equivalent_quarantine_duplicate(record)
                if tree_sha256(original) != proof["tree_sha256"]:
                    raise ReplayError("RESTORATION_AMBIGUOUS: final original tree hash changed")
                if optional_file_sha256(plugin_manifest_path(original)) != proof["plugin_manifest_sha256"]:
                    raise ReplayError("RESTORATION_AMBIGUOUS: final original plugin manifest hash changed")
                if config_hash(codex_home) != manifest.get("config_hash"):
                    raise ReplayError("RESTORATION_AMBIGUOUS: final config hash mismatch")
                final_plugin_list = final_plugin_list_reader() if final_plugin_list_reader else current_plugin_list
                if normalized_plugin_list(final_plugin_list) != manifest.get("normalized_before_plugin_list"):
                    raise ReplayError("RESTORATION_AMBIGUOUS: final normalized plugin state mismatch")
                actions.append(f"deleted-equivalent-quarantine-duplicate:{quarantine}")
                verified_equivalent = True
            except ReplayError as exc:
                errors.append(str(exc))
            continue
        if not quarantine.exists():
            if original.exists():
                actions.append(f"original-present-no-quarantine:{original}")
                continue
            errors.append(f"RESTORATION_AMBIGUOUS: neither original nor quarantine exists for {original}")
            continue
        if tree_sha256(quarantine) != record.package.tree_sha256:
            errors.append(f"RESTORATION_AMBIGUOUS: quarantine hash mismatch for {quarantine}")
            continue
        original.parent.mkdir(parents=True, exist_ok=True)
        quarantine.rename(original)
        fsync_path(original.parent)
        fsync_path(quarantine.parent)
        actions.append(f"restored-quarantine-to-original:{original}")
    if errors:
        raise ReplayError("; ".join(errors))
    update_transaction_phase(transaction, "restored")
    with contextlib.suppress(FileNotFoundError):
        transaction.manifest_path.unlink()
        fsync_path(transaction.manifest_path.parent)
    return RestorationResult(
        actions=tuple(actions),
        verified_equivalent_rehydration=verified_equivalent,
        final_persistent_state_equivalent_to_before=True,
    )


def recover_stale_quarantines(paths: RuntimePaths) -> list[str]:
    recovery_dir = paths.state_root / "recovery"
    if not recovery_dir.is_dir():
        return []
    recovered: list[str] = []
    for manifest_path in sorted(recovery_dir.glob("*.json")):
        payload = json.loads(manifest_path.read_text(encoding="utf-8"))
        if payload.get("phase") == "restored":
            manifest_path.unlink()
            recovered.append(f"removed-restored-manifest:{manifest_path.name}")
            continue
        records = payload.get("records")
        if not isinstance(records, list):
            raise ReplayError(f"RESTORATION_AMBIGUOUS: invalid recovery manifest {manifest_path}")
        for item in records:
            original = Path(item["original_path"]).resolve()
            quarantine = Path(item["quarantine_path"]).resolve()
            expected_hash = item["tree_sha256"]
            if original.exists() and quarantine.exists():
                raise ReplayError(f"RESTORATION_AMBIGUOUS: original and quarantine both exist: {original}")
            if original.exists() and not quarantine.exists():
                continue
            if not original.exists() and quarantine.exists() and tree_sha256(quarantine) == expected_hash:
                original.parent.mkdir(parents=True, exist_ok=True)
                quarantine.rename(original)
                fsync_path(original.parent)
                fsync_path(quarantine.parent)
                recovered.append(str(original))
                continue
            raise ReplayError(f"RESTORATION_AMBIGUOUS: cannot safely recover {original}")
        manifest_path.unlink()
        fsync_path(manifest_path.parent)
    return recovered


def stage_one_candidate(root: Path, candidate: CandidatePlugin, run_dir: Path, marketplace_root: Path) -> None:
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
    plugin_dest = marketplace_root / "plugins" / candidate.name
    plugin_dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, plugin_dest)


def repo_relative_existing_file(root: Path, path: str) -> Path:
    candidate = (root / path).resolve() if not Path(path).is_absolute() else Path(path).resolve()
    root_resolved = root.resolve()
    if root_resolved != candidate and root_resolved not in candidate.parents:
        raise ReplayError(f"file must be inside this repository: {path}")
    if not candidate.is_file():
        raise ReplayError(f"file does not exist: {path}")
    return candidate


def repo_relative_existing_dir(root: Path, path: str) -> Path:
    candidate = (root / path).resolve() if not Path(path).is_absolute() else Path(path).resolve()
    root_resolved = root.resolve()
    if root_resolved != candidate and root_resolved not in candidate.parents:
        raise ReplayError(f"directory must be inside this repository: {path}")
    if not candidate.is_dir():
        raise ReplayError(f"directory does not exist: {path}")
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
    allowed_prefixes = candidate_skill_prefixes([installed_path])
    for line_index, line in enumerate(stdout.splitlines(), start=1):
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        strings = list(command_execution_evidence_strings(event))
        if any(points_to_any_skill_prefix(value, allowed_prefixes) for value in strings):
            event_type = first_event_type(event)
            return ConsumptionEvidence(line_index=line_index, event_type=event_type)
    return None


def candidate_skill_prefixes(installed_paths: Iterable[str]) -> list[str]:
    prefixes: list[str] = []
    for installed_path in installed_paths:
        prefixes.append(str(Path(installed_path) / "skills"))
        stable_suffix = stable_cache_suffix(installed_path)
        if stable_suffix:
            prefixes.append(f"{stable_suffix}/skills/")
    return prefixes


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


def points_to_any_skill_prefix(value: str, skills_prefixes: Iterable[str]) -> bool:
    return any(points_to_skill(value, prefix) for prefix in skills_prefixes)


def is_plugin_cache_skill_read(value: str) -> bool:
    return "/plugins/cache/" in value and "SKILL.md" in value


def parse_consumer_isolation_violations(
    stdout: str,
    candidate_installed_paths: Iterable[str],
) -> list[ConsumerIsolationViolation]:
    allowed_prefixes = candidate_skill_prefixes(candidate_installed_paths)
    violations: list[ConsumerIsolationViolation] = []
    for line_index, line in enumerate(stdout.splitlines(), start=1):
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        event_type = first_event_type(event)
        for command in command_execution_evidence_strings(event):
            if is_plugin_cache_skill_read(command) and not points_to_any_skill_prefix(command, allowed_prefixes):
                violations.append(
                    ConsumerIsolationViolation(
                        line_index=line_index,
                        event_type=event_type,
                        command=command,
                    )
                )
    return violations


def parse_skill_read_events(stdout: str, roots: Iterable[Path | str]) -> list[SkillReadEvent]:
    prefixes = [str(Path(root) / "skills") for root in roots]
    events: list[SkillReadEvent] = []
    for line_index, line in enumerate(stdout.splitlines(), start=1):
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        event_type = first_event_type(event)
        for command in command_execution_evidence_strings(event):
            if points_to_any_skill_prefix(command, prefixes):
                events.append(SkillReadEvent(line_index=line_index, event_type=event_type, command=command))
    return events


def parse_candidate_read_events(stdout: str, installed_paths: Iterable[str]) -> list[SkillReadEvent]:
    prefixes = candidate_skill_prefixes(installed_paths)
    events: list[SkillReadEvent] = []
    for line_index, line in enumerate(stdout.splitlines(), start=1):
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        event_type = first_event_type(event)
        for command in command_execution_evidence_strings(event):
            if points_to_any_skill_prefix(command, prefixes):
                events.append(SkillReadEvent(line_index=line_index, event_type=event_type, command=command))
    return events


def read_event_payload(events: list[SkillReadEvent]) -> list[dict[str, Any]]:
    return [
        {
            "line_index": event.line_index,
            "event_type": event.event_type,
            "command": event.command,
        }
        for event in events
    ]


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
    marketplace_root: Path,
    plugin_id: str | list[str],
    workspace: Path,
    output_dir: Path,
    prompt: str,
    *,
    stdout_path: Path,
    stderr_path: Path,
    writable_dirs: list[Path] | None = None,
    timeout_seconds: float = DEFAULT_CHILD_TIMEOUT_SECONDS,
    terminate_grace_seconds: float = DEFAULT_CHILD_TERMINATE_GRACE_SECONDS,
) -> CommandResult:
    plugin_ids = [plugin_id] if isinstance(plugin_id, str) else plugin_id
    args = [
        str(codex),
        "exec",
        "--ignore-user-config",
        "--json",
        *codex_config_args(marketplace_root),
    ]
    for one_plugin_id in plugin_ids:
        args.extend(
            [
                "-c",
                f"plugins.{one_plugin_id}.enabled=true",
            ]
        )
    args.extend(
        [
            "-s",
            "workspace-write",
            "-C",
            str(workspace),
            "--add-dir",
            str(output_dir),
            "--skip-git-repo-check",
            "--ephemeral",
            "-",
        ]
    )
    for writable_dir in writable_dirs or []:
        args[args.index("--skip-git-repo-check"):args.index("--skip-git-repo-check")] = [
            "--add-dir",
            str(writable_dir),
        ]
    stdout_path.parent.mkdir(parents=True, exist_ok=True)
    stderr_path.parent.mkdir(parents=True, exist_ok=True)
    start_new_session = os.name == "posix"
    with stdout_path.open("w", encoding="utf-8") as stdout_fh:
        with stderr_path.open("w", encoding="utf-8") as stderr_fh:
            proc = subprocess.Popen(
                args,
                cwd=None,
                stdin=subprocess.PIPE,
                stdout=stdout_fh,
                stderr=stderr_fh,
                text=True,
                start_new_session=start_new_session,
            )
            try:
                proc.communicate(input=prompt, timeout=timeout_seconds)
            except subprocess.TimeoutExpired as exc:
                terminate_child_tree(proc, start_new_session, terminate_grace_seconds)
                raise ReplayError(
                    f"candidate child exec timed out after {timeout_seconds:g}s; "
                    f"stdout/stderr were preserved under {stdout_path.parent}"
                ) from exc
    stdout = stdout_path.read_text(encoding="utf-8")
    stderr = stderr_path.read_text(encoding="utf-8")
    return CommandResult(tuple(args), proc.returncode, stdout, stderr)


def terminate_child_tree(proc: subprocess.Popen[str], use_process_group: bool, grace_seconds: float) -> None:
    if proc.poll() is not None:
        return
    if use_process_group:
        with contextlib.suppress(ProcessLookupError):
            os.killpg(proc.pid, signal.SIGTERM)
    else:
        with contextlib.suppress(ProcessLookupError):
            proc.terminate()
    try:
        proc.wait(timeout=grace_seconds)
        return
    except subprocess.TimeoutExpired:
        pass
    if use_process_group:
        with contextlib.suppress(ProcessLookupError):
            os.killpg(proc.pid, signal.SIGKILL)
    else:
        with contextlib.suppress(ProcessLookupError):
            proc.kill()
    proc.wait()


def ancestor_pids(pid: int | None = None) -> set[int]:
    current = pid or os.getpid()
    ancestors = {current}
    while current > 1:
        stat_path = Path(f"/proc/{current}/stat")
        try:
            parts = stat_path.read_text(encoding="utf-8").split()
            parent = int(parts[3])
        except (OSError, ValueError, IndexError):
            break
        if parent in ancestors:
            break
        ancestors.add(parent)
        current = parent
    return ancestors


def assert_no_concurrent_codex_consumers(codex_home: Path) -> None:
    user = os.environ.get("USER")
    args = ["ps", "-u", user, "-o", "pid=,ppid=,stat=,etime=,cmd="] if user else ["ps", "-o", "pid=,ppid=,stat=,etime=,cmd="]
    result = run_command(args, check=False)
    if result.returncode != 0:
        raise ReplayError("CONCURRENT_SHARED_CODEX_HOME_CONSUMER: process preflight failed")
    protected = ancestor_pids()
    conflicts: list[str] = []
    for line in result.stdout.splitlines():
        fields = line.strip().split(None, 4)
        if len(fields) < 5:
            continue
        try:
            pid = int(fields[0])
        except ValueError:
            continue
        if pid in protected:
            continue
        command = fields[4]
        if "candidate_plugin_replay.py" in command:
            continue
        if "codex" not in command:
            continue
        if command_has_explicit_codex_home(command, codex_home):
            conflicts.append(f"pid={pid} cmd={command}")
    if conflicts:
        raise ReplayError("CONCURRENT_SHARED_CODEX_HOME_CONSUMER: " + "; ".join(conflicts[:3]))


def command_has_explicit_codex_home(command: str, codex_home: Path) -> bool:
    codex_home_text = str(codex_home)
    try:
        tokens = shlex.split(command)
    except ValueError:
        tokens = command.split()
    for index, token in enumerate(tokens):
        if token == f"CODEX_HOME={codex_home_text}":
            return True
        if token.startswith("CODEX_HOME="):
            return token.split("=", 1)[1] == codex_home_text
        if token in {"--codex-home", "--codex_home"} and index + 1 < len(tokens):
            return tokens[index + 1] == codex_home_text
        if token.startswith("--codex-home=") or token.startswith("--codex_home="):
            return token.split("=", 1)[1] == codex_home_text
    return False


@contextlib.contextmanager
def catch_sigterm_as_error():
    if os.name != "posix":
        yield
        return
    previous = signal.getsignal(signal.SIGTERM)

    def _handler(_signum, _frame):
        raise ReplayError("received SIGTERM during candidate replay")

    signal.signal(signal.SIGTERM, _handler)
    try:
        yield
    finally:
        signal.signal(signal.SIGTERM, previous)


def run_replay(
    root: Path,
    plugin: str,
    candidate_commit: str,
    task_arg: str,
    input_args: list[str],
    writable_dir_args: list[str] | None = None,
) -> dict[str, Any]:
    return run_replay_multi(root, [plugin], candidate_commit, task_arg, input_args, writable_dir_args, legacy_single=True)


def run_replay_multi(
    root: Path,
    plugins: list[str],
    candidate_commit: str,
    task_arg: str,
    input_args: list[str],
    writable_dir_args: list[str] | None = None,
    *,
    legacy_single: bool = False,
) -> dict[str, Any]:
    runtime = ensure_runtime_available(root)
    paths = runtime_paths(root)
    task = repo_relative_existing_file(root, task_arg)
    inputs = [repo_relative_existing_file(root, item) for item in input_args]
    writable_dirs = [repo_relative_existing_dir(root, item) for item in (writable_dir_args or [])]
    candidates = [resolve_candidate_plugin(root, candidate_commit, plugin) for plugin in plugins]
    resolved_commit = candidates[0].commit
    if any(candidate.commit != resolved_commit for candidate in candidates):
        raise ReplayError("candidate plugins must resolve to the same commit")
    run_id = time.strftime("%Y%m%dT%H%M%SZ", time.gmtime()) + f"-{os.getpid()}"
    run_dir = paths.state_root / "runs" / run_id
    run_dir.mkdir(parents=True, exist_ok=True)
    plugin_ids = [f"{plugin}{CANDIDATE_NAMESPACE_SUFFIX}" for plugin in plugins]
    installed_paths: dict[str, str] = {}
    before_snapshots: dict[str, list[dict[str, Any]]] = {}
    quarantine: QuarantineTransaction | None = None
    read_proof: dict[str, Any] | None = None
    result_payload: dict[str, Any] | None = None
    try:
        with replay_lock(root):
            stale_recoveries = recover_stale_quarantines(paths)
            cleanup_stale_candidates(paths.codex)
            before_list = run_codex_json(paths.codex, ["plugin", "list", "--json"])
            before_normalized = normalized_plugin_list(before_list)
            before_snapshots = {
                plugin: same_name_installed_snapshot(before_list, plugin)
                for plugin in plugins
            }
            marketplace_root = safe_stage_candidates(root, candidates, run_dir)
            candidate_skill_names_by_plugin = candidate_skill_name_union(marketplace_root, candidates)
            candidate_skill_names = set().union(*candidate_skill_names_by_plugin.values()) if candidate_skill_names_by_plugin else set()
            try:
                add_payloads: dict[str, Any] = {}
                installed_plugin_ids: dict[str, str] = {}
                for plugin in plugins:
                    plugin_id, installed_path, add_payload = add_candidate_plugin(paths.codex, marketplace_root, plugin)
                    installed_plugin_ids[plugin] = plugin_id
                    installed_paths[plugin] = installed_path
                    add_payloads[plugin] = add_payload
                (run_dir / "plugin-add.json").write_text(
                    json.dumps(add_payloads, indent=2, sort_keys=True) + "\n",
                    encoding="utf-8",
                )
                workspace, output_dir, prompt = prepare_workspace(root, run_dir, task, inputs)
                stdout_path = run_dir / "child.stdout.jsonl"
                stderr_path = run_dir / "child.stderr"
                codex_home = effective_codex_home()
                discovery_root = plugin_discovery_root(codex_home).resolve()
                conflict_candidates = detect_conflicting_cached_packages(discovery_root, candidate_skill_names)
                if conflict_candidates:
                    assert_no_concurrent_codex_consumers(codex_home)
                quarantine = prepare_quarantine_transaction(
                    paths,
                    run_id,
                    before_list,
                    installed_paths,
                    conflict_candidates,
                )
                if quarantine:
                    activate_quarantine(quarantine)
                with catch_sigterm_as_error():
                    child = run_child_exec(
                        paths.codex,
                        marketplace_root,
                        list(installed_plugin_ids.values()),
                        workspace,
                        output_dir,
                        prompt,
                        stdout_path=stdout_path,
                        stderr_path=stderr_path,
                        writable_dirs=writable_dirs,
                    )
                if not stdout_path.exists():
                    stdout_path.write_text(child.stdout, encoding="utf-8")
                if not stderr_path.exists():
                    stderr_path.write_text(child.stderr, encoding="utf-8")
                evidence_by_plugin = {
                    plugin: parse_consumption(child.stdout, installed_path)
                    for plugin, installed_path in installed_paths.items()
                }
                original_conflict_events = (
                    parse_skill_read_events(child.stdout, [record.package.path for record in quarantine.records])
                    if quarantine
                    else []
                )
                quarantine_events = (
                    parse_skill_read_events(child.stdout, [record.quarantine_path for record in quarantine.records])
                    if quarantine
                    else []
                )
                candidate_read_events = parse_candidate_read_events(child.stdout, installed_paths.values())
                if quarantine:
                    read_proof = write_post_child_evidence(
                        quarantine,
                        stdout_path=stdout_path,
                        stderr_path=stderr_path,
                        installed_paths=installed_paths,
                        candidate_read_events=candidate_read_events,
                        original_conflict_events=original_conflict_events,
                        quarantine_events=quarantine_events,
                    )
                if child.returncode != 0:
                    raise ReplayError(f"candidate child exec failed ({child.returncode}): {child.stderr.strip()}")
                if original_conflict_events or quarantine_events:
                    examples = "; ".join(
                        [f"original line {item.line_index}: {item.command}" for item in original_conflict_events[:2]]
                        + [f"quarantine line {item.line_index}: {item.command}" for item in quarantine_events[:2]]
                    )
                    raise ReplayError("candidate consumer isolation failed; conflicting cached package was read: " + examples)
                missing = [plugin for plugin, evidence in evidence_by_plugin.items() if evidence is None]
                if missing:
                    raise ReplayError(
                        "candidate actual consumption was not proven by parsed JSON event for: "
                        + ", ".join(sorted(missing))
                    )
                plugin_results = []
                for plugin in plugins:
                    evidence = evidence_by_plugin[plugin]
                    assert evidence is not None
                    plugin_results.append(
                        {
                            "name": plugin,
                            "plugin_id": installed_plugin_ids[plugin],
                            "installed_path": installed_paths[plugin],
                            "actual_consumption": {
                                "proven": True,
                                "event_type": evidence.event_type,
                                "line_index": evidence.line_index,
                            },
                            "add_payload": add_payloads[plugin],
                        }
                    )
                result: dict[str, Any] = {
                    "candidate_commit": resolved_commit,
                    "runtime_version": runtime["version"],
                    "plugins": plugin_results,
                    "actual_consumption_by_plugin": {
                        item["name"]: item["actual_consumption"] for item in plugin_results
                    },
                    "consumer_isolation": {
                        "enforced": True,
                        "candidate_skill_names": sorted(candidate_skill_names),
                        "candidate_skill_names_by_plugin": {
                            plugin: sorted(names) for plugin, names in candidate_skill_names_by_plugin.items()
                        },
                        "conflicts_suppressed": [
                            {
                                "original_path": str(record.package.path),
                                "quarantine_path": str(record.quarantine_path),
                                "overlapping_skill_names": list(record.overlapping_skill_names),
                                "tree_sha256": record.package.tree_sha256,
                            }
                            for record in quarantine.records
                        ] if quarantine else [],
                        "candidate_path_reads": len(candidate_read_events),
                        "original_conflict_path_reads": len(original_conflict_events),
                        "quarantine_path_reads": len(quarantine_events),
                        "candidate_read_events": read_event_payload(candidate_read_events),
                        "original_conflict_read_events": read_event_payload(original_conflict_events),
                        "quarantine_read_events": read_event_payload(quarantine_events),
                        "stale_recoveries": stale_recoveries,
                        "quarantine_manifest_path": str(quarantine.manifest_path) if quarantine else None,
                        "original_paths": [
                            str(record.package.path) for record in quarantine.records
                        ] if quarantine else [],
                        "quarantine_paths": [
                            str(record.quarantine_path) for record in quarantine.records
                        ] if quarantine else [],
                        "persistent_plugin_state_equal": True,
                        "config_hash": config_hash(effective_codex_home()),
                        "allowed_candidate_skill_roots": [
                            str(Path(installed_path) / "skills") for installed_path in installed_paths.values()
                        ],
                    },
                    "stdout_path": str(stdout_path),
                    "stderr_path": str(stderr_path),
                    "writable_dirs": [str(path) for path in writable_dirs],
                }
                result_payload = result
                if legacy_single and len(plugin_results) == 1:
                    single = plugin_results[0]
                    result.update(
                        {
                            "plugin_id": single["plugin_id"],
                            "installed_path": single["installed_path"],
                            "actual_consumption": single["actual_consumption"],
                            "add_payload": single["add_payload"],
                        }
                    )
                (run_dir / "run.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
                return result
            finally:
                restore_error: Exception | None = None
                restoration: RestorationResult | None = None
                if quarantine:
                    try:
                        restoration = restore_quarantine(
                            quarantine,
                            read_proof=read_proof,
                            current_plugin_list=run_codex_json(paths.codex, ["plugin", "list", "--json"]),
                            final_plugin_list_reader=lambda: run_codex_json(paths.codex, ["plugin", "list", "--json"]),
                            codex_home=effective_codex_home(),
                        )
                    except Exception as exc:  # noqa: BLE001 - preserve exact failure after cleanup attempt.
                        restore_error = exc
                for plugin_id in plugin_ids:
                    with contextlib.suppress(Exception):
                        remove_candidate_plugin(paths.codex, plugin_id)
                with contextlib.suppress(Exception):
                    shutil.rmtree(run_dir / "marketplace")
                after_list = run_codex_json(paths.codex, ["plugin", "list", "--json"])
                assert_candidate_absent(after_list)
                for plugin in plugins:
                    assert_production_unchanged(
                        before_snapshots[plugin],
                        same_name_installed_snapshot(after_list, plugin),
                    )
                if normalized_plugin_list(after_list) != before_normalized:
                    raise ReplayError("persistent plugin list changed")
                if result_payload is not None:
                    result_payload["restoration"] = {
                        "actions": list(restoration.actions) if restoration else [],
                        "verified_equivalent_rehydration": (
                            restoration.verified_equivalent_rehydration if restoration else False
                        ),
                        "final_persistent_state_equivalent_to_before": (
                            restoration.final_persistent_state_equivalent_to_before if restoration else True
                        ),
                    }
                    result_payload["consumer_isolation"]["final_persistent_state_equivalent_to_before"] = (
                        restoration.final_persistent_state_equivalent_to_before if restoration else True
                    )
                    (run_dir / "run.json").write_text(
                        json.dumps(result_payload, indent=2, sort_keys=True) + "\n",
                        encoding="utf-8",
                    )
                if restore_error:
                    raise restore_error
    except Exception:
        with contextlib.suppress(Exception):
            shutil.rmtree(run_dir / "marketplace")
        raise


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Replay a committed AI_Skills candidate plugin with repo-local Codex.")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("ensure-runtime", help="download and verify the fixed repo-local Codex runtime")
    replay = sub.add_parser("replay", help="run a committed candidate plugin through the fixed repo-local runtime")
    replay.add_argument("--plugin", action="append", required=True)
    replay.add_argument("--candidate-commit", required=True)
    replay.add_argument("--task", required=True)
    replay.add_argument("--input", action="append", default=[], required=True)
    replay.add_argument("--writable-dir", action="append", default=[])
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    root = repo_root()
    try:
        if args.command == "ensure-runtime":
            result = ensure_runtime(root)
        elif args.command == "replay":
            if len(args.plugin) == 1:
                result = run_replay(root, args.plugin[0], args.candidate_commit, args.task, args.input, args.writable_dir)
            else:
                result = run_replay_multi(root, args.plugin, args.candidate_commit, args.task, args.input, args.writable_dir)
        else:
            raise ReplayError(f"unknown command: {args.command}")
    except ReplayError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
