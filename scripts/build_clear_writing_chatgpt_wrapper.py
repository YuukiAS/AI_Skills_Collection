#!/usr/bin/env python3
"""Build the source-authoritative, single-entry ChatGPT Clear Writing package."""

from __future__ import annotations

import argparse
import hashlib
import io
import json
from pathlib import Path, PurePosixPath
import posixpath
import re
import stat
import zipfile


ROOT = Path(__file__).resolve().parents[1]
TASK = "clear-writing--single-entry-artifact-finalization"
PROJECTION = "CW06_ROUTE_PROJECTION_V1"
ZIP_SPEC = "CW06_DETERMINISTIC_ZIP_V1"
WRAPPER = "packaging/chatgpt/writing-style/clear-writing/SKILL.md"
CONFIG = "scripts/codex_marketplace_config.json"
ICON = "assets/codex/plugin-icons/writing-style/composer.svg"
PROVENANCE = "docs/provenance/WRITING_SKILL_REPOS_2026_07_28.md"
ROUTES = (
    "writing-fidelity", "response-clarity", "product-ui-copy",
    "scientific-prose", "scientific-rewrite", "chinese-prose",
)
SUPPORT_DIRS = ("references", "scripts", "assets", "evals")
ROUTE_ROOT = "skills/clear-writing/references/routes"
TRANSFORMS = {
    "scientific-rewrite": (
        "skills/writing/core/scientific-rewrite/scripts/rewrite_support.py",
        f"{ROUTE_ROOT}/scientific-rewrite/scripts/rewrite_support.py",
    ),
    "scientific-prose": (
        PROVENANCE,
        f"{ROUTE_ROOT}/scientific-prose/references/provenance/WRITING_SKILL_REPOS_2026_07_28.md",
    ),
}
OLD_SKILL_DIRS = ("fidelity", "response-clarity", "product-ui-copy", "sci", "scientific-rewrite", "zh")
OLD_DELETE_PATHS = (
    ".codex-plugin/assets/composer.svg", ".codex-plugin/assets/logo.svg",
    "skills/fidelity/SKILL.md", "skills/fidelity/assets/app-facing.svg",
    "skills/fidelity/evals/trigger_queries.json", "skills/fidelity/references/failure-summary.md",
    "skills/product-ui-copy/SKILL.md", "skills/product-ui-copy/assets/app-facing.svg",
    "skills/product-ui-copy/evals/trigger_queries.json", "skills/response-clarity/SKILL.md",
    "skills/response-clarity/assets/app-facing.svg", "skills/response-clarity/evals/trigger_queries.json",
    "skills/sci/SKILL.md", "skills/sci/assets/app-facing.svg", "skills/sci/evals/trigger_queries.json",
    "skills/sci/references/scientific-report-checklist.md", "skills/sci/references/source-notes.md",
    "skills/scientific-rewrite/SKILL.md", "skills/scientific-rewrite/assets/app-facing.svg",
    "skills/scientific-rewrite/scripts/rewrite_support.py", "skills/zh/SKILL.md",
    "skills/zh/assets/app-facing.svg", "skills/zh/evals/trigger_queries.json",
    "skills/zh/references/chinese-prose-checklist.md",
    "skills/zh/references/group-meeting-chinese-report-prompt.md", "skills/zh/references/source-notes.md",
)


