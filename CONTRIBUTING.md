# 贡献指南

感谢关注 [Awesome-TCM-LLM](https://github.com/tyang816/Awesome-TCM-LLM)！

## 如何添加资源

**单一数据源**：请修改 [`data/catalog.yml`](data/catalog.yml)，不要只改 `README.md`。

首次参与请安装依赖：

```bash
python3 -m pip install -r requirements.txt
```

1. 在 `data/catalog.yml` 的 `items` 中新增条目（参考已有字段）。
2. 本地生成并验证：

```bash
python3 scripts/build_readme.py
python3 scripts/validate_catalog.py
python3 scripts/check_links.py --workers 12 --timeout 20
```

会同时生成中文 [`README.md`](README.md) 与英文 [`README_EN.md`](README_EN.md)，文首可互相切换。英文摘要维护在 [`data/i18n_en.yml`](data/i18n_en.yml)（按条目 `id`），新增资源时请一并补上。

3. 提交 PR，包含 `catalog.yml`、`i18n_en.yml`、生成的 `catalog.json`、`README.md` 与 `README_EN.md`。

项目页 [tyang816.github.io/projects/tcm/](https://tyang816.github.io/projects/tcm/)（英文）与 [zh/projects/tcm](https://tyang816.github.io/zh/projects/tcm/)（中文）读取 `data/catalog.json`，无需单独维护第二份列表。作者站点：[中文主页](https://tyang816.github.io/zh/) · [English](https://tyang816.github.io/)。

## 条目字段

| 字段 | 说明 |
|------|------|
| `id` | 稳定唯一 ID（kebab-case） |
| `name` | 显示名 |
| `type` | `news` / `resource` / `survey` / `dataset` / `model_hf` |
| `year` | 年份 |
| `summary_zh` | 一句话中文摘要 |
| `links` | 论文/代码/模型/数据集等 URL |
| `tags` | 如 `multimodal`, `benchmark`, `open-weights`, `agent`, `general-medical` |
| `verified_at` | 链接核验日期 `YYYY-MM-DD` |
| `status` | 默认 `published` |
| `doi` | 可选 DOI 标识；当 DOI 跳转尚未注册时，可保留 DOI 并把期刊页面放在 `links` |

通用医疗（非中医主线）请加标签 `general-medical`；门户默认可隐藏此类条目。

## 收录范围与开放状态

- 主线范围：中医药大模型、智能体、评测、数据集、知识图谱以及直接相关的方法研究。
- 邻近范围：对中医大模型有明确方法学参考价值的中文医疗或历史研究；须说明关联，并使用 `general-medical` 或 `history` 标签。
- 不收录：无法追溯来源、只有营销描述、与中医或中文医疗无明确关系的条目。
- “论文公开”“代码开源”“开放权重”“数据开放”须分别以 `论文`、`代码`、`模型`、`数据集` 链接表示，不能仅凭论文或产品页面称为完整开源。
- 新闻中的“首个”“最佳”“准确率”等主张应忠实归因于原始来源，避免改写为仓库自身结论。

## 链接要求

- 优先 DOI / 官方仓库 / Hugging Face 规范 URL。
- `published` 条目必须至少提供一个可访问、可追溯的来源链接；否则使用 `draft`。
- 提交前运行 `python3 scripts/check_links.py --workers 12 --timeout 20`。
- 标题与链接内容须对齐（避免挂错论文）。

## 英文版本

- 每个发布条目都必须在 `data/i18n_en.yml` 中存在对应 ID。
- 至少提供 `summary_en`；纯中文名称或期刊名建议同时提供 `name_en`、`title_en` 或 `venue_en`。
- 中医专名可以保留中文，但应附英文、拼音或通行译名，避免英文 README 出现无法理解的整段中文。

## 派生文件与历史脚本

`README.md`、`README_EN.md` 和 `data/catalog.json` 均由 `scripts/build_readme.py` 生成，请勿手工修改。`scripts/seed_catalog.py` 仅保留为历史种子生成器，默认写入 `data/catalog.seed.yml`，不用于日常维护。

## 医疗安全

本目录仅用于研究和信息索引，不构成医疗建议，也不表示维护者认可条目的有效性、安全性或临床适用性。涉及诊断、处方或治疗的项目，应由合格专业人员独立评估。

## Issue

也可用 [Issue 模板](https://github.com/tyang816/Awesome-TCM-LLM/issues/new/choose) 建议新资源，维护者会核验后写入 catalog。
