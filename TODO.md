# TODO：修复 Windows Codex App 插件市场安装时的路径过长问题

## 1. 问题背景

按照当前 `README.md` 在 Windows Codex App 中添加 Git 插件市场：

- 来源：`https://github.com/YuukiAS/AI_Skills_Collection.git`
- Git 引用：`main`
- 稀疏路径：`plugins/codex`

Codex App 的 Git checkout 失败，返回状态码 `128`：

```text
git checkout HEAD failed with status exit code: 128
fatal: cannot create directory at
'plugins/codex/plugins/bioinformatics/skills/bioinformatics-workflows/references/source-skills/domains-bioinformatics-databases-bioinformatics-database-retrieval/references/providers':
Filename too long
```

这不是用户填写了错误的仓库地址、Git 引用或稀疏路径。当前 README 的安装参数在语义上是正确的。真正的问题是生成发布层的物理路径过深：

```text
plugins/codex/
  plugins/<plugin>/
    skills/<aggregate-skill>/
      references/source-skills/<full-flattened-source-path>/
        ...
```

`build_codex_marketplace.py` 当前把完整源目录路径通过 `skill_flat_name(source_dir)` 编码到聚合 skill 的内部目录名中；在 bioinformatics 等深层 skill 上，这会与 Codex App 自己较长的本地 checkout 根目录叠加，超过 Windows 路径限制。

现有 Ubuntu GitHub Actions、Marketplace 生成和内容验证均未覆盖 Windows checkout 路径预算，因此工作流可以全部通过，但实际 Codex App 无法安装。

## 2. 本任务目标

必须实际修复生成器、生成层、测试、CI 和文档，使以下安装在普通 Windows 环境中直接成功：

```text
Source: https://github.com/YuukiAS/AI_Skills_Collection.git
Git reference: main
Sparse path: plugins/codex
```

不能把以下措施当作正式解决方案：

- 要求用户开启 Windows registry long paths；
- 要求用户运行 `git config --global core.longpaths true`；
- 要求用户把 Codex App 或仓库安装到更短路径；
- 删除 bioinformatics provider references 或其他源材料来规避报错；
- 让用户改用 CLI，从而放弃 Codex App Marketplace；
- 手工修改 `plugins/codex/` 而不修复生成器。

`core.longpaths` 最多可以在 troubleshooting 中作为临时诊断说明，不能成为 README 的主安装步骤或验收条件。

## 3. 必须保留的行为

本轮修复不得破坏：

1. 当前九个用户可见插件及其逻辑名称：
   - `ai-skills-core`
   - `workflow-core`
   - `writing-style`
   - `web-development`
   - `research-writing`
   - `statistical-modeling`
   - `bioinformatics`
   - `medical-imaging`
   - `cardiacnexus`
2. 每个活动 skill 的 frontmatter `name` 和触发边界。
3. 聚合 skill 的源工作流、脚本、references、assets、evals 和 provenance 链。
4. `plugins/codex/` 作为自包含、无 symlink、可 sparse checkout 的生成发布层。
5. 当前 `.github/workflows/codex-marketplace.yml` 的既有发布机制：
   - pull request 检查；
   - push 到 `main`；
   - `workflow_dispatch`；
   - 自动生成并验证；
   - `github-actions[bot]` 自动提交生成层；
   - `[skip codex-marketplace]` 防止循环触发。
6. CLI、profiles、registry 和 repo/user/codex-home 安装方式。

不要重新设计发布流程，也不要另建一套重复的 Marketplace workflow。

## 4. 先完成路径审计

在修改生成布局前，先为构建器增加可重复的路径审计，至少输出：

- 生成发布层中最长的前 20 个文件路径；
- 最长的前 20 个目录路径；
- 路径长度；
- 所属插件；
- 所属活动 skill；
- 对应源 skill；
- 是否超过 Windows 安全预算。

长度必须按从仓库根目录开始的完整 Git 路径计算，即必须包含：

```text
plugins/codex/...
```

不能只从 `CODEX_ROOT` 内部开始计算，否则会漏掉 sparse path 自身的长度。

新增一个明确的命令或构建参数，例如：

```bash
python3 scripts/build_codex_marketplace.py --path-report
```

具体命令名可以调整，但必须能够供本地测试和 CI 调用。

## 5. 重构生成发布层的物理路径

### 5.1 逻辑名称与物理目录名分离

用户可见的插件名、skill frontmatter `name`、描述和 provenance 不得为了缩短路径而改名。

