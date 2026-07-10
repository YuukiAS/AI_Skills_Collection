from __future__ import annotations

import json
import sys
import tempfile
import unittest
from contextlib import contextmanager
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import build_codex_marketplace as build  # noqa: E402
import skill_utils  # noqa: E402


def write_skill(
    root: Path,
    rel: str,
    name: str,
    *,
    requires_network: bool = False,
    writes_files: bool = True,
    executes_code: bool = False,
    trusted: bool = False,
    secrets: list[str] | None = None,
    scope: str = "project",
    body: str = "Body.\n",
) -> Path:
    skill_dir = root / rel
    skill_dir.mkdir(parents=True, exist_ok=True)
    lines = [
        "---",
        f"name: {name}",
        f"description: Test skill {name}.",
        "status: active",
        "provenance: user-authored",
        f"trusted: {str(trusted).lower()}",
        f"requires_network: {str(requires_network).lower()}",
        f"writes_files: {str(writes_files).lower()}",
        f"executes_code: {str(executes_code).lower()}",
        "secrets_needed:",
    ]
    for secret in secrets or []:
        lines.append(f"  - {secret}")
    lines.extend(["last_reviewed: 2026-07-10", "profile_tags:", f"recommended_scope: {scope}", "---", "", body])
    (skill_dir / "SKILL.md").write_text("\n".join(lines), encoding="utf-8")
    return skill_dir


def write_config(root: Path, plugins: list[dict]) -> None:
    config_dir = root / "scripts"
    config_dir.mkdir(parents=True, exist_ok=True)
    (config_dir / "codex_marketplace_config.json").write_text(
        json.dumps({"name": "test-market", "displayName": "Test Market", "plugins": plugins}, indent=2) + "\n",
        encoding="utf-8",
    )


def plugin(name: str, skills: list[dict], version: str = "1.1.0") -> dict:
    return {
        "name": name,
        "version": version,
        "displayName": name.title(),
        "description": f"{name} test plugin.",
        "category": "Productivity",
        "defaultPrompt": ["Use this plugin."],
        "skills": skills,
    }


@contextmanager
def patched_build_root(root: Path):
    old = {
        "build_ROOT": build.ROOT,
        "build_SKILLS_ROOT": build.SKILLS_ROOT,
        "build_CONFIG_PATH": build.CONFIG_PATH,
        "build_CODEX_ROOT": build.CODEX_ROOT,
        "build_MARKETPLACE_PATH": build.MARKETPLACE_PATH,
        "utils_ROOT": skill_utils.ROOT,
        "utils_SKILLS_ROOT": skill_utils.SKILLS_ROOT,
    }
    build.ROOT = root
    build.SKILLS_ROOT = root / "skills"
    build.CONFIG_PATH = root / "scripts" / "codex_marketplace_config.json"
    build.CODEX_ROOT = root / "plugins" / "codex"
    build.MARKETPLACE_PATH = build.CODEX_ROOT / ".agents" / "plugins" / "marketplace.json"
    skill_utils.ROOT = root
    skill_utils.SKILLS_ROOT = root / "skills"
    try:
        yield
    finally:
        build.ROOT = old["build_ROOT"]
        build.SKILLS_ROOT = old["build_SKILLS_ROOT"]
        build.CONFIG_PATH = old["build_CONFIG_PATH"]
        build.CODEX_ROOT = old["build_CODEX_ROOT"]
        build.MARKETPLACE_PATH = old["build_MARKETPLACE_PATH"]
        skill_utils.ROOT = old["utils_ROOT"]
        skill_utils.SKILLS_ROOT = old["utils_SKILLS_ROOT"]


