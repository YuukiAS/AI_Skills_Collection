import pathlib,json,importlib.util,shutil
p=pathlib.Path('outputs/stages')
spec=importlib.util.spec_from_file_location('support','/overflow/htzhu/mingcheng_new/.codex-global/plugins/cache/ai-skills-candidate-053/writing-style/0.2+codex.local-20260913T044041Z-2704773/skills/scientific-rewrite/scripts/rewrite_support.py');s=importlib.util.module_from_spec(spec);spec.loader.exec_module(s)
def save(n,o): (p/n).write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
shutil.copyfile('outputs/混淆矩阵.md',p/'final_candidate.md')
save('assembly_packet.json',dict(schema=s.ASSEMBLY_PACKET_SCHEMA,reader_plan_sha256=s.sha256_text((p/'reader_plan.json').read_text()),realized_bundle_sha256s={f'b{i}':s.sha256_text((p/f'realized/b{i}.md').read_text()) for i in range(1,4)},bundle_order=['b1','b2','b3'],operation='concatenate_realized_bundles'))
save('semantic_audit.json',dict(schema=s.SEMANTIC_AUDIT_SCHEMA,decision='PASS',findings=[],checks=['行实际、列预测；猫8=5+3，狗5=2+3，总计13。','二分类猫为阳性，TP5/FN3/FP2/TN3一致。','不平衡条件95/5，猫敏感性100%，狗识别率0%，准确度95%。','F1=190/195>97.4%，舍入约97.4%；限定猫为阳性。','约登公式的分子分母、加减关系和J=0完整保留。','仅清理页面包装；术语及约登指数参考资料身份保留。','将零值结论限定于类别区分能力，并澄清指数不是概率，避免沿用不严谨表述。']))
receipt=s.validate_stage_package(pathlib.Path('inputs/01-source.wiki').read_text(),p,prompt=(p/'prompt.md').read_text(),receipt_path=p/'stage_receipt.json')
print(json.dumps(receipt,ensure_ascii=False,indent=2))
