# CARE 分割通信修正与稳定性实验报告（2026-08-28）

## 30 秒版本：简要结论

这轮实验先消除了上一轮中最容易影响解释的两个混杂因素：whole-myocardium 统一按 `{1,4,5}` 合并计算；FedAvg 中每个 client 的 AdamW optimizer state 也在通信轮之间持续保留。除此之外，实验条件没有变：仍是同一 CARE fold-0、同一 checkpoint、LGE-only 输入、7 个真实 center/client，并且每个 client 做 20 次本地更新。

在这些条件下，当前证据支持一个更细的判断。与原始 checkpoint 相比，decoder pooled 的改善最稳定；full-model pooled 也呈现改善趋势，但不同 seed 之间波动更大。decoder 设置下，FedAvg R=1/R=5 仍低于 pooled，说明 one-shot gap 的方向比较稳定。full-model 设置下，R=1/R=5 的 scar Dice 反而达到或略高于 pooled 的跨 seed 平均，但这个优势并没有在每个 seed 中稳定出现。把通信从 R=1 增加到 R=5 后，也没有稳定优于 R=1；因此在当前小预算实验里，few-round 通信还看不出明确的性价比优势。