class CodexMarketplaceTests(unittest.TestCase):
    def test_repository_config_has_nine_plugins(self) -> None:
        data = json.loads((REPO_ROOT / "scripts" / "codex_marketplace_config.json").read_text(encoding="utf-8"))
        self.assertEqual(
            [plugin["name"] for plugin in data["plugins"]],
            [
                "ai-skills-core",
                "workflow-core",
                "writing-style",
                "web-development",
                "research-writing",
                "statistical-modeling",
                "bioinformatics",
                "medical-imaging",
                "cardiacnexus",
            ],
        )

    def test_cross_plugin_frontmatter_name_duplicate_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_skill(root, "skills/a/one", "same-name")
            write_skill(root, "skills/b/two", "same-name")
            write_config(
                root,
                [
                    plugin("one", [{"type": "copy", "source": "skills/a/one"}]),
                    plugin("two", [{"type": "copy", "source": "skills/b/two"}]),
                ],
            )
            with patched_build_root(root), self.assertRaisesRegex(build.BuildError, "duplicate marketplace active skill"):
                build.generate_layer(root / "out")

    def test_aggregate_metadata_is_union_and_strictest_scope(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_skill(
                root,
                "skills/a/network",
                "network",
                requires_network=True,
                trusted=True,
                secrets=["OPENAI_API_KEY"],
                scope="global",
            )
            write_skill(root, "skills/b/runner", "runner", executes_code=True, writes_files=False, scope="project")
            write_config(
                root,
                [
                    plugin(
                        "agg",
                        [
                            {
                                "type": "aggregate",
                                "name": "combined",
                                "description": "Combined workflow.",
                                "source_skills": ["skills/a/network", "skills/b/runner"],
                            }
                        ],
                    )
                ],
            )
            with patched_build_root(root):
                build.generate_layer(root / "out")
                meta, _ = build.read_frontmatter(root / "out/plugins/agg/skills/combined/SKILL.md")
            self.assertTrue(meta["requires_network"])
            self.assertTrue(meta["writes_files"])
            self.assertTrue(meta["executes_code"])
            self.assertFalse(meta["trusted"])
            self.assertEqual(meta["secrets_needed"], ["OPENAI_API_KEY"])
            self.assertEqual(meta["recommended_scope"], "project")
            self.assertEqual(meta["provenance"], "generated")
            self.assertEqual(meta["source_skills"], ["skills/a/network", "skills/b/runner"])

    def test_secret_reference_without_frontmatter_declaration_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_skill(root, "skills/a/secret", "secret", body="Use OPENAI_API_KEY here.\n")
            write_config(root, [plugin("p", [{"type": "copy", "source": "skills/a/secret"}])])
            with patched_build_root(root), self.assertRaisesRegex(build.BuildError, "OPENAI_API_KEY"):
                build.generate_layer(root / "out")

    def test_invalid_semver_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_skill(root, "skills/a/one", "one")
            write_config(root, [plugin("p", [{"type": "copy", "source": "skills/a/one"}], version="v1")])
            with patched_build_root(root), self.assertRaisesRegex(build.BuildError, "semantic version"):
                build.generate_layer(root / "out")

    def test_placeholder_word_is_not_rewritten(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            skill_dir = write_skill(root, "skills/a/place", "place")
            (skill_dir / "script.py").write_text("placeholder = 'keep placeholder text'\n", encoding="utf-8")
            write_config(root, [plugin("p", [{"type": "copy", "source": "skills/a/place"}])])
            with patched_build_root(root):
                build.generate_layer(root / "out")
            copied = root / "out/plugins/p/skills/place/script.py"
            self.assertEqual(copied.read_text(encoding="utf-8"), "placeholder = 'keep placeholder text'\n")

    def test_nested_skill_md_is_renamed_in_aggregate_snapshot(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            skill_dir = write_skill(root, "skills/a/nested", "nested")
            nested = skill_dir / "references" / "child"
            nested.mkdir(parents=True)
            (nested / "SKILL.md").write_text("---\nname: child\n---\nchild\n", encoding="utf-8")
            write_config(
                root,
                [
                    plugin(
                        "p",
                        [
                            {
                                "type": "aggregate",
                                "name": "agg",
                                "description": "Aggregate.",
                                "source_skills": ["skills/a/nested"],
                            }
                        ],
                    )
                ],
            )
            with patched_build_root(root):
                build.generate_layer(root / "out")
            source_root = root / "out/plugins/p/skills/agg/_src/nested"
            self.assertFalse((source_root / "references/child/SKILL.md").exists())
            self.assertTrue((source_root / "references/child/source.md").exists())

    def test_generation_has_no_symlink_and_is_deterministic(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_skill(root, "skills/a/one", "one")
            write_config(root, [plugin("p", [{"type": "copy", "source": "skills/a/one"}])])
            with patched_build_root(root):
                build.generate_layer(root / "out1")
                build.generate_layer(root / "out2")
                self.assertEqual(build.compare_layers(root / "out1", root / "out2"), [])
                self.assertFalse(any(path.is_symlink() for path in (root / "out1").rglob("*")))

    def test_long_bioinformatics_source_path_uses_short_artifacts(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            skill_dir = write_skill(
                root,
                "skills/domains/bioinformatics/databases/bioinformatics-database-retrieval",
                "bioinformatics-database-retrieval",
            )
            providers = skill_dir / "references" / "providers"
            providers.mkdir(parents=True)
            (providers / "ncbi.md").write_text("provider notes\n", encoding="utf-8")
            write_config(
                root,
                [
                    plugin(
                        "bioinformatics",
                        [
                            {
                                "type": "aggregate",
                                "name": "bioinformatics-workflows",
                                "artifact_id": "bio",
                                "description": "Bioinformatics workflows.",
                                "source_skills": [
                                    {
                                        "source": "skills/domains/bioinformatics/databases/bioinformatics-database-retrieval",
                                        "artifact_id": "db",
                                    }
                                ],
                            }
                        ],
                    )
                ],
            )
            with patched_build_root(root):
                build.generate_layer(root / "out")
                report = build.path_report(root / "out")
            self.assertTrue((root / "out/plugins/bioinformatics/skills/bio/_src/db/references/providers/ncbi.md").exists())
            generated_paths = [path.relative_to(root / "out").as_posix() for path in (root / "out").rglob("*")]
            self.assertFalse(any("domains-bioinformatics-databases-bioinformatics-database-retrieval" in path for path in generated_paths))
            self.assertEqual(report["over_budget_count"], 0)

    def test_artifact_id_conflict_fails_with_sources(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_skill(root, "skills/a/one", "one")
            write_skill(root, "skills/b/two", "two")
            write_config(
                root,
                [
                    plugin(
                        "p",
                        [
                            {"type": "copy", "source": "skills/a/one", "artifact_id": "same"},
                            {"type": "copy", "source": "skills/b/two", "artifact_id": "same"},
                        ],
                    )
                ],
            )
            with patched_build_root(root), self.assertRaisesRegex(build.BuildError, "duplicate artifact_id same"):
                build.generate_layer(root / "out")

    def test_path_report_is_deterministic(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_skill(root, "skills/a/one", "one")
            write_config(root, [plugin("p", [{"type": "copy", "source": "skills/a/one", "artifact_id": "o"}])])
            with patched_build_root(root):
                build.generate_layer(root / "out1")
                build.generate_layer(root / "out2")
                self.assertEqual(build.path_report(root / "out1"), build.path_report(root / "out2"))

    def test_source_snapshot_content_is_preserved_without_active_nested_skill(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            skill_dir = write_skill(root, "skills/a/full", "full")
            (skill_dir / "references").mkdir()
            (skill_dir / "scripts").mkdir()
            (skill_dir / "references" / "guide.md").write_text("guide\n", encoding="utf-8")
            (skill_dir / "scripts" / "tool.py").write_text("print('ok')\n", encoding="utf-8")
            nested = skill_dir / "references" / "nested"
            nested.mkdir()
            (nested / "SKILL.md").write_text("---\nname: nested\n---\nnested\n", encoding="utf-8")
            write_config(
                root,
                [
                    plugin(
                        "p",
                        [
                            {
                                "type": "aggregate",
                                "name": "agg",
                                "artifact_id": "a",
                                "description": "Aggregate.",
                                "source_skills": [{"source": "skills/a/full", "artifact_id": "f"}],
                            }
                        ],
                    )
                ],
            )
            with patched_build_root(root):
                build.generate_layer(root / "out")
            source_root = root / "out/plugins/p/skills/a/_src/f"
            self.assertEqual((source_root / "references/guide.md").read_text(encoding="utf-8"), "guide\n")
            self.assertEqual((source_root / "scripts/tool.py").read_text(encoding="utf-8"), "print('ok')\n")
            self.assertFalse((source_root / "references/nested/SKILL.md").exists())
            self.assertTrue((source_root / "references/nested/source.md").exists())

    def test_current_repository_marketplace_paths_fit_windows_budget(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "codex"
            build.generate_layer(out)
            report = build.path_report(out)
        self.assertEqual(report["over_budget_count"], 0)
        self.assertLessEqual(report["max_file_length"], build.WINDOWS_PATH_BUDGET)
        self.assertLessEqual(report["max_dir_length"], build.WINDOWS_PATH_BUDGET)


if __name__ == "__main__":
    unittest.main()