生成器需要支持短的、稳定的物理 artifact id。物理 artifact id 只用于 `plugins/codex/` 内部目录，不改变逻辑身份。

Marketplace 配置可以采用类似结构：

```json
{
  "type": "aggregate",
  "name": "bioinformatics-workflows",
  "artifact_id": "bio",
  "source_skills": [
    {
      "source": "skills/domains/bioinformatics/databases/bioinformatics-database-retrieval",
      "artifact_id": "db"
    }
  ]
}
```

也可以采用其他等价设计，但必须满足：

- artifact id 稳定且确定性生成；
- 允许对特别长的路径显式指定短 id；
- 同一作用域内发生冲突时构建失败；
- 不得依赖 Python 的非确定性 hash；
- 不能重新引入完整源路径作为目录名。

### 5.2 缩短聚合 skill 的 source snapshot 前缀

当前路径：

```text
skills/<aggregate>/references/source-skills/<full-flat-source-path>/
```

必须替换为明显更短的结构，例如：

```text
skills/<short-artifact-id>/_src/<short-source-id>/
```

或其他同等紧凑的结构。

推荐把 source snapshot 继续保留在对应活动 skill 内部，避免安装器只复制 `skills/` 时丢失插件根目录旁边的支持文件。若采用插件级共享 source 目录，必须先证明 Codex App 安装后这些文件仍然存在且活动 skill 能稳定访问，不能只在仓库 checkout 中测试。

### 5.3 保留 source tree 的内部功能

缩短外层目录时，必须保留每个源 skill 内部实际需要的：

- `references/`
- `scripts/`
- `assets/`
- `evals/`
- 其他被源 workflow 引用的文件

不得静默删掉 `references/providers/`。

复制后的顶层源说明文件可以从 `source-skill.md` 缩短为 `source.md`，但必须同步更新聚合 `SKILL.md` 中的引用。

源 skill 内部存在嵌套 `SKILL.md` 时，仍然不能让它们成为活动 skill；需要继续重命名为非活动说明文件，并保持所有引用有效。

### 5.4 copy 类型也必须接受路径预算检查

不要只修复 aggregate 类型。直接 copy 的 skill 当前也使用 `skill_flat_name(source_dir)` 作为物理目录名。

需要为 copy 和 aggregate 两类 entry 统一支持紧凑 artifact id，并由路径预算测试覆盖。

## 6. 增加硬性 Windows 路径预算

构建器必须在写入或验证 Marketplace 时扫描所有生成文件和目录，并对完整仓库相对路径执行硬限制。

建议初始安全预算：

```text
从仓库根目录开始，任一生成文件或目录路径不超过 140 个字符。
```

该值为给 Codex App 未知的本地 checkout 前缀预留空间。实现时可以基于真实 Windows/Codex App 测试采用更严格的数值，但不得放宽到再次触发默认 Windows checkout 失败。

要求：

- 超过预算时构建失败；
- 错误信息列出最长路径、长度、来源插件和源 skill；
- `--validate` 和 `--check` 都必须执行该检查；
- 路径检查同时覆盖文件和目录；
- 不能只检查单个 path component 长度；
- 不能只在 Windows 上运行，Linux CI 也要进行确定性的预算验证。

如果内部某些真实文件名使 140 字符预算仍无法满足，继续缩短生成层的物理 artifact 路径。不要删除内容，也不要把路径预算简单调大。

## 7. 修复生成的引用

`aggregate_skill_markdown()` 当前生成：

```text
references/source-skills/<flat>/source-skill.md
```

修改生成器后，所有引用必须指向新的实际位置。

增加验证：

- 聚合 `SKILL.md` 中列出的每个 source workflow 文件都存在；
- source workflow 中相对引用的本地文件仍存在；
- 不允许生成悬空链接；
- 不允许同一 source snapshot 被无意复制多次；
- provenance 中的 `source_skills` 继续记录规范源路径，而不是短 artifact id。

短 artifact id 是发布物理实现细节，不能替代正式来源记录。

## 8. 增加回归测试

更新 `tests/test_codex_marketplace.py`，至少增加以下测试。

### 8.1 精确复现本次长路径

构造或直接使用等价源路径：

```text
skills/domains/bioinformatics/databases/bioinformatics-database-retrieval/references/providers
```

生成 `bioinformatics-workflows` 后，断言：

