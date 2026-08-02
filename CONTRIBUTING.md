# 贡献指南

感谢关注 [Awesome-TCM-LLM](https://github.com/tyang816/Awesome-TCM-LLM)！

## 如何添加资源

**单一数据源**：请修改 [`data/catalog.yml`](data/catalog.yml)，不要只改 `README.md`。

1. 在 `data/catalog.yml` 的 `items` 中新增条目（参考已有字段）。
2. 本地运行：

```bash
python3 scripts/build_readme.py
```

3. 提交 PR，包含 `catalog.yml`、生成的 `catalog.json` 与 `README.md`。

项目页 [tyang816.github.io/projects/tcm/](https://tyang816.github.io/projects/tcm/)（英文）与 [zh/projects/tcm](https://tyang816.github.io/zh/projects/tcm/)（中文）读取 `data/catalog.json`，无需单独维护第二份列表。作者站点：[中文主页](https://tyang816.github.io/zh/) · [English](https://tyang816.github.io/)。

## 条目字段

| 字段 | 说明 |
|------|------|
| `id` | 稳定唯一 ID（kebab-case） |
| `name` | 显示名 |
| `type` | `news` / `resource` / `dataset` / `model_hf` |
| `year` | 年份 |
| `summary_zh` | 一句话中文摘要 |
| `links` | 论文/代码/模型/数据集等 URL |
| `tags` | 如 `multimodal`, `benchmark`, `open-weights`, `agent`, `general-medical` |
| `verified_at` | 链接核验日期 `YYYY-MM-DD` |
| `status` | 默认 `published` |

通用医疗（非中医主线）请加标签 `general-medical`；门户默认可隐藏此类条目。

## 链接要求

- 优先 DOI / 官方仓库 / Hugging Face 规范 URL。
- 提交前可用 `python3 scripts/check_links.py` 抽检。
- 标题与链接内容须对齐（避免挂错论文）。

## Issue

也可用 [Issue 模板](https://github.com/tyang816/Awesome-TCM-LLM/issues/new/choose) 建议新资源，维护者会核验后写入 catalog。
