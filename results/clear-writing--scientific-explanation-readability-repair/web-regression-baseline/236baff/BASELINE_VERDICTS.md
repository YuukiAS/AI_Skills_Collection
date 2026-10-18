# Clear Writing 科研解释可读性修复基线判定

Candidate: `236baff177f5cff87170233f851e5f6afe8d698a`

Plugin: `writing-style@ai-skills-candidate` (`0.4`)

Runtime: `codex-cli 0.153.4`

四次 replay 都由 `scripts/candidate_plugin_replay.py` 启动，`run.json` 均记录 `actual_consumption.proven=true`。这些样本属于已知回归或正向保护，不是 G7 fresh evidence。

## 判定

### KR-WEB-06 — FAIL

输出保留了输入事实、公式、误差来源和适用限制，但没有把完整推理单元稳定组织成自然段。背景扣除、漂移估计、最终校准、误差传播和质量控制被连续拆成许多短段，多个一步公式与紧邻解释分别独立成块；单块可懂，整篇却形成明显的讲义碎片流。它还继续扩展教学数字、误差传播和区间判据，使纵向阅读成本进一步增加。

失败依据是整篇语义连续性，而不是段落、标题、公式或总字数的固定数量。

### KR-WEB-07 — PASS

输出把 `building structure`、`feature memory`、`audit trail`、`benchmark` 还原为自然中文概念，同时准确保留 `Temporal Fusion Transformer (TFT)`、`TFT`、`split_mode=building_holdout`、命令和路径。结论与跨季节证据缺口也没有被改写。

因此本轮不需要新增词表、英文比例或第三套语言机制。

### KR-WEB-08 — PASS（正向深度保护）

输出保留了三种估计方式的真实对照、收缩的因果直觉、小样本与大样本例子、公式解释、可能受益和可能受害的条件，以及当前信息不足以给出实际方法排名的不确定性。篇幅较长，但结构承担比较和推导作用，没有靠机械压短取得清晰。

这项 PASS 只说明必要深度得到保留，不表示每个扩展示例都是后续回答的最低要求。

### KR-WEB-09 — PASS（样本级）

输出先说明 `LRC` 的整体用途，再解释 $x_{g,t,k}$、$\hat m_{g,k}$、$r_{g,t,k}$、$\alpha_k$ 和 $q_{g,t}$ 的对象层级、下标角色、观测或估计状态及后续用途，然后比较两种基线。对于未定义的 $u_{a,b,c}$，输出明确指出缺少定义，没有猜测。

这项样本级 PASS 不否定前序 Reviewer 在真实产物中发现的通用合同缺口；当前 source 仍未要求普通科研解释在首次引入陌生对象时建立上述 reader model，也未规定定义不足时的停止边界。本轮仍按冻结 Plan 补齐该合同，并用修复后的完整回归确认不退化。

## 基线结论

继承候选真实复现了 G2-R1 的整篇碎片化问题。G2-R2 在这份定义充分的泛化输入上表现良好，但 source contract 仍缺少 Reviewer 要求的通用保障。允许的 production 修复仍严格限于冻结 Plan 的 A/B 两项，不扩大到新的语言机制、路由或状态机。
