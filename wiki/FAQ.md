# FAQ

## 为什么打开 README 几乎看不到列表？

默认只展开开源权重表，避免 300+ 条铺满一屏。点「新闻 / 综述 / 论文 / 数据集」标题即可；条目多的栏里再点年份。

## 为什么 README 里找不到某篇按年份排的论文？

2023 年起按**类型**分栏：模型在「开源模型」及表下折叠，其余在论文栏的 Agent / 多模态 / RAG / 评测 / 其他。2022 及更早在「历史锚点」。项目页仍可按年份和标签搜。

## 为什么同一个模型在 HF 速查和开源表里都出现？

开源表来自 `type: resource` 的模型条目（含论文、机构、特色）。HF 速查来自 `type: model_hf`，用来列多尺寸 / GGUF。两者互补，不是两套清单。

## 新闻里的「某某医院大模型」为什么不在开源表？

没有核验过的可下载权重，不会标 `open-weights`，只出现在新闻或「论文/产品向」折叠区。

## 项目页和 README 哪个新？

同一份 `data/catalog.yml`。README 适合浏览，项目页适合筛选。Wiki 不另维护第二份条目。

## 如何启用 GitHub 上的 Wiki 标签页？

仓库 Settings → Features → Wikis。首次可建空白 Home，再按 [PUBLISH.md](https://github.com/tyang816/Awesome-TCM-LLM/blob/main/wiki/PUBLISH.md) 把 `wiki/` 推到 `*.wiki.git`。未打开前，用仓库内 `wiki/*.md` 即可预览。

## survey/ 目录是什么？

综述投稿工作区，不替代本清单。论文写完可以回流 catalog；不要把 catalog 倒灌进手稿当参考文献库。

## 我可以只提交英文或只提交中文吗？

可以先补中文 `summary_zh` 开 PR，但请尽量同时写 `i18n_en.yml`，否则英文 README 会缺摘要。
