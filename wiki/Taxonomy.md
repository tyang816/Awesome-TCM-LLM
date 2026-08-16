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

## 决定 resource 落点的顺序

1. `history` 或 `year < 2023`，且没有 `model` → **历史锚点**
2. 含 `model` + `general-medical` → **通用中文医疗模型**
3. 含 `model` → **中医专用模型**
4. 否则按第一个命中的方法标签：`agent` → `multimodal` → `rag`/`kg` → `benchmark`/`evaluation` → **其他方法**

一条只进一个论文子栏，避免同一项刷屏。模型不再重复出现在「论文与方法」里。

## 常用 tags

| 标签 | 含义 |
| --- | --- |
| `model` | 发布了领域模型（权重可有可无） |
| `open-weights` | 权重可下载（HF / 网盘等已核验） |
| `multimodal` | 舌/面/脉/影像等非纯文本 |
| `agent` | 多智能体或工具工作流 |
| `rag` / `kg` | 检索增强或知识图谱 |
| `benchmark` / `evaluation` | 基准或评估研究 |
| `dataset` / `sft` / `corpus` | 数据资产 |
| `general-medical` | 中文医疗但非中医主线 |
| `history` | LLM 之前的计算中医锚点 |
| `product` / `policy` | 产业或政策新闻 |
| `tool` | 平台、系统、可运行工具 |
| `ancient-books` / `herbal` | 古籍或本草专项 |

## dataset.section

| section | 栏名 |
| --- | --- |
| `公开资料整理` | 索引类列表 |
| `原始书籍 / 预训练语料` | 古籍与 CPT 语料 |
| `评测基准` | 可下载或可引用的 bench |
| `考试数据集` | 执业 / 考研等 |
| `指令/对话数据集` | SFT / 多轮问诊 |
| `知识图谱` | 实体关系数据 |
| `语料/指令` | 未归入上面的补充 |
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
