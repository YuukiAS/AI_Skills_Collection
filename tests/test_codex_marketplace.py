from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from contextlib import contextmanager
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import build_codex_marketplace as build  # noqa: E402
import skill_utils  # noqa: E402


CENTRAL_PLUGIN_NAMES = [
    "workflow-core",
    "ai-skills-core",
    "writing-style",
    "research-writing",
    "presentations",
    "scientific-visualization",
    "web-development",
    "statistical-modeling",
    "bioinformatics",
    "medical-imaging",
]
EXPECTED_PLUGIN_VERSIONS = {name: "0.1" for name in CENTRAL_PLUGIN_NAMES} | {
    "ai-skills-core": "0.2",
    "presentations": "0.3",
}
REPOSITORY_SEMVER_RE = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$")
PLUGIN_VERSION_RE = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)$")


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


def plugin(name: str, skills: list[dict], version: str = "1.1") -> dict:
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
        "build_PLUGIN_PAYLOAD_ROOT": build.PLUGIN_PAYLOAD_ROOT,
        "build_MARKETPLACE_PATH": build.MARKETPLACE_PATH,
        "build_OLD_NESTED_MARKETPLACE_PATH": build.OLD_NESTED_MARKETPLACE_PATH,
        "utils_ROOT": skill_utils.ROOT,
        "utils_SKILLS_ROOT": skill_utils.SKILLS_ROOT,
    }
    build.ROOT = root
    build.SKILLS_ROOT = root / "skills"
    build.CONFIG_PATH = root / "scripts" / "codex_marketplace_config.json"
    build.CODEX_ROOT = root / "plugins" / "codex"
    build.PLUGIN_PAYLOAD_ROOT = build.CODEX_ROOT / "plugins"
    build.MARKETPLACE_PATH = root / ".agents" / "plugins" / "marketplace.json"
    build.OLD_NESTED_MARKETPLACE_PATH = build.CODEX_ROOT / ".agents" / "plugins" / "marketplace.json"
    skill_utils.ROOT = root
    skill_utils.SKILLS_ROOT = root / "skills"
    try:
        yield
    finally:
        build.ROOT = old["build_ROOT"]
        build.SKILLS_ROOT = old["build_SKILLS_ROOT"]
        build.CONFIG_PATH = old["build_CONFIG_PATH"]
        build.CODEX_ROOT = old["build_CODEX_ROOT"]
        build.PLUGIN_PAYLOAD_ROOT = old["build_PLUGIN_PAYLOAD_ROOT"]
        build.MARKETPLACE_PATH = old["build_MARKETPLACE_PATH"]
        build.OLD_NESTED_MARKETPLACE_PATH = old["build_OLD_NESTED_MARKETPLACE_PATH"]
        skill_utils.ROOT = old["utils_ROOT"]
        skill_utils.SKILLS_ROOT = old["utils_SKILLS_ROOT"]


def copy_sparse_paths(source: Path, target: Path, *paths: str) -> None:
    for rel in paths:
        src = source / rel
        dst = target / rel
        if src.is_dir():
            shutil.copytree(src, dst)
        else:
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)


