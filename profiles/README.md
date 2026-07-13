# Profiles

Profile 是手工挑选的安装组合，不是完整 domain。

- Profile：面向一个工作流的组合，例如 `research-main`。
- Domain：某个领域的完整 active skills，例如完整 `bayesian`。
- 精确 skill：单个 selector，例如 `domain/bayesian/pymc`。

安装示例：

```bash
ai-skills install --target repo --profile research-main --mode copy --write-agents-md
ai-skills install --target repo --domain bayesian --mode symlink --write-agents-md
ai-skills install --target repo --skill domain/bayesian/pymc --mode symlink --write-agents-md
```

## v3.1 推荐 Profile

- `global-baseline`：最小全局基线，包含流程路由和写作保真。
- `research-main`：科研写作主力，包含报告、论文、文献、引用、PDF/DOCX/可视化支持。
- `presentation-desktop`：桌面演示工作，包含 research/business deck planning。
- `frontend-research-product`：科研产品前端、视觉系统、参考研究和实现 QA。
- `medical-imaging-project`：通用医学影像项目，不复制 CardiacNexus 专用 skill。
- `bioinformatics-project`：常用生物信息项目组合。
- `server-research-baseline`：compute node 基线，包含 CJK/math PDF render 和通用 Slurm workflow。
- `ai-skills-maintainer`：维护本仓库 registry、catalog、provenance、marketplace、icon 和 profile。

## 兼容 Profile

旧 `codex-*` profile 仍保留，方便已有脚本继续使用。新文档优先推荐 v3.1 profile。

- `codex-core-global`
- `codex-workflow-core`
- `codex-webdev`
- `codex-research-writing`
- `codex-scientific-diagrams`
- `codex-writing-style`
- `codex-bayesian-jsdm`
- `codex-cardiacnexus`
- `codex-bioinformatics-light`
- `codex-skill-maintenance`

`codex-cardiacnexus` 只保留通用支持组合；项目专用 CardiacNexus skills 在 `exports/cardiacnexus-repo-local/`，后续应合并进 CardiacNexus repo。
