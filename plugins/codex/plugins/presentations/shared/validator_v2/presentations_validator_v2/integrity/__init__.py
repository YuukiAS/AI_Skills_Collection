"""Authority and candidate comparisons against independently resolved Git objects."""

from pathlib import Path

from ..io import (DIGEST, OID, EvidenceMissing, InputError, canonical, identifier,
                  read_json, records, repo_path, sha256, tagged, unique_ids)
from ..review import coverage
from ..schemas import Finding
from .git import blob, blob_oid, changed_paths, git, identity, tree


def validate(authority_dir, candidate_dir, repo):
    authority_dir, candidate_dir, repo = map(Path, (authority_dir, candidate_dir, repo))
    authority = read_json(authority_dir / "authority_manifest.json")
    candidate = read_json(candidate_dir / "candidate_manifest.json")
    baseline = tagged(candidate["baseline_commit"], OID, "baseline_commit")
    commit = tagged(candidate["candidate_commit"], OID, "candidate_commit")
    candidate_tree = tagged(candidate["candidate_tree"], OID, "candidate_tree")
    if (baseline != authority["baseline_commit"]
            or candidate["repository"] != authority["repository"]
            or identity(repo) != authority["repository"]):
        raise InputError("Repository or baseline does not match authority")
    tree(repo, baseline)
    if candidate_tree != tree(repo, commit):
        raise InputError("Candidate tree does not match its Git commit")
    if not git(repo, "merge-base", baseline, commit).strip().decode() == baseline:
        raise InputError("Baseline is not an ancestor of the candidate")
    if authority.get("require_head", False):
        if git(repo, "rev-parse", "HEAD").strip().decode() != commit:
            raise InputError("Candidate is not the required local HEAD")
    if "candidate_commit" in authority and authority["candidate_commit"] != commit:
        raise InputError("Candidate differs from frozen replay commit")
    identity_data = {
        "authority_sha256": sha256(canonical(authority)), "repository": authority["repository"],
        "baseline_commit": baseline, "candidate_commit": commit, "candidate_tree": candidate_tree,
    }
    rows = [Finding("GIT_IDENTITY", "PASS", commit, "Resolved repository, baseline and tree")]
    context = (authority, candidate_dir, repo, baseline, commit)
    for detector in DETECTORS:
        try:
            rows.extend(detector(*context))
        except EvidenceMissing as exc:
            rows.append(Finding(detector.__name__.upper(), "NOT_VERIFIED", commit, str(exc)))
        except (InputError, KeyError, TypeError, ValueError, AttributeError) as exc:
            rows.append(Finding(detector.__name__.upper(), "FAIL", commit, str(exc)))
    identity_data["verified_artifact_hashes"] = sorted({
        row.evidence["sha256"] for row in rows
        if row.detector == "ARTIFACT_BINDING" and row.status == "PASS"
    })
    return rows, identity_data


def compare(code, target, condition, message, **evidence):
    return Finding(code, "PASS" if condition else "FAIL", target, message, evidence=evidence)


def sources(authority, directory, repo, baseline, commit):
    expected = records(authority["mandatory_source_identities"])
    actual = records(read_json(directory / "source_identity_manifest.json"))
    rows = [compare("SOURCE_SET", "sources", expected.keys() == actual.keys(),
                    "Exact source identity set", missing=sorted(expected.keys() - actual.keys()),
                    extra=sorted(actual.keys() - expected.keys()))]
    for name, record in expected.items():
        bound = record["commit"]
        lookup = commit if bound == "candidate" else tagged(bound, OID, "source commit")
        path = repo_path(record["path"])
        immutable = record["immutable"]
        if not isinstance(immutable, bool):
            raise InputError("immutable must be boolean")
        identifier(record["role"])
        authority_blob = tagged(record["git_blob_sha"], OID, "authority source blob")
        expected_row = {**record, "commit": lookup}
        if name not in actual:
            continue
        if canonical(actual[name]) != canonical(expected_row):
            rows.append(compare("SOURCE_BINDING", name, False, "Source tuple differs from authority"))
            continue
        tree(repo, lookup)
        try:
            real = blob_oid(repo, lookup, path)
            lock_ok = not immutable or blob_oid(repo, commit, path) == authority_blob
        except EvidenceMissing:
            rows.append(compare("SOURCE_BINDING", name, False,
                                "Required source path could not be resolved", path=path, commit=lookup))
            continue
        rows.append(compare("SOURCE_BINDING", name, real == authority_blob and lock_ok,
                            "Resolved source and immutability at exact Git paths",
                            path=path, commit=lookup, git_blob_sha=real))
    return rows