class BuildError(ValueError):
    pass


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def json_bytes(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8")


def safe_path(name: str) -> None:
    path = PurePosixPath(name)
    if (not name or path.is_absolute() or ".." in path.parts or "\\" in name or ":" in name
            or any(character in name for character in "*?[]")):
        raise BuildError(f"unsafe package path: {name}")
    if name != path.as_posix() or name.endswith("/"):
        raise BuildError(f"not an exact file path: {name}")


def deterministic_zip(files: dict[str, bytes]) -> bytes:
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", compression=zipfile.ZIP_STORED) as archive:
        for name in sorted(files, key=lambda item: item.encode("utf-8")):
            safe_path(name)
            entry = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            entry.compress_type = zipfile.ZIP_STORED
            entry.create_system = 3
            entry.external_attr = 0o100644 << 16
            entry.internal_attr = 0
            entry.extra = b""
            entry.comment = b""
            archive.writestr(entry, files[name])
        archive.comment = b""
    return buffer.getvalue()


def read_zip(path: Path) -> dict[str, bytes]:
    files: dict[str, bytes] = {}
    with zipfile.ZipFile(path) as archive:
        for entry in archive.infolist():
            safe_path(entry.filename)
            if entry.filename in files or stat.S_ISLNK(entry.external_attr >> 16):
                raise BuildError(f"duplicate or symlink entry: {entry.filename}")
            files[entry.filename] = archive.read(entry)
    return files


def source_bytes(root: Path, relative: str) -> bytes:
    path = root / relative
    if path.is_symlink() or not path.is_file() or not path.resolve().is_relative_to(root.resolve()):
        raise BuildError(f"missing or non-contained source file: {relative}")
    if any(parent.is_symlink() for parent in path.parents if parent != root.parent):
        raise BuildError(f"symlink source parent: {relative}")
    return path.read_bytes()


def manifests(plugin: dict, personal_version: str) -> tuple[dict, dict]:
    interface = {
        "displayName": "Clear Writing",
        "shortDescription": "Clear, faithful writing",
        "longDescription": plugin["description"],
        "developerName": "YuukiAS",
        "category": plugin["category"],
        "capabilities": ["Interactive"],
        "defaultPrompt": plugin["defaultPrompt"][:3],
        "brandColor": plugin["brandColor"],
        "composerIcon": "./assets/app-facing.svg",
        "logo": "./assets/app-facing.svg",
        "websiteURL": "https://github.com/YuukiAS/AI_Skills_Collection",
    }
    common = {
        "name": "writing-style", "version": personal_version,
        "description": plugin["description"],
        "author": {"name": "YuukiAS", "email": "humc2013@gmail.com", "url": "https://github.com/YuukiAS"},
        "homepage": "https://github.com/YuukiAS/AI_Skills_Collection",
        "repository": "https://github.com/YuukiAS/AI_Skills_Collection",
    }
    portable = {**common, "$schema": "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
                "extensions": {"com.openai": {"interface": interface}}}
    compat = {**common, "skills": "./skills/", "interface": interface}
    return portable, compat


def validate_references(files: dict[str, bytes]) -> None:
    for name, data in files.items():
        if not name.startswith(ROUTE_ROOT + "/") or Path(name).suffix not in {".md", ".py", ".json", ".yaml"}:
            continue
        text = data.decode("utf-8")
        route = PurePosixPath(name).parts[4]
        base = f"{ROUTE_ROOT}/{route}"
        references = re.findall(
            r"(?<![A-Za-z0-9_./-])((?:references|assets|scripts)/[A-Za-z0-9_./-]+\.[A-Za-z0-9]+)", text
        )
        for relative in references:
            if route == "scientific-rewrite" and relative == "scripts/run_fedfisher.sh":
                continue  # The frozen Plan identifies this literal as a user-project example.
            if f"{base}/{relative}" not in files:
                raise BuildError(f"missing route support: {name}: {relative}")
        for target in re.findall(r"\]\(([^\s)]+)(?:\s+[^)]*)?\)", text):
            target = target.split("#", 1)[0]
            if not target or ":" in target or target.startswith("/"):
                continue
            resolved = posixpath.normpath(f"{PurePosixPath(name).parent}/{target}")
            if resolved not in files:
                raise BuildError(f"missing linked support: {name}: {target}")


def validate_package(files: dict[str, bytes], version: str) -> None:
    skills = [name for name in files if PurePosixPath(name).name == "SKILL.md"]
    if skills != ["skills/clear-writing/SKILL.md"]:
        raise BuildError(f"expected exactly one discoverable Skill: {skills}")
    roots = {PurePosixPath(name).parts[0] for name in files}
    if roots != {"plugin.json", ".codex-plugin", "assets", "skills"}:
        raise BuildError(f"unexpected package roots: {roots}")
    for name in files:
        safe_path(name)
        if name not in {"plugin.json", ".codex-plugin/plugin.json", "assets/app-facing.svg", skills[0]}:
            if not any(name.startswith(f"{ROUTE_ROOT}/{route}/") for route in ROUTES):
                raise BuildError(f"file outside package allowlist: {name}")
    portable = json.loads(files["plugin.json"])
    compat = json.loads(files[".codex-plugin/plugin.json"])
    if any(key in portable for key in ("skills", "mcpServers", "apps", "interface")):
        raise BuildError("portable manifest must use fixed skills discovery and OpenAI extensions")
    interface = portable["extensions"]["com.openai"]["interface"]
    if interface != compat["interface"] or interface["capabilities"] != ["Interactive"]:
        raise BuildError("root/compat interface mismatch")
    if len(interface["shortDescription"]) > 30:
        raise BuildError("listing subtitle exceeds 30 characters")
    if compat["skills"] != "./skills/":
        raise BuildError("compat skills path must point to root skills")
    for manifest in (portable, compat):
        if manifest["name"] != "writing-style" or manifest["version"] != version:
            raise BuildError("root/compat identity mismatch")
    for field in ("logo", "composerIcon"):
        if interface[field].removeprefix("./") not in files:
            raise BuildError(f"missing interface asset: {field}")
    for route in ROUTES:
        route_path = f"{ROUTE_ROOT}/{route}/ROUTE.md"
        if route_path not in files:
            raise BuildError(f"missing route: {route}")
        if route in TRANSFORMS and TRANSFORMS[route][1] not in files:
            raise BuildError(f"missing projected target: {route}")
    validate_references(files)


def build_payload(root: Path, expected_version: str) -> tuple[dict[str, bytes], dict]:
    if not re.fullmatch(r"[0-9]+\.[0-9]+", expected_version):
        raise BuildError("expected plugin version must have two components")
    config_bytes = source_bytes(root, CONFIG)
    plugins = [p for p in json.loads(config_bytes)["plugins"] if p["name"] == "writing-style"]
    if len(plugins) != 1 or plugins[0]["version"] != expected_version:
        raise BuildError("writing-style source version does not match --expect-plugin-version")
    plugin = plugins[0]
    if plugin["displayName"] != "Clear Writing":
        raise BuildError("unexpected writing-style display identity")
    expected_routes = {f"skills/writing/core/{route}" for route in ROUTES}
    if {entry["source"] for entry in plugin["skills"]} != expected_routes or len(plugin["skills"]) != 6:
        raise BuildError("Codex must retain all six direct source routes")
    files: dict[str, bytes] = {}
    mapping: list[dict] = []
    applied: list[dict] = []

    def copy(relative: str, destination: str, data: bytes | None = None) -> None:
        original = source_bytes(root, relative)
        generated = original if data is None else data
        if destination in files:
            raise BuildError(f"duplicate generated file: {destination}")
        files[destination] = generated
        mapping.append({"source_path": relative, "source_sha256": sha256(original),
                        "generated_path": destination, "generated_sha256": sha256(generated)})

    copy(WRAPPER, "skills/clear-writing/SKILL.md")
    copy(ICON, "assets/app-facing.svg")
    for route in ROUTES:
        source = f"skills/writing/core/{route}"
        original = source_bytes(root, f"{source}/SKILL.md")
        projected = original
        if route in TRANSFORMS:
            old, new = (value.encode("utf-8") for value in TRANSFORMS[route])
            if original.count(old) != 1 or new in original:
                raise BuildError(f"frozen transform occurrence count mismatch: {route}")
            projected = original.replace(old, new)
            if old in projected or projected.replace(new, old) != original:
                raise BuildError(f"projection inverse parity failure: {route}")
            applied.append({"source_path": f"{source}/SKILL.md", "source_token": old.decode(),
                            "generated_token": new.decode(), "expected_count": 1, "actual_count": 1})
        copy(f"{source}/SKILL.md", f"{ROUTE_ROOT}/{route}/ROUTE.md", projected)
        for directory in SUPPORT_DIRS:
            support = root / source / directory
            if support.is_symlink():
                raise BuildError(f"symlink support directory: {support}")
            for path in sorted(support.rglob("*")) if support.exists() else []:
                if path.is_symlink():
                    raise BuildError(f"symlink support: {path}")
                if path.is_file() and "__pycache__" not in path.parts and path.suffix != ".pyc":
                    relative = path.relative_to(root).as_posix()
                    destination = f"{ROUTE_ROOT}/{route}/{path.relative_to(root / source).as_posix()}"
                    copy(relative, destination)
    copy(PROVENANCE, TRANSFORMS["scientific-prose"][1])
    personal_version = f"{expected_version}.0"
    portable, compat = manifests(plugin, personal_version)
    files["plugin.json"] = json_bytes(portable)
    files[".codex-plugin/plugin.json"] = json_bytes(compat)
    validate_package(files, personal_version)
    archive = deterministic_zip(files)
    receipt = {
        "schema": "CLEAR_WRITING_CHATGPT_BUILD_RECEIPT_V1",
        "plugin_name": "writing-style", "writing_style_version": expected_version,
        "personal_wrapper_version": personal_version,
        "transform_rule_version": PROJECTION, "zip_spec_version": ZIP_SPEC,
        "metadata_source": {"path": CONFIG, "sha256": sha256(config_bytes)},
        "files": mapping, "transforms": applied, "support_file_parity": True,
        "wrapper_archive_sha256": sha256(archive),
        "file_allowlist": sorted(files),
        "file_manifest": [{"path": name, "sha256": sha256(files[name]), "size_bytes": len(files[name])}
                          for name in sorted(files)],
    }
    return files, receipt


def output_files(root: Path) -> dict[str, bytes]:
    files: dict[str, bytes] = {}
    if root.is_symlink():
        raise BuildError("output root is a symlink")
    for path in root.rglob("*") if root.exists() else []:
        if path.is_symlink():
            raise BuildError(f"symlink output: {path}")
        if path.is_file():
            files[path.relative_to(root).as_posix()] = path.read_bytes()
    return files


def write_output(files: dict[str, bytes], output: Path, archive: Path) -> None:
    existing = output_files(output)
    if set(existing) - set(files):
        raise BuildError("output contains stale or unrelated files; choose a clean task-owned output directory")
    for name, data in files.items():
        destination = output / name
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(data)
    archive.parent.mkdir(parents=True, exist_ok=True)
    archive.write_bytes(deterministic_zip(files))


def restore_payload(baseline: dict[str, bytes], candidate: dict[str, bytes]) -> tuple[dict[str, bytes], dict, dict]:
    compat = json.loads(baseline[".codex-plugin/plugin.json"])
    if compat["name"] != "writing-style" or compat["version"] != "0.5.0" or "plugin.json" in baseline:
        raise BuildError("restore requires the saved legacy writing-style 0.5.0 release")
    if set(baseline) != set(OLD_DELETE_PATHS) | {".codex-plugin/plugin.json"}:
        raise BuildError("saved 0.5.0 file set differs from the frozen migration baseline")
    if {p for p in baseline if p.endswith("/SKILL.md")} != {f"skills/{name}/SKILL.md" for name in OLD_SKILL_DIRS}:
        raise BuildError("restore baseline must expose exactly the original six skills")
    validate_package(candidate, "0.6.0")
    restored = dict(baseline)
    compat["version"] = "0.6.1"
    restored[".codex-plugin/plugin.json"] = json_bytes(compat)
    portable = {key: value for key, value in compat.items() if key not in ("skills", "interface")}
    portable["$schema"] = "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"
    portable["extensions"] = {"com.openai": {"interface": compat["interface"]}}
    restored["plugin.json"] = json_bytes(portable)
    only06 = set(candidate) - set(baseline)
    deletes = only06 - set(restored)
    if deletes & set(restored) or (set(candidate) | set(restored)) - deletes != set(restored):
        raise BuildError("restore overlay/deletion set mismatch")
    for path in set(baseline) - {".codex-plugin/plugin.json"}:
        if restored[path] != baseline[path]:
            raise BuildError(f"restore behavior drift: {path}")
    for path in restored.keys() | deletes:
        safe_path(path)
    return restored, {"all_06_only_paths": sorted(only06)}, {"tool_delete_paths": sorted(deletes)}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    for command in ("build", "check"):
        sub = commands.add_parser(command)
        sub.add_argument("--expect-plugin-version", required=True)
        sub.add_argument("--projection-rule", choices=[PROJECTION], required=True)
        sub.add_argument("--zip-spec", choices=[ZIP_SPEC], required=True)
        sub.add_argument("--output-root", type=Path, required=True)
        sub.add_argument("--archive", type=Path, required=True)
        sub.add_argument("--receipt", type=Path, required=True)
    restore = commands.add_parser("prepare-restore")
    restore.add_argument("--baseline-archive", type=Path, required=True)
    restore.add_argument("--candidate-archive", type=Path, required=True)
    restore.add_argument("--output-root", type=Path, required=True)
    restore.add_argument("--archive", type=Path, required=True)
    restore.add_argument("--receipt-dir", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        if args.command == "prepare-restore":
            files, only06, deletes = restore_payload(read_zip(args.baseline_archive), read_zip(args.candidate_archive))
            write_output(files, args.output_root, args.archive)
            args.receipt_dir.mkdir(parents=True, exist_ok=True)
            (args.receipt_dir / "RESTORE_06_ONLY_PATHS.json").write_bytes(json_bytes(only06))
            (args.receipt_dir / "RESTORE_DELETE_PATHS.json").write_bytes(json_bytes(deletes))
        else:
            files, receipt = build_payload(ROOT, args.expect_plugin_version)
            if args.command == "build":
                write_output(files, args.output_root, args.archive)
                args.receipt.parent.mkdir(parents=True, exist_ok=True)
                args.receipt.write_bytes(json_bytes(receipt))
            elif (output_files(args.output_root) != files
                  or args.archive.read_bytes() != deterministic_zip(files)
                  or args.receipt.read_bytes() != json_bytes(receipt)):
                raise BuildError("source/output/archive/receipt parity failure")
        print(f"{args.command}: PASS archive_sha256={sha256(args.archive.read_bytes())}")
        return 0
    except (BuildError, KeyError, OSError, UnicodeError, json.JSONDecodeError, zipfile.BadZipFile) as error:
        parser.exit(1, f"build failed: {error}\n")


if __name__ == "__main__":
    raise SystemExit(main())
