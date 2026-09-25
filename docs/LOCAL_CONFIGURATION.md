# Local Configuration

AI_Skills_Collection keeps server configuration split into three layers:

- Live Slurm discovery reads the current scheduler with bounded read-only commands when available.
- Public site profiles in `site-profiles/*.json` are safe to commit. They are optional hard-policy overlays, not the list of supported servers.
- Private local overrides live outside this repository, normally at `~/.config/ai-skills/local-overrides.toml`. They contain local site ids, account names, partitions, QOS values, scratch paths, private TeX/Python paths, module initialization details, and local route preferences.

Do not commit private overrides, hostnames, tokens, account names, or personal paths.

## Workflow

1. Create the local template:

```bash
ai-skills environment init --site cuhk-central-cluster
```

For a third-party Slurm cluster that has no committed profile, choose a safe local id and initialize it directly:

```bash
ai-skills environment init --site my-local-slurm
```

2. Edit `~/.config/ai-skills/local-overrides.toml` and fill only values you know. Leave unknown account, QOS, partition, module and path fields blank until confirmed.

3. Inspect local state without writing project files:

```bash
ai-skills environment doctor --site cuhk-central-cluster
ai-skills environment plan --site cuhk-central-cluster --target user
```

4. Preview materialization:

```bash
ai-skills environment apply --site cuhk-central-cluster --target user --dry-run
```

5. Apply only after reviewing the plan:

```bash
ai-skills environment apply --site cuhk-central-cluster --target user
```

6. Compare or refresh later:

```bash
ai-skills environment diff --site cuhk-central-cluster --target user
ai-skills environment sync --site cuhk-central-cluster --target user --dry-run
ai-skills environment sync --site cuhk-central-cluster --target user
```

7. Remove only manifest-managed environment skills:

```bash
ai-skills environment uninstall --target user --dry-run
ai-skills environment uninstall --target user
```

`doctor` never submits Slurm jobs. The `--submit-smoke-job` flag only records explicit user acknowledgement; this repository still reports that automatic submission is not implemented by default.

No-profile Slurm sites can plan/apply/doctor without adding a repository profile. If no live scheduler is available and local facts are insufficient, routing mutation fails closed instead of guessing.

## Field Meanings

| Field | Required | Purpose |
|---|---:|---|
| `account` | Usually | Slurm allocation/account. Ask the user or site docs; do not infer it. |
| `partition` | Usually | Slurm partition/queue. Required when no safe site default exists. |
| `local_site_id` | Optional | Stable private id for the current Slurm deployment. Use this when no public profile exists or raw cluster identity should not appear in tracked output. |
| `policy_overlay_id` | Optional | Public profile id to apply as a hard-policy overlay. It is separate from `local_site_id`. |
| `partition_priority` | Optional | Comma-separated local preference among legal compatible partitions. |
| `accelerator_priority` | Optional | Comma-separated local accelerator preference among legal compatible routes. Hard accelerator requirements still win. |
| `qos` | Usually | Slurm QoS or queue class. Leave blank until confirmed. |
| `scratch_root` | Usually | Private writable scratch/work directory for temporary outputs. |
| `render_resource_dirs` | Optional | Comma-separated local CJK render resource directories, for example `$HOME/render_resources/chinese_math_pdf`; on the YuukiAS workstation the current TRACE-compatible location is `/home/yuukias/render_resources/chinese_math_pdf`. |
| `texlive_path` | Optional | Private TeX Live root/bin path when modules do not expose TeX. |
| `python_path` | Optional | Preferred Python executable or environment path. |
| `module_init` | Usually | Shell snippet or script path needed before `module load`. |

## Codex Prompt

```text
请为当前机器配置 AI_Skills_Collection 的本地环境 overlay。先读取 README、目标 site profile、local-overrides.example.toml 和 docs/LOCAL_CONFIGURATION.md；运行 environment detect/plan，只询问无法从机器安全检测出的 account、QOS、partition、scratch、module 和私有路径。不得猜测或提交任何账号、主机名、token、私有路径。先生成或更新 ~/.config/ai-skills/local-overrides.toml，再运行 doctor 和 dry-run；只有在我确认计划后才执行 apply。最后报告安装位置、实际使用的 site、仍缺失的字段和回滚命令。
```
