# 2026-11-10 news / papers / surveys gap-fill

- Date (Asia/Shanghai): 2026-11-10
- Tree: `/home/tanyang/TCM-LM-Web/Awesome-TCM-LLM`
- `verified_at`: 2026-11-10
- No git commit or push; existing uncommitted work left in place.

## Named items the user asked for

### 1) 李强签署国务院令公布《中医药传统知识保护条例》

- Status: **newly added** (not previously in the catalog).
- id: `news-202611-tcm-tk-ordinance`
- date: 2026.11.09
- Primary pages opened:
  - Xinhua: https://www.news.cn/politics/leaders/20261109/115bf875b154445787539419282ce542/c.html (2026-11-09 17:01:52, 新华社北京11月9日电)
  - gov.cn news: https://www.gov.cn/yaowen/liebiao/202611/content_7085599.htm (2026-11-09 17:06, 来源新华社)
  - Official text: https://www.gov.cn/zhengce/zhengceku/202611/content_7085592.htm (国令第850号; 成文 2026-10-23; 发布 2026-11-09; 国务院第97次常务会议 2026-09-18 通过; 施行 2027-01-01; 共32条)

### 2) 2026 Artificial Intelligence Review (AIR) TCM survey

- Status: **already present**; not re-added.
- Existing id: `surv-wu2026`
- Title: Artificial intelligence in Traditional Chinese Medicine herbs: a survey
- Authors: Jinrun Wu, Qiang He, Dong Yang, Yuliang Cai, Jiawei Zhang, Xi Lu, Hua Zhu
- Venue: Artificial Intelligence Review (2026) 59:120
- DOI: https://doi.org/10.1007/s10462-026-11513-w
- Publisher page reports publication on 21 February 2026.

## Additional verified additions

| id | type | year | key URL |
| --- | --- | --- | --- |
| news-202609-classic-industries-opinion | news | 2026 | https://www.miit.gov.cn/jgsj/xfpgys/wjfb/art/2026/art_ece6902ba0b24ad2806e670618f17a9f.html |
| news-202610-shuxiaohe | news | 2026 | https://www.ncsti.gov.cn/kjdt/xwjj/202610/t20261027_259363.html |
| news-202407-digital-tcm-opinion | news | 2024 | http://www.natcm.gov.cn/bangongshi/zhengcewenjian/2024-08-14/34672.html |
| news-202607-digital-tcm-forum | news | 2026 | https://wjw.beijing.gov.cn/xwzx_20031/mtjj/202607/t20260706_4748255.html |
| surv-wang2026-tcm-rd-ai | survey | 2026 | https://doi.org/10.1186/s13020-025-01288-7 |
| graphrag-tcm | resource | 2026 | https://doi.org/10.1145/3820664.3820702 |
| graphrag-or-ft-tcm | resource | 2026 | https://doi.org/10.1007/978-981-92-3495-0_22 |
| tcm-sea | resource | 2026 | https://arxiv.org/abs/2610.40663 |

Notes:

- MIIT official notice (成文 2026-08-28, 发布 2026-09-07) was opened; the full opinion text, including the Chinese-materia-medica listing and the AI / 大模型 / 智慧药房 / 知识图谱 clauses, was read on the Xinhua full-text page sourced from 工信微报.
- GraphRAG-TCM ACM HTML timed out on repeated fetches; title, authors (Xian-Fang Wang, Hao Ren, Xiao-Lei Wang, Zi-Rui Han, Pei-Wu Qin), venue (ISBCB 2026), and DOI were verified via the Crossref works API. Author-reported F1 / hallucination figures from secondary snippets were not copied into the catalog.
- GraphRAG-or-Fine-Tuning Springer HTML returned 403; title, authors (Yu Tong, Zhihan Lin, Chuipu Cai), ICIC 2026 / LNCS, first-online 15 July 2026, and DOI were verified via Crossref. KG size and QA-set counts from secondary snippets were not copied.
- TCM-SEA / TCM-MisDx was opened on arXiv. No separate dataset entry: the paper does not provide an independent public download URL.
- 2024 digital-TCM opinion is older than the 2025–2026 window but is a major SATCM + National Data Administration policy that was missing and explicitly mentions TCM large models.

## Already in catalog (not re-added)

- `surv-wu2026` (AIR 2026 herbs survey)
- `news-202611-data-elements-tcm` (厉将斌 / 数据要素大赛访谈; NDA or other reprints of the same story)
- `news-202611-ai-tcm-data-meeting` (广安门 10-30 会议; later 市中医药局稿 is the same event)
- `news-202611-traditional-medicine-ai-report`, `news-202610-wtmc-exhibits` (世界传统医药大会 AI 报告与已列展品)
- `tcm-clinical-reason` / `ds-tcm-clinical-reason` (arXiv 2610.04215)
- `large-language-models` (arXiv 2609.17544, LLMs vs physicians)
- `dongyuan` (arXiv 2603.28191)
- Related Chinese Medicine review `surv-guop2026` (DOI 10.1186/s13020-025-01194-y), distinct from the newly added 01288-7 R&D review

## Notable items found but not added

- ICLR 2026 bilingual acupuncture QA on OpenReview: desk-rejected, not a published item.
- NATCM reprint of a 2026-03-09 Xinhua interview with 肖伟 on a 中药工业智能大模型: interview comments, not a formal policy instrument or product launch.
- Fujian provincial digital-TCM media feature, Zhengzhou proposal reply, and a Nanjing base-opening notice: local or secondary; not added without a fully opened primary page in this pass.
- WST / 李花 review: SciEngine body was unusable, so metadata was not invented.
- US20260051402A1 / JP7911908B2 and similar DL-only patents, and unreleased Fu-bianzheng internal benches: out of this news/papers/surveys pass or already rejected earlier.
- Commercial corpora without a citable official release page.

## Counts

The append script writes before/after counts below after a successful write.

### Before

- all: 1381
- news: 72
- papers_nomodel: 390
- surveys: 76
- resource: 496

### After

- all: 1390
- news: 77
- papers_nomodel: 393
- surveys: 77
- resource: 499

Added ids: news-202611-tcm-tk-ordinance, news-202609-classic-industries-opinion, news-202610-shuxiaohe, news-202407-digital-tcm-opinion, news-202607-digital-tcm-forum, surv-wang2026-tcm-rd-ai, graphrag-tcm, graphrag-or-ft-tcm, tcm-sea
