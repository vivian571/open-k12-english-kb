# English Knowledge Base Ingestion & Contribution Guide

本项目支持持续更新与扩充英语学习资料（词汇、语法微专题、长难句、完形填空、写作模板等）。

## 1. 资料更新规范

所有新增资料均遵循**结构化与去重**原则：

### A. 语法微专题 (Grammar Topics)
- 文件路径：`data/grammar_topics.json`
- 结构规范：
  ```json
  {
    "id": "chap_XX_pYY",
    "name": "考点名称",
    "prerequisites": ["前置基础考点ID"],
    "subpoints": ["子概念1", "子概念2"]
  }
  ```

### B. 启发式思维卡片 (Concept & Mnemonic Cards)
- 文件路径：`data/cards_samples.json`
- 核心要求：
  - 严禁枯燥的规则复述。
  - 必须提供：
    1. **生活化隐喻 (Metaphor)**：将抽象语法转化为生活场景。
    2. **速记口诀 (Formula/Mnemonic)**：朗朗上口的口诀。
    3. **经典易错点 (Common Traps)**：学生常踩的思维陷阱。
    4. **启发式破题提问 (Heuristic Question)**：不透露答案，引导学生自己思考的第 1 问。

---

## 2. 自动化更新工具 (Automated Importers)

项目提供了更新脚本 `scripts/update_materials.py`：

```bash
# 1. 批量导入外部 JSON 考点或卡片
python3 scripts/update_materials.py --import-cards path/to/new_cards.json

# 2. 校验数据格式一致性与前置依赖环路检查
python3 scripts/update_materials.py --validate

# 3. 自动同步更新 HTML 工作台内置数据
python3 scripts/update_materials.py --sync-workbench
```

---

## 3. 提交与 PR 流程

1. Fork 本仓库。
2. 创建特性分支：`git checkout -b feature/add-reading-comprehension`。
3. 补充测试用例并执行 `pytest`。
4. 提交并发起 Pull Request。
