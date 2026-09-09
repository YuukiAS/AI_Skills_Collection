# 公开安全的科研说明与流程噪声混合样例

FedFisher 在 MMs 数据集上取得 Dice=0.81，但这个结论只覆盖一次通信设置 [12]。这组结果不能直接说明更多通信轮数时仍然保持同样收益，也不能替代跨数据集验证。

CARE 的初步结果来自同一批公开切分，但报告里没有把通信轮数、客户端数量和后处理写在同一个地方。为了避免读者误以为两个方法使用了完全一致的训练预算，后续比较需要把这些条件放回同一段。

公式 $\mathcal{L}_{total}=\mathcal{L}_{seg}+0.2\mathcal{L}_{reg}$ 只用于 FedFisher 的消融实验。CARE 的训练没有使用这个正则项，因此不能把这个公式当作两种方法共享的损失函数。

复现实验脚本位于 `scripts/run_fedfisher.sh`，配置文件是 `configs/mm_fedfisher.yaml`。这些路径只需要保留在复现实验说明里，不应该抢在主要科学结论之前出现。

以下是内部执行记录，不属于给研究读者看的正文：最终结果已通过独立规划者的审核；本轮满足收口条件；等待外部规划者审核；GitHub Actions run 34360618786；implementation commit ee8dd6edda2a2e4dd8f3210504225a56432b11a0；任务记录位于 `results/051_writing_style_rebuild/RESULT.md` 和 `automation/reviewed_handoff/tasks/051_writing_style_rebuild/CURRENT.json`。
