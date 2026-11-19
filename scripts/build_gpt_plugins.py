#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import shutil
import tempfile
from pathlib import Path

import build_codex_marketplace as build

CONFIG_PATH = build.ROOT / 'scripts/gpt_plugin_config.json'
OUTPUT = Path('plugins/gpt/plugins')


def config():
    return json.loads(CONFIG_PATH.read_text(encoding='utf-8'))


def source_mirrors():
    for plugin in config()['plugins']:
        entries = {entry['artifact_id']: entry['source'] for entry in plugin['skills']}
        for item in build.config_copy_items(plugin.get('shared'), plugin['name']):
            parts = Path(item['target']).parts
            if len(parts) < 3 or parts[0] != 'skills' or parts[1] not in entries:
                raise build.BuildError(f"invalid GPT skill reference target: {item['target']}")
            yield build.ROOT / item['source'], build.ROOT / entries[parts[1]] / Path(*parts[2:])


def generate(target_root: Path):
    for plugin in config()['plugins']:
        dest = target_root / OUTPUT / plugin['name']
        if dest.exists():
            shutil.rmtree(dest)
        skills = dest / 'skills'
        skills.mkdir(parents=True)
        for entry in plugin['skills']:
            build.generate_copy_skill(entry, skills, plugin['name'])
        manifest = build.build_plugin_json(plugin)
        # Reuse manifest fields and author without a Codex distribution claim.
        manifest['interface']['longDescription'] = plugin['description']
        path = dest / '.codex-plugin/plugin.json'
        path.parent.mkdir()
        path.write_text(build.json_dump(manifest), encoding='utf-8')


def files(root):
    return {str(p.relative_to(root)): p.read_bytes() for p in (root / OUTPUT).rglob('*') if p.is_file()}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--write', action='store_true')
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    if args.write:
        for source, dest in source_mirrors():
            dest.parent.mkdir(parents=True, exist_ok=True)
            if not dest.exists() or dest.read_bytes() != source.read_bytes():
                shutil.copy2(source, dest)
        generate(build.ROOT)
    errors = [str(dest.relative_to(build.ROOT)) for source, dest in source_mirrors()
              if not dest.exists() or source.read_bytes() != dest.read_bytes()]
    if args.check or not args.write:
        with tempfile.TemporaryDirectory(prefix='gpt-plugins-') as tmp:
            generate(Path(tmp))
            expected, actual = files(Path(tmp)), files(build.ROOT)
            errors += sorted(k for k in expected.keys() | actual.keys() if expected.get(k) != actual.get(k))
    print(json.dumps({'plugins': len(config()['plugins']), 'errors': errors}, ensure_ascii=False))
    return bool(errors)


if __name__ == '__main__':
    raise SystemExit(main())
