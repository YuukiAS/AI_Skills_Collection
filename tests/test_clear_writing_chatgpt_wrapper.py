from __future__ import annotations

import io
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
import zipfile
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))
import build_clear_writing_chatgpt_wrapper as builder


class ClearWritingChatGPTWrapperTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "source"
        for relative in (builder.WRAPPER, builder.CONFIG, builder.ICON, builder.PROVENANCE):
            target = self.root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(REPO_ROOT / relative, target)
        for route in builder.ROUTES:
            relative = f"skills/writing/core/{route}"
            shutil.copytree(REPO_ROOT / relative, self.root / relative, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
        config = json.loads((self.root / builder.CONFIG).read_text())
        next(p for p in config["plugins"] if p["name"] == "writing-style")["version"] = "0.6"
        (self.root / builder.CONFIG).write_bytes(builder.json_bytes(config))

    def build(self) -> tuple[dict, dict]:
        return builder.build_payload(self.root, "0.6")

    def test_single_entry_roots_and_no_old_runtime_or_maintenance(self) -> None:
        files, receipt = self.build()
        self.assertEqual({p for p in files if p.endswith("/SKILL.md")}, {"skills/clear-writing/SKILL.md"})
        self.assertEqual(files["skills/clear-writing/SKILL.md"], (self.root / builder.WRAPPER).read_bytes())
        self.assertEqual(set(receipt["file_allowlist"]), set(files))
        self.assertFalse(set(files) & set(builder.OLD_DELETE_PATHS))
        self.assertFalse(any(Path(p).name == "TODO.md" for p in files))
        self.assertEqual(files["assets/app-facing.svg"], (self.root / builder.ICON).read_bytes())

    def test_projection_inverse_and_every_support_file_are_byte_identical(self) -> None:
        files, receipt = self.build()
        self.assertEqual(len(receipt["transforms"]), 2)
        for route in builder.ROUTES:
            source = self.root / f"skills/writing/core/{route}"
            projected = files[f"{builder.ROUTE_ROOT}/{route}/ROUTE.md"]
            if route in builder.TRANSFORMS:
                old, new = [s.encode() for s in builder.TRANSFORMS[route]]
                self.assertEqual(projected.count(new), 1)
                self.assertNotIn(old, projected)
                projected = projected.replace(new, old)
                self.assertIn(new.decode(), files)
            self.assertEqual(projected, (source / "SKILL.md").read_bytes())
            for directory in builder.SUPPORT_DIRS:
                for path in (source / directory).rglob("*"):
                    if path.is_file():
                        destination = f"{builder.ROUTE_ROOT}/{route}/{path.relative_to(source).as_posix()}"
                        self.assertEqual(files[destination], path.read_bytes())
        for record in receipt["files"]:
            self.assertEqual(record["source_sha256"], builder.sha256((self.root / record["source_path"]).read_bytes()))
            self.assertEqual(record["generated_sha256"], builder.sha256(files[record["generated_path"]]))
        self.assertEqual(files[builder.TRANSFORMS["scientific-prose"][1]], (self.root / builder.PROVENANCE).read_bytes())

    def test_frozen_transform_count_drift_fails_closed(self) -> None:
        path = self.root / "skills/writing/core/scientific-rewrite/SKILL.md"
        path.write_bytes(path.read_bytes() + builder.TRANSFORMS["scientific-rewrite"][0].encode())
        with self.assertRaisesRegex(builder.BuildError, "occurrence count"):
            self.build()

    def test_missing_support_and_extra_discoverable_skill_fail(self) -> None:
        files, _ = self.build()
        del files[f"{builder.ROUTE_ROOT}/writing-fidelity/assets/app-facing.svg"]
        with self.assertRaisesRegex(builder.BuildError, "missing route support"):
            builder.validate_package(files, "0.6.0")
        files, _ = self.build()
        files[f"{builder.ROUTE_ROOT}/chinese-prose/references/SKILL.md"] = b"unexpected skill"
        with self.assertRaisesRegex(builder.BuildError, "exactly one discoverable"):
            builder.validate_package(files, "0.6.0")

    def test_markdown_bare_scripts_and_nested_support_dependencies_are_checked(self) -> None:
        for reference in (b"[appendix](references/absent.md)", b"Run scripts/required_check.py"):
            path = self.root / "skills/writing/core/writing-fidelity/SKILL.md"
            original = path.read_bytes()
            path.write_bytes(original + b"\n" + reference)
            with self.assertRaisesRegex(builder.BuildError, "missing route support"):
                self.build()
            path.write_bytes(original)
        support = self.root / "skills/writing/core/writing-fidelity/references/failure-summary.md"
        support.write_bytes(support.read_bytes() + b"\n[details](absent.md)\n")
        with self.assertRaisesRegex(builder.BuildError, "missing linked support"):
            self.build()

    def test_two_raw_builds_and_all_zip_headers_are_identical(self) -> None:
        files, receipt = self.build()
        first = builder.deterministic_zip(files)
        second_files, second_receipt = self.build()
        self.assertEqual(first, builder.deterministic_zip(second_files))
        self.assertEqual(receipt, second_receipt)
        self.assertEqual(receipt["wrapper_archive_sha256"], builder.sha256(first))
        with zipfile.ZipFile(io.BytesIO(first)) as archive:
            self.assertEqual(archive.comment, b"")
            self.assertEqual(archive.namelist(), sorted(files, key=lambda s: s.encode()))
            for entry in archive.infolist():
                self.assertFalse(entry.is_dir())
                self.assertEqual(entry.date_time, (1980, 1, 1, 0, 0, 0))
                self.assertEqual(entry.compress_type, zipfile.ZIP_STORED)
                self.assertEqual(entry.create_system, 3)
                self.assertEqual(entry.external_attr, 0o100644 << 16)
                self.assertEqual(entry.internal_attr, 0)
                self.assertEqual((entry.extra, entry.comment), (b"", b""))
                self.assertEqual(archive.read(entry), files[entry.filename])

    def test_manifests_identity_interface_schema_shape_and_fixed_skill_discovery(self) -> None:
        files, _ = self.build()
        portable = json.loads(files["plugin.json"])
        compat = json.loads(files[".codex-plugin/plugin.json"])
        self.assertEqual(portable["$schema"], "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json")
        self.assertEqual(portable["name"], compat["name"])
        self.assertEqual(portable["version"], compat["version"])
        self.assertEqual(portable["version"], "0.6.0")
        self.assertEqual(portable["extensions"]["com.openai"]["interface"], compat["interface"])
        self.assertEqual(compat["interface"]["capabilities"], ["Interactive"])
        self.assertEqual(compat["skills"], "./skills/")
        self.assertFalse(set(portable) & {"skills", "interface", "mcpServers", "apps"})
        config = json.loads((self.root / builder.CONFIG).read_text())
        prompts = next(p for p in config["plugins"] if p["name"] == "writing-style")["defaultPrompt"][:3]
        self.assertEqual(compat["interface"]["defaultPrompt"], prompts)

    def test_cli_build_check_tampering_and_stale_output(self) -> None:
        base = Path(self.temp.name)
        output, archive, receipt = base / "package", base / "plugin.zip", base / "receipt.json"
        args = ["--expect-plugin-version", "0.6", "--projection-rule", builder.PROJECTION,
                "--zip-spec", builder.ZIP_SPEC, "--output-root", str(output),
                "--archive", str(archive), "--receipt", str(receipt)]
        with mock.patch.object(builder, "ROOT", self.root):
            self.assertEqual(builder.main(["build", *args]), 0)
            first = archive.read_bytes()
            self.assertEqual(builder.main(["build", *args]), 0)
            self.assertEqual(first, archive.read_bytes())
            self.assertEqual(builder.main(["check", *args]), 0)
            archive.write_bytes(first + b"drift")
            with self.assertRaises(SystemExit):
                builder.main(["check", *args])
            (output / "unknown.txt").write_text("do not delete me")
            with self.assertRaises(SystemExit):
                builder.main(["build", *args])
            self.assertEqual((output / "unknown.txt").read_text(), "do not delete me")

    def test_version_and_source_symlink_fail_closed(self) -> None:
        with self.assertRaisesRegex(builder.BuildError, "source version"):
            builder.build_payload(self.root, "0.7")
        path = self.root / builder.ICON
        path.unlink()
        try:
            path.symlink_to(REPO_ROOT / builder.ICON)
        except OSError:
            self.skipTest("symlinks unavailable on this host")
        with self.assertRaisesRegex(builder.BuildError, "source file"):
            self.build()

    def test_direct_codex_and_profile_routes_remain_six(self) -> None:
        config = json.loads((REPO_ROOT / builder.CONFIG).read_text())
        plugin = next(p for p in config["plugins"] if p["name"] == "writing-style")
        expected = {f"skills/writing/core/{route}" for route in builder.ROUTES}
        self.assertEqual(len(plugin["skills"]), 6)
        self.assertEqual({s["source"] for s in plugin["skills"]}, expected)
        profile = json.loads((REPO_ROOT / "profiles/codex-writing-style.json").read_text())
        self.assertEqual(set(profile["skills"]), expected)
        self.assertEqual(len(profile["skills"]), 6)

    def test_restore_tool_sets_keep_root_manifest_out_of_delete_paths(self) -> None:
        candidate, _ = self.build()
        compat = json.loads((REPO_ROOT / "plugins/codex/plugins/writing-style/.codex-plugin/plugin.json").read_text())
        compat["version"] = "0.5.0"
        baseline = {path: b"original behavior" for path in builder.OLD_DELETE_PATHS}
        baseline[".codex-plugin/plugin.json"] = builder.json_bytes(compat)
        restored, all_only, tool = builder.restore_payload(baseline, candidate)
        only = set(candidate) - set(baseline)
        self.assertEqual(set(all_only["all_06_only_paths"]), only)
        self.assertIn("plugin.json", only)
        self.assertNotIn("plugin.json", tool["tool_delete_paths"])
        self.assertEqual(set(tool["tool_delete_paths"]), only - set(restored))
        self.assertFalse(set(restored) & set(tool["tool_delete_paths"]))
        overlay = {**candidate, **restored}
        for path in tool["tool_delete_paths"]:
            del overlay[path]
        self.assertEqual(overlay, restored)
        for path in set(baseline) - {".codex-plugin/plugin.json"}:
            self.assertEqual(restored[path], baseline[path])
        for path in ("plugin.json", ".codex-plugin/plugin.json"):
            self.assertEqual(json.loads(restored[path])["version"], "0.6.1")
        drifted = {**baseline, "unfrozen.txt": b"drift"}
        with self.assertRaisesRegex(builder.BuildError, "file set"):
            builder.restore_payload(drifted, candidate)

    def test_archive_traversal_symlink_and_duplicates_are_rejected(self) -> None:
        path = Path(self.temp.name) / "untrusted.zip"
        for name in ("../outside", "/absolute", "dir/", "a\\b", "a/../b", "assets/*", "assets/**", "file?.md"):
            with zipfile.ZipFile(path, "w") as archive:
                archive.writestr(name, "unsafe")
            with self.assertRaises(builder.BuildError):
                builder.read_zip(path)

    def test_glob_cannot_enter_restore_upload_or_delete_sets(self) -> None:
        files, _ = self.build()
        files[f"{builder.ROUTE_ROOT}/writing-fidelity/assets/*"] = b"bad path"
        with self.assertRaisesRegex(builder.BuildError, "unsafe package path"):
            builder.validate_package(files, "0.6.0")


if __name__ == "__main__":
    unittest.main()
