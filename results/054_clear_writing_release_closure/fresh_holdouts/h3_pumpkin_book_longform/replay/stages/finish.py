exec(Path('outputs/.work/prepare.py').read_text().split("s=Path('inputs/01-source.md')")[0])
d=Path('outputs/.work'); out=Path('outputs/神经网络：从感知机到深度学习.md');s=out.read_text()
plan=m.load_json(d/'reader_plan.json')
heads=['# 神经网络：','## 从误分类点','## 隐层怎样','## 误差逆传播：','## 梯度下降','## 其他网络','## 从多层网络','## 参考文献']
starts=[s.index(h) for h in heads]+[len(s)]
bindings={}
for i,b in enumerate(plan['bundle_order']):
 t=s[starts[i]:starts[i+1]];(d/'bundles'/f'{b}.md').write_text(t);bindings[b]=m.sha256_text(t)
assembled=''.join((d/'bundles'/f'{b}.md').read_text() for b in plan['bundle_order'])
assert assembled==s
(d/'final_candidate.md').write_text(assembled)
m.write_json(d/'assembly_packet.json',dict(schema=m.ASSEMBLY_PACKET_SCHEMA,reader_plan_sha256=m.sha256_file(d/'reader_plan.json'),realized_bundle_sha256s=bindings,bundle_order=plan['bundle_order']))
m.write_json(d/'semantic_audit.json',dict(schema=m.SEMANTIC_AUDIT_SCHEMA,decision='PASS',findings=[],reviewed_candidate_sha256=m.sha256_text(s),checks=['逐项对照8个语义组：分类回归定位、M-P归因、0/1边界、可分前提、M两类错误、非负损失、哑节点、SGD重算M、解不唯一、异或逐点例子均在正文。','30个展示公式中重复训练集仅出现一次，其余完整保留，BP三条链式推导保留各步及负号；输出/隐层的g和e定义与式号对应。','局部与全局区别及进一步系统学习限制保留；RBF中心固定条件、3.2/5.18/5.19、能量求和、RBM双向条件独立及5.20/5.22/5.23均在正文。','1986/1989/2012/2015、Hinton师生与AlexNet、ImageNet领先第二名、三位学者归因及全部三篇书目信息保留；参考文献排版断词复原。','人工根蒂色泽与图片输入两种路径、对数几率回归输出角色、特征学习的分类约束保留。','补充固定M下求导和零损失边界说明，由阶跃定义及损失直接推出；一般Boltzmann机和受限机名称分开，避免英文缩写误指一般模型。','不作外部历史核查；网络深度效果与历史叙述沿既有论述范围重组。','删除组队课程包装；正文无流程记录；所有数学表达在数学分隔符中。']))
receipt=m.validate_stage_package(Path('inputs/01-source.md').read_text(),d,receipt_path=d/'stage_receipt.json',prompt=(d/'prompt.md').read_text())
print(json.dumps(receipt,ensure_ascii=False,indent=2))
