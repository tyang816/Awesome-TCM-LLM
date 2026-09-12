# Taxonomy

分类只认 catalog 里的 `type` 和 `tags`。机构名误写进 `tags` 的，生成器会忽略，不当作语义标签。

## type

| type | README 去向 | 说明 |
| --- | --- | --- |
| `news` | 新闻 | 产品发布、备案、政策 |
| `resource` | 开源模型 **或** 论文 | 默认论文/系统；`tags` 含 `model` 则进开源模型栏 |
| `survey` | 综述 | 综述 / scoping review / 评论 |
| `dataset` | 数据集 | 用 `section` 再分栏 |
| `model_hf` | 开源模型 · HF 折叠 | 精选 Hugging Face 权重，可与 resource 模型互补 |
| `patent` | 专利 | 中医大模型、知识图谱问答、RAG 问诊等公开专利，不限中国；`venue` 写公开号 |

## 决定 resource 落点的顺序

1. `history` 或 `year < 2023`，且不是命名大模型（无 `model`，或带 `plm`）→ **历史锚点**
2. 含 `model`（且不含 `plm`）+ `east-asian-tm` → **日韩汉方 / 韩医**
3. 含 `model` + `product` → **闭源中文医疗产品**
4. 含 `model` + `general-medical` → **通用中文医疗模型**
5. 含 `model`（且不含 `plm`）→ **中医专用模型**（有核验权重进表，否则进论文/产品折叠）
6. 否则按第一个命中的方法标签：`agent` → `multimodal` → `rag`/`kg` → `prescription`/`herbal` → `extract`/`plm` → `benchmark`/`evaluation` → `tool` → **其他方法**

`model` 只给**发布了命名领域大模型**的条目（权重可有可无）。任务论文、BERT 编码器、平台工具不要标 `model`。一条只进一个论文子栏。模型不再重复出现在「论文」里。

## 常用 tags

| 标签 | 含义 |
| --- | --- |
| `model` | 发布了命名领域大模型（权重可有可无）；不要给方法论文或 BERT 编码器 |
| `plm` | BERT / 编码器时代的预训练模型，进「抽取 / 编码器」或历史锚点 |
| `extract` | 命名实体、关系、证据等抽取任务 |
| `open-weights` | 权重可下载（HF / 网盘等已核验） |
| `multimodal` | 舌/面/脉/影像等非纯文本 |
| `agent` | 多智能体或工具工作流 |
| `rag` / `kg` | 检索增强或知识图谱 |
| `benchmark` / `evaluation` | 基准或评估研究 |
| `dataset` / `sft` / `corpus` | 数据资产 |
| `general-medical` | 中文医疗但非中医主线 |
| `east-asian-tm` | 日韩汉方 / 韩医等东亚传统医学 |
| `history` | LLM 之前的计算中医锚点 |
| `product` / `policy` | 产业或政策新闻；模型条目加 `product` 进闭源产品栏 |
| `tool` | 平台、系统、可运行工具 |
| `patent` | 发明专利 / 发明公布 |
| `ancient-books` / `herbal` | 古籍或本草专项 |
| `dead-site` | 成果已发表，但官网不可达或已改作他用；README 标「官网已挂」，仍收论文/镜像 |
| `site-issue` | 官网还能打开，但检索/下载等核心功能不通；README 标「服务异常」 |

## dataset.section

| section | 栏名 |
| --- | --- |
| `公开资料整理` | 索引类列表 |
| `中药组方 / 提取物` | 方剂组成、中药提取物/成分–靶点等**公开库**（TCMSP / ETCM 等；不收制剂专利全集） |
| `临床结构化 / 处方` | 症状–证候–处方等结构化研究集（如 TCM-PD、TCM-Lung），不是门户数据库 |
| `通用中文医疗` | CMB / CMExam / Huatuo-26M / CMeKG / CBLUE 等常被中医实验当对照的开源中文医疗数据与评测（加 `general-medical`） |
| `东亚传统医学` | 汉方 / 韩医公开库与门户（加 `east-asian-tm`） |
| `原始书籍 / 预训练语料` | 古籍与 CPT 语料 |
| `评测基准` | 可下载或可引用的 bench |
| `考试数据集` | 执业 / 考研等 |
| `指令/对话数据集` | SFT / 多轮问诊 / 指令微调 |
| `知识图谱` | 实体关系数据 |
| `Hugging Face 开源模型（精选）` | **不再进数据集栏**，生成时并入开源模型折叠栏 |

## 新增条目时最少字段

```yaml
- id: example-model
  name: 示例 (Example)
  type: resource
  year: 2026
  summary_zh: 一句话说明它解决什么问题
  tags: [model, open-weights]
  links:
    论文: https://arxiv.org/abs/xxxx.xxxxx
    模型: https://huggingface.co/org/name
    代码: https://github.com/org/repo
  status: published
  verified_at: '2026-08-16'
```

英文摘要写到 `data/i18n_en.yml`，键为同一 `id`。完整流程见 [[Contributing]]。
