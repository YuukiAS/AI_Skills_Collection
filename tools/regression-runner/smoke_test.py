#!/usr/bin/env python3
"""One reproducible cluster-only exercise. Every answer and judgement is synthetic."""
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
from runner import Run, RunnerError, clipboard, dump, read, validate

HERE = Path('tools/regression-runner')
EXAMPLES = HERE / 'examples'
OUTPUT = HERE / 'runs'
LOG = Path('docs/design/regression-runner/SMOKE_RUN.md')


def make_case(cid, turns, text='回答包含所问数字。'):
    return {'schema_version': 1, 'id': cid, 'name': cid, 'version': 'synthetic-v1',
            'model': '模拟模型', 'plugins': [], 'attachments': [], 'turns': turns,
            'criteria': [{'id': 'C1', 'text': text, 'kind': 'requirement'}]}


def turn(n, prompt, mode, after=None):
    conv = {'mode': mode}
    if after is not None:
        conv['after_turn'] = after
    return {'n': n, 'prompt': prompt, 'conversation': conv}


def main():
    lines = ['# 集群模拟运行记录', '',
             '本轮仅用假数据；剪贴板是文本文件，提问弹窗用标准输入代替。没有访问或控制浏览器，没有调用外部模型。判定输入也是固定假数据，只验证判定落盘与引句检查。', '',
             '复现：`python3 tools/regression-runner/smoke_test.py`。仅替换该测试自己的 `tools/regression-runner/runs/synthetic-smoke/`，不碰真实运行目录。', '']
    passed = []
    def check(condition, label):
        assert condition, label
        passed.append(label)
    cases = [make_case('SYN-BRANCH', [turn(1, '请回复数字一。\n这是模拟题面第二行。', 'new'), turn(2, '再回复数字二。', 'continue'), turn(3, '换个问法，回复数字三。', 'branch', 1)]),
             make_case('SYN-FAIL', [turn(1, '请回复数字四。', 'new')]),
             make_case('SYN-UNKNOWN', [turn(1, '请比较图中的两个数字。', 'new')], '回答准确比较图片中的两个数字。'),
             make_case('SYN-SKIP', [turn(1, '请回复数字五。', 'new')])]
    slugs = ['synthetic-branch', 'synthetic-fail', 'synthetic-unknown', 'synthetic-skip']
    for slug, c in zip(slugs, cases):
        dump(EXAMPLES / slug / 'case.yaml', c)
    batch = EXAMPLES / 'synthetic-smoke.batch'
    batch.write_text('\n'.join(slug + '/case.yaml' for slug in slugs) + '\n', encoding='utf-8')
    output = OUTPUT / batch.stem
    if output.exists():
        shutil.rmtree(output)  # Fixed synthetic output only.
    with tempfile.TemporaryDirectory(prefix='regression-runner-smoke-') as tmp:
        mock = Path(tmp) / 'clipboard.txt'
        run = Run(batch, OUTPUT)
        first = run.prepare(mock)
        prompt = run.root / 'SYN-BRANCH/turn-1-prompt.md'
        check(read(mock) == cases[0]['turns'][0]['prompt'] == read(prompt), '多行提示词逐字进入模拟剪贴板和 prompt 文件')
        invalid = run.capture('好了', mock)
        check(invalid['action'] == 'retry' and not (prompt.parent / 'turn-1-reply.md').exists(), '原样提示词被拒绝且只提醒一次')
        clipboard('write', '', mock)
        check(run.capture('好了', mock)['action'] == 'stopped', '再次空剪贴板被拒绝并保留断点')
        clipboard('write', '数字一。\n中文与换行保留。', mock)
        check(not Run(batch, OUTPUT).prepare(mock)['clipboard_written'] and read(mock).startswith('数字一'), '续跑待完成轮次不会覆盖用户已复制的回答')
        run.capture('好了', mock)
        h = hashlib.sha256((prompt.parent / 'turn-1-reply.md').read_bytes()).hexdigest()
        # CLI simulate invokes input(), not any Codex or browser tools.
        def simulate(stdin):
            p = subprocess.run([sys.executable, str(HERE / 'runner.py'), 'simulate', str(batch), '--runs-dir', str(OUTPUT), '--mock-clipboard', str(mock)],
                               input=stdin, text=True, encoding='utf-8', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            assert p.returncode == 0, p.stderr
            lines.extend(['```text', p.stdout.rstrip(), '```', ''])
            return p.stdout
        stopped = simulate('停\n')
        check('stopped' in stopped and not (prompt.parent / 'turn-2-reply.md').exists(), '标准输入“停”后不保存后续回答')
        resumed = simulate('好了\n数字二。\n好了\n数字三。\n')
        check('从第 1 轮回答后创建分支' in resumed and 'judge' in resumed, '标准输入续跑完成第 2、3 轮，并显示正确分支位置')
        check(h == hashlib.sha256((prompt.parent / 'turn-1-reply.md').read_bytes()).hexdigest(), '已完成的第 1 轮回答保持原 hash')
        run = Run(batch, OUTPUT)
        bad = Path(tmp) / 'bad-judge.json'
        dump(bad, [{'criterion':'C1','status':'通过','reason':'假依据测试','evidence':[{'turn':3,'quote':'不存在的原文'}]}])
        try:
            run.judge('SYN-BRANCH', bad)
        except RunnerError:
            check(not (prompt.parent / 'judgement.md').exists(), '伪造依据句被拒绝，未产生判定文件')
        else:
            raise AssertionError('fabricated quote accepted')
        assess = Path(tmp) / 'assessment.json'
        dump(assess, [{'criterion':'C1','status':'通过','reason':'假回答给出数字。','evidence':[{'turn':3,'quote':'数字三。'}]}])
        run.judge('SYN-BRANCH', assess)
        simulate('好了\n没有所问内容。\n')
        dump(assess, [{'criterion':'C1','status':'失败','reason':'假回答未给出所问数字。','evidence':[{'turn':1,'quote':'没有所问内容。'}]}])
        Run(batch, OUTPUT).judge('SYN-FAIL', assess)
        simulate('好了\n没有收到图片，无法比较。\n')
        dump(assess, [{'criterion':'C1','status':'无法判定','reason':'归档文本缺少可核对的图片。','evidence':[{'turn':1,'quote':'没有收到图片，无法比较。'}]}])
        Run(batch, OUTPUT).judge('SYN-UNKNOWN', assess)
        simulate('跳过\n')
        final = Run(batch, OUTPUT)
        check(final.prepare(mock)['action'] == 'done', '跳过余下本案例后结束批次')
        results = read(final.root / 'RESULTS.md')
        check(all(x in results for x in ('通过', '失败', '无法判定', '跳过')), '结果表分别保留通过、失败、无法判定、跳过')
        check(len(list(final.root.glob('*/turn-*-reply.md'))) == 5, '总计划 6 轮，实际保存 5 轮，跳过 1 轮')
        invalid_case = make_case('BAD', [turn(1,'x','branch',1)])
        check(bool(validate(invalid_case)[0]), '格式检查拒绝不存在或未来的分支轮次')
        del invalid_case['model']
        check(bool(validate(invalid_case)[0]), '格式检查拒绝缺少必填字段')
        source = EXAMPLES / slugs[0] / 'case.yaml'
        original = source.read_bytes()
        try:
            changed = dict(cases[0], version='changed')
            dump(source, changed)
            try:
                Run(batch, OUTPUT)
            except RunnerError:
                check(True, '冻结后输入变化拒绝混用旧运行')
            else:
                raise AssertionError('changed batch accepted')
        finally:
            source.write_bytes(original)
        # Additional checks use disposable runs so the evidence batch is intact.
        with tempfile.TemporaryDirectory(prefix='regression-runner-check-') as extra:
            r = Run(batch, extra)
            r.prepare(mock)
            clipboard('write', '模拟回答。', mock)
            r.capture('好了', mock)
            target = r.root / 'SYN-BRANCH/turn-1-prompt.md'
            target.write_text('改动', encoding='utf-8')
            try:
                Run(batch, extra)
            except RunnerError:
                check(True, '归档提示词漂移被拒绝')
            else:
                raise AssertionError('changed prompt accepted')
        for source_path in Path('docs/design/plugin-reset-2026-11/regressions').glob('*/case.yaml'):
            if source_path.parent.name in ('edge-revision','obsidian-existing-capability','keychron-object-evidence'):
                c = __import__('runner').load_case(source_path)
                check(not validate(c)[0] and bool(validate(c)[1]), '旧格式兼容导入但不会伪装成就绪：' + source_path.parent.name)
    lines += ['已通过 '+str(len(passed))+' 项检查：', ''] + ['- '+x for x in passed]
    lines += ['', '假批次结果：[RESULTS.md](../../../tools/regression-runner/runs/synthetic-smoke/RESULTS.md)。', '',
              '运行边界：Mac `pbcopy/pbpaste`、Windows PowerShell 系统剪贴板和 Codex 桌面提问弹窗均未在本机实测；真实迁移案例因缺口未执行。']
    LOG.write_text('\n'.join(lines)+'\n', encoding='utf-8')
    print(f'synthetic smoke: {len(passed)} checks passed; 4 cases; 5 saved replies; 3 judgements; 1 skipped case')


if __name__ == '__main__':
    main()
