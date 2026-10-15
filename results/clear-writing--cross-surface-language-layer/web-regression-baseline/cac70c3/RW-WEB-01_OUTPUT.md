现在还不能交付到生产环境：构建和单元测试已通过，备份也已创建，但恢复演练尚未执行。在演练通过前，不得安排生产切换。

这意味着发布准备已有进展，但备份能否成功恢复还没有验证。目前没有发生任何生产写入，你不需要立即操作。

下一步由维护者运行恢复检查：
python tools/restore_check.py --snapshot snapshots/sample-service-2026-10-15.tar.zst

当前状态为 release_status=WAITING_FOR_RESTORE_CHECK。应等恢复演练通过后，再安排生产切换。