- 构建成功；
- provider references 仍然存在；
- 生成路径不再包含完整的 `domains-bioinformatics-databases-bioinformatics-database-retrieval` 目录名；
- 所有生成路径均满足预算。

### 8.2 artifact id 冲突

同一作用域内两个 entry 使用相同 artifact id 时，构建必须失败并打印两个源路径。

### 8.3 确定性

同一配置连续生成两次，目录名、文件内容和路径报告完全一致。

### 8.4 内容完整性

对具有 `references/`、`scripts/` 和嵌套说明文件的源 skill，生成后内容仍存在且未被改写。

### 8.5 当前真实仓库路径预算

测试必须对当前完整 `scripts/codex_marketplace_config.json` 生成一次临时 Marketplace，并断言没有任何路径超过预算。不能只测试人工构造的小 fixture。

## 9. 增加 Windows 端到端测试

在现有 `.github/workflows/codex-marketplace.yml` 中增加 Windows 兼容性测试，但不要替换现有 Ubuntu 发布 job。

Windows 测试至少完成：

1. 在 `windows-latest` 上生成 Marketplace；
2. 使用默认短路径支持关闭的情形进行 Git checkout 测试，例如显式设置：

```powershell
git config --global core.longpaths false
```

3. 把测试仓库放到一个故意较长的临时父目录中；
4. 执行与 Codex App 等价的 sparse checkout：

```text
plugins/codex
```

5. 验证 checkout 成功；
6. 验证九个插件和 marketplace manifest 存在；
7. 运行生成层 validate。

若 GitHub-hosted Windows runner 的系统设置导致 `core.longpaths=false` 仍无法可靠复现，应保留平台无关的 140 字符硬预算作为主 gate，并在 Windows job 中至少执行真实 sparse checkout。不要因为 runner 默认开启 long paths 就删除路径预算测试。

发布 job 的自动提交、权限和 `[skip codex-marketplace]` 逻辑必须保持不变。

## 10. 更新文档

更新：

- `README.md`
- `docs/CODEX_MARKETPLACE.md`

要求：

1. 保留当前 Codex App 安装参数；修复后用户仍应使用：

```text
Source: https://github.com/YuukiAS/AI_Skills_Collection.git
Git reference: main
Sparse path: plugins/codex
```

2. 将旧的 `references/source-skills/<flat>/` 说明更新为新的紧凑 source snapshot 结构。
3. 增加 Windows 安装验收说明。
4. troubleshooting 中可以记录 `Filename too long` 的历史原因，但必须说明该问题应由 Marketplace 发布层修复，而不是要求普通用户修改全局 Git/Windows 设置。
5. 不得把 CLI 描述成 Windows 用户遇到本问题后的正式替代方案。

## 11. 重新生成并验证发布层

完成代码修改后，必须重新生成并提交 `plugins/codex/`。

至少运行：

```bash
python3 scripts/build_codex_marketplace.py --write
python3 scripts/build_codex_marketplace.py --validate
python3 scripts/build_codex_marketplace.py --check
python3 scripts/build_codex_marketplace.py --path-report
python3 scripts/skills.py validate
python3 scripts/skills.py audit --all
python3 -m unittest discover -s tests
git diff --check
```

还要运行 Windows sparse-checkout 回归测试，或提供对应 GitHub Actions 成功结果。

## 12. 完成标准

只有同时满足以下条件，任务才算完成：

- 截图中的具体路径不再出现在生成层；
- Windows Codex App 可以使用 README 当前参数添加 Marketplace；
- 不需要用户开启 `core.longpaths`；
- `references/providers/` 等源材料未丢失；
- 当前九个插件名称和活动 skill 边界保持不变；
- 所有生成路径通过硬预算；
- Linux 和 Windows 测试通过；
- `plugins/codex/` 由生成器产生且 freshness check 通过；
- 现有 GitHub Actions 自动发布机制未被破坏；
- 没有手工补丁、悬空引用、symlink 或未跟踪生成文件。

## 13. 最终报告

最终报告必须包括：

1. 本次失败的根因；
2. 修改前和修改后的最长路径及长度；
3. 新的物理发布布局；
4. artifact id 的生成和冲突规则；
5. 证明 source references 未丢失的检查；
6. Linux 单元测试结果；
7. Windows sparse-checkout 结果；
8. Marketplace 生成、validate 和 check 结果；
9. GitHub Actions 是否保持自动发布；
10. commit SHA 和最终 `git status --short`。

不得只修改 README、建议用户开启 long paths，或留下后续实现计划。必须完成实际修复。