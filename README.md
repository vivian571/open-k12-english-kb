# Open K-12 English Knowledge Base (开源初中英语知识库)

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![GitHub Pages](https://img.shields.io/badge/GitHub_Pages-Online-emerald.svg)](https://vivian571.github.io/open-k12-english-kb/)
[![Curriculum: K-12 English](https://img.shields.io/badge/Curriculum-K--12_English-purple.svg)](https://github.com/vivian571/open-k12-english-kb)

本项目是一个面向初中阶段（中考体系）的结构化、可检索、可扩展的开源英语知识库。收录了**初中英语全量语法知识图谱（10 大核心专题、64 个必考考点与前置依赖树）**，以及**外研版（WY）七年级上册同步教材与学习资料索引**。

🌐 **在线可视化知识库网站**：[https://vivian571.github.io/open-k12-english-kb/](https://vivian571.github.io/open-k12-english-kb/)

---

## 📚 知识库核心内容

### 1. 中考英语全量语法知识图谱 (64 核心考点)
数据文件：[`data/grammar_topics.json`](data/grammar_topics.json)

覆盖初中英语 10 大核心语法专题，每个考点均严格标注了知识层级与前置学习依赖（Prerequisites）：
- **第 1 章 名词 (P6-P17)**：可数与不可数名词、规则/不规则复数、名词所有格
- **第 2 章 冠词 (P18-P23)**：不定冠词 a/an、定冠词 the 与零冠词规则
- **第 3 章 代词 (P24-P37)**：人称/物主/反身代词、不定代词与指示代词
- **第 4 章 数词 (P38-P43)**：基数词、序数词、分数/倍数及表达规范
- **第 5 章 介词 (P44-P57)**：时间介词、空间与方位介词、动词固定介词搭配
- **第 6 章 动词：情态与非谓语 (P58-P71)**：情态动词表推测、动名词 doing、不定式 to do、分词 done
- **第 7 章 形容词与副词 (P72-P81)**：比较级与最高级规则、特殊比较结构、程度与方式副词
- **第 8 章 动词时态与语态 (P82-P99)**：8 大核心时态（一般现在/过去/将来，现在/过去进行，现在完成时等）及被动语态
- **第 9 章 简单句与主谓一致 (P100-P111)**：五大基本句型、主谓一致三大原则（语法/意义/就近）
- **第 10 章 复合句体系 (P112-P127)**：宾语从句、状语从句、定语从句（关系代词与关系副词）

---

### 2. 同步教材与学习资料库（外研版 WY 七年级上册）
数据文件：[`data/textbooks_catalog.json`](data/textbooks_catalog.json)  
说明文档：[`docs/textbooks/wy_grade7_curriculum.md`](docs/textbooks/wy_grade7_curriculum.md)

收录模块：
- **Starter 预备级**：学生日常活动安排与开学准备对白
- **Unit: Family Ties**：温馨家庭瞬间分享、亲情主题精读与经典谚语
- **Unit: School Life**：埃玛图书馆交友记、写作俱乐部与经典电影双语阅读
- **同步辅导笔记**：启帆课同步学习笔记（句型转换、名词、数词与一般现在时）
- **词汇与短语专项**：
  - 汉译英核心词汇列表（30 页乱序默写版，防机械性疲劳）
  - 汉语核心词汇与日常对话搭配资料（30 页功能意念短语）

---

## 📂 仓库目录结构

```
open-k12-english-kb/
├── index.html                   # 在线交互式知识库工作台（GitHub Pages 自动托管）
├── README.md                    # 知识库体系说明
├── LICENSE                      # Apache-2.0 开源许可协议
├── .gitignore                   # 忽略配置
├── data/
│   ├── grammar_topics.json      # 10 大专题 64 个考点拓扑图谱
│   └── textbooks_catalog.json   # 外研版七年级上册教材与资料元数据
└── docs/
    ├── CONTRIBUTING.md          # 资料补充与更新贡献规范
    └── textbooks/
        └── wy_grade7_curriculum.md # 外研版七上教材详细分析
```

---

## 🌐 访问可视化交互工作台

项目已配置 GitHub Pages，支持直接通过浏览器打开：
👉 [https://vivian571.github.io/open-k12-english-kb/](https://vivian571.github.io/open-k12-english-kb/)

功能包括：
1. **64 核心考点快速搜索与拓扑树查看**。
2. **教材与资料模块详细目录与关联语法匹配**。
3. **长难句“抓主干·剥挂件”语法拆解展示**。

---

## 🤝 持续更新与贡献

若需补充新课本、新学期材料或专项题库，请查阅 [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md)。
欢迎提交 Issue 或 Pull Request 扩充知识库！
