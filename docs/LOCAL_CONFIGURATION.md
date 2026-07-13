# Local Configuration

AI_Skills_Collection keeps server configuration split into two layers:

- Public site profiles in `site-profiles/*.json` are safe to commit. They describe site ids, detection hints, scheduler family, public constraints, and which skills should be materialized for that site.
- Private local overrides live outside this repository, normally at `~/.config/ai-skills/local-overrides.toml`. They contain account names, partitions, QOS values, scratch paths, private TeX/Python paths, and module initialization details.

Do not commit private overrides, hostnames, tokens, account names, or personal paths.

## Workflow

1. Create the local template:

```bash
ai-skills environment init --site cuhk-central-cluster
```

2. Edit `~/.config/ai-skills/local-overrides.toml` and fill only values you know.

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

## Field Meanings

| Field | Required | Purpose |
|---|---:|---|
| `account` | Usually | Slurm allocation/account. Ask the user or site docs; do not infer it. |
| `partition` | Usually | Slurm partition/queue. Required when no safe site default exists. |
| `qos` | Usually | Slurm QoS or queue class. Leave blank until confirmed. |
| `scratch_root` | Usually | Private writable scratch/work directory for temporary outputs. |
| `texlive_path` | Optional | Private TeX Live root/bin path when modules do not expose TeX. |
| `python_path` | Optional | Preferred Python executable or environment path. |
| `module_init` | Usually | Shell snippet or script path needed before `module load`. |

## Codex Prompt

```text
请为当前机器配置 AI_Skills_Collection 的本地环境 overlay。先读取 README、目标 site profile、local-overrides.example.toml 和 docs/LOCAL_CONFIGURATION.md；运行 environment detect/plan，只询问无法从机器安全检测出的 account、QOS、partition、scratch、module 和私有路径。不得猜测或提交任何账号、主机名、token、私有路径。先生成或更新 ~/.config/ai-skills/local-overrides.toml，再运行 doctor 和 dry-run；只有在我确认计划后才执行 apply。最后报告安装位置、实际使用的 site、仍缺失的字段和回滚命令。
```
