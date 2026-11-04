import json
import subprocess
import tempfile
import unittest
from pathlib import Path
from design_guard import build_check, do_promote, load, sha256
from argparse import Namespace


def run(*args):
    return subprocess.check_output(args, text=True).strip()


class GuardTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.repo = self.root / 'repo'
        self.repo.mkdir()
        run('git', '-C', str(self.repo), 'init', '-q')
        run('git', '-C', str(self.repo), 'config', 'user.email', 'test@example.org')
        run('git', '-C', str(self.repo), 'config', 'user.name', 'Test')
        (self.repo / 'ui').mkdir()
        (self.repo / 'ui' / 'graph.css').write_text('body { font-size: 12px; }\n')
        (self.repo / 'ui' / 'implementation.ts').write_text('const bindings = 2;\n')
        run('git', '-C', str(self.repo), 'add', '.')
        run('git', '-C', str(self.repo), 'commit', '-qm', 'base')
        self.base = run('git', '-C', str(self.repo), 'rev-parse', 'HEAD')
        (self.repo / 'ui' / 'graph.css').write_text('body { font-size: 16px; }\n')
        run('git', '-C', str(self.repo), 'add', '.')
        run('git', '-C', str(self.repo), 'commit', '-qm', 'fix font')
        self.head = run('git', '-C', str(self.repo), 'rev-parse', 'HEAD')
        self.baseline = {
            'schema': 'fd-baseline-v1', 'current_commit': self.base, 'surface': 'browser',
            'accepted': [{'id':'binding-switch','status':'PARTIAL_ACCEPT','user_source':'PDF p.196'}]
        }
        self.task = {
            'schema':'fd-change-v1','baseline_commit':self.base,'classification':'S1',
            'feedback':'图中文字太小，但实现台保留','allowed_paths':['ui/graph.css'],
            'keep':['binding-switch'],'repair_checks':['font-visible']
        }
        self.proof_dir = self.root / 'proof'
        self.proof_dir.mkdir()
        (self.proof_dir / 'screen.png').write_bytes(b'\x89PNG\r\n\x1a\n' + b'test')
        (self.proof_dir / 'binding.mp4').write_bytes(b'test video')
        self.proof = {'schema':'fd-proof-v1','candidate_commit':self.head,'surface':'browser',
            'checks':[
                {'id':'binding-switch','result':'PASS','candidate_commit':self.head,'evidence':'binding.mp4','kind':'REAL_INTERACTION','sha256':sha256(self.proof_dir/'binding.mp4')},
                {'id':'font-visible','result':'PASS','candidate_commit':self.head,'evidence':'screen.png','kind':'SCREENSHOT','sha256':sha256(self.proof_dir/'screen.png')},
            ]}

    def check(self):
        return build_check(self.repo, self.baseline, self.task, self.proof, self.proof_dir)

    def test_valid_repair_ready_not_user_pass(self):
        r = self.check()
        self.assertEqual(r['status'], 'READY_FOR_VISUAL_REVIEW')
        self.assertIn('Not user acceptance', r['note'])

    def test_reject_extra_changed_file(self):
        (self.repo / 'ui' / 'implementation.ts').write_text('const bindings = 0;\n')
        run('git', '-C', str(self.repo), 'add', '.')
        run('git', '-C', str(self.repo), 'commit', '-qm', 'bad regression')
        self.proof['candidate_commit'] = run('git', '-C', str(self.repo), 'rev-parse', 'HEAD')
        r = self.check()
        self.assertEqual(r['status'], 'REJECTED')
        self.assertIn('ui/implementation.ts', r['out_of_scope'])

    def test_reject_old_screenshot(self):
        self.proof['candidate_commit'] = self.base
        self.assertIn('STALE_PROOF', str(self.check()['issues']))

    def test_reject_unchanged_keep_not_checked(self):
        self.proof['checks'] = self.proof['checks'][1:]
        self.assertIn('binding-switch', str(self.check()['issues']))

    def test_reject_s3_without_user(self):
        self.task['classification']='S3'
        self.assertIn('S3 requires explicit', str(self.check()['issues']))

    def test_reject_dirty_worktree(self):
        (self.repo/'ui'/'graph.css').write_text('uncommitted')
        self.assertIn('DIRTY_WORKTREE', str(self.check()['issues']))

    def test_reject_missing_evidence_hash(self):
        del self.proof['checks'][0]['sha256']
        self.assertIn('MISSING_EVIDENCE_HASH', str(self.check()['issues']))

    def test_reject_wrong_surface(self):
        self.proof['surface']='static-mock'
        self.assertIn('WRONG_SURFACE', str(self.check()['issues']))

    def test_reject_tampered_evidence(self):
        (self.proof_dir/'screen.png').write_bytes(b'changed')
        self.assertIn('EVIDENCE_HASH_MISMATCH', str(self.check()['issues']))

    def test_promote_requires_explicit_approval_and_preserves_keep(self):
        baseline_path=self.root/'baseline.json'
        report_path=self.root/'report.json'
        approval_path=self.root/'approval.json'
        out_path=self.root/'new-baseline.json'
        baseline_path.write_text(json.dumps(self.baseline))
        report_path.write_text(json.dumps(self.check()))
        approval_path.write_text(json.dumps({'explicit_user_approval':False, 'candidate_commit':self.head,'user_source':'user reply'}))
        with self.assertRaises(ValueError):
            do_promote(Namespace(baseline=baseline_path,report=report_path,approval=approval_path,out=out_path))
        approval_path.write_text(json.dumps({'explicit_user_approval':True, 'candidate_commit':self.head,'user_source':'user reply'}))
        do_promote(Namespace(baseline=baseline_path,report=report_path,approval=approval_path,out=out_path))
        promoted=load(out_path)
        self.assertEqual(promoted['current_commit'],self.head)
        self.assertEqual(promoted['accepted'],self.baseline['accepted'])


if __name__=='__main__':
    unittest.main()
