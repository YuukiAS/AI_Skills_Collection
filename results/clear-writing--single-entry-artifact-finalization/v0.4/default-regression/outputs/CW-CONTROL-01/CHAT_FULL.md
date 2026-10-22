我会使用 Clear Writing，读取指定输入，保留合同原有结构、全部字段和精确字符串，并在交付后全文回读核对。


已保存至 [release-handoff-contract.md](outputs/release-handoff-contract.md)，并全文回读，确认与输入逐字节一致。

# 发布交接合同

## Authority

- `release_status=WAITING_FOR_CI`
- 未获授权执行 `git push origin main`。

## Required command

```bash
python scripts/build_codex_marketplace.py --validate --check
```

## Completion

只有 `ci_status=PASS` 且 `review_decision=PASS` 时才能进入 `READY_FOR_RELEASE`。