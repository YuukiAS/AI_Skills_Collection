import hashlib
import json
from pathlib import Path, PurePosixPath
import re


class InputError(ValueError):
    """Malformed or contradictory evidence."""


class EvidenceMissing(Exception):
    """Required evidence was not available to the validator."""


OID = re.compile(r"[0-9a-f]{40}")
DIGEST = re.compile(r"[0-9a-f]{64}")


def unique_pairs(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise InputError(f"Duplicate mapping key: {key!r}")
        result[key] = value
    return result


def json_load(text):
    def reject_constant(value):
        raise InputError(f"Invalid JSON constant: {value}")

    return json.loads(text, object_pairs_hook=unique_pairs, parse_constant=reject_constant)


def read(path: Path) -> bytes:
    try:
        return path.read_bytes()
    except OSError as exc:
        raise EvidenceMissing(f"Cannot read {path}: {exc.strerror}") from exc


def read_json(path: Path):
    blob = read(path).decode("utf-8")
    if path.suffix == ".jsonl":
        return [json_load(line) for line in blob.splitlines() if line.strip()]
    return json_load(blob)


def read_contract(path: Path):
    if path.suffix == ".json":
        return read_json(path)
    try:
        import yaml
    except ImportError as exc:
        raise EvidenceMissing("PyYAML is required for a YAML contract") from exc

    class StrictSafeLoader(yaml.SafeLoader):
        pass

    def construct_mapping(loader, node):
        loader.flatten_mapping(node)
        return unique_pairs(loader.construct_pairs(node, deep=True))

    StrictSafeLoader.add_constructor(
        yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, construct_mapping
    )
    try:
        return yaml.load(read(path), Loader=StrictSafeLoader)
    except yaml.YAMLError as exc:
        raise InputError(f"Invalid YAML contract: {exc}") from exc


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical(value) -> bytes:
    return json.dumps(value, sort_keys=True, allow_nan=False,
                      separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def tagged(value, pattern, field):
    if not isinstance(value, str) or not pattern.fullmatch(value):
        raise InputError(f"{field} must match {pattern.pattern}")
    return value


def identifier(value):
    if not isinstance(value, str) or not value or value != value.strip():
        raise InputError(f"Invalid identifier {value!r}")
    return value


def unique_ids(values):
    if not isinstance(values, list):
        raise InputError("Expected an array of IDs")
    result = {identifier(value) for value in values}
    if len(result) != len(values):
        raise InputError("Duplicate IDs in array")
    return result


def records(values, key="id"):
    if not isinstance(values, list):
        raise InputError("Expected an array of records")
    seen = {}
    for value in values:
        if not isinstance(value, dict):
            raise InputError("Record must be an object")
        record_id = identifier(value.get(key))
        if record_id in seen:
            raise InputError(f"Duplicate {key}: {record_id}")
        seen[record_id] = value
    return seen


def repo_path(value):
    value = identifier(value)
    path = PurePosixPath(value)
    if (path.is_absolute() or path.as_posix() != value or value == "."
            or ".." in path.parts or any(c in value for c in "\x00:\\")):
        raise InputError(f"Not a canonical repository path: {value!r}")
    return value


def child_path(root: Path, path: str) -> Path:
    result = (root / repo_path(path)).resolve()
    if not result.is_relative_to(root.resolve()):
        raise InputError(f"Path escapes evidence root: {path!r}")
    return result
