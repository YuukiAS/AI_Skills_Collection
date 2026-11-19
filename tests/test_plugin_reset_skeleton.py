from __future__ import annotations

import json
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import build_codex_marketplace as build
import build_gpt_plugins as gpt
from skill_utils import read_frontmatter

LEGACY = ['writing-fidelity', 'response-clarity', 'scientific-prose',
          'product-ui-copy', 'scientific-rewrite', 'chinese-prose']


class PluginResetSkeletonTests(unittest.TestCase):
    def test_gpt_packages_are_reproducible_and_keep_reasoned_decision_out_of_codex(self):
        with tempfile.TemporaryDirectory() as tmp:
            gpt.generate(Path(tmp))
            self.assertEqual(gpt.files(Path(tmp)), gpt.files(ROOT))
        codex = build.load_marketplace_config()
        self.assertNotIn('reasoned-decision', build.plugin_names(codex))
        manifests = {p['name']: p for p in gpt.config()['plugins']}
        self.assertEqual(set(manifests), {'reasoned-decision', 'content-selection', 'writing-style', 'research-writing'})
        for name in ['reasoned-decision', 'content-selection']:
            manifest = json.loads((ROOT / gpt.OUTPUT / name / '.codex-plugin/plugin.json').read_text())
            self.assertEqual(manifest['version'], '0.1')
            self.assertEqual(manifest['author'], build.AUTHOR)
            self.assertEqual(manifest['skills'], './skills/')

    def test_common_entry_and_evidence_have_one_source_and_accessible_copies(self):
        for source, dest in gpt.source_mirrors():
            self.assertEqual(source.read_bytes(), dest.read_bytes())
        for skill in (ROOT / gpt.OUTPUT).glob('*/skills/*/SKILL.md'):
            _, body = read_frontmatter(skill)
            for target in re.findall(r'\]\(([^)]+)\)', body):
                self.assertTrue((skill.parent / target).is_file(), (skill, target))

    def test_six_legacy_entries_resolve_in_source_and_generated_payload(self):
        config = build.load_marketplace_config()
        writing = next(p for p in config['plugins'] if p['name'] == 'writing-style')
        self.assertEqual([p['artifact_id'] for p in writing['skills']], ['clear-writing'])
        self.assertEqual(len(build.compatibility_skill_entries(writing)), 6)
        for entry in writing['compatibility_skills']:
            for base in [ROOT / entry['source'], ROOT / 'plugins/codex/plugins/writing-style/skills' / entry['artifact_id']]:
                meta, body = read_frontmatter(base / 'SKILL.md')
                target = (base / meta['redirect_to']).resolve()
                self.assertTrue(target.is_file())
                self.assertEqual(read_frontmatter(target)[0]['name'], 'clear-writing')
                self.assertIn(meta['redirect_to'], body)
                self.assertTrue((base / 'history/legacy-skill.md').is_file())

    def test_completed_skill_sources_have_no_placeholders(self):
        for plugin in gpt.config()['plugins']:
            for entry in plugin['skills']:
                text = (ROOT / entry['source'] / 'SKILL.md').read_text()
                self.assertNotIn('GPT-WRITES', text, entry['source'])

    def test_content_selection_schema_fields_match_appendix_c(self):
        design = (ROOT / 'docs/design/plugin-reset-2026-11/designs/CONTENT_SELECTION_AND_CLEAR_WRITING_DESIGN_V0_1.md').read_text()
        for filename, start, end in [('content-plan', '### C.1', '### C.2'), ('artifact-review', '### C.2', '## 附录 D')]:
            section = design.split(start, 1)[1].split(end, 1)[0]
            fields = []
            for line in section.splitlines():
                if line.startswith('| `'):
                    fields += re.findall(r'`([^`]+)`', line.split('|')[1])
            schema = json.loads((ROOT / f'skills/writing/core/content-selection/schemas/{filename}.schema.json').read_text())
            self.assertEqual(set(schema['properties']), set(fields))
            self.assertTrue(all(value == {} for value in schema['properties'].values()))

    def test_seven_cases_keep_private_locators_out_of_public_yaml(self):
        cases = ROOT / 'docs/design/plugin-reset-2026-11/regressions'
        self.assertEqual({p.name for p in cases.iterdir()}, {'edge-revision', 'obsidian-existing-capability', 'keychron-object-evidence', 'deck-v7-content', 'reexplain-after-confusion', 'longform-fidelity', 'ui-copy', 'notes-formula-explanation', 'supervisor-story', 'student-brief', 'accepted-material-minor-edit'})
        for path in cases.glob('*/case.yaml'):
            text = path.read_text()
            self.assertNotIn('/users/', text)
            self.assertNotIn('/overflow/', text)
            for field in ['输入来源路径', '证据文件路径', '期望行为', '判定方式']:
                self.assertIn(field + ':', text)
            for field in ['输入来源路径', '证据文件路径']:
                value = json.loads(re.search(r'^' + field + r': (.*)$', text, re.M).group(1))
                if value != '私有，见本地映射':
                    self.assertTrue((ROOT / value.split('#', 1)[0]).is_file())
        deck = (cases / 'deck-v7-content/case.yaml').read_text()
        self.assertIn('shared/presentations-validator/', deck)
        self.assertIn('validator/presentations-generic-20261119', deck)

    def test_profiles_use_the_unified_entry(self):
        old_paths = {f'skills/writing/core/{name}' for name in LEGACY}
        for path in (ROOT / 'profiles').glob('*.json'):
            data = json.loads(path.read_text())
            self.assertFalse(old_paths & set(data.get('skills', []) + data.get('secondary_skills', [])), path)
        self.assertIn('skills/writing/core/clear-writing', json.loads((ROOT / 'profiles/global-baseline.json').read_text())['skills'])

    def test_legacy_and_new_helper_cli_and_import_paths_work(self):
        paths = [ROOT / 'skills/writing/core' / name / 'scripts/rewrite_support.py' for name in ['scientific-rewrite', 'clear-writing']]
        paths += [ROOT / 'plugins/codex/plugins/writing-style/skills' / name / 'scripts/rewrite_support.py' for name in ['scientific-rewrite', 'clear-writing']]
        outputs = [subprocess.check_output([sys.executable, str(p), '--help'], text=True) for p in paths]
        self.assertTrue(all(output == outputs[0] for output in outputs))
        self.assertEqual(paths[1].read_bytes(), paths[3].read_bytes())


if __name__ == '__main__':
    unittest.main()
