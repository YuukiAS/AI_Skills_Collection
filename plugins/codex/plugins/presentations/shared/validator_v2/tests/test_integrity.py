import copy
import hashlib
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
import zlib

from presentations_validator_v2.cli import parser, run


class Bundle:
    """Disposable Git object fixture. No refs or objects in the working repository."""
    def __init__(self, root):
        self.root = root
        self.git_dir = root / "repo" / ".git"
        (self.git_dir / "objects").mkdir(parents=True)
        (self.git_dir / "refs").mkdir()
        (self.git_dir / "config").write_text(
            '[core]\nrepositoryformatversion = 0\nbare = false\n'
            '[remote "origin"]\nurl = https://github.com/example/deck.git\n'
        )
        self.authority_dir = root / "authority"
        self.candidate_dir = root / "candidate"
        self.authority_dir.mkdir()
        self.candidate_dir.mkdir()
        files = {
            "artifact.pdf": b"render bytes",
            "course.tex": b"locked course source",
            "copy.txt": b"frozen copy",
            "object.tsv": b"x\ty",
        }
        self.blobs = {key: self.git_object("blob", value) for key, value in files.items()}
        self.tree = self.git_tree(self.blobs)
        self.old = self.git_commit(self.tree)
        self.new = self.git_commit(self.tree, self.old)
        unrelated = self.git_commit(self.tree, self.new)
        (self.git_dir / "HEAD").write_text(unrelated + "\n")
        self.artifact_hash = hashlib.sha256(files["artifact.pdf"]).hexdigest()
        self.source = {
            "id": "src", "role": "content", "path": "course.tex", "commit": "candidate",
            "git_blob_sha": self.blobs["course.tex"], "immutable": True,
        }
        self.authority = {
            "repository": "example/deck", "baseline_commit": self.old,
            "mandatory_source_identities": [self.source],
            "pages": [{"id": "first", "components": ["chrome"]},
                      {"id": "second", "components": ["chrome"]}],
            "components": [{"id": "chrome", "type": "shared", "consumers": ["first", "second"]}],
            "requirements": [{"id": "preserve", "rule": "Copy freeze"}],
            "feedback": [{"id": "feedback", "artifact_id": "original", "historical_page": 4,
                          "lifecycle": "open", "targets": ["first"]}],
            "round_scope": {"paths": {}, "pages": [], "components": []},
            "locks": [{"id": "lock", "path": "course.tex", "git_blob_sha": self.blobs["course.tex"]}],
            "required_objects": [{"id": "object", "path": "object.tsv",
                                  "sha256": hashlib.sha256(files["object.tsv"]).hexdigest()}],
            "object_decisions": [],
            "visible_copy": [{"id": "copy", "path": "copy.txt",
                              "sha256": hashlib.sha256(files["copy.txt"]).hexdigest()}],
            "artifacts": [{"id": "render", "path": "artifact.pdf"}],
        }
        self.candidate = {
            "candidate_manifest.json": {
                "repository": "example/deck", "baseline_commit": self.old,
                "candidate_commit": self.new, "candidate_tree": self.tree,
            },
            "source_identity_manifest.json": [{**self.source, "commit": self.new}],
            "derived_page_registry.json": self.authority["pages"],
            "derived_component_registry.json": self.authority["components"],
            "derived_gate_registry.json": self.authority["requirements"],
            "derived_feedback_registry.jsonl": self.authority["feedback"],
            "patch_manifest.json": {
                "changed_paths": [], "modified_pages": [], "modified_components": [],
                "regression_pages": [], "lock_evidence": self.authority["locks"],
                "required_object_relocations": [],
            },
            "render_identity_manifest.json": [
                {"id": "render", "path": "artifact.pdf", "commit": self.new,
                 "sha256": self.artifact_hash},
            ],
            "review_scope.json": {
                "verdict": "PASS", "candidate_commit": self.new,
                "pages": ["first", "second"], "components": ["chrome"],
                "requirements": ["preserve"], "unreviewed_requirements": [],
                "artifact_hashes": [self.artifact_hash],
            },
        }
        self.candidate = copy.deepcopy(self.candidate)

    def git_object(self, kind, payload):
        wire = f"{kind} {len(payload)}\0".encode() + payload
        oid = hashlib.sha1(wire).hexdigest()
        path = self.git_dir / "objects" / oid[:2] / oid[2:]
        path.parent.mkdir(exist_ok=True)
        path.write_bytes(zlib.compress(wire))
        return oid

    def git_tree(self, entries):
        return self.git_object("tree", b"".join(
            b"100644 " + name.encode() + b"\0" + bytes.fromhex(oid)
            for name, oid in sorted(entries.items())
        ))

    def git_commit(self, tree, parent=None):
        lines = [f"tree {tree}"]
        if parent:
            lines.append(f"parent {parent}")
        lines.extend(["author Example <example@example.org> 0 +0000",
                      "committer Example <example@example.org> 0 +0000", "", "Fixture", ""])
        return self.git_object("commit", "\n".join(lines).encode())

    def write(self):
        (self.authority_dir / "authority_manifest.json").write_text(json.dumps(self.authority))
        for name, value in self.candidate.items():
            if isinstance(value, str):
                text = value
            elif name.endswith(".jsonl"):
                text = "\n".join(json.dumps(row) for row in value)
            else:
                text = json.dumps(value)
            (self.candidate_dir / name).write_text(text)

    def run(self, *flags):
        self.write()
        return run(parser().parse_args([
            "validate", "--authority-bundle", str(self.authority_dir), "--candidate-bundle",
            str(self.candidate_dir), "--repo", str(self.git_dir.parent), *flags,
        ]))


