# 导入失败处理

先检查导入状态，再按检查结果执行对应分支。第 2 至第 4 步是条件分支，仅在条件满足时执行；只有终态为 `READY` 才算完成。

1. **检查导入状态。** 运行：

   ```bash
   python tools/inspect_import.py --job JOB-2048
   ```

2. **如果 `schema_status=INVALID`：**
   - 停止写入。
   - 修正列名。
   - 返回第 1 步，重新检查。

3. **如果 `schema_status=VALID`，但 `row_status=PARTIAL`：**
   - 保留 `imports/JOB-2048/rejected.csv`。
   - 只重试失败行。

4. **如果 `schema_status=VALID`，且 `row_status=COMPLETE`：** 运行：

   ```bash
   python tools/finalize_import.py --job JOB-2048
   ```

5. **确认是否完成。** 只有终态为 `READY` 时，才能判定导入完成。
