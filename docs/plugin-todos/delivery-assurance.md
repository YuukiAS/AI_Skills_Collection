# Delivery Assurance — Plugin TODO

> Planned dedicated Marketplace plugin. Product shape is already frozen as an independent plugin in `docs/design/SHARED_CAPABILITY_PRODUCT_SHAPE_DECISIONS_2026-11-12.md`. This inbox records real post-freeze delivery and acceptance failures before the plugin is implemented.

## 2026-11-22：跨组件接口必须用真实生产者输出驱动真实消费者回归，不能靠双方各自伪造测试输入
status: NEW
source: PC+Server+VPS / Cloudflare B 首次新版 successor 连续失败
evidence: successor 提交端在真实生产路径中导出 `CLOUDFLARED_HANDOFF_COMPONENT=cloudflare-backup`，新版候选稳定期及首次跨版本兼容代码却读取 `CLOUDFLARED_HANDOFF_FROM_COMPONENT`。仓库相关测试在此前多轮均通过，但真实 `9921640`、`10214470`、`10218095` 三代候选都在 cloudflared 已成功注册后、60 秒稳定期开始前因同一字段契约错误退出。旧 owner 被安全保留，因此服务未中断，但“测试全绿”没有证明真实交付链能运行。
problem: 这是典型的交付验收失真：发送端测试和接收端测试分别使用各自构造的环境/状态，因此两边都能 PASS，却没有任何测试证明真实生产者生成的字节、字段、参数、文件或环境能被真实消费者按同一合同读取。接口名、字段 schema、序列化格式、命令行参数、环境变量、状态文件和生成物只要跨进程/脚本/版本边界，就必须有 producer→consumer 闭环验收。
project-specific context: 具体 Cloudflare 字段名、job ID 和 Slurm 只属于本案例。通用交付门槛应覆盖：
1. 对跨组件接口建立 contract-consumption 回归：由真实生产函数/脚本生成输入，再直接交给真实消费函数/脚本；禁止测试在两端各自手写“正确 fixture”后把双 PASS 当成接口成立。
2. 对环境变量、状态文件、JSON/YAML 字段、CLI 参数、事件名和生成配置至少做一次发送方→接收方精确一致性测试；重命名必须有显式兼容和冲突规则。
3. 跨版本交付必须包含旧生产者→新消费者、新生产者→新消费者两条适用路径；第一代升级路径不能只靠稳态测试替代。
4. release/deploy 前的 acceptance 应从实际生产入口构造输入，至少跑到第一个真实消费点；“函数单测通过”“脚本存在”“安装哈希一致”均不足以证明接口可用。
5. 同一类真实生产失败连续出现第二次时触发重复失败断路：暂停再次宣称 ready，检查测试是否忠实覆盖实际 consumer path、是否存在 fixture drift、stale install 或 source/consumer 不一致。
6. 用户不应成为第一个发现接口字段对不上的集成测试者；如果真实生产事件发现的是静态契约错误，应记录为 Delivery Assurance gate failure，而不是普通验收失败。
