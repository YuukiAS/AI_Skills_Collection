# Frontend Design：反馈连续性守卫（可运行实验原型）

这个目录提供真实的 Python 机械校验工具及 10 项测试，而不是另一份仅靠文字执行的设计原则。它尚未接入正式 Frontend Design 插件，也未在 Asteria 的真实界面中完成视觉对照。

## 运行

进入本目录，执行：

    python3 -m unittest -v test_design_guard

本地临时 Git 仓库测试已覆盖：越界修改、旧截图复用、KEEP 未回归、未授权整体重做、工作区有未提交修改、证据未哈希、错误宿主、证据内容被改变、未经批准提升基线，以及正常局部修改。测试是机械模拟，不能作为真实 UI 成功的证据。

## 使用的三个 JSON 文件

baseline.json 保存用户真正认可过的局部，不把历史视觉母版、制作方 PASS 或单个局部好评自动当成整产品通过：

    {
      "schema": "fd-baseline-v1",
      "current_commit": "<原产品完整提交>",
      "surface": "browser",
      "accepted": [{
        "id": "binding-switch",
        "status": "PARTIAL_ACCEPT",
        "user_source": "原始用户反馈的定位",
        "description": "实现台绑定切换必须保留"
      }]
    }

task.json 由 Frontend Design/Codex 根据用户反馈及设计基准构建，不要求用户自己填写：

    {
      "schema": "fd-change-v1",
      "baseline_commit": "<原产品完整提交>",
      "classification": "S2",
      "feedback": "整屏过载，但实现台方向正确",
      "allowed_paths": ["src/views/overview/", "src/styles/overview.css"],
      "keep": ["binding-switch"],
      "repair_checks": ["density-fixed"],
      "explicit_user_redesign_approval": false
    }

Codex 必须用既有 Playwright/真实 Obsidian 自动化执行改后任务，生成截图、录制和 proof.json；本机械工具不会伪造这些真实证据：

    {
      "schema": "fd-proof-v1",
      "candidate_commit": "<修改后实际 Git HEAD>",
      "surface": "browser",
      "checks": [{
        "id": "binding-switch",
        "result": "PASS",
        "kind": "REAL_INTERACTION",
        "candidate_commit": "<修改后实际 Git HEAD>",
        "evidence": "binding-switch.mp4",
        "sha256": "<实际录制文件校验值>"
      }, {
        "id": "density-fixed",
        "result": "PASS",
        "kind": "SCREENSHOT",
        "candidate_commit": "<修改后实际 Git HEAD>",
        "evidence": "overview-after.png",
        "sha256": "<实际截图文件校验值>"
      }]
    }

proof.json、图片和录制须放在同一目录。使用绝对路径运行：

    python3 design_guard.py check --repo /path/to/product-repo \
      --baseline /path/to/baseline.json --task /path/to/task.json \
      --proof /path/to/proof.json --report /path/to/check-report.json

工具按原提交与实际 HEAD 的 Git diff 核查范围，检查工作区干净、同一宿主、同一候选、需要保留的交互是否有实际证据及其哈希。机械检查通过时仅输出 READY_FOR_VISUAL_REVIEW，**不输出 USER_ACCEPTED**。

用户真正看过实物并明确接受后，approval.json 必须包含明确认可来源及精确候选提交：

    {
      "explicit_user_approval": true,
      "user_source": "<用户明确接受的可定位记录>",
      "candidate_commit": "<用户实际接受的 Git commit>"
    }

这时才能运行：

    python3 design_guard.py promote --baseline /path/to/baseline.json \
      --report /path/to/check-report.json --approval /path/to/approval.json \
      --out /path/to/new-baseline.json

提升基线不会改变历史局部接受范围，不自动提交、推送或合并。

## 接下来要接入正式插件的内容

一是让 Frontend coordinator 根据项目真实设计 authority 自动准备 baseline 与局部 task；二是让现有浏览器/Obsidian 工具产生真实 proof，至少完成同一任务旧坏新好的对比；三是在设计方向未知时先用真实数据制作少量可见、可操作候选，不提前完整开发。这三项应由现有 web-development 插件维护流程集成，不新造第二个设计插件或状态服务。

正式生产源码仍由当前 Frontend Design / Verified Workflow / AI Skills Maintainer 约束管理。实验中的文件存在不证明新版正式插件已经发布，也不证明 Claude/Astra 已经产生更好看的设计。
