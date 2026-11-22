#!/usr/bin/env python3
"""Validate JSON-form YAML v1 or read-only original four-field YAML."""
import argparse
import sys
from runner import RunnerError, load_case, validate


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('cases', nargs='+')
    parser.add_argument('--allow-gaps', action='store_true', help='草稿允许空字段；实际执行仍会跳过')
    args = parser.parse_args()
    bad = 0
    for path in args.cases:
        try:
            case = load_case(path)
            errors, gaps = validate(case)
            label = case.get('id', 'unknown')
            print(f'{label}: 格式错误 {len(errors)}；缺口 {len(gaps)}')
            for error in errors:
                print('  错误：' + error)
            for gap in gaps:
                print('  缺口：' + gap)
            bad += bool(errors or (gaps and not args.allow_gaps))
        except (RunnerError, OSError, ValueError) as exc:
            print('读取失败：' + (str(exc) if isinstance(exc, RunnerError) else type(exc).__name__))
            bad += 1
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main())