class CodexMarketplaceTests(unittest.TestCase):
    def test_repository_config_has_marketplace_plugin_set(self) -> None:
        data = json.loads((REPO_ROOT / "scripts" / "codex_marketplace_config.json").read_text(encoding="utf-8"))
        self.assertEqual([plugin["name"] for plugin in data["plugins"]], CENTRAL_PLUGIN_NAMES)
        self.assertEqual(data["marketplacePluginBudget"], 10)

    def test_central_plugins_have_exactly_one_source_only_todo_inbox(self) -> None:
        data = json.loads((REPO_ROOT / "scripts" / "codex_marketplace_config.json").read_text(encoding="utf-8"))
        plugin_names = {plugin["name"] for plugin in data["plugins"]}
        todo_names = {path.stem for path in (REPO_ROOT / "docs/plugin-todos").glob("*.md") if path.name != "README.md"}
        self.assertEqual(plugin_names, set(CENTRAL_PLUGIN_NAMES))
        self.assertEqual(todo_names, plugin_names)

        payload_root = REPO_ROOT / "plugins/codex/plugins"
        payload_paths = [path.relative_to(REPO_ROOT).as_posix() for path in payload_root.rglob("*")]
        for maintenance_dir in ["docs/plugin-todos", "plugin-todos", "docs/plugin-changelogs", "plugin-changelogs", "docs/provenance", "provenance"]:
            self.assertFalse(any(maintenance_dir in path for path in payload_paths), maintenance_dir)

    def test_ai_skills_core_marketplace_is_refinement_companion(self) -> None:
        data = json.loads((REPO_ROOT / "scripts" / "codex_marketplace_config.json").read_text(encoding="utf-8"))
        core = next(plugin for plugin in data["plugins"] if plugin["name"] == "ai-skills-core")
        skill_sources = [entry["source"] for entry in core["skills"]]
        skill_artifacts = [entry["artifact_id"] for entry in core["skills"]]
        serialized = json.dumps(core, ensure_ascii=False)

        self.assertEqual(core["version"], "0.2")
        self.assertEqual(core["name"], "ai-skills-core")
        self.assertEqual(core["displayName"], "AI Skills Maintainer")
        self.assertIn("Maintenance companion", core["description"])
        self.assertIn("skills/core/codex-system/project-skill-installer", skill_sources)
        self.assertIn("skills/core/codex-system/ai-skills-repository-maintainer", skill_sources)
        self.assertIn("skills/core/codex-system/skill-library-analysis", skill_sources)
        self.assertNotIn("skills/core/codex-system/codex-workflow-protocol", skill_sources)
        self.assertEqual(skill_artifacts, ["proj", "maint", "analysis"])
        self.assertIn("Refine an existing AI_Skills plugin from a real failure.", core["defaultPrompt"])
        self.assertIn("source, generated layer, replay, regression, version, and changelog closure", serialized)
        self.assertIn("extend an existing skill instead of creating another entry", serialized)

    def test_release_versions_are_independent_and_maturity_is_not_version(self) -> None:
        version = (REPO_ROOT / "VERSION").read_text(encoding="utf-8").strip()
        setup_version = subprocess.check_output([sys.executable, "setup.py", "--version"], cwd=REPO_ROOT, text=True).strip()
        registry = json.loads((REPO_ROOT / "registry.json").read_text(encoding="utf-8"))
        config = json.loads((REPO_ROOT / "scripts" / "codex_marketplace_config.json").read_text(encoding="utf-8"))
        readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
        readme_match = re.search(r"Repository / CLI release: `([^`]+)`", readme)
        self.assertIsNotNone(readme_match)

        self.assertRegex(version, REPOSITORY_SEMVER_RE)
        self.assertEqual({version, setup_version, registry["version"], readme_match.group(1)}, {version})

        plugin_versions = {plugin["name"]: plugin["version"] for plugin in config["plugins"]}
        self.assertEqual(plugin_versions, EXPECTED_PLUGIN_VERSIONS)
        self.assertEqual(
            {name: version for name, version in plugin_versions.items() if name not in {"ai-skills-core", "presentations"}},
            {name: "0.1" for name in CENTRAL_PLUGIN_NAMES if name not in {"ai-skills-core", "presentations"}},
        )
        for plugin_version in plugin_versions.values():
            self.assertRegex(plugin_version, PLUGIN_VERSION_RE)
            self.assertNotRegex(plugin_version, REPOSITORY_SEMVER_RE)

        for plugin_name in CENTRAL_PLUGIN_NAMES:
            plugin_json = json.loads(
                (REPO_ROOT / "plugins/codex/plugins" / plugin_name / ".codex-plugin/plugin.json").read_text(
                    encoding="utf-8"
                )
            )
            self.assertEqual(plugin_json["version"], plugin_versions[plugin_name])

        maturity_text = (REPO_ROOT / "docs/PLUGIN_MATURITY.md").read_text(encoding="utf-8")
        maturity_rows = re.findall(r"^\| `([^`]+)` \| `([^`]+)`", maturity_text, flags=re.MULTILINE)
        self.assertEqual({name for name, _ in maturity_rows}, set(CENTRAL_PLUGIN_NAMES))
        for _, maturity in maturity_rows:
            self.assertFalse(REPOSITORY_SEMVER_RE.match(maturity), maturity)
            self.assertFalse(PLUGIN_VERSION_RE.match(maturity), maturity)

    def test_plugin_changelogs_match_marketplace_set_and_versions(self) -> None:
        config = json.loads((REPO_ROOT / "scripts" / "codex_marketplace_config.json").read_text(encoding="utf-8"))
        plugin_versions = {plugin["name"]: plugin["version"] for plugin in config["plugins"]}
        changelog_root = REPO_ROOT / "docs/plugin-changelogs"
        changelog_names = {path.stem for path in changelog_root.glob("*.md") if path.name != "README.md"}
        todo_names = {path.stem for path in (REPO_ROOT / "docs/plugin-todos").glob("*.md") if path.name != "README.md"}
        self.assertEqual(changelog_names, set(CENTRAL_PLUGIN_NAMES))
        self.assertEqual(todo_names, set(CENTRAL_PLUGIN_NAMES))
        self.assertEqual(changelog_names, set(plugin_versions))

        index = (changelog_root / "README.md").read_text(encoding="utf-8")
        self.assertIn("Independent plugin versioning starts at `0.1`", index)
        for plugin_name, version in plugin_versions.items():
            text = (changelog_root / f"{plugin_name}.md").read_text(encoding="utf-8")
            latest = re.search(r"^## ([0-9]+\.[0-9]+)\b", text, flags=re.MULTILINE)
            self.assertIsNotNone(latest, plugin_name)
            self.assertEqual(latest.group(1), version)
            self.assertIn("Earlier `4.x` values were legacy lockstep release metadata", text)

    def test_readme_release_dashboard_matches_sources(self) -> None:
        config = json.loads((REPO_ROOT / "scripts" / "codex_marketplace_config.json").read_text(encoding="utf-8"))
        plugin_versions = {plugin["name"]: plugin["version"] for plugin in config["plugins"]}
        maturity_text = (REPO_ROOT / "docs/PLUGIN_MATURITY.md").read_text(encoding="utf-8")
        maturity = dict(re.findall(r"^\| `([^`]+)` \| `([^`]+)`", maturity_text, flags=re.MULTILINE))
        readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
        repo_version = (REPO_ROOT / "VERSION").read_text(encoding="utf-8").strip()
        self.assertIn(f"Repository / CLI release: `{repo_version}`", readme)
        for plugin_name in CENTRAL_PLUGIN_NAMES:
            row = re.search(
                rf"^\| `{re.escape(plugin_name)}` \| `([^`]+)` \| `([^`]+)` \| .*docs/plugin-changelogs/{re.escape(plugin_name)}\.md",
                readme,
                flags=re.MULTILINE,
            )
            self.assertIsNotNone(row, plugin_name)
            self.assertEqual(row.group(1), plugin_versions[plugin_name])
            self.assertEqual(row.group(2), maturity[plugin_name])

    def test_generated_layer_matches_source_config(self) -> None:
        summary, differences = build.check_layer()
        self.assertEqual(summary["errors"], [])
        self.assertEqual(differences, [])

    def test_text_transform_workflow_is_pinned_to_bridge_kit_commit(self) -> None:
        workflow = (REPO_ROOT / ".github/workflows/ai-bridge-text-transform.yml").read_text(encoding="utf-8")
        transform_docs = (REPO_ROOT / "docs/AI_BRIDGE_TEXT_TRANSFORM.md").read_text(encoding="utf-8")

        bridge_kit_commit = "27fff1659e3840438602c1b832d0e09a7b12ff91"
        self.assertIn(bridge_kit_commit, workflow)
        self.assertIn(bridge_kit_commit, transform_docs)
        self.assertIn("gpt-codex-ai-bridge-kit[text-transform]", workflow)
        self.assertIn("AI_BRIDGE_PRIVATE_REVIEW_AGE_KEY", workflow)
        self.assertIn("OPENAI_REVIEW_API_KEY", workflow)
        self.assertIn("OPENAI_VISUAL_REVIEW_API_KEY", workflow)
        self.assertIn("OPENAI_TEXT_TRANSFORM_MODEL", workflow)
        self.assertNotIn("@main", workflow)

    def test_codex_marketplace_ci_installs_presentation_test_dependencies(self) -> None:
        workflow = (REPO_ROOT / ".github/workflows/codex-marketplace.yml").read_text(encoding="utf-8")
        install_step = workflow.index("Install presentation regression test dependencies")
        import_check_step = workflow.index("Verify presentation regression imports")
        unittest_step = workflow.index("Test Codex marketplace builder")
        self.assertLess(install_step, unittest_step)
        self.assertLess(import_check_step, unittest_step)
        self.assertIn('python3 -m pip install "Pillow>=10" "python-pptx>=1.0" "matplotlib>=3.8"', workflow)
        self.assertIn('from PIL import Image, ImageDraw, ImageFont; import matplotlib; from pptx import Presentation', workflow)

    def test_repository_config_keeps_cardiacnexus_out_of_marketplace(self) -> None:
        data = json.loads((REPO_ROOT / "scripts" / "codex_marketplace_config.json").read_text(encoding="utf-8"))
        plugin_names = [plugin["name"] for plugin in data["plugins"]]
        self.assertNotIn("cardiacnexus", plugin_names)
        self.assertFalse((REPO_ROOT / "exports/cardiacnexus-repo-local").exists())
        self.assertFalse((REPO_ROOT / "skills/projects/cmr/cardiacnexus-feature-contracts/SKILL.md").exists())

    def test_restored_plugins_are_published_for_marketplace_set(self) -> None:
        data = json.loads((REPO_ROOT / "scripts" / "codex_marketplace_config.json").read_text(encoding="utf-8"))
        plugin_names = {plugin["name"] for plugin in data["plugins"]}
        self.assertTrue({"presentations", "scientific-visualization", "web-development", "statistical-modeling"} <= plugin_names)

    def test_render_and_slurm_are_not_central_marketplace_skills(self) -> None:
        data = json.loads((REPO_ROOT / "scripts" / "codex_marketplace_config.json").read_text(encoding="utf-8"))
        serialized = json.dumps(data)
        self.assertNotIn("skills/tools/documents-media/render-chinese-math-pdf", serialized)
        self.assertNotIn("skills/tools/hpc/slurm-workflows", serialized)
        self.assertTrue((REPO_ROOT / "skills/tools/hpc/slurm-workflows/SKILL.md").exists())

    def test_restored_plugin_payload_directories_are_present(self) -> None:
        for name in ["presentations", "scientific-visualization", "web-development", "statistical-modeling"]:
            self.assertTrue((REPO_ROOT / "plugins/codex/plugins" / name / ".codex-plugin" / "plugin.json").exists())

    def test_canonical_integration_history_exists(self) -> None:
        history = REPO_ROOT / "docs/provenance/INTEGRATION_HISTORY.md"
        text = history.read_text(encoding="utf-8")
        self.assertIn("| date | source_type | source | revision | permission/license | decision | target | integration_commit | note |", text)
        self.assertIn("CardiacNexus repo-local skills", text)
        self.assertIn("migrated-repo-local", text)
        self.assertIn("repo-local-canonical", text)
        self.assertFalse((REPO_ROOT / "docs/provenance/CLONED_SKILL_SOURCES.md").exists())

    def test_v36_profiles_exist_and_server_profile_carries_overlay_skills(self) -> None:
        for name in [
            "global-baseline",
            "research-main",
            "presentation-desktop",
            "frontend-research-product",
            "medical-imaging-project",
            "bioinformatics-project",
            "server-research-baseline",
            "ai-skills-maintainer",
        ]:
            self.assertTrue((REPO_ROOT / "profiles" / f"{name}.json").exists())
        server = json.loads((REPO_ROOT / "profiles/server-research-baseline.json").read_text(encoding="utf-8"))
        self.assertIn("skills/tools/hpc/slurm-workflows", server["skills"])
        self.assertIn("skills/tools/documents-media/render-chinese-math-pdf", server["skills"])

    def test_cuhk_payload_excludes_nonessential_zip_assets(self) -> None:
        root = REPO_ROOT / "skills/tools/documents-media/presentations/shared/templates/cuhk/beamer/source"
        self.assertFalse((root / ".vscode/settings.json").exists())
        self.assertFalse(any((root / "assets").glob("*.xcf")))
        self.assertFalse(any((root / "images").glob("Fig*.png")))
        self.assertFalse(any((root / "images").glob("Table*.png")))
        self.assertTrue((root / "assets/logo_RGB.png").exists())

    def test_marketplace_app_facing_skills_have_icon_metadata(self) -> None:
        data = json.loads((REPO_ROOT / "scripts" / "codex_marketplace_config.json").read_text(encoding="utf-8"))
        for plugin_data in data["plugins"]:
            for entry in plugin_data["skills"]:
                if entry["type"] == "aggregate":
                    self.assertTrue(entry.get("icon_small"), entry["name"])
                    self.assertTrue((REPO_ROOT / entry["icon_small"]).exists())
                elif entry["type"] == "copy":
                    skill_dir = REPO_ROOT / entry["source"]
                    text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
                    self.assertIn("icon_small:", text, entry["source"])
                    self.assertTrue((skill_dir / "assets/app-facing.svg").exists() or (skill_dir / "assets/workflow-core.svg").exists())

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
                meta, _ = build.read_frontmatter(root / "out/plugins/codex/plugins/agg/skills/combined/SKILL.md")
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
            with patched_build_root(root), self.assertRaisesRegex(build.BuildError, "two-part plugin release version"):
                build.generate_layer(root / "out")

    def test_placeholder_word_is_not_rewritten(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            skill_dir = write_skill(root, "skills/a/place", "place")
            (skill_dir / "script.py").write_text("placeholder = 'keep placeholder text'\n", encoding="utf-8")
            write_config(root, [plugin("p", [{"type": "copy", "source": "skills/a/place"}])])
            with patched_build_root(root):
                build.generate_layer(root / "out")
            copied = root / "out/plugins/codex/plugins/p/skills/place/script.py"
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
            source_root = root / "out/plugins/codex/plugins/p/skills/agg/_src/nested"
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
            self.assertTrue((root / "out/plugins/codex/plugins/bioinformatics/skills/bio/_src/db/references/providers/ncbi.md").exists())
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
            source_root = root / "out/plugins/codex/plugins/p/skills/a/_src/f"
            self.assertEqual((source_root / "references/guide.md").read_text(encoding="utf-8"), "guide\n")
            self.assertEqual((source_root / "scripts/tool.py").read_text(encoding="utf-8"), "print('ok')\n")
            self.assertFalse((source_root / "references/nested/SKILL.md").exists())
            self.assertTrue((source_root / "references/nested/source.md").exists())

    def test_current_repository_marketplace_paths_fit_windows_budget(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "repo"
            build.generate_layer(out)
            report = build.path_report(out)
        self.assertEqual(report["over_budget_count"], 0)
        self.assertLessEqual(report["max_file_length"], build.WINDOWS_PATH_BUDGET)
        self.assertLessEqual(report["max_dir_length"], build.WINDOWS_PATH_BUDGET)

    def test_manifest_is_generated_at_repository_root(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_skill(root, "skills/a/one", "one")
            write_config(root, [plugin("p", [{"type": "copy", "source": "skills/a/one"}])])
            with patched_build_root(root):
                build.generate_layer(root / "out")
                manifest = json.loads((root / "out/.agents/plugins/marketplace.json").read_text(encoding="utf-8"))
                summary = build.validate_layer(root / "out")
            self.assertEqual(summary["errors"], [])
            self.assertTrue((root / "out/plugins/codex/plugins/p/.codex-plugin/plugin.json").exists())
            self.assertFalse((root / "out/plugins/codex/.agents/plugins/marketplace.json").exists())
            self.assertEqual(manifest["plugins"][0]["source"]["path"], "./plugins/codex/plugins/p")

    def test_plugin_interface_metadata_and_shared_payload_are_generated(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_skill(root, "skills/a/one", "one")
            assets = root / "assets"
            assets.mkdir()
            (assets / "icon.svg").write_text("<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 1 1\" />\n", encoding="utf-8")
            (assets / "logo.svg").write_text("<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 1 1\" />\n", encoding="utf-8")
            shared = root / "shared/payload"
            shared.mkdir(parents=True)
            (shared / "guide.md").write_text("shared guide\n", encoding="utf-8")
            write_config(
                root,
                [
                    {
                        **plugin("p", [{"type": "copy", "source": "skills/a/one"}]),
                        "brandColor": "#123456",
                        "composerIcon": "./assets/icon.svg",
                        "logo": "./assets/logo.svg",
                        "shared": [{"source": "shared/payload", "target": "shared"}],
                    }
                ],
            )
            with patched_build_root(root):
                build.generate_layer(root / "out")
            payload = json.loads((root / "out/plugins/codex/plugins/p/.codex-plugin/plugin.json").read_text(encoding="utf-8"))
            self.assertEqual(payload["interface"]["brandColor"], "#123456")
            self.assertEqual(payload["interface"]["composerIcon"], "./.codex-plugin/assets/composer.svg")
            self.assertEqual(payload["interface"]["logo"], "./.codex-plugin/assets/logo.svg")
            self.assertTrue((root / "out/plugins/codex/plugins/p/.codex-plugin/assets/composer.svg").exists())
            self.assertTrue((root / "out/plugins/codex/plugins/p/.codex-plugin/assets/logo.svg").exists())
            self.assertTrue((root / "out/plugins/codex/plugins/p/shared/guide.md").exists())

    def test_validate_fails_when_only_old_nested_manifest_exists(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_skill(root, "skills/a/one", "one")
            write_config(root, [plugin("p", [{"type": "copy", "source": "skills/a/one"}])])
            with patched_build_root(root):
                build.generate_layer(root / "generated")
                broken = root / "broken"
                copy_sparse_paths(root / "generated", broken, "plugins/codex/plugins")
                nested = broken / "plugins/codex/.agents/plugins/marketplace.json"
                nested.parent.mkdir(parents=True)
                shutil.copy2(root / "generated/.agents/plugins/marketplace.json", nested)
                summary = build.validate_layer(broken)
            self.assertTrue(any(".agents/plugins/marketplace.json: file does not exist" in item for item in summary["errors"]))
            self.assertTrue(any("old nested marketplace manifest must not exist" in item for item in summary["errors"]))

    def test_sparse_paths_must_include_manifest_and_payload(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_skill(root, "skills/a/one", "one")
            write_config(root, [plugin("p", [{"type": "copy", "source": "skills/a/one"}])])
            with patched_build_root(root):
                generated = root / "generated"
                build.generate_layer(generated)
                only_manifest = root / "only-manifest"
                only_payload = root / "only-payload"
                both = root / "both"
                copy_sparse_paths(generated, only_manifest, ".agents/plugins")
                copy_sparse_paths(generated, only_payload, "plugins/codex/plugins")
                copy_sparse_paths(generated, both, ".agents/plugins", "plugins/codex/plugins")
                manifest_summary = build.validate_layer(only_manifest)
                payload_summary = build.validate_layer(only_payload)
                both_summary = build.validate_layer(both)
            self.assertTrue(any("marketplace source.path does not resolve" in item for item in manifest_summary["errors"]))
            self.assertTrue(any(".agents/plugins/marketplace.json: file does not exist" in item for item in payload_summary["errors"]))
            self.assertEqual(both_summary["errors"], [])

    def test_check_layer_compares_manifest_and_payload(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_skill(root, "skills/a/one", "one")
            write_config(root, [plugin("p", [{"type": "copy", "source": "skills/a/one"}])])
            with patched_build_root(root):
                build.generate_layer(root)
                summary, differences = build.check_layer()
                self.assertEqual(summary["errors"], [])
                self.assertEqual(differences, [])
                (root / ".agents/plugins/marketplace.json").write_text("{}\n", encoding="utf-8")
                summary, differences = build.check_layer()
            self.assertTrue(differences)
            self.assertTrue(any(".agents/plugins/marketplace.json" in item for item in differences))


if __name__ == "__main__":
    unittest.main()