def registries(authority, directory, repo, baseline, commit):
    pages = records(authority["pages"])
    components = records(authority["components"])
    rows = []
    for name, file, expected in (
        ("FEEDBACK", "derived_feedback_registry.jsonl", authority["feedback"]),
        ("PAGE", "derived_page_registry.json", authority["pages"]),
        ("COMPONENT", "derived_component_registry.json", authority["components"]),
        ("GATE", "derived_gate_registry.json", authority["requirements"]),
    ):
        expected_by_id = records(expected)
        actual = read_json(directory / file)
        actual_by_id = records(actual)
        rows.append(compare(f"{name}_FIDELITY", file,
                            list(expected_by_id) == list(actual_by_id)
                            and canonical(expected_by_id) == canonical(actual_by_id),
                            "Ordered full record fidelity",
                            changed_ids=sorted(key for key in expected_by_id.keys() & actual_by_id.keys()
                                               if canonical(expected_by_id[key]) != canonical(actual_by_id[key])),
                            missing=sorted(expected_by_id.keys() - actual_by_id.keys()),
                            extra=sorted(actual_by_id.keys() - expected_by_id.keys())))
    inverse = {name: set() for name in components}
    for page_id, page in pages.items():
        for component_id in unique_ids(page["components"]):
            if component_id not in inverse:
                raise InputError(f"Unknown component {component_id} on {page_id}")
            inverse[component_id].add(page_id)
    for name, component in components.items():
        rows.append(compare("COMPONENT_INVERSE", name,
                            inverse[name] == unique_ids(component["consumers"]),
                            "Page bindings equal component consumer inverse"))
    for row in records(authority["feedback"]).values():
        if "targets" in row:
            valid = unique_ids(row["targets"]) <= (pages.keys() | components.keys())
            rows.append(compare("FEEDBACK_ANCESTRY", row["id"], valid,
                                "Frozen feedback targets resolve to stable IDs"))
    return rows


def scope_and_locks(authority, directory, repo, baseline, commit):
    patch = read_json(directory / "patch_manifest.json")
    changes = changed_paths(repo, baseline, commit)
    scope = authority["round_scope"]
    bindings = scope["paths"]
    expected_targets = {"pages": set(), "components": set()}
    for path in sorted(changes & bindings.keys()):
        for key in expected_targets:
            targets = unique_ids(bindings[path][key])
            expected_targets[key].update(targets)
    allowed = all(expected_targets[key] <= unique_ids(scope[key]) for key in expected_targets)
    scope_ok = (
        changes <= bindings.keys()
        and unique_ids(patch["changed_paths"]) == changes
        and all(bindings[path]["pages"] or bindings[path]["components"]
                for path in changes & bindings.keys())
        and allowed
        and all(unique_ids(patch[f"modified_{key}"]) == expected_targets[key]
                for key in expected_targets)
    )
    components = records(authority["components"])
    consumers = set().union(*(unique_ids(components[key]["consumers"])
                              for key in expected_targets["components"]))
    scope_ok = scope_ok and consumers <= unique_ids(patch["regression_pages"])
    rows = [compare("ROUND_SCOPE", commit, scope_ok, "Git diff, round scope and consumer regression",
                    changed_paths=sorted(changes), affected_consumers=sorted(consumers))]
    locks = records(authority["locks"])
    claimed = records(patch.get("lock_evidence", []))
    rows.append(compare("LOCK_SET", commit, locks.keys() == claimed.keys(),
                        "Exact required lock evidence", missing=sorted(locks.keys() - claimed.keys())))
    for lock_id, lock in locks.items():
        if lock_id not in claimed:
            continue
        path = repo_path(lock["path"])
        frozen = tagged(lock["git_blob_sha"], OID, "lock blob")
        try:
            old, new = (blob_oid(repo, candidate, path) for candidate in (baseline, commit))
        except EvidenceMissing:
            rows.append(compare("LOCK", lock_id, False, "Locked path unavailable", path=path))
            continue
        rows.append(compare("LOCK", lock_id,
                            old == new == frozen
                            and claimed[lock_id] == {"id": lock_id, "path": path,
                                                     "git_blob_sha": new},
                            "Independent baseline and candidate lock comparison",
                            path=path, baseline_blob=old, candidate_blob=new))
    return rows