class IntegrityTests(unittest.TestCase):
    def mutation(self, label, change, wanted, detector):
        with self.subTest(mutation=label), TemporaryDirectory() as tmp:
            bundle = Bundle(Path(tmp))
            change(bundle)
            result, code = bundle.run()
            self.assertEqual(result["state"], wanted, result)
            self.assertIn(detector, {row["detector"] for row in result["rows"]
                                     if row["status"] in {"FAIL", "NOT_VERIFIED"}})
            self.assertIn(code, {1, 2})

    def test_historical_commit_does_not_need_head(self):
        with TemporaryDirectory() as tmp:
            result, code = Bundle(Path(tmp)).run()
            self.assertEqual(result["state"], "DETERMINISTIC_PASS", result)
            self.assertEqual(code, 0)

    def test_duplicate_key_before_materialization(self):
        def change(b):
            source = json.dumps(b.candidate["candidate_manifest.json"])
            b.candidate["candidate_manifest.json"] = '{"repository":"shadow",' + source[1:]
        self.mutation("duplicate JSON key", change, "DETERMINISTIC_FAIL", "INPUT")

    def test_duplicate_id_rejected(self):
        def change(b):
            b.candidate["derived_page_registry.json"] *= 2
        self.mutation("duplicate ID", change, "DETERMINISTIC_FAIL", "REGISTRIES")

    def test_exact_source_tuple(self):
        for field, value in (("path", "copy.txt"), ("role", "notes"), ("commit", "old"),
                             ("git_blob_sha", None), ("immutable", False)):
            def change(b):
                row = b.candidate["source_identity_manifest.json"][0]
                if value is None:
                    del row[field]
                else:
                    row[field] = b.old if value == "old" else value
            self.mutation(field, change, "DETERMINISTIC_FAIL", "SOURCE_BINDING")

    def test_coordinated_source_substitution(self):
        def path_and_blob(b):
            b.candidate["source_identity_manifest.json"][0].update(
                path="copy.txt", git_blob_sha=b.blobs["copy.txt"]
            )

        def stale_immutable(b):
            # The candidate reports the real historical blob; its new tree changed that path.
            b.source["commit"] = b.old
            b.candidate["source_identity_manifest.json"][0]["commit"] = b.old
            replacement = b.git_object("blob", b"changed")
            new_tree = b.git_tree({**b.blobs, "course.tex": replacement})
            new = b.git_commit(new_tree, b.old)
            b.candidate["candidate_manifest.json"].update(candidate_commit=new, candidate_tree=new_tree)
            b.candidate["render_identity_manifest.json"][0]["commit"] = new
            b.candidate["review_scope.json"]["candidate_commit"] = new

        for change in (path_and_blob, stale_immutable):
            self.mutation(change.__name__, change, "DETERMINISTIC_FAIL", "SOURCE_BINDING")

    def test_fake_relocation_and_wrong_real_destination(self):
        for permission_exists in (False, True):
            def change(b):
                if permission_exists:
                    b.authority["object_decisions"] = [
                        {"id": "approval", "object_id": "object", "action": "relocate",
                         "destination": "allowed.tsv"}
                    ]
                b.candidate["patch_manifest.json"]["required_object_relocations"] = [
                    {"authority_record_id": "approval", "object_id": "object",
                     "action": "relocate", "destination": "copy.txt"}
                ]
            self.mutation(permission_exists, change, "DETERMINISTIC_FAIL", "OBJECT_DECISION")

    def test_feedback_component_full_fidelity(self):
        for file, code, fields in (
            ("derived_feedback_registry.jsonl", "FEEDBACK_FIDELITY",
             {"artifact_id": "shadow", "historical_page": 99, "provenance": "made up"}),
            ("derived_component_registry.json", "COMPONENT_FIDELITY",
             {"type": "local", "style_contract": "new"}),
        ):
            def change(b):
                b.candidate[file][0].update(fields)
            self.mutation(file, change, "DETERMINISTIC_FAIL", code)

    def test_partial_global_review_and_artifact_namespace(self):
        for key, value in (("pages", ["first"]), ("components", []), ("requirements", []),
                           ("artifact_hashes", []), ("artifact_hashes", ["render"]),
                           ("artifact_hashes", ["a" * 64])):
            def change(b):
                b.candidate["review_scope.json"][key] = value
            code = "ARTIFACTS_AND_REVIEW" if value == ["render"] else "REVIEW_SCOPE"
            self.mutation((key, value), change, "DETERMINISTIC_FAIL", code)

    def test_missing_lock_and_mandatory_identity(self):
        def no_lock(b):
            b.candidate["patch_manifest.json"].pop("lock_evidence")
        self.mutation("missing lock", no_lock, "DETERMINISTIC_FAIL", "LOCK_SET")
        for field in ("baseline_commit", "candidate_commit", "candidate_tree"):
            def change(b):
                del b.candidate["candidate_manifest.json"][field]
            self.mutation(field, change, "DETERMINISTIC_FAIL", "INPUT")

    def test_combined_layout_rejects_unbound_candidate_pdf(self):
        with TemporaryDirectory() as tmp:
            b = Bundle(Path(tmp))
            wrong_pdf = b.root / "wrong.pdf"
            wrong_pdf.write_bytes(b"Not the Git-bound candidate artifact")
            result, code = b.run(
                "--pdf", str(wrong_pdf), "--contract", "contract.yaml",
                "--source-manifest", "manifest.json", "--object-map", "map.json",
                "--source-root", str(b.root),
            )
            self.assertEqual(code, 1, result)
            self.assertIn("not a verified Git artifact", result["rows"][0]["message"])

    def test_replay_no_substitution(self):
        with TemporaryDirectory() as tmp:
            b = Bundle(Path(tmp))
            case = {"repository": "example/deck", "locators": [
                {"id": "exact", "commit": b.old, "path": "artifact.pdf",
                 "sha256": b.artifact_hash},
                {"id": "missing", "commit": b.old, "path": "artifact-v2.pdf",
                 "sha256": b.artifact_hash},
            ]}
            config = b.root / "replay.json"
            config.write_text(json.dumps(case))
            result, code = run(parser().parse_args([
                "replay", "--repo", str(b.git_dir.parent), "--config", str(config)
            ]))
            self.assertEqual(code, 2)
            self.assertEqual([row["status"] for row in result["rows"]], ["PASS", "NOT_VERIFIED"])
