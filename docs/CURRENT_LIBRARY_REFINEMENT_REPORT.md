# 当前技能库整改报告

日期：2026-08-16  
版本：`4.3.0`  
发布实现提交：`0e7939bcd914448e2dfef94ae2b98b25a213ce85`

这轮修的不是“再多加几个技能”，而是把当前最常用的入口理顺：用户用自然语言说科研写作、文献、引用、中文报告、英文科研表达、组会 PPT 或 Beamer 时，不需要记住内部 skill 名，也不应该被旧规则带到错误路线。

## 1. 这轮修了什么

### 科研写作与文献

`research-writing` 现在保留三个用户入口：`research-reporting`、`research-paper-workflow`、`literature-and-citations`。它们下面的具体职责重新分清：

- 写论文正文、改 Results、改 Discussion、写 rebuttal：走 `scientific-writing` 和 `paper-workflow-orchestrator`。
- 整篇论文结构、claim-evidence spine、图文一致性、投稿前完整性检查：走 `paper-workflow-orchestrator`。
- 审稿式风险检查：走 `peer-review`。
- 固定维度量化评分：走 `scholar-evaluation`。
- 按主题找论文、找最近论文、扩展候选文献：走 `research-lookup`。
- 已知 DOI/PMID/arXiv/URL/标题/author-year 的记录补全、BibTeX 清理、去重和参考文献整理：走 `citation-management`。
- 引用是否存在、引用支撑哪一句话、图表证据是否匹配：走 `citation-verification`。

### Writing Style

`writing-style` 现在是三层，不再混成一个“润色”入口：

- `writing-fidelity`：先保真，保护事实、数字、结构、引用、公式、用户纠错和版本身份。
- `chinese-prose`：中文“说人话”终审，降低模板腔、翻译腔、日志腔和不必要英文。
- `scientific-prose`：英文科研表达终审，减少 generic AI prose、过度防御和证据强度不匹配。

这不是 AI 检测规避，也不是把限制删掉。真实 limitation、证据边界和专业内容必须保留。

### Presentations

`presentations` 继续作为中央 Marketplace 插件存在，不新增另一个 presentation plugin。修复重点是旧规则“academic/research 默认 Beamer”：

- 明确说 PPT、PowerPoint、`.pptx`、editable、Slides、后续要自己改：走可编辑 Presentation/Slides。
- 明确说 Beamer、LaTeX slides、`.tex`、academic PDF、锁定 TeX 模板：走 Beamer/LaTeX。
- 在 `presentation-desktop` 中只说组会 PPT、research slides、paper talk、科研汇报且没指定格式：默认可编辑 deck。
- 只要故事线或逐页计划：可以停在 deck plan。

Presentation 完成门槛也提高了：deck plan、artifact creation、render、visual QA、可编辑性检查都要接上，不能因为文件存在就算完成。中文 slide 文案最终交给 `writing-fidelity` + `chinese-prose`，英文科研 slide prose 可交给 `scientific-prose`。

### Marketplace

中央 Marketplace 保持 10 个插件，`marketplacePluginBudget=10`：

`workflow-core`、`ai-skills-core`、`writing-style`、`research-writing`、`presentations`、`scientific-visualization`、`web-development`、`statistical-modeling`、`bioinformatics`、`medical-imaging`。

四个恢复的历史能力没有再被删除：`presentations`、`scientific-visualization`、`web-development`、`statistical-modeling`。

## 2. Before -> After

以前“帮我评价这篇论文”容易在审稿、量化评分、正文修改之间抢入口。现在审稿式风险走 `peer-review`，打分表式评价走 `scholar-evaluation`，正文修改走论文写作链。

以前 `citation-management` 同时写着 Google Scholar / PubMed 主题搜索，和 `research-lookup` 重叠。现在它只处理已知论文或已知标识符的记录定位、元数据补全、BibTeX 和 bibliography hygiene；主题找新论文交给 `research-lookup`。

以前中文报告“去 AI 味”容易被理解成泛泛润色，甚至可能删掉限制或专业内容。现在先用 `writing-fidelity` 固定事实边界，再用 `chinese-prose` 把中文改成人能读的正文。