def objects(authority, directory, repo, baseline, commit):
    required = records(authority["required_objects"])
    permissions = records(authority["object_decisions"])
    patch = read_json(directory / "patch_manifest.json")
    decisions = records(patch["required_object_relocations"], "object_id")
    rows = [compare("OBJECT_SCOPE", commit, decisions.keys() <= required.keys(),
                    "Only known objects may be relocated or retired")]
    for object_id, obj in required.items():
        decision = decisions.get(object_id)
        if decision:
            permission = permissions.get(decision.get("authority_record_id"))
            if (not permission or permission.get("object_id") != object_id
                    or permission.get("action") != decision.get("action")
                    or "destination" not in decision
                    or permission.get("destination") != decision["destination"]
                    or decision.get("action") not in {"relocate", "retire"}
                    or (decision["action"] == "retire" and decision["destination"] is not None)):
                rows.append(compare("OBJECT_DECISION", object_id, False,
                                    "No matching relocation or retirement authority"))
                continue
            if decision["action"] == "retire":
                rows.append(compare("OBJECT_DECISION", object_id, True, "Authorized retirement"))
                continue
        path = repo_path(decision["destination"] if decision else obj["path"])
        digest = tagged(obj["sha256"], DIGEST, "required object digest")
        try:
            ok = sha256(blob(repo, commit, path)) == digest
        except EvidenceMissing:
            ok = False
        rows.append(compare("REQUIRED_OBJECT", object_id, ok,
                            "Required object identity at its authorized location", path=path))
    for entry_id, entry in records(authority["visible_copy"]).items():
        path = repo_path(entry["path"])
        digest = tagged(entry["sha256"], DIGEST, "visible copy digest")
        try:
            ok = sha256(blob(repo, commit, path)) == digest
        except EvidenceMissing:
            ok = False
        rows.append(compare("VISIBLE_COPY", entry_id, ok, "Exact frozen copy evidence blob", path=path))
    return rows


def artifacts_and_review(authority, directory, repo, baseline, commit):
    expected = records(authority["artifacts"])
    supplied = records(read_json(directory / "render_identity_manifest.json"))
    rows = [compare("ARTIFACT_SET", commit, expected.keys() == supplied.keys() and bool(expected),
                    "Exact nonempty rendered artifact set")]
    hashes = set()
    for name in expected.keys() & supplied.keys():
        expected_entry = expected[name]
        artifact_commit = expected_entry.get("commit", "candidate")
        artifact_commit = commit if artifact_commit == "candidate" else artifact_commit
        tree(repo, artifact_commit)
        path = repo_path(expected_entry["path"])
        candidate_entry = supplied[name]
        declared = tagged(candidate_entry["sha256"], DIGEST, "artifact digest")
        render_bytes = blob(repo, artifact_commit, path)
        actual = sha256(render_bytes)
        hashes.add(actual)
        if "rendered_copy" in expected_entry:
            rows.extend(rendered_copy(name, render_bytes, expected_entry["rendered_copy"]))
        rows.append(compare("ARTIFACT_BINDING", name,
                            actual == declared == expected_entry.get("sha256", actual)
                            and candidate_entry["path"] == path
                            and candidate_entry["commit"] == artifact_commit,
                            "Rendered artifact path, commit and SHA-256", sha256=actual, path=path))
    mandatory = {
        "artifact_hashes": hashes,
        "pages": set(records(authority["pages"])),
        "components": set(records(authority["components"])),
        "requirements": set(records(authority["requirements"])),
    }
    rows.append(coverage(read_json(directory / "review_scope.json"), mandatory, commit))
    return rows


def rendered_copy(artifact_id, data, authority):
    from ..render import document

    with document(data) as pdf:
        if not isinstance(authority, list) or len(authority) != len(pdf):
            return [compare("RENDERED_COPY", artifact_id, False, "Rendered page coverage differs")]
        rows = []
        for index, (page, expected) in enumerate(zip(pdf, authority), start=1):
            if not isinstance(expected, list) or not all(isinstance(line, str) for line in expected):
                raise InputError("Visible copy authority must list exact text lines by page")
            actual = [line for line in page.get_text(sort=False).splitlines() if line.strip()]
            rows.append(compare("RENDERED_COPY", f"{artifact_id}/{index}", actual == expected,
                                "Exact PDF text layer against frozen copy"))
        return rows


DETECTORS = (sources, registries, scope_and_locks, objects, artifacts_and_review)
