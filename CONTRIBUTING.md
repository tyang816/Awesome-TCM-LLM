# 贡献指南

感谢关注 [Awesome-TCM-LLM](https://github.com/tyang816/Awesome-TCM-LLM)！

## 如何添加资源

**单一数据源**：请修改 [`data/catalog.yml`](data/catalog.yml)，不要只改 `README.md`。

1. 在 `data/catalog.yml` 的 `items` 中新增条目（参考已有字段）。
2. 本地运行：

```bash
python3 scripts/build_readme.py
```

会同时生成：

- 中文 [`README.md`](README.md) 与英文 [`README_EN.md`](README_EN.md)（默认只展开开源模型表，其余栏目折叠）
- [`data/catalog.json`](data/catalog.json)（项目页用）
- Wiki 生成页 [`wiki/Models.md`](wiki/Models.md)、[`wiki/Datasets.md`](wiki/Datasets.md)、[`wiki/Benchmarks.md`](wiki/Benchmarks.md)

英文摘要维护在 [`data/i18n_en.yml`](data/i18n_en.yml)（按条目 `id`），新增资源时请一并补上。**不要手改 README**，下次生成会被覆盖。

3. 提交 PR，包含 `catalog.yml`、`i18n_en.yml`、生成的 `catalog.json`、`README.md`、`README_EN.md`，以及有变动的 `wiki/*.md`。

Wiki 手写页（导航、选型、分类法）在 [`wiki/`](wiki/)；如何发布到 GitHub Wiki 见 [`wiki/PUBLISH.md`](wiki/PUBLISH.md)。

项目页 [tyang816.github.io/projects/tcm/](https://tyang816.github.io/projects/tcm/)（英文）与 [zh/projects/tcm](https://tyang816.github.io/zh/projects/tcm/)（中文）读取 `data/catalog.json`，无需单独维护第二份列表。作者站点：[中文主页](https://tyang816.github.io/zh/) · [English](https://tyang816.github.io/)。

## 条目字段

| 字段 | 说明 |
|------|------|
| `id` | 稳定唯一 ID（kebab-case） |
| `name` | 显示名 |
| `type` | `news` / `resource` / `survey` / `dataset` / `model_hf` / `patent`。`resource` 若带 `model` 标签会进入 README **开源模型**（有权重进表，否则进折叠栏），否则按 `agent` / `multimodal` / `rag`/`kg` / `benchmark` 分到「论文」。`patent` 进入 README **专利**（收中医大模型 / 知识图谱 / RAG / 智能问诊与处方推荐等系统专利，不限中国；不收中药组方制剂全集） |
| `year` | 年份 |
| `summary_zh` | 一句话中文摘要 |
| `links` | 论文/代码/模型/数据集等 URL |
| `section` | 数据集分栏。组方/提取物公开库用 `中药组方 / 提取物`；CMB / Huatuo-26M / CMExam 等通用中文医疗数据用 `通用中文医疗`；汉方/韩医公开库用 `东亚传统医学`，都不要和中医大模型语料混栏 |
| `tags` | 如 `multimodal`, `benchmark`, `open-weights`, `agent`, `general-medical`, `product`, `east-asian-tm`。官网不可达加 `dead-site`（标「官网已挂」）；门户在但核心功能不通加 `site-issue`（标「服务异常」）。有问题也要收、也要标 |
| `verified_at` | 链接核验日期 `YYYY-MM-DD` |
| `status` | 默认 `published` |

通用医疗（非中医主线）请加标签 `general-medical`；闭源产品加 `product`（不要标 `open-weights`）；汉方/韩医加 `east-asian-tm`。门户默认可隐藏 `general-medical`。

## 链接要求

- 优先 DOI / 官方仓库 / Hugging Face 规范 URL。官网挂了仍应收：`tags` 加 `dead-site`，历史入口用 `原网站`；门户在但核心功能不通加 `site-issue`。核验链用论文 / DOI / 镜像。专利用 Google Patents（CN / US / EP / WO / JP / KR 等），`venue` 写公开号（授权件优先 `…B`）。全球补漏可用 `python3 scripts/search_patents_bq.py`（需 `gcloud auth login`，查 `patents-public-data`）。
- 提交前可用 `python3 scripts/check_links.py` 抽检。
- 标题与链接内容须对齐（避免挂错论文）。

## Issue

也可用 [Issue 模板](https://github.com/tyang816/Awesome-TCM-LLM/issues/new/choose) 建议新资源，维护者会核验后写入 catalog。
