# Awesome-TCM-LLM Wiki

这份 Wiki 解释 **怎么读、怎么选、怎么贡献**。条目清单仍以仓库 [README](https://github.com/tyang816/Awesome-TCM-LLM) 为准，数据源是 [`data/catalog.yml`](https://github.com/tyang816/Awesome-TCM-LLM/blob/main/data/catalog.yml)。

## 仓库地图

```
想找模型 ──► README 开源模型表 / [[Models]]
想找数据 ──► README 数据集 / [[Datasets]]
想做评测 ──► [[Benchmarks]]
想入门    ──► [[Getting-Started]]
想投稿条  ──► [[Contributing]] + 仓库 CONTRIBUTING.md
想懂分类  ──► [[Taxonomy]]
卡住了    ──► [[FAQ]]
```

| 入口 | 适合 |
| --- | --- |
| [README](https://github.com/tyang816/Awesome-TCM-LLM/blob/main/README.md) | 两分钟带走 + 开源权重表，其余点标题打开 |
| [项目页](https://tyang816.github.io/zh/projects/tcm/) | 搜索、按标签筛选 |
| 本 Wiki | 选型、分类法、贡献约定 |
| [`survey/`](https://github.com/tyang816/Awesome-TCM-LLM/tree/main/survey) | 综述手稿工作区（不替代清单） |

## 专栏怎么划分

| 专栏 | 收什么 | 不收什么 |
| --- | --- | --- |
| 开源模型 | `type: resource` 且 `tags` 含 `model`，以及 HF 精选权重 | 纯方法论文、纯评测集 |
| 论文 | Agent / 多模态 / RAG·图谱 / 评测论文 / 其他 | 已进开源模型栏的条目 |
| 数据集 | `type: dataset` | HF 模型权重（回到开源模型栏） |
| 综述 | `type: survey` | 单点技术论文 |
| 新闻 | `type: news` | 论文发布（应写成 resource） |
| 历史锚点 | 2022 及更早，或 `history` | 2023 年后的 LLM 工作 |

更细的字段说明见 [[Taxonomy]]。

## 维护约定

1. **只改 catalog，不手改 README。** 运行 `python3 scripts/build_readme.py` 会同时刷新中英文 README、`data/catalog.json`，以及本 Wiki 的 Models / Datasets / Benchmarks。
2. 新增条目请补 `data/i18n_en.yml` 英文摘要。
3. 如何把 `wiki/` 推到 GitHub Wiki，见仓库内 [PUBLISH.md](https://github.com/tyang816/Awesome-TCM-LLM/blob/main/wiki/PUBLISH.md)。
