from __future__ import annotations

import gzip
import io
import importlib.util
import json
from pathlib import Path
import shutil
import stat
import sys
import tarfile
import tempfile
import unittest
import warnings
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

    def baseline(self) -> dict[str, bytes]:
        candidate, _ = self.build()
        compat = json.loads(candidate[".codex-plugin/plugin.json"])
        compat["version"] = "0.5.0"
        files = {path: b"original behavior\x00\xff" for path in builder.OLD_DELETE_PATHS}
        files[".codex-plugin/plugin.json"] = builder.json_bytes(compat)
        self.assertEqual(len(files), 27)
        return files

    def archive(self, files: dict[str, bytes], format: str, directories: tuple[str, ...] = ()) -> Path:
        path = Path(self.temp.name) / f"input.{format}"
        if format == "zip":
            with zipfile.ZipFile(path, "w") as archive:
                for name in directories:
                    archive.writestr(name + "/", b"")
                for name, data in files.items():
                    archive.writestr(name, data)
        else:
            with tarfile.open(path, "w:gz") as archive:
                for name in directories:
                    entry = tarfile.TarInfo(name)
                    entry.type = tarfile.DIRTYPE
                    archive.addfile(entry)
                for name, data in files.items():
                    entry = tarfile.TarInfo(name)
                    entry.size = len(data)
                    archive.addfile(entry, io.BytesIO(data))
        return path

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
            with self.assertRaisesRegex(builder.BuildError, "missing (route|linked) support"):
                self.build()
            path.write_bytes(original)
        support = self.root / "skills/writing/core/writing-fidelity/references/failure-summary.md"
        support.write_bytes(support.read_bytes() + b"\n[details](absent.md)\n")
        with self.assertRaisesRegex(builder.BuildError, "missing linked support"):
            self.build()

    def test_nested_link_uses_containing_support_directory(self) -> None:
        root = self.root / "skills/writing/core/writing-fidelity/references"
        path = root / "failure-summary.md"
        path.write_bytes(path.read_bytes() + b"\n[detail](references/nested.md)\n")
        (root / "references").mkdir()
        (root / "references/nested.md").write_text("Nested support")
        self.build()

    def test_reference_style_link_target_is_checked(self) -> None:
        path = self.root / "skills/writing/core/writing-fidelity/references/failure-summary.md"
        path.write_bytes(path.read_bytes() + b"\n[appendix][details]\n\n[details]: absent.md\n")
        with self.assertRaisesRegex(builder.BuildError, "missing linked support"):
            self.build()

    def test_angle_link_and_footnote_are_valid_markdown(self) -> None:
        root = self.root / "skills/writing/core/writing-fidelity/references"
        path = root / "failure-summary.md"
        path.write_bytes(path.read_bytes() + b"\n[appendix](<appendix.md>)\n\n[^note]: This is explanatory prose\n")
        (root / "appendix.md").write_text("Appendix")
        self.build()

    def test_collect_only_creates_missing_output_directory(self) -> None:
        script = REPO_ROOT / "results/clear-writing--single-entry-artifact-finalization/known-regression/run_local_replays.py"
        spec = importlib.util.spec_from_file_location("cw06_collect_replay", script)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        here = Path(self.temp.name) / "collect"
        durable = Path(self.temp.name) / "durable"
        (here / "runs").mkdir(parents=True)
        for index in range(13):
            case = f"CASE-{index:02d}"
            (here / "runs" / f"{case}.json").write_text(json.dumps({"case": case}))
            output = durable / case / "replay/outputs"
            output.mkdir(parents=True)
            (output / "last-message.txt").write_text("[answer](outputs/answer.md)")
            (output / "answer.md").write_text("Actual artifact")
        self.assertFalse((here / "outputs").exists())
        with mock.patch.object(module, "HERE", here), mock.patch.object(module, "DURABLE", durable):
            module.collect_artifacts()
        self.assertEqual(len(list((here / "outputs").glob("*_OUTPUT.md"))), 13)

    def test_replay_interruption_cannot_silently_launch_a_second_attempt(self) -> None:
        script = REPO_ROOT / "results/clear-writing--single-entry-artifact-finalization/known-regression/run_local_replays.py"
        spec = importlib.util.spec_from_file_location("cw06_local_replay", script)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        with mock.patch.object(module, "HERE", Path(self.temp.name) / "replays"):
            with mock.patch.object(module.subprocess, "run", side_effect=RuntimeError("interruption")) as call:
                with self.assertRaisesRegex(RuntimeError, "interruption"):
                    module.replay("CASE", "FIXTURE", "commit", "archive-hash")
                with self.assertRaises(FileExistsError):
                    module.replay("CASE", "FIXTURE", "commit", "archive-hash")
                self.assertEqual(call.call_count, 1)

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
        baseline = self.baseline()
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

    def test_zip_tar_gz_and_tgz_baselines_are_byte_equivalent(self) -> None:
        baseline = self.baseline()
        for format in ("zip", "tar.gz", "tgz"):
            with self.subTest(format=format):
                path = self.archive(baseline, format)
                self.assertEqual(builder.read_archive(path), baseline)
                self.assertEqual(builder.read_zip(path), baseline)
                # Content, not the supplied suffix, determines the format.
                renamed = path.with_name("misnamed.tar.gz" if format == "zip" else "misnamed.zip")
                shutil.copyfile(path, renamed)
                self.assertEqual(builder.read_archive(renamed), baseline)

    def test_safe_directories_are_ignored_without_extraction(self) -> None:
        files = {"assets/nested/icon.svg": b"icon", "empty.txt": b""}
        for format in ("zip", "tar.gz", "tgz"):
            with self.subTest(format=format):
                path = self.archive(files, format, ("assets", "assets/nested", "empty"))
                with mock.patch.object(zipfile.ZipFile, "extract", side_effect=AssertionError("no extraction")), \
                        mock.patch.object(zipfile.ZipFile, "extractall", side_effect=AssertionError("no extraction")), \
                        mock.patch.object(tarfile.TarFile, "extract", side_effect=AssertionError("no extraction")), \
                        mock.patch.object(tarfile.TarFile, "extractall", side_effect=AssertionError("no extraction")):
                    self.assertEqual(builder.read_archive(path), files)
        # An explicit directory after its child is still safe, not a duplicate.
        path = Path(self.temp.name) / "late-directory.zip"
        with zipfile.ZipFile(path, "w") as archive:
            archive.writestr("assets/icon.svg", b"icon")
            archive.writestr("assets/", b"")
        self.assertEqual(builder.read_archive(path), {"assets/icon.svg": b"icon"})

    def test_unsafe_file_and_directory_paths_are_rejected_in_all_formats(self) -> None:
        names = ("../outside", "/absolute", "a\\b", "a/../b", "C:/drive", "C:relative",
                 "assets/*", "assets/**", "file?.md", "file[0].md", ".", "a/./b", "a//b")
        for format in ("zip", "tar.gz", "tgz"):
            for name in names:
                for directory in (False, True):
                    with self.subTest(format=format, name=name, directory=directory):
                        path = self.archive({} if directory else {name: b"unsafe"}, format,
                                            (name,) if directory else ())
                        with self.assertRaises(builder.BuildError):
                            builder.read_archive(path)

    def test_zip_special_member_types_and_nul_names_are_rejected(self) -> None:
        path = Path(self.temp.name) / "untrusted.zip"
        for kind in (stat.S_IFLNK, stat.S_IFCHR, stat.S_IFBLK, stat.S_IFIFO, stat.S_IFSOCK):
            for directory in (False, True):
                with self.subTest(kind=kind, directory=directory):
                    entry = zipfile.ZipInfo("unsafe/" if directory else "unsafe")
                    entry.create_system = 3
                    entry.external_attr = (kind | 0o777) << 16
                    with zipfile.ZipFile(path, "w") as archive:
                        archive.writestr(entry, b"")
                    with self.assertRaisesRegex(builder.BuildError, "unsafe ZIP member"):
                        builder.read_archive(path)
        raw = builder.deterministic_zip({"nulXname": b"payload"})
        path.write_bytes(raw.replace(b"nulXname", b"nul\x00name"))
        with self.assertRaisesRegex(builder.BuildError, "unsafe ZIP member"):
            builder.read_archive(path)

    def test_zip_directory_metadata_is_checked_before_ignoring(self) -> None:
        path = Path(self.temp.name) / "directory.zip"
        for kind, name, data, safe in (
            (stat.S_IFDIR, "directory", b"", True),
            (stat.S_IFREG, "directory/", b"", False),
            (stat.S_IFDIR, "directory/", b"hidden payload", False),
        ):
            with self.subTest(kind=kind, name=name, safe=safe):
                entry = zipfile.ZipInfo(name)
                entry.create_system = 3
                entry.external_attr = (kind | 0o755) << 16
                with zipfile.ZipFile(path, "w") as archive:
                    archive.writestr(entry, data)
                if safe:
                    self.assertEqual(builder.read_archive(path), {})
                else:
                    with self.assertRaises(builder.BuildError):
                        builder.read_archive(path)

    def test_tar_links_devices_fifo_and_unknown_types_are_rejected(self) -> None:
        path = Path(self.temp.name) / "untrusted.tgz"
        for kind in (tarfile.SYMTYPE, tarfile.LNKTYPE, tarfile.CHRTYPE, tarfile.BLKTYPE,
                     tarfile.FIFOTYPE, tarfile.CONTTYPE, tarfile.GNUTYPE_SPARSE, b"?"):
            with self.subTest(kind=kind):
                entry = tarfile.TarInfo("unsafe")
                entry.type = kind
                entry.linkname = "target"
                with tarfile.open(path, "w:gz") as archive:
                    archive.addfile(entry)
                with self.assertRaises(builder.BuildError):
                    builder.read_archive(path)

    def test_duplicate_and_file_directory_conflicts_are_rejected(self) -> None:
        cases = (
            (("same", False), ("same", False)),
            (("same", True), ("same", True)),
            (("same", True), ("same", False)),
            (("same", False), ("same", True)),
            (("parent", False), ("parent/child", False)),
            (("parent/child", False), ("parent", False)),
            (("parent", False), ("parent/child", True)),
            (("parent/child", True), ("parent", False)),
        )
        for format in ("zip", "tar.gz", "tgz"):
            for members in cases:
                with self.subTest(format=format, members=members):
                    path = Path(self.temp.name) / f"conflicts.{format}"
                    with warnings.catch_warnings():
                        warnings.simplefilter("ignore", UserWarning)
                        if format == "zip":
                            with zipfile.ZipFile(path, "w") as archive:
                                for name, directory in members:
                                    archive.writestr(name + "/" if directory else name, b"")
                        else:
                            with tarfile.open(path, "w:gz") as archive:
                                for name, directory in members:
                                    entry = tarfile.TarInfo(name)
                                    entry.type = tarfile.DIRTYPE if directory else tarfile.REGTYPE
                                    archive.addfile(entry)
                    with self.assertRaisesRegex(builder.BuildError, "duplicate|file/directory conflict"):
                        builder.read_archive(path)

    def test_non_zip_and_non_gzip_tar_fail_closed(self) -> None:
        path = Path(self.temp.name) / "untrusted.tar.gz"
        for mode in ("w", "w:bz2", "w:xz"):
            with self.subTest(mode=mode):
                with tarfile.open(path, mode) as archive:
                    archive.addfile(tarfile.TarInfo("plain.txt"))
                with self.assertRaises(builder.BuildError):
                    builder.read_archive(path)
        for data in (b"", b"not an archive", b"PK\x03\x04broken", b"\x1f\x8bbroken"):
            path.write_bytes(data)
            with self.subTest(data=data), self.assertRaises(builder.BuildError):
                builder.read_archive(path)

    def test_corrupt_zip_and_gzip_streams_raise_build_error(self) -> None:
        path = Path(self.temp.name) / "corrupt.archive"
        path.write_bytes(builder.deterministic_zip({"file.txt": b"payload"}).replace(b"payload", b"damaged"))
        with self.assertRaisesRegex(builder.BuildError, "cannot read ZIP or gzip tar"):
            builder.read_archive(path)
        # Valid gzip header followed by an invalid DEFLATE block.
        path.write_bytes(b"\x1f\x8b\x08\x00\x00\x00\x00\x00\x00\xff\x07")
        with self.assertRaisesRegex(builder.BuildError, "cannot read ZIP or gzip tar"):
            builder.read_archive(path)

    def assert_invalid_gzip_trailer_rejected(self, offset: int | None) -> None:
        files = {"file.txt": b"payload"}
        for format in ("tar.gz", "tgz"):
            with self.subTest(format=format):
                path = self.archive(files, format)
                self.assertEqual(builder.read_archive(path), files)
                data = bytearray(path.read_bytes())
                if offset is None:
                    del data[-8:]
                else:
                    data[offset] ^= 1
                with self.assertRaises((EOFError, gzip.BadGzipFile)):
                    gzip.decompress(data)
                path.write_bytes(data)
                with self.assertRaisesRegex(builder.BuildError, "cannot read ZIP or gzip tar"):
                    builder.read_archive(path)

    def test_gzip_missing_trailer_is_rejected(self) -> None:
        self.assert_invalid_gzip_trailer_rejected(None)

    def test_gzip_bad_crc_is_rejected(self) -> None:
        self.assert_invalid_gzip_trailer_rejected(-8)

    def test_gzip_wrong_isize_is_rejected(self) -> None:
        self.assert_invalid_gzip_trailer_rejected(-4)

    def test_archive_restore_rejects_unexpected_and_missing_baseline_files(self) -> None:
        candidate, _ = self.build()
        baseline = self.baseline()
        missing = dict(baseline)
        del missing[builder.OLD_DELETE_PATHS[0]]
        for format in ("zip", "tar.gz", "tgz"):
            for drifted in ({**baseline, "unexpected.txt": b"drift"}, missing):
                with self.subTest(format=format, files=len(drifted)):
                    path = self.archive(drifted, format)
                    with self.assertRaisesRegex(builder.BuildError, "file set"):
                        builder.restore_payload(builder.read_archive(path), candidate)

    def test_cli_prepare_restore_is_equivalent_for_all_input_formats(self) -> None:
        baseline = self.baseline()
        candidate, _ = self.build()
        expected, only06, deletes = builder.restore_payload(baseline, candidate)
        archives = {}
        for label, files in (("baseline", baseline), ("candidate", candidate)):
            for format in ("zip", "tar.gz", "tgz"):
                path = self.archive(files, format, ("assets", "skills", "unused"))
                saved = path.with_name(f"{label}.{format}")
                shutil.copyfile(path, saved)
                archives[label, format] = saved
        for baseline_format in ("zip", "tar.gz", "tgz"):
            for candidate_format in ("zip", "tar.gz", "tgz"):
                with self.subTest(baseline=baseline_format, candidate=candidate_format):
                    output = Path(self.temp.name) / f"restore-{baseline_format}-{candidate_format}"
                    package, archive, receipts = output / "package", output / "restore.zip", output / "receipts"
                    self.assertEqual(builder.main([
                        "prepare-restore", "--baseline-archive", str(archives["baseline", baseline_format]),
                        "--candidate-archive", str(archives["candidate", candidate_format]),
                        "--output-root", str(package), "--archive", str(archive), "--receipt-dir", str(receipts),
                    ]), 0)
                    self.assertEqual(builder.output_files(package), expected)
                    self.assertEqual(archive.read_bytes(), builder.deterministic_zip(expected))
                    self.assertEqual((receipts / "RESTORE_06_ONLY_PATHS.json").read_bytes(), builder.json_bytes(only06))
                    self.assertEqual((receipts / "RESTORE_DELETE_PATHS.json").read_bytes(), builder.json_bytes(deletes))

    def test_glob_cannot_enter_restore_upload_or_delete_sets(self) -> None:
        files, _ = self.build()
        files[f"{builder.ROUTE_ROOT}/writing-fidelity/assets/*"] = b"bad path"
        with self.assertRaisesRegex(builder.BuildError, "unsafe package path"):
            builder.validate_package(files, "0.6.0")


if __name__ == "__main__":
    unittest.main()
