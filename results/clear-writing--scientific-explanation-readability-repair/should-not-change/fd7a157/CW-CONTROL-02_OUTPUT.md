# 导入失败处理流程

先检查导入状态，再按检查结果执行对应分支。只有终态为 `READY`，才算完成。

1. **检查导入状态。** 运行 `python tools/inspect_import.py --job JOB-2048`。

2. **如果 `schema_status=INVALID`：** 停止写入，修正列名，然后返回第 1 步重新检查。

3. **如果 `schema_status=VALID`，但 `row_status=PARTIAL`：** 保留 `imports/JOB-2048/rejected.csv`，只重试失败行。

4. **如果 `schema_status=VALID`，且 `row_status=COMPLETE`：** 运行 `python tools/finalize_import.py --job JOB-2048`。

5. **确认终态。** 只有终态为 `READY` 时，才能认定处理完成；未达到 `READY` 时，不能标记为完成。
