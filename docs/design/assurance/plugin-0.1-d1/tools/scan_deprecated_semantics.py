#!/usr/bin/env python3
"""D5: scan current Blueprint text; never scan or rewrite frozen versions."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import sys

DESIGN = Path(__file__).resolve().parents[1]

# Each concept is tied to an approved revision, rather than guessed from age.
RULES = [
    ("separate-freeze-explanation", r"冻结说明|FREEZE_EXPLANATION(?:\.md(?:/\.pdf)?|\.pdf)?",
     "REVISION_0.2_PLAN.md#修订二；MERGE_DECISIONS.md §30：改为 Blueprint freeze-review"),
    ("explanation-identity", r"explanation_sha256",
     "REVISION_0.2_PLAN.md#修订二 第2项；MERGE_DECISIONS.md §30：只批准 snapshot_sha256"),
    ("old-regression-count", r"(?:共\s*)?[8八]\s*个(?:回归)?用例|新能力\s*12|(?:共\s*)?18\s*条检查",
     "REVISION_0.2_PLAN.md#补充决定 第1项；MERGE_DECISIONS.md §30：9用例，14+3+1+2=20条"),
    ("old-gate-scope", r"D6、D8\s*只针对新增和改写的节点（[^）]+）",
     "MERGE_DECISIONS.md §30；D1 本轮裁决：D6 按自身字段差异，D8 按读者文字差异"),
    ("old-blueprint-identity", r"blueprint_sha256",
     "MERGE_DECISIONS.md §22、§30；SPEC.md §6.5：区分快照、语义及完整包身份"),
]

# Only these exact local phrases are migration/history statements. A negative
# elsewhere in the field must not hide a new positive use of a deleted concept.
PERMITTED = [
    r"不再另写冻结说明", r"取消原来对单独冻结说明的四项检查",
    r"不再另有冻结说明文件身份", r"不另生成冻结说明", r"不再转述成单独冻结说明",
    r"其中单独冻结说明的规则已由 0\.2 修订计划和 MERGE_DECISIONS 第 30 节取代",
    r"本仓库提交 `2965b008` 的第一版冻结说明",
    r"0\.1 的 `FREEZE_EXPLANATION\.md/\.pdf` 与 `versions/0\.1/` 只作历史保留",
    r"(?:不再包含|不含)\s*`?explanation_sha256`?",
    r"不再有\s*`explanation_sha256`",
    r"不再用旧 blueprint_sha256 或 explanation_sha256",
    r"`freeze\.json` 的必填字段 `blueprint_sha256` 以 `snapshot_sha256` 和 `bundle_sha256` 两项代替",
]


def strings(value, pointer=""):
    if isinstance(value, dict):
        for key, child in value.items():
            if pointer == "" and key == "versions":
                continue
            escaped = key.replace("~", "~0").replace("/", "~1")
            yield from strings(child, pointer + "/" + escaped)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from strings(child, f"{pointer}/{index}")
    elif isinstance(value, str):
        yield pointer, value


def scan(bundle):
    findings, permitted, checked = [], [], 0
    node_count = sum(1 for pointer, _ in strings(bundle)
                     if re.fullmatch(r"/nodes/\d+(?:/children/\d+)*/id", pointer))
    for pointer, text in strings(bundle):
        checked += 1
        allowed = [m.span() for pattern in PERMITTED for m in re.finditer(pattern, text)]
        for rule, pattern, authority in RULES:
            for match in re.finditer(pattern, text):
                item = {"rule": rule, "pointer": pointer, "offset": match.start(),
                        "match": match.group(), "authority": authority,
                        "context": text[max(0, match.start()-45):match.end()+65]}
                if any(start <= match.start() and match.end() <= end for start, end in allowed):
                    permitted.append(item)
                else:
                    findings.append(item)
    return {"scope": "all current strings including all node fields, walkthroughs and evidence; excludes versions",
            "nodes_checked": node_count, "strings_checked": checked,
            "residual_count": len(findings), "permitted_migration_or_history_count": len(permitted),
            "findings": findings, "permitted": permitted}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("blueprint", nargs="?", type=Path, default=DESIGN / "blueprint.json")
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    raw = args.blueprint.read_bytes()
    report = scan(json.loads(raw))
    report["source_sha256"] = hashlib.sha256(raw).hexdigest()
    report["rules"] = [{"id": name, "pattern": pattern, "authority": authority}
                       for name, pattern, authority in RULES]
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({key: report[key] for key in
                      ["nodes_checked", "strings_checked", "residual_count",
                       "permitted_migration_or_history_count"]}, ensure_ascii=False))
    for finding in report["findings"]:
        print(f"{finding['pointer']} [{finding['rule']}] {finding['context']}")
    return 1 if report["residual_count"] else 0


if __name__ == "__main__":
    sys.exit(main())
