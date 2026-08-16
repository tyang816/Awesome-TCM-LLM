# Getting Started

README 首屏「两分钟带走」是结论；本页把理由写全。

## 1. 先确认任务

| 你的任务 | 下一步 |
| --- | --- |
| 本地跑一个中医问答 / 辨证模型 | [[Models]] → 开源权重表，优先有 **代码 + 权重 + 数据** 三件套的 |
| 做舌诊、面诊、多模态 | 模型标签含 `multimodal`；数据看 TCM-Ladder、舌象集、ZhongJing-OMNI |
| 搭问诊 / 处方 Agent | README「智能体」栏 + GraphRAG 系统，不要只 fine-tune 一个 7B |
| 报数字、做对比实验 | [[Benchmarks]]，先分清「考试回忆」和「辨证/临床」 |
| 写相关工作 / 开题 | README 综述栏（近两年打开，更早折叠） |
| 继续预训练 | 数据集「原始书籍 / 预训练语料」 |

## 2. 开源权重怎么挑（经验规则）

1. **能复现再谈效果。** 只有新闻稿、没有权重的条目在开源模型表下方的折叠区，不适合当实验底座。
2. **看配套数据是否公开。** ChatTCM、ShizhenGPT、神农、白泽、TCMChat 这类「模型+语料」组合，后续微调成本更低。
3. **参数量先对齐硬件。** 7B–14B 适合单卡试验；32B / Omni 先确认推理栈（vLLM / GGUF）。
4. **中医专用 ≠ 一定更强。** 通用中文医疗模型（华佗、孙思邈等）常被用作对照，不要漏掉。
5. **同名可能不同源。** 例如「仲景」存在 ZhongJingGPT 与 AAAI CMtMedQA 两条线，以 catalog 的 `id` 和作者机构为准。

## 3. 推荐阅读顺序

1. 一篇 2025–2026 的 scoping review（README 综述栏前几条）
2. 一个开源模型的论文 + 其评测协议（Qibo / BianCang / ShizhenGPT / 仲景 任选）
3. 一个基准的任务定义（TCM-Ladder 或 LingLan / MTCMB）
4. 再回到项目页用标签扫 `agent` / `rag` / `multimodal`

## 4. 不建议一上来就做的事

- 把「新闻里的医院大模型」当成可复现基线
- 只用执业考试准确率论证临床能力
- 在 README 里手改一条（下次生成会被覆盖）

接下来：[[Models]] · [[Datasets]] · [[Contributing]]
