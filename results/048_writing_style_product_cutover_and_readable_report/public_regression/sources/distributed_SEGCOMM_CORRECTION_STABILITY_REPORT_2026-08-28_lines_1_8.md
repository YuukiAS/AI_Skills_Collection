# CARE 分割通信 correction + stability 实验报告（2026-08-28）

## 30 秒版本

这轮修正了上一轮最重要的两个混杂：whole-myocardium 现在按 `{1,4,5}` 合并计算，FedAvg 中每个 client 的 AdamW optimizer state 在通信轮之间持续保留。实验仍使用同一 CARE fold-0、同一 checkpoint、LGE-only 输入、7 个真实 center/client 和每个 client 20 次本地更新。

当前证据支持一个更细的判断：decoder pooled 相比原始 checkpoint 的改善最稳定；full-model pooled 也有改善趋势，但 seed 间波动更大。decoder 下 FedAvg R=1/R=5 仍低于 pooled，one-shot gap 方向稳定；full-model 下 R=1/R=5 的 scar Dice 反而达到或略高于 pooled 的跨 seed 平均，但这个优势不是每个 seed 都稳定。R=5 增加 5 倍通信后，没有稳定优于 R=1，因此当前小预算下看不出 few-round 的性价比优势。
