#!/usr/bin/env python3
"""Local clipboard regression helper; no browser/network dependencies."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
from urllib.parse import quote


class RunnerError(Exception):
    pass


def read(path):
    return Path(path).read_text(encoding='utf-8-sig')


def write(path, content):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    # Replace only a fully written temporary file, including on Windows.
    fd, tmp = tempfile.mkstemp(dir=path.parent, prefix='.runner-')
    try:
        with os.fdopen(fd, 'w', encoding='utf-8', newline='') as stream:
            stream.write(content)
        os.replace(tmp, path)
    finally:
        if Path(tmp).exists():
            Path(tmp).unlink()


def dump(path, value):
    write(path, json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def digest(value):
    return hashlib.sha256(value.encode('utf-8')).hexdigest()


def private_markers(value):
    return bool(re.search(r'[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}|/(?:Users|users|home)/[^/\s]+|[A-Za-z]:\\Users\\[^\\\s]+|https?://github\.com/[^/\s]+', value))


def load_case(path):
    raw = read(path)
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        # Read-only compatibility with the original four-field case.yaml files.
        data = {}
        for line in raw.splitlines():
            if not line.strip() or line.lstrip().startswith('#'):
                continue
            key, sep, value = line.partition(':')
            if not sep or key not in ('输入来源路径', '证据文件路径', '期望行为', '判定方式'):
                raise RunnerError('v1 使用 JSON 形式的 YAML；旧格式仅支持原有四个字段')
            try:
                data[key] = json.loads(value.strip())
            except json.JSONDecodeError as exc:
                raise RunnerError('旧字段必须使用 JSON 双引号字符串') from exc
        if not data:
            raise RunnerError('空案例')
        return {'schema_version': 1, 'id': Path(path).parent.name,
                'name': Path(path).parent.name, 'version': '', 'model': '',
                'plugins': None, 'attachments': None, 'turns': [],
                'criteria': [{'id': 'C1', 'text': data.get('期望行为', ''), 'kind': 'requirement'},
                             {'id': 'C2', 'text': data.get('判定方式', ''), 'kind': 'requirement'}],
                'legacy': data}
    if not isinstance(data, dict):
        raise RunnerError('案例必须是对象')
    return data


def validate(case):
    errors, gaps = [], []
    required = ('schema_version', 'id', 'name', 'version', 'model', 'plugins', 'attachments', 'turns', 'criteria')
    errors += ['缺少字段 ' + key for key in required if key not in case]
    if errors:
        return errors, gaps
    if type(case['schema_version']) is not int or case['schema_version'] != 1:
        errors.append('schema_version 必须为 1')
    if not isinstance(case['id'], str) or not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_-]*', case['id']):
        errors.append('id 只能包含字母、数字、下划线和连字符')
    for key in ('name', 'version', 'model'):
        if not isinstance(case[key], str):
            errors.append(key + ' 必须是字符串')
        elif not case[key].strip():
            gaps.append(key)
    for key in ('plugins', 'attachments'):
        if case[key] is None:
            gaps.append(key)
        elif not isinstance(case[key], list) or any(not isinstance(x, str) or not x.strip() for x in case[key]):
            errors.append(key + ' 必须为字符串列表；未知用 null，明确无需用 []')
    if not isinstance(case['turns'], list):
        errors.append('turns 必须是列表')
    else:
        if not case['turns']:
            gaps.append('turns（完整冻结轮序与提示词）')
        for n, turn in enumerate(case['turns'], 1):
            if not isinstance(turn, dict):
                errors.append(f'turn-{n} 必须是对象')
                continue
            if type(turn.get('n')) is not int or turn['n'] != n:
                errors.append(f'turn-{n} 编号必须连续，从 1 开始')
            if not isinstance(turn.get('prompt'), str):
                errors.append(f'turn-{n}.prompt 必须为字符串')
            elif not turn['prompt'].strip():
                gaps.append(f'turn-{n}.prompt')
            conv = turn.get('conversation')
            if not isinstance(conv, dict) or conv.get('mode') not in ('new', 'continue', 'branch'):
                errors.append(f'turn-{n}.conversation.mode 无效')
                continue
            if conv['mode'] == 'continue' and n == 1:
                errors.append('第 1 轮不能续上一轮')
            if conv['mode'] == 'branch':
                k = conv.get('after_turn')
                if type(k) is not int or not 1 <= k < n:
                    errors.append(f'turn-{n} 分支必须引用已经存在的前一轮')
    if not isinstance(case['criteria'], list):
        errors.append('criteria 必须是列表')
    else:
        if not case['criteria']:
            gaps.append('criteria')
        seen = set()
        for criterion in case['criteria']:
            if not isinstance(criterion, dict):
                errors.append('每条判据必须是对象')
                continue
            cid = criterion.get('id')
            if not isinstance(cid, str) or not re.fullmatch(r'C[1-9][0-9]*', cid) or cid in seen:
                errors.append('判据 id 必须为不重复的 C1、C2…')
            seen.add(str(cid))
            if not isinstance(criterion.get('text'), str) or not criterion['text'].strip():
                errors.append('判据 text 不能为空')
            if criterion.get('kind', 'requirement') not in ('requirement', 'failure_condition', 'inconclusive_condition'):
                errors.append('判据 kind 无效')
    if private_markers(json.dumps(case, ensure_ascii=False)):
        errors.append('含疑似邮箱、个人目录或账号链接；不要自动脱敏改写原文')
    return errors, gaps


def load_batch(path):
    path = Path(path).resolve()
    entries = [line.strip() for line in read(path).splitlines() if line.strip()]
    if not entries:
        raise RunnerError('批次为空；每行填写一个相对于批次文件的案例路径')
    loaded = []
    ids = set()
    for entry in entries:
        p = (path.parent / entry).resolve()
        c = load_case(p)
        errors, gaps = validate(c)
        if errors:
            raise RunnerError(f'{Path(entry).name}: ' + '；'.join(errors))
        if c['id'] in ids:
            raise RunnerError('批次案例 id 重复：' + c['id'])
        ids.add(c['id'])
        loaded.append({'source': entry, 'source_sha256': digest(read(p)), 'case': c, 'gaps': gaps})
    return loaded


def clipboard(action, value=None, mock=None):
    if mock:
        if action == 'write':
            write(mock, value)
            return None
        return read(mock) if Path(mock).exists() else ''
    if sys.platform == 'darwin':
        cmd = ['pbcopy'] if action == 'write' else ['pbpaste']
        result = subprocess.run(cmd, input=value.encode('utf-8') if action == 'write' else None,
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return result.stdout.decode('utf-8') if action == 'read' else None
    if sys.platform == 'win32':
        # Force UTF-8 on both pipe ends; do not interpolate prompt/reply as code.
        ps = '[Console]::InputEncoding = [Text.UTF8Encoding]::new($false); [Console]::OutputEncoding = [Text.UTF8Encoding]::new($false); '
        ps += ('Set-Clipboard -Value ([Console]::In.ReadToEnd())' if action == 'write'
               else '$v = Get-Clipboard -Raw; if ($null -ne $v) { [Console]::Out.Write($v) }')
        result = subprocess.run(['powershell.exe', '-NoProfile', '-NonInteractive', '-Command', ps],
                                input=value.encode('utf-8') if action == 'write' else None,
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return result.stdout.decode('utf-8') if action == 'read' else None
    raise RunnerError('真实剪贴板仅支持本机 Mac / Windows；Linux 只能显式使用 --mock-clipboard')


class Run:
    def __init__(self, batch, root):
        self.entries = load_batch(batch)
        bid = Path(batch).stem
        if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_-]*', bid):
            raise RunnerError('批次文件名只能包含字母、数字、下划线和连字符')
        self.root = Path(root) / bid
        identity = {'batch': bid, 'entries': self.entries}
        snapshot = self.root / 'batch.json'
        if snapshot.exists():
            if json.loads(read(snapshot)) != identity:
                raise RunnerError('批次或案例已变化；保留旧运行并使用新的批次文件名')
        else:
            dump(snapshot, identity)
        for entry in self.entries:
            d = self.directory(entry)
            for turn in entry['case']['turns']:
                p = d / f"turn-{turn['n']}-prompt.md"
                r = d / f"turn-{turn['n']}-reply.md"
                if p.exists() and read(p) != turn['prompt']:
                    raise RunnerError('已归档提示词与冻结案例不一致')
                if r.exists() and (not p.exists() or not read(r).strip() or read(r).strip() == turn['prompt'].strip()):
                    raise RunnerError('已有回答为空、仍是提示词或缺少对应提示词')
            manifest = d / 'judgement-inputs.json'
            if manifest.exists():
                for name, sha in json.loads(read(manifest)).items():
                    if not (d / name).exists() or digest(read(d / name)) != sha:
                        raise RunnerError('判定引用的对话已改变，不能沿用旧结果')
        self.summary()

    def directory(self, entry):
        return self.root / entry['case']['id']

    def next(self):
        for i, e in enumerate(self.entries, 1):
            d = self.directory(e)
            if e['gaps'] or (d / 'skipped.json').exists() or (d / 'judgement.json').exists():
                continue
            for turn in e['case']['turns']:
                if not (d / f"turn-{turn['n']}-reply.md").exists():
                    return i, e, turn
            return i, e, None
        return None

    def prepare(self, mock=None, recopy=False):
        item = self.next()
        if not item:
            return {'action': 'done', 'message': '批次已处理；有缺口或跳过的案例仍为未完成'}
        i, e, turn = item
        if turn is None:
            return {'action': 'judge', 'case': e['case']['id'], 'directory': str(self.directory(e))}
        c = e['case']
        prompt = self.directory(e) / f"turn-{turn['n']}-prompt.md"
        exists = prompt.exists()
        if exists and read(prompt) != turn['prompt']:
            raise RunnerError('已归档提示词与冻结案例不一致')
        if not exists or recopy:
            clipboard('write', turn['prompt'], mock)
            write(prompt, turn['prompt'])
        conv = turn['conversation']
        mode = {'new': '新对话', 'continue': '接着上一轮', 'branch': f"从第 {conv.get('after_turn')} 轮回答后创建分支"}[conv['mode']]
        return {'action': 'ask', 'case': c['id'], 'turn': turn['n'],
                'clipboard_written': not exists or recopy,
                'message': f"案例 {i}/{len(self.entries)}：{c['name']}；第 {turn['n']}/{len(c['turns'])} 轮；{mode}。模型：{c['model']}；插件：{', '.join(c['plugins']) or '无需'}；附件：{', '.join(c['attachments']) or '无需'}。" +
                ('提示词已在剪贴板。' if not exists or recopy else '这是待完成轮次，未改动剪贴板；需要提示词时先重新复制。') +
                '请粘贴发送，等完整回答后点击“复制”，再答 好了 / 跳过（余下本案例）/ 停。',
                'checkpoint': turn.get('checkpoint', '')}

    def capture(self, answer, mock=None):
        if answer == '停':
            self.summary()
            return {'action': 'stopped', 'message': '已保留断点；下次用同一批次继续'}
        item = self.next()
        if not item or item[2] is None:
            raise RunnerError('当前没有待复制回答的轮次')
        _, e, turn = item
        d = self.directory(e)
        if answer == '跳过':
            dump(d / 'skipped.json', {'from_turn': turn['n'], 'reason': '用户跳过余下本案例'})
            self.summary()
            return {'action': 'skipped'}
        if answer != '好了':
            raise RunnerError('只接受 好了 / 跳过 / 停；没有用户明确答复不得读取剪贴板')
        if not (d / f"turn-{turn['n']}-prompt.md").exists():
            raise RunnerError('请先准备本轮提示词')
        reply = clipboard('read', mock=mock)
        normalize = lambda s: s.replace('\r\n', '\n').replace('\r', '\n').strip()
        if not normalize(reply) or normalize(reply) == normalize(turn['prompt']):
            # At most one immediate reminder. Never store empty/prompt content.
            attempt = d / f"turn-{turn['n']}-capture-retry.json"
            repeated = attempt.exists()
            dump(attempt, {'invalid_clipboard': True})
            return {'action': 'stopped' if repeated else 'retry',
                    'message': '剪贴板为空或仍是提示词，未保存。' + ('已提醒过一次，停在当前断点。' if repeated else '请复制完整回答，再答 好了 / 跳过 / 停。')}
        if private_markers(reply):
            raise RunnerError('回答含疑似个人信息，未落盘；停在本轮，不自动改写')
        write(d / f"turn-{turn['n']}-reply.md", reply)
        retry = d / f"turn-{turn['n']}-capture-retry.json"
        if retry.exists():
            retry.unlink()
        self.summary()
        return {'action': 'saved', 'case': e['case']['id'], 'turn': turn['n'], 'checkpoint': turn.get('checkpoint', '')}

    def judge(self, cid, source):
        entry = next((e for e in self.entries if e['case']['id'] == cid), None)
        if entry is None or entry['gaps']:
            raise RunnerError('案例不存在或仍有缺口')
        d, c = self.directory(entry), entry['case']
        if (d / 'judgement.json').exists() or (d / 'skipped.json').exists():
            raise RunnerError('已判定或跳过；不覆盖旧结果')
        if any(not (d / f"turn-{t['n']}-reply.md").exists() for t in c['turns']):
            raise RunnerError('轮次未完成，不能判定')
        rows = json.loads(read(source))
        if not isinstance(rows, list) or [r.get('criterion') for r in rows if isinstance(r, dict)] != [x['id'] for x in c['criteria']]:
            raise RunnerError('判定必须按顺序覆盖全部判据，一条一次')
        lines = [f"# {c['id']} 判定", '', '仅依据归档对话与冻结判据；引句定位不等于语义判定已获独立复核。', '']
        for criterion, row in zip(c['criteria'], rows):
            status = row.get('status')
            if status not in ('通过', '失败', '无法判定') or not isinstance(row.get('reason'), str) or not row['reason'].strip():
                raise RunnerError('每条必须填写 通过 / 失败 / 无法判定 和 reason')
            evidence = row.get('evidence', [])
            if not isinstance(evidence, list) or (status != '无法判定' and not evidence):
                raise RunnerError('通过或失败必须有回答原文引句；无法判定仍须说明缺什么')
            lines += [f"## {criterion['id']}：{status}", '', criterion['text'], '', row['reason'], '']
            for ev in evidence:
                n, q = ev.get('turn'), ev.get('quote')
                if type(n) is not int or not 1 <= n <= len(c['turns']) or not isinstance(q, str) or not q.strip():
                    raise RunnerError('引句需要有效 turn 和非空 quote')
                reply = d / f'turn-{n}-reply.md'
                if q not in read(reply):
                    raise RunnerError('依据句不在指定轮次回答原文中')
                lines += [f'[第 {n} 轮回答](turn-{n}-reply.md)', '', *['> ' + line for line in q.splitlines()], '']
        if private_markers(json.dumps(rows, ensure_ascii=False)):
            raise RunnerError('判定含疑似个人信息，未保存')
        write(d / 'judgement.md', '\n'.join(lines))
        dump(d / 'judgement-inputs.json', {
            p.name: digest(read(p)) for p in d.glob('turn-*-*.md')})
        dump(d / 'judgement.json', rows)
        self.summary()
        return {'action': 'judged', 'case': cid}

    def summary(self):
        lines = ['# 批次结果', '', '| 案例 | 版本 | 通过与否 | 失败的标准 | 依据文件链接 |', '| --- | --- | --- | --- | --- |']
        cell = lambda s: str(s).replace('|', '\\|').replace('\n', ' ')
        for e in self.entries:
            c, d = e['case'], self.directory(e)
            rows = json.loads(read(d / 'judgement.json')) if (d / 'judgement.json').exists() else None
            if e['gaps']:
                status = '未就绪：' + '、'.join(e['gaps'])
            elif (d / 'skipped.json').exists():
                status = '已跳过（未完成）'
            elif rows:
                status = '失败' if any(r['status'] == '失败' for r in rows) else ('无法判定' if any(r['status'] == '无法判定' for r in rows) else '通过')
            else:
                status = '待判定' if all((d / f"turn-{t['n']}-reply.md").exists() for t in c['turns']) else '未完成'
            failed = '、'.join(r['criterion'] for r in rows or [] if r['status'] == '失败') or '—'
            links = [f'[冻结案例](batch.json)']
            if rows:
                links.append(f'[判定]({quote(c["id"])}/judgement.md)')
            for t in c['turns']:
                if (d / f"turn-{t['n']}-reply.md").exists():
                    links.append(f'[第{t["n"]}轮]({quote(c["id"])}/turn-{t["n"]}-reply.md)')
            lines.append('| ' + ' | '.join(map(cell, [c['id'], c['version'] or '未提供', status, failed, ' '.join(links)])) + ' |')
        write(self.root / 'RESULTS.md', '\n'.join(lines) + '\n')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['inspect', 'next', 'capture', 'judge', 'results', 'simulate'])
    parser.add_argument('batch')
    parser.add_argument('--runs-dir', default='runs')
    parser.add_argument('--mock-clipboard')
    parser.add_argument('--copy-pending', action='store_true')
    parser.add_argument('--answer')
    parser.add_argument('--case')
    parser.add_argument('--input')
    args = parser.parse_args()
    try:
        if args.command == 'inspect':
            entries = load_batch(args.batch)
            result = {'cases': [{'id': e['case']['id'], 'turns': len(e['case']['turns']), 'gaps': e['gaps']} for e in entries],
                      'total_turns': sum(len(e['case']['turns']) for e in entries)}
        else:
            run = Run(args.batch, args.runs_dir)
            if args.command == 'next':
                result = run.prepare(args.mock_clipboard, args.copy_pending)
            elif args.command == 'capture':
                result = run.capture(args.answer, args.mock_clipboard)
            elif args.command == 'judge':
                if not args.case or not args.input:
                    raise RunnerError('judge 需要 --case 和 --input')
                result = run.judge(args.case, args.input)
            elif args.command == 'simulate':
                if not args.mock_clipboard:
                    raise RunnerError('simulate 必须显式使用 --mock-clipboard')
                while True:
                    result = run.prepare(args.mock_clipboard)
                    print(json.dumps(result, ensure_ascii=False), flush=True)
                    if result['action'] != 'ask':
                        return 0
                    answer = input('标准输入代替弹窗：')
                    if answer == '好了':
                        value = input('模拟用户点击复制后的回答（单行）：')
                        clipboard('write', value, args.mock_clipboard)
                    result = run.capture(answer, args.mock_clipboard)
                    print(json.dumps(result, ensure_ascii=False), flush=True)
                    if result['action'] in ('stopped', 'retry'):
                        return 0
            else:
                result = {'action': 'results', 'file': str(run.root / 'RESULTS.md')}
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (RunnerError, OSError, ValueError, subprocess.SubprocessError) as exc:
        # Avoid dumping OS exception paths or command payloads into durable logs.
        print('错误：' + (str(exc) if isinstance(exc, RunnerError) else type(exc).__name__), file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())
