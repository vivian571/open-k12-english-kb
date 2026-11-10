# Open K-12 English Grammar Knowledge Base & Heuristic Tutor
# 开源初中英语全量知识库与启发式无痛助教

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Dataset: OmniEdu](https://img.shields.io/badge/Pedagogy-OmniEdu_arXiv:2609.23088-green.svg)](https://arxiv.org/abs/2609.23088)
[![MCP Ready](https://img.shields.io/badge/MCP-FastMCP_Ready-purple.svg)](https://modelcontextprotocol.io)

本项目基于 127 页手绘全彩知识体系教材及北京大学等团队发布的 **OmniEdu（arXiv:2609.23088）** 启发式教育模型规范，构建了**全量初中英语语法图谱、10 大语法核心模块、64 个核心考点知识树**以及**针对中国初中生的无痛拆解教学引擎**。

---

## 🌟 核心特色与架构

1. **结构化语法知识图谱（64 个中考考点，拓扑前置关系全标注）**
   - 覆盖中考英语必考 10 大核心专题：名词、冠词、代词、数词、介词、非谓语动词/情态动词、形容词副词、时态语态、简单句与主谓一致、复合句（宾语/状语/定语从句）。
   - 每个考点清晰标注其前置依赖知识（Prerequisites），构建学习路径。

2. **基于 OmniEdu 启发式教学框架（From Solver to Tutor）**
   - **严禁直接报答案（Non-Leakage）**：根据论文 Stage 4 `sr_8` / `sr_10` 量表，坚决杜绝直接给出完整句型或得数。
   - **抓主干·拆挂件（Painless Sentence Parsing）**：将复杂长难句先拎出 `[谁 + 做了什么]` 主干，再将从句/介宾短语作为修饰挂件逐层剥离。
   - **错因诊断先肯定（Preserve Correct Work）**：精准定位孩子草稿的第一个错误点，分流概念盲区（Conceptual Gap）与程序粗心（Procedural Error）。
   - **三级渐进锦囊（Progressive Hints）**：`💡 锦囊1(线索雷达)` $\rightarrow$ `🧭 锦囊2(关系桥梁)` $\rightarrow$ `🚀 锦囊3(起手第一步)`。

3. **双形态交互交付**
   - **单文件交互式沉浸式 Web 工作台**（`k12_english_workbench.html`）：免装环境、支持知识图谱浏览、真题无痛拆解模拟、口诀记忆卡与双向答题。
   - **MCP (Model Context Protocol) 插件**：可直接接入 Cursor、Claude Desktop、WorkBuddy 等本地 AI 编程客户端。

---

## 📂 仓库目录结构

```
open-k12-english-kb/
├── data/
│   ├── grammar_topics.json       # 10大专题、64考点拓扑知识图谱
│   └── cards_samples.json        # 精选 64 考点速记口诀与易错避坑卡片
├── docs/
│   ├── 01_grammar_knowledge_graph.md   # 知识图谱与中考前置拓扑说明书
│   └── 02_omniedu_pedagogy_guide.md    # OmniEdu 启发式拆解规范手册
├── scripts/
│   ├── tutor_engine.py          # 启发式教学推理核心脚本（CLI + API 联动）
│   └── export_cards.py          # 导出 Markdown / Anki 格式卡片工具
├── k12_english_workbench.html   # 可视化交互式学习工作台 (单文件直接双击运行)
├── pyproject.toml               # Python 项目配置
└── README.md                    # 本文档
```

---

## 🚀 快速开始

### 方式一：直接在浏览器打开交互式工作台
打开 `k12_english_workbench.html` 即可使用，无需本地安装 Python 或 Node。

### 方式二：使用 CLI 启发式助教
```bash
# 诊断一道英语填空/改错
python3 scripts/tutor_engine.py plan \
  --question "I look forward to (hear) from you soon." \
  --attempt "孩子填了 hear，因为看到前面有个 to" \
  --grade "八年级"

# 拆解英语阅读长难句
python3 scripts/tutor_engine.py plan \
  --question "The scientist who won the Nobel Prize spent over thirty years conducting experiments in his laboratory." \
  --mode english_reading
```

---

## 📄 引用与致谢

- **OmniEdu 论文**：[arXiv:2609.23088](https://arxiv.org/abs/2609.23088) *OmniEdu: Open Foundation Models for Learning and Teaching*
- **官方开源代码**：[haolpku/Omni-Edu](https://github.com/haolpku/Omni-Edu)
