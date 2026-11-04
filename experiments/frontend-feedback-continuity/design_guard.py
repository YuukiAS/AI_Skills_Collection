#!/usr/bin/env python3
"""Frontend Design continuity guard (experimental). Python 3.10+, stdlib only.

Mechanically checks scope, candidate identity and evidence completeness.
Does not make design decisions or substitute for visual assessment.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import subprocess
import sys

BASELINE_SCHEMA = 'fd-baseline-v1'
TASK_SCHEMA = 'fd-change-v1'
PROOF_SCHEMA = 'fd-proof-v1'
CHECK_SCHEMA = 'fd-check-v1'


def load(path: str | Path) -> dict:
    with open(path, encoding='utf-8') as f:
        data = json.load(f)
    if not isinstance(data, dict):
        raise ValueError(f'Expected JSON object: {path}')
    return data


def dump(path: str | Path, value: dict) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')


def git(repo: Path, *args: str) -> str:
    p = subprocess.run(['git', '-C', str(repo), *args], capture_output=True, text=True, check=True)
    return p.stdout.strip()


def within_scope(path: str, allowed: list[str]) -> bool:
    if path.startswith('/') or '..' in PurePosixPath(path).parts:
        return False
    for entry in allowed:
        if entry.startswith('/') or '..' in PurePosixPath(entry).parts or entry.strip() == '':
            continue
        if entry.endswith('/') and path.startswith(entry):
            return True
        if path == entry:
            return True
    return False


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda: f.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def validate_baseline(value: dict) -> None:
    if value.get('schema') != BASELINE_SCHEMA:
        raise ValueError('Invalid baseline schema')
    if not value.get('current_commit') or not value.get('surface'):
        raise ValueError('Baseline needs current_commit and surface')
    if not isinstance(value.get('accepted'), list):
        raise ValueError('Baseline accepted must be list')
    ids = [x.get('id') for x in value['accepted']]
    if len(ids) != len(set(ids)) or any(not x for x in ids):
        raise ValueError('Accepted ids must be unique and nonempty')
    for x in value['accepted']:
        if x.get('status') not in ('ACCEPTED', 'PARTIAL_ACCEPT', 'CANDIDATE'):
            raise ValueError('Accepted entry must declare exact status')
        if x['status'] != 'CANDIDATE' and not x.get('user_source'):
            raise ValueError('Accepted item needs user_source')


def validate_task(task: dict, baseline: dict) -> None:
    if task.get('schema') != TASK_SCHEMA:
        raise ValueError('Invalid task schema')
    if task.get('baseline_commit') != baseline['current_commit']:
        raise ValueError('Task baseline differs from current baseline')
    if task.get('classification') not in ('S1', 'S2', 'S3'):
        raise ValueError('Must classify as S1, S2 or S3')
    if not task.get('feedback') or not task.get('repair_checks'):
        raise ValueError('Need feedback and at least one observable repair check')
    if not isinstance(task.get('allowed_paths'), list) or not task['allowed_paths']:
        raise ValueError('Need explicit allowed_paths')
    known = {x['id'] for x in baseline['accepted'] if x['status'] in ('ACCEPTED', 'PARTIAL_ACCEPT')}
    if set(task.get('keep', [])) - known:
        raise ValueError('KEEP refers to a nonexistent or unaccepted baseline item')
    if task['classification'] == 'S3' and not task.get('explicit_user_redesign_approval'):
        raise ValueError('S3 requires explicit user redesign approval')


def build_check(repo: Path, baseline: dict, task: dict, proof: dict, proof_dir: Path) -> dict:
    issues = []
    try:
        validate_baseline(baseline)
        validate_task(task, baseline)
    except (ValueError, KeyError) as exc:
        issues.append(f'CONTRACT: {exc}')
    target = git(repo, 'rev-parse', 'HEAD')
    before = baseline.get('current_commit', '')
    if git(repo, 'status', '--porcelain'):
        issues.append('DIRTY_WORKTREE: exact candidate evidence requires a clean worktree')
    ancestor = subprocess.run(['git', '-C', str(repo), 'merge-base', '--is-ancestor', before, target], capture_output=True)
    if ancestor.returncode != 0:
        issues.append('BASELINE_NOT_ANCESTOR: candidate does not descend from baseline')
    changed = git(repo, 'diff', '--name-only', f'{before}..{target}').splitlines()
    extra = [p for p in changed if not within_scope(p, task.get('allowed_paths', []))]
    if extra:
        issues.append('OUT_OF_SCOPE_FILES: ' + ', '.join(extra))
    if proof.get('schema') != PROOF_SCHEMA:
        issues.append('INVALID_PROOF_SCHEMA')
    if proof.get('candidate_commit') != target:
        issues.append('STALE_PROOF: candidate_commit does not match actual HEAD')
    if proof.get('surface') != baseline.get('surface'):
        issues.append('WRONG_SURFACE: evidence is not from target runtime')
    observations = {x.get('id'): x for x in proof.get('checks', [])}
    required = list(task.get('keep', [])) + list(task.get('repair_checks', []))
    for cid in required:
        obs = observations.get(cid)
        if not obs or obs.get('result') != 'PASS':
            issues.append('MISSING_OR_FAILED_CHECK: ' + cid)
            continue
        rel = obs.get('evidence', '')
        evidence = (proof_dir / rel).resolve()
        if not rel or not evidence.is_relative_to(proof_dir.resolve()) or not evidence.is_file():
            issues.append('MISSING_EVIDENCE: ' + cid)
            continue
        if not obs.get('sha256'):
            issues.append('MISSING_EVIDENCE_HASH: ' + cid)
        elif sha256(evidence) != obs['sha256']:
            issues.append('EVIDENCE_HASH_MISMATCH: ' + cid)
        if obs.get('candidate_commit') != target:
            issues.append('CHECK_CANDIDATE_MISMATCH: ' + cid)
        kind = obs.get('kind')
        if not kind or kind == 'SELF_REPORT':
            issues.append('INVALID_EVIDENCE_KIND: ' + cid)
    return {
        'schema': CHECK_SCHEMA,
        'status': 'READY_FOR_VISUAL_REVIEW' if not issues else 'REJECTED',
        'baseline_commit': before,
        'candidate_commit': target,
        'classification': task.get('classification'),
        'changed_files': changed,
        'out_of_scope': extra,
        'required_checks': required,
        'issues': issues,
        'note': 'This is mechanical admission only; visual quality requires real review. Not user acceptance.',
    }


def do_check(args: argparse.Namespace) -> int:
    repo = Path(args.repo).resolve()
    report = build_check(repo, load(args.baseline), load(args.task), load(args.proof), Path(args.proof).resolve().parent)
    dump(args.report, report)
    print(report['status'], '|', '; '.join(report['issues']) if report['issues'] else 'Scope and evidence identity verified')
    return 0 if report['status'] == 'READY_FOR_VISUAL_REVIEW' else 2


def do_promote(args: argparse.Namespace) -> int:
    baseline = load(args.baseline)
    check = load(args.report)
    approval = load(args.approval)
    validate_baseline(baseline)
    if check.get('status') != 'READY_FOR_VISUAL_REVIEW' or check.get('schema') != CHECK_SCHEMA:
        raise ValueError('Cannot promote without a successful exact-candidate mechanical check')
    if check.get('baseline_commit') != baseline['current_commit']:
        raise ValueError('Baseline moved since check')
    if not approval.get('explicit_user_approval') or not approval.get('user_source'):
        raise ValueError('No explicit user approval with source')
    if approval.get('candidate_commit') != check['candidate_commit']:
        raise ValueError('Approval is for a different candidate')
    # Only move accepted baseline when user explicitly approved exact candidate.
    baseline['current_commit'] = check['candidate_commit']
    baseline.setdefault('history', []).append({
        'commit': check['candidate_commit'],
        'previous': check['baseline_commit'],
        'approval_source': approval['user_source'],
    })
    dump(args.out, baseline)
    print('PROMOTED_EXPLICITLY_APPROVED_CANDIDATE', check['candidate_commit'])
    return 0


def main() -> int:
    p = argparse.ArgumentParser(description='Guard changes against a verified design baseline')
    sub = p.add_subparsers(dest='command', required=True)
    check = sub.add_parser('check', help='Validate diff scope + exact-candidate evidence')
    for name in ('repo', 'baseline', 'task', 'proof', 'report'):
        check.add_argument('--' + name, required=True)
    promote = sub.add_parser('promote', help='Move baseline only with explicit user approval')
    for name in ('baseline', 'report', 'approval', 'out'):
        promote.add_argument('--' + name, required=True)
    args = p.parse_args()
    try:
        return do_check(args) if args.command == 'check' else do_promote(args)
    except (ValueError, FileNotFoundError, subprocess.CalledProcessError, KeyError) as exc:
        print('ERROR:', exc, file=sys.stderr)
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
