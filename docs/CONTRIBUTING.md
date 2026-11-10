# English Knowledge Base Contribution Guide

本项目专注于构建高质量、结构化、模块化的初中英语知识库。

## 一、知识库收录范围

1. **语法体系与考点拓扑 (`data/grammar_topics.json`)**：
   - 覆盖中考 10 大核心语法专题。
   - 包含考点名称、子概念细分以及前置学习依赖（Prerequisites）。

2. **教材与学习资料索引 (`data/textbooks_catalog.json`)**：
   - 主流教材版本（如外研版 WY、人教版 PEP 等）单元精读、课文对话与重难点。
   - 同步句型转换、核心词汇背诵表、日常交际搭配短语。

---

## 二、格式校验规范

提交新内容前，请确保 JSON 格式合法且无重复 ID：

```bash
# 验证 JSON 合法性
python3 -m json.tool data/grammar_topics.json > /dev/null
python3 -m json.tool data/textbooks_catalog.json > /dev/null
```

---

## 三、提交与 PR 流程

1. Fork 本仓库。
2. 创建特性分支：`git checkout -b feature/add-grade8-materials`。
3. 补充新资料元数据与 Markdown 说明文档。
4. 发起 Pull Request。