以前 research presentation 因为“学术”容易默认 Beamer。现在格式按交付物决定：要可编辑 PPT 就走 Presentation/Slides，要 LaTeX slides 才走 Beamer。

以前 PPT 文件生成后容易把“有文件”当完成。现在必须 render 和视觉 QA，检查标题信息、裁切、溢出、对比度、图表/公式可读性、页面密度、叙事连续性和可编辑性。

## 3. Example Usage

1. “帮我把这段 Results 改成论文正文，别改数字和统计结论。”  
   预期：进入 `research-paper-workflow` / `scientific-writing`，同时触发 `writing-fidelity` 保真；输出是可投稿风格的 Results 段落，不改证据边界。

2. “这篇论文结构乱，帮我重排主张、证据和图的顺序。”  
   预期：进入 `paper-workflow-orchestrator`；输出 claim-evidence spine、章节职责和图文协调建议。

3. “投稿前按 reviewer 角度帮我挑硬伤。”  
   预期：进入 `peer-review`；输出审稿式风险、可能被质疑的 claims、证据缺口和修复优先级。

4. “帮我找最近两年关于 diffusion MRI uncertainty 的关键论文。”  
   预期：进入 `research-lookup`；输出候选论文、检索依据和可继续核验的来源。

5. “这个 DOI 和 BibTeX 帮我核一下，看看作者、标题、年份对不对。”  
   预期：进入 `citation-management`；输出已知记录的 metadata/BibTeX 修正建议。

6. “这句话引用 Smith 2023 合适吗？帮我核验支撑关系。”  
   预期：进入 `citation-verification`；输出 citation 是否存在、是否支撑该 claim、是否需要换引用。

7. “把这份中文技术报告说人话，但实验结果和限制别动。”  
   预期：先 `writing-fidelity` 后 `chinese-prose`；输出自然中文正文，保留事实、数字、术语、限制和证据边界。

8. “这段英文 discussion 太像 AI 模板，帮我改成严谨科研表达。”  
   预期：进入 `scientific-prose`；输出更具体、证据强度匹配、不过度防御的英文科研段落。

9. “给我做一份 12 页组会 PPT，后面我要自己改。”  
   预期：进入 `presentation-desktop` 的可编辑 Presentation/Slides 路线；输出 deck plan、可编辑文件创建要求和 render/visual QA 标准。

10. “给这个 conference talk 做 Beamer slides，输出 `.tex`。”  
    预期：进入 Beamer/LaTeX 路线；输出 `.tex` 源和 PDF/render QA，不切到 PPTX。

## 4. 没采用什么，为什么

没有新增 `humanizer` skill。中文“说人话”和英文科研去模板腔已经由 `writing-style` 三层覆盖，单独新增 humanizer 会制造重复入口，也容易被误解成 AI 检测规避。

没有新增第二个 presentation plugin。`presentations` 已经是中央 Marketplace 插件，本轮修的是它的路由、写作交接和 QA，不是再开一个并行入口。

没有把所有相邻 skill 强行 merge/delete。149 个 active skills 里有不少领域技能只在具体上下文中触发；本轮只处理高频阻断边界，避免为了“看起来少”牺牲可达性。

没有处理新的 Notion、AI Resources、Research 候选或外部 repo。本轮是当前库有限整改，不是新 intake。

## 5. 发布与安装结果

正式版本：`4.3.0`。

Marketplace smoke 使用最终 `origin/main` 的 Git marketplace：

- `writing-style@yuukias-ai-skills`：安装/升级成功，版本 `4.3.0`，关键 skills 为 `fidelity`、`zh`、`sci`。
- `research-writing@yuukias-ai-skills`：安装/升级成功，版本 `4.3.0`，关键 skills 为 `report`、`paper`、`litcite`。
- `presentations@yuukias-ai-skills`：安装成功，版本 `4.3.0`，关键 skills 为 `business`、`research`。

Source CLI smoke：

