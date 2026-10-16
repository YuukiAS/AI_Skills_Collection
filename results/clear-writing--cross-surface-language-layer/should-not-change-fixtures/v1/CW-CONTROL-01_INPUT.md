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
