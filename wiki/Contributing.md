# Contributing

仓库根目录的 [CONTRIBUTING.md](https://github.com/tyang816/Awesome-TCM-LLM/blob/main/CONTRIBUTING.md) 是规范正文。本页只补「改完目录之后 README / Wiki 会怎样」。

## 工作流

1. 在 `data/catalog.yml` 追加或修改条目。
2. 在 `data/i18n_en.yml` 补 `summary_en`（及需要时的 `name_en` / `orgs_en`）。
3. 运行：

```bash
python3 scripts/build_readme.py
```

4. 提交：`catalog.yml`、`i18n_en.yml`、`catalog.json`、`README.md`、`README_EN.md`，以及若有变更的 `wiki/Models.md`、`wiki/Datasets.md`、`wiki/Benchmarks.md`。

不要只改 README。生成脚本会按 [[Taxonomy]] 重排专栏和折叠块。

## 写一条好摘要

- 一句话说清 **任务 + 方法 + 是否开源**。
- 模型写清底座或参数量（若论文给出）。
- 同名工作在摘要里点出差异（机构 / 数据 / 会议）。
- 链接优先 DOI、官方仓库、Hugging Face 规范 URL。

## 标签尽量少而准

模型：`model`，有权重再加 `open-weights`。  
方法：`agent` / `rag` / `kg` / `multimodal` 选最能代表主贡献的。  
评测：数据集用 `type: dataset` + `section: 评测基准`；论文用 `resource` + `benchmark` 或 `evaluation`。

## Issue 与 PR

- 只知道一篇论文、不确定字段：开 Issue，维护者代写入 catalog。
- 已经写好 YAML：直接 PR，并附生成后的 diff。

同步 GitHub Wiki 的步骤见 [PUBLISH.md](https://github.com/tyang816/Awesome-TCM-LLM/blob/main/wiki/PUBLISH.md)。