- `presentation-desktop` 安装到临时 repo 成功，commit `0e7939bcd914448e2dfef94ae2b98b25a213ce85`。
- 目标 `.agents/skills/` 包含 `research-presentations`、`business-presentations`、`writing-fidelity`、`scientific-prose`、`chinese-prose`。
- `verify_server_installation.py --profile presentation-desktop --json` 通过，安装 5 个 skills，marketplace manifest 检查为 10 plugins，payload errors 为 0。
- 默认 `verify_server_installation.py --json` 也通过，安装 7 个 `server-research-baseline` skills，payload errors 为 0。

最终 GitHub Actions：

- workflow：`Codex Marketplace`
- run_id：`31969240116`
- head_sha：`0e7939bcd914448e2dfef94ae2b98b25a213ce85`
- conclusion：`success`

## 6. 剩余限制与风险

这轮没有逐字重审 149 个 skill 的全部正文，而是基于现有 active-skill audit 和 Planner 复核，重点检查高频入口、source/generated 一致性、Marketplace、profile、安装路径和发布版本。

安装 smoke 中本机缺少 `latexmk` 和 Python `pptx` 模块，它们被记录为 optional tooling warnings，不影响技能安装、marketplace payload 或 profile 安装结果。真实 PPTX/LaTeX artifact render 仍取决于执行环境是否安装相应工具。

部分冷门领域技能仍可能有未来优化空间，但没有发现会阻断本轮 4.3.0 发布的用户级错误。

## 7. 技术附录

### 关键提交

- 001 implementation：`ed5508ab6e20be905f9c89de2f928b135f8dc5ed`
- 002 implementation：`0ecd81fd82157a4f2dbc53a942b2070b1624c4f6`
- 003 initial implementation：`b2ac1b246007ee848ea058bc54bf9eaef1c3e1a0`
- 003 revision implementation：`71db67690b2ce37523c4d7924244f5892f6d8a4a`
- 4.3.0 release implementation：`0e7939bcd914448e2dfef94ae2b98b25a213ce85`

### 版本文件

- `setup.py`：`4.3.0`
- `scripts/codex_marketplace_config.json`：10 个插件全部 `4.3.0`
- `registry.json`：`version=4.3.0`，`skill_count=149`
- `CHANGELOG.md`：新增 `4.3.0 - 2026-08-16`

### 生成与验证

已运行并通过：

```bash
python3 scripts/skills.py registry --write
python3 scripts/skills.py validate
python3 scripts/skills.py audit --all
python3 scripts/skills.py catalog --write
python3 scripts/audit_skill_provenance.py --write
python3 scripts/build_codex_marketplace.py --write --validate --check --path-report
python3 scripts/provenance_audit.py --check
python3 scripts/icon_audit.py --scope marketplace --check
python3 -m unittest discover -s tests
git diff --check
```

关键结果：

- registry：149 active skills
- profiles：18
- marketplace：10 plugins、25 active skills、63 source snapshots
- Windows path budget overage：0
- unittest：102 tests，OK

### 安装 Smoke 命令

Marketplace：

```bash
codex plugin marketplace add https://github.com/YuukiAS/AI_Skills_Collection.git --ref main --sparse .agents/plugins --sparse plugins/codex/plugins --json
codex plugin add writing-style@yuukias-ai-skills --json
codex plugin add research-writing@yuukias-ai-skills --json
codex plugin add presentations@yuukias-ai-skills --json
codex plugin list --marketplace yuukias-ai-skills --json
```

Source CLI：

```bash
python3 scripts/skills.py install --target repo --project /tmp/ai-skills-presentation-profile-smoke-31969240116 --profile presentation-desktop --mode copy --write-agents-md --json
python3 scripts/verify_server_installation.py --profile presentation-desktop --json
python3 scripts/verify_server_installation.py --json
```

### Git State

提交本报告前，发布实现提交 `0e7939bcd914448e2dfef94ae2b98b25a213ce85` 已推送到 `origin/main`，对应 GitHub Actions 成功。最终 Planner 复核应以包含本报告和 `results/004_current_library_acceptance/RESULT.md` 的最新 `origin/main` 为准。
