#!/usr/bin/env python3
"""Build README.md, README_EN.md, wiki catalog pages, and data/catalog.json."""

from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from pathlib import Path

try:
    import yaml
except ImportError:
    print("Please install PyYAML: pip install pyyaml", file=sys.stderr)
    sys.exit(1)

ROOT = Path(__file__).resolve().parents[1]
CATALOG_YML = ROOT / "data" / "catalog.yml"
CATALOG_JSON = ROOT / "data" / "catalog.json"
I18N_EN_YML = ROOT / "data" / "i18n_en.yml"
README_ZH = ROOT / "README.md"
README_EN = ROOT / "README_EN.md"
WIKI_DIR = ROOT / "wiki"

SITE_ZH = "https://tyang816.github.io/zh/"
SITE_EN = "https://tyang816.github.io/"
DEFAULT_PORTAL = "https://tyang816.github.io/projects/tcm/"
PORTAL_ZH = "https://tyang816.github.io/zh/projects/tcm/"
WIKI_HOME = "https://github.com/tyang816/Awesome-TCM-LLM/wiki"

DATASET_SECTION_ORDER_ZH = [
    "公开资料整理",
    "原始书籍 / 预训练语料",
    "评测基准",
    "考试数据集",
    "指令/对话数据集",
    "知识图谱",
    "语料/指令",
]

HF_SECTION = "Hugging Face 开源模型（精选）"

SECTION_EN = {
    "公开资料整理": "Curated lists",
    "原始书籍 / 预训练语料": "Books / pretraining corpora",
    "评测基准": "Benchmarks",
    "考试数据集": "Exam datasets",
    "指令/对话数据集": "Instruction / dialogue datasets",
    "知识图谱": "Knowledge graphs",
    "Hugging Face 开源模型（精选）": "Hugging Face models (selected)",
    "语料/指令": "Corpora / instructions",
    "其他": "Other",
}

LINK_LABEL_EN = {
    "论文": "Paper",
    "代码": "Code",
    "灵丹代码": "Lingdan code",
    "模型": "Model",
    "数据集": "Dataset",
    "链接": "Link",
    "DOI": "DOI",
    "预训练数据": "Pretrain data",
    "SFT数据": "SFT data",
    "指令数据": "Instruction data",
    "网站": "Website",
    "新闻": "News",
    "数据": "Data",
    "资料": "Resources",
    "榜单": "Leaderboard",
    "平台": "Platform",
    "相关 MedCare": "Related MedCare",
    "GGUF": "GGUF",
    "JMIR": "JMIR",
    "ScienceDirect": "ScienceDirect",
    "正式发表": "Published",
    "arXiv": "arXiv",
    "预印本": "Preprint",
}

SEMANTIC_TAGS = {
    "model",
    "open-weights",
    "multimodal",
    "agent",
    "rag",
    "kg",
    "benchmark",
    "evaluation",
    "dataset",
    "sft",
    "corpus",
    "general-medical",
    "history",
    "product",
    "policy",
    "tool",
    "ancient-books",
    "herbal",
    "survey",
    "reasoning",
    "prescription",
}

# First match wins for non-model leftover papers.
PAPER_CATEGORY_RULES = [
    ("eval", lambda tags: "benchmark" in tags or "evaluation" in tags),
    ("agent", lambda tags: "agent" in tags),
    ("multimodal", lambda tags: "multimodal" in tags),
    ("rag_kg", lambda tags: "rag" in tags or "kg" in tags),
]

PAPER_LINK_KEYS = ("论文", "DOI", "正式发表", "arXiv", "Paper", "Published")
CODE_LINK_KEYS = ("代码", "Code", "灵丹代码")
WEIGHT_LINK_KEYS = ("模型", "Model", "GGUF")

# Lists longer than this nest by year inside a section fold.
FLAT_LIMIT = 12


def strip_md_bold(text: str) -> str:
    return re.sub(r"\*\*([^*]+)\*\*", r"\1", text or "")


def load_i18n_en() -> dict:
    if not I18N_EN_YML.exists():
        return {}
    data = yaml.safe_load(I18N_EN_YML.read_text(encoding="utf-8")) or {}
    return data if isinstance(data, dict) else {}


def apply_i18n(entry: dict, i18n: dict) -> dict:
    """Return a shallow copy with English fields filled from data/i18n_en.yml."""
    out = dict(entry)
    patch = i18n.get(entry.get("id")) or {}
    if isinstance(patch, str):
        patch = {"summary_en": patch}
    for key in ("summary_en", "title_en", "name_en"):
        if patch.get(key) and not out.get(key):
            out[key] = patch[key]
    if patch.get("orgs_en"):
        out["orgs"] = list(patch["orgs_en"])
    return out


def published(items: list[dict]) -> list[dict]:
    return [i for i in items if i.get("status", "published") == "published"]


def tags_of(entry: dict) -> set[str]:
    return {t for t in (entry.get("tags") or []) if isinstance(t, str)}


def year_of(entry: dict) -> int:
    try:
        return int(entry.get("year") or 0)
    except (TypeError, ValueError):
        return 0


def link_md(label: str, url: str) -> str:
    return f"[[{label}]({url})]"


def format_links(links: dict | None, lang: str = "zh") -> str:
    if not links:
        return ""
    parts = []
    for key, url in links.items():
        if not url:
            continue
        if lang == "en":
            label = LINK_LABEL_EN.get(key, key)
            if re.search(r"[\u4e00-\u9fff]", label):
                label = re.sub(r"[\u4e00-\u9fff]+", "", label).strip() or "Link"
        else:
            label = key
        parts.append(link_md(label, url))
    return (" " + " ".join(parts)) if parts else ""


def entry_blurb(entry: dict, lang: str) -> str:
    if lang == "en":
        return entry.get("summary_en") or entry.get("title_en") or ""
    return entry.get("summary_zh") or entry.get("title_zh") or entry.get("name", "")


def display_name(entry: dict, lang: str) -> str:
    if lang == "en":
        return entry.get("name_en") or entry.get("title_en") or entry.get("name", "")
    return entry.get("title_zh") or entry.get("name", "")


def format_resource_line(entry: dict, lang: str) -> str:
    bits = ["-"]
    if entry.get("venue"):
        bits.append(f"[*{entry['venue']}*]")
    bits.append(f"**{display_name(entry, lang)}**")
    blurb = entry_blurb(entry, lang)
    if blurb:
        bits.append(blurb)
    orgs = entry.get("orgs") or []
    if lang == "en":
        orgs = [o for o in orgs if not re.search(r"[\u4e00-\u9fff]", o)]
    if orgs:
        sep = ", " if lang == "en" else "，"
        bits.append(f"[{sep.join(orgs)}]")
    return " ".join(bits) + format_links(entry.get("links"), lang)


def format_news_line(entry: dict, lang: str) -> str:
    date = entry.get("date") or str(entry.get("year", ""))
    if lang == "en":
        text = entry.get("summary_en") or entry.get("name") or ""
    else:
        text = entry.get("summary_zh", "")
    line = f"- [{date}] {text}"
    links = entry.get("links") or {}
    if lang == "zh" and links.get("链接"):
        line += f" {link_md('链接', links['链接'])}"
    elif lang == "en" and (links.get("链接") or links.get("Link")):
        url = links.get("Link") or links.get("链接")
        line += f" {link_md('Link', url)}"
    else:
        line += format_links(links, lang)
    return line


def format_dataset_line(entry: dict, lang: str) -> str:
    title = display_name(entry, lang)
    return f"- {title}{format_links(entry.get('links'), lang)}"


def lang_switcher(lang: str) -> str:
    if lang == "zh":
        return "**语言 / Language:** [中文](README.md) | [English](README_EN.md)"
    return "**Language / 语言:** [English](README_EN.md) | [中文](README.md)"


def badges() -> str:
    return (
        "![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-green)  "
        "[![Awesome](https://awesome.re/badge.svg)](https://awesome.re) "
        "![Stars](https://img.shields.io/github/stars/tyang816/Awesome-TCM-LLM?color=yellow)  "
        "![Forks](https://img.shields.io/github/forks/tyang816/Awesome-TCM-LLM?color=blue&label=Fork)"
    )


def details_block(summary: str, body_lines: list[str], open_: bool = False) -> list[str]:
    if not body_lines:
        return []
    attr = " open" if open_ else ""
    return [
        f"<details{attr}>",
        f"<summary>{summary}</summary>",
        "",
        *body_lines,
        "",
        "</details>",
        "",
    ]


def group_by_year(entries: list[dict]) -> dict[int, list[dict]]:
    by_year: dict[int, list[dict]] = defaultdict(list)
    for entry in entries:
        year = year_of(entry)
        if year:
            by_year[year].append(entry)
    return by_year


def emit_year_groups(entries: list[dict], lang: str, line_fn) -> list[str]:
    """Always fold by year so opening a section never dumps a wall of text."""
    lines: list[str] = []
    by_year = group_by_year(entries)
    for year in sorted(by_year.keys(), reverse=True):
        items = by_year[year]
        label = f"{year} · {len(items)}"
        lines += details_block(label, [line_fn(i, lang) for i in items])
    return lines


def emit_list(entries: list[dict], lang: str, line_fn) -> list[str]:
    if len(entries) <= FLAT_LIMIT:
        return [line_fn(i, lang) for i in entries]
    return emit_year_groups(entries, lang, line_fn)


def decade_bucket(year: int) -> str:
    if year >= 2020:
        return "2020–2022"
    if year >= 2010:
        return "2010s"
    if year >= 2000:
        return "2000s"
    return "1970s–1990s"


def emit_decades(entries: list[dict], lang: str, line_fn) -> list[str]:
    by_decade: dict[str, list[dict]] = defaultdict(list)
    order = ["2020–2022", "2010s", "2000s", "1970s–1990s"]
    for entry in entries:
        by_decade[decade_bucket(year_of(entry))].append(entry)
    lines: list[str] = []
    for label in order:
        items = by_decade.get(label) or []
        if not items:
            continue
        lines += details_block(f"{label} · {len(items)}", [line_fn(i, lang) for i in items])
    return lines


def fold(summary: str, body_lines: list[str]) -> list[str]:
    return details_block(summary, body_lines)


def bold_teaser(entries: list[dict], n: int = 3) -> str:
    names = []
    for entry in entries[:n]:
        text = " ".join(
            x
            for x in (
                entry.get("summary_zh"),
                entry.get("summary_en"),
                entry.get("name"),
            )
            if x
        )
        match = re.search(r"\*\*([^*]+)\*\*", text)
        names.append(match.group(1) if match else (entry.get("name") or "")[:20])
    return " · ".join(n for n in names if n)


def first_link(links: dict, keys: tuple[str, ...]) -> str | None:
    for key in keys:
        if links.get(key):
            return links[key]
    return None


def weight_url(entry: dict) -> str | None:
    links = entry.get("links") or {}
    for url in links.values():
        if url and "huggingface.co/" in url and "/datasets/" not in url:
            return url
    return first_link(links, WEIGHT_LINK_KEYS)


def is_open_weights(entry: dict) -> bool:
    return weight_url(entry) is not None


def hf_urls(entry: dict) -> set[str]:
    urls = set()
    for url in (entry.get("links") or {}).values():
        if url and "huggingface.co/" in url:
            urls.add(url.rstrip("/").lower())
    return urls


def first_org(entry: dict, lang: str) -> str:
    orgs = entry.get("orgs") or []
    if lang == "en":
        orgs = [o for o in orgs if not re.search(r"[\u4e00-\u9fff]", o)]
    if not orgs:
        return "—"
    text = orgs[0]
    if "，" in text:
        text = text.split("，", 1)[0]
    if "," in text:
        text = text.split(",", 1)[0]
    return text.strip() or "—"


def focus_labels(entry: dict, lang: str) -> str:
    tags = tags_of(entry)
    mapping = [
        ("multimodal", "多模态", "MM"),
        ("agent", "Agent", "Agent"),
        ("rag", "RAG", "RAG"),
        ("kg", "图谱", "KG"),
        ("benchmark", "评测", "Bench"),
    ]
    labels = []
    for tag, zh, en in mapping:
        if tag in tags:
            labels.append(zh if lang == "zh" else en)
    return " · ".join(labels) if labels else "—"


def compact_model_links(entry: dict, lang: str) -> str:
    links = entry.get("links") or {}
    paper = first_link(links, PAPER_LINK_KEYS)
    weight = weight_url(entry)
    code = first_link(links, CODE_LINK_KEYS)
    data = first_link(links, ("数据集", "数据", "Dataset", "Data"))
    labels = {
        "zh": ("论文", "权重", "代码", "数据"),
        "en": ("Paper", "Weights", "Code", "Data"),
    }[lang]
    parts = []
    for url, label in ((paper, labels[0]), (weight, labels[1]), (code, labels[2]), (data, labels[3])):
        if url:
            parts.append(f"[{label}]({url})")
    return " · ".join(parts) if parts else "—"


def classify_items(items: list[dict]) -> dict[str, list[dict]]:
    buckets: dict[str, list[dict]] = defaultdict(list)
    for entry in published(items):
        kind = entry.get("type")
        tags = tags_of(entry)
        year = year_of(entry)
        if kind == "news":
            buckets["news"].append(entry)
        elif kind == "survey":
            buckets["survey"].append(entry)
        elif kind == "dataset":
            buckets["dataset"].append(entry)
        elif kind == "model_hf":
            buckets["model_hf"].append(entry)
        elif kind == "resource":
            historical = "history" in tags or year < 2023
            if historical:
                buckets["history"].append(entry)
            elif "model" in tags:
                if "general-medical" in tags:
                    buckets["model_general"].append(entry)
                else:
                    buckets["model_tcm"].append(entry)
            else:
                placed = False
                for name, pred in PAPER_CATEGORY_RULES:
                    if pred(tags):
                        buckets[name].append(entry)
                        placed = True
                        break
                if not placed:
                    buckets["method"].append(entry)
    for key in buckets:
        buckets[key].sort(key=lambda x: (year_of(x), x.get("date") or "", x.get("name") or ""), reverse=True)
    return buckets


def count_pack(buckets: dict[str, list[dict]]) -> dict[str, int]:
    return {
        "news": len(buckets["news"]),
        "models": len(buckets["model_tcm"]) + len(buckets["model_general"]) + len(buckets["model_hf"]),
        "surveys": len(buckets["survey"]),
        "datasets": len(buckets["dataset"]),
        "papers": sum(len(buckets[k]) for k in ("agent", "multimodal", "rag_kg", "eval", "method", "history")),
        "open": sum(1 for e in buckets["model_tcm"] if is_open_weights(e)),
    }


def catalog_index(buckets: dict[str, list[dict]]) -> dict[str, dict]:
    out: dict[str, dict] = {}
    for items in buckets.values():
        for entry in items:
            if entry.get("id"):
                out[entry["id"]] = entry
    return out


def takeaway_link(entry: dict | None, lang: str) -> str:
    if not entry:
        return "—"
    name = display_name(entry, lang)
    url = weight_url(entry) or first_link(entry.get("links") or {}, PAPER_LINK_KEYS + CODE_LINK_KEYS)
    return f"**[{name}]({url})**" if url else f"**{name}**"


def takeaway_block(buckets: dict[str, list[dict]], lang: str) -> list[str]:
    idx = catalog_index(buckets)
    n_open = count_pack(buckets)["open"]
    biancang = takeaway_link(idx.get("biancang"), lang)
    zhongjing = takeaway_link(idx.get("zhongjing"), lang)
    medchatzh = takeaway_link(idx.get("medchatzh"), lang)
    shizhen = takeaway_link(idx.get("shizhengpt"), lang)
    chattcm = takeaway_link(idx.get("chattcm"), lang)
    shennong = takeaway_link(idx.get("shennong-tcm-llm"), lang)
    xinghe = takeaway_link(idx.get("xinghe"), lang)
    ladder = takeaway_link(idx.get("tcm-ladder"), lang)
    linglan = takeaway_link(idx.get("linglan"), lang)

    if lang == "zh":
        return [
            "## 先看这里",
            "",
            f"真能下载复现的中医权重大概 {n_open} 个，都在[开源模型](#开源模型)里。新闻里医院、公司发的，多数没有公开权重，当不了实验底座。",
            "",
            "2025 年以后，多模态、Agent 和评测明显变多；再单独训一个 7B 问答，往往不够。执业考试分数测的是回忆，不能当成辨证或临床能力——要比的话看 TCM-Ladder、LingLan、MTCMB。",
            "",
            "| 你想做什么 | 可以先看 | 备注 |",
            "| --- | --- | --- |",
            f"| 本机跑通一个模型 | {biancang}、{zhongjing} | 论文、权重、代码都有 |",
            f"| 做中医问诊 | {medchatzh} | 还有配套问诊数据 |",
            f"| 舌诊、四诊 | {shizhen} | 多模态，数据和权重都开 |",
            f"| 自己接着训 | {chattcm}、{shennong} | 预训练或指令数据是公开的 |",
            f"| 电脑比较一般 | {xinghe} | 9B，有 GGUF |",
            f"| 做对比实验 | {ladder}、{linglan} | 任务说得比较清楚；更多在[数据集](#数据集) |",
            "| 写相关工作 | 近两年的 scoping review | 先翻[综述](#综述)，别从单篇模型论文起 |",
            "",
            "同名不一定是同一个东西。「仲景」至少有 ZhongJingGPT 和 AAAI 那条 CMtMedQA；TCM-Eval 也不止一套。说不清时看 [Getting Started](wiki/Getting-Started.md)。",
            "",
        ]
    return [
        "## Start here",
        "",
        f"Only about {n_open} TCM checkpoints are actually public; they are under [Open models](#open-models). Hospital and company releases in the news usually ship no weights, so they make poor experimental baselines.",
        "",
        "Since 2025 the interesting work has been multimodal models, agents, and evaluation—not another 7B chatbot. Licensing-exam scores measure recall, not whether a model can do pattern differentiation. For comparisons, TCM-Ladder, LingLan, and MTCMB are a better place to start.",
        "",
        "| If you want to… | Try | Note |",
        "| --- | --- | --- |",
        f"| Get a model running | {biancang}, {zhongjing} | Paper, weights, and code |",
        f"| Build TCM inquiry | {medchatzh} | Comes with consult dialogues |",
        f"| Tongue / four diagnoses | {shizhen} | Multimodal; weights and data are public |",
        f"| Train further | {chattcm}, {shennong} | Pretrain or instruction data is released |",
        f"| Stay small | {xinghe} | 9B, GGUF available |",
        f"| Run a comparison | {ladder}, {linglan} | Tasks are spelled out; more under [Datasets](#datasets) |",
        "| Write related work | Recent scoping reviews | Skim [Surveys](#surveys) before individual model papers |",
        "",
        "Same name does not mean the same project. ZhongJingGPT is not the AAAI CMtMedQA line, and more than one benchmark is called TCM-Eval. [Getting Started](wiki/Getting-Started.md) if that is confusing.",
        "",
    ]


def model_table(entries: list[dict], lang: str) -> list[str]:
    if not entries:
        return []
    if lang == "zh":
        header = [
            "| 模型 | 年 | 特色 | 链接 |",
            "| --- | :---: | --- | --- |",
        ]
    else:
        header = [
            "| Model | Year | Focus | Links |",
            "| --- | :---: | --- | --- |",
        ]
    rows = []
    for entry in entries:
        name = display_name(entry, lang).replace("|", "/")
        year = str(year_of(entry) or "—")
        focus = focus_labels(entry, lang)
        links = compact_model_links(entry, lang)
        rows.append(f"| **{name}** | {year} | {focus} | {links} |")
    return header + rows


def build_model_section(buckets: dict[str, list[dict]], lang: str) -> list[str]:
    tcm = buckets["model_tcm"]
    general = buckets["model_general"]
    hf = buckets["model_hf"]
    open_tcm = [e for e in tcm if is_open_weights(e)]
    paper_tcm = [e for e in tcm if not is_open_weights(e)]

    title = "## 开源模型" if lang == "zh" else "## Open models"
    hint = (
        "上面是起步用的。要翻全部能下的权重，或只有论文/产品、以及常被拿来当底座的通用中文医疗模型，点开即可。"
        if lang == "zh"
        else "The table above is a shortlist. Expand the folds for every public checkpoint, paper-only or product models, and general Chinese medical LLMs people use as bases."
    )
    lines = [title, "", hint, ""]
    if open_tcm:
        summary = (
            f"能下载的权重，共 {len(open_tcm)} 个"
            if lang == "zh"
            else f"Public weights ({len(open_tcm)})"
        )
        lines += fold(summary, model_table(open_tcm, lang))

    if paper_tcm:
        summary = (
            f"只有论文或产品、没有核验权重的（{len(paper_tcm)}）"
            if lang == "zh"
            else f"Paper or product only, no verified weights ({len(paper_tcm)})"
        )
        lines += fold(summary, emit_list(paper_tcm, lang, format_resource_line))
    if general:
        summary = (
            f"通用中文医疗模型，常当底座或对照（{len(general)}）"
            if lang == "zh"
            else f"General Chinese medical models, often used as bases ({len(general)})"
        )
        lines += fold(summary, emit_list(general, lang, format_resource_line))
    if hf:
        summary = (
            f"Hugging Face 上的其他尺寸和 GGUF（{len(hf)}）"
            if lang == "zh"
            else f"Other Hugging Face sizes and GGUF ({len(hf)})"
        )
        lines += fold(summary, [format_dataset_line(e, lang) for e in hf])
    return lines


def build_news_section(news: list[dict], lang: str) -> list[str]:
    title = "## 新闻" if lang == "zh" else "## News"
    teaser = bold_teaser(news, 3)
    summary = (
        f"{len(news)} 条，最近有：{teaser}"
        if lang == "zh"
        else f"{len(news)} items; recent: {teaser}"
    )
    return [title, ""] + fold(summary, emit_list(news, lang, format_news_line))


def build_survey_section(surveys: list[dict], lang: str) -> list[str]:
    title = "## 综述" if lang == "zh" else "## Surveys"
    summary = (
        f"{len(surveys)} 篇，按年收着"
        if lang == "zh"
        else f"{len(surveys)} surveys, grouped by year"
    )
    return [title, ""] + fold(summary, emit_list(surveys, lang, format_resource_line))


def build_paper_section(buckets: dict[str, list[dict]], lang: str) -> list[str]:
    specs = [
        ("agent", "Agent", "Agents", "问诊流程、多智能体"),
        ("multimodal", "多模态 / 四诊", "Multimodal", "舌、面、脉"),
        ("rag_kg", "RAG / 知识图谱", "RAG / knowledge graphs", "检索和医案、方剂图谱"),
        ("eval", "评测论文", "Evaluation", "基准和考试；要下载评测集走下面「数据集」"),
        ("method", "其他", "Other", "处方、对齐、抽取之类"),
        ("history", "更早的工作", "Before LLMs", "专家系统、舌脉、本体"),
    ]
    title = "## 论文" if lang == "zh" else "## Papers"
    intro = (
        "模型已经分出去了。按题目点开一栏就行，不用按年份通读。"
        if lang == "zh"
        else "Models are listed above. Open one topic; you do not have to read by year."
    )
    lines = [title, "", intro, ""]
    for key, zh, en, hint in specs:
        items = buckets.get(key) or []
        if not items:
            continue
        heading = zh if lang == "zh" else en
        summary = (
            f"{heading}（{len(items)}）：{hint}"
            if lang == "zh"
            else f"{heading} ({len(items)}): {hint}"
        )
        body = (
            emit_decades(items, lang, format_resource_line)
            if key == "history"
            else emit_list(items, lang, format_resource_line)
        )
        lines += fold(summary, body)
    return lines


def build_dataset_section(datasets: list[dict], lang: str) -> list[str]:
    title = "## 数据集" if lang == "zh" else "## Datasets"
    intro = (
        "按用途点开。想对一下评测集，看 [Datasets](wiki/Datasets.md) 和 [Benchmarks](wiki/Benchmarks.md)。"
        if lang == "zh"
        else "Grouped by use. For a longer note on benches, see [Datasets](wiki/Datasets.md) and [Benchmarks](wiki/Benchmarks.md)."
    )
    lines = [title, "", intro, ""]
    by_section: dict[str, list[dict]] = defaultdict(list)
    for entry in datasets:
        section = entry.get("section") or "其他"
        if section == HF_SECTION:
            continue
        by_section[section].append(entry)

    seen = set()
    for section in DATASET_SECTION_ORDER_ZH:
        entries = by_section.get(section) or []
        if not entries:
            continue
        seen.add(section)
        heading = section if lang == "zh" else SECTION_EN.get(section, section)
        summary = f"{heading}（{len(entries)}）" if lang == "zh" else f"{heading} ({len(entries)})"
        lines += fold(summary, [format_dataset_line(e, lang) for e in entries])
    for section, entries in by_section.items():
        if section in seen:
            continue
        heading = section if lang == "zh" else SECTION_EN.get(section, section)
        summary = f"{heading}（{len(entries)}）" if lang == "zh" else f"{heading} ({len(entries)})"
        lines += fold(summary, [format_dataset_line(e, lang) for e in entries])
    return lines


def footer(lang: str, portal: str) -> list[str]:
    if lang == "zh":
        return [
            "---",
            "",
            f"要搜索或按标签筛，用[项目页]({PORTAL_ZH})。说明写在 [Wiki](wiki/Home.md)。",
            "改条目请编辑 `data/catalog.yml`，再运行 `python3 scripts/build_readme.py`，不要直接改这个 README。",
            "",
        ]
    return [
        "---",
        "",
        f"Search and filter by tag on the [project page]({portal}). Longer notes live in the [wiki](wiki/Home.md).",
        "Add entries in `data/catalog.yml` and run `python3 scripts/build_readme.py`. Do not edit this README by hand.",
        "",
    ]


def build_readme(catalog: dict, lang: str, i18n_en: dict | None = None) -> str:
    meta = catalog.get("meta") or {}
    portal = meta.get("portal_url", DEFAULT_PORTAL)
    i18n_en = i18n_en or {}

    items = catalog.get("items") or []
    if lang == "en":
        items = [apply_i18n(i, i18n_en) for i in items]
    buckets = classify_items(items)
    n = count_pack(buckets)

    if lang == "zh":
        header = [
            "# 🔥 开源中文医疗大模型",
            "",
            lang_switcher("zh"),
            "",
            badges(),
            "",
            f"收集中医大模型相关的模型、数据、评测和论文，也带一点通用中文医疗。"
            f"现在大概有 {n['news']} 条新闻、{n['models']} 个模型、{n['surveys']} 篇综述、"
            f"{n['datasets']} 个数据集、{n['papers']} 篇方法论文。[欢迎补条目](CONTRIBUTING.md)。",
            "",
            f"[项目页]({portal}) · [中文项目页]({PORTAL_ZH}) · [Wiki](wiki/Home.md) · [主页]({SITE_ZH})",
            "",
        ]
    else:
        header = [
            "# 🔥 Awesome TCM / Chinese Medical LLMs",
            "",
            lang_switcher("en"),
            "",
            badges(),
            "",
            f"Models, data, benchmarks, and papers around TCM LLMs, plus a few general Chinese medical ones. "
            f"Right now: {n['news']} news items, {n['models']} models, {n['surveys']} surveys, "
            f"{n['datasets']} datasets, {n['papers']} method papers. [PRs welcome](CONTRIBUTING.md).",
            "",
            f"[Project page]({portal}) · [Wiki](wiki/Home.md) · [Homepage]({SITE_EN})",
            "",
        ]

    lines = header
    lines += takeaway_block(buckets, lang)
    lines += build_model_section(buckets, lang)
    lines += build_news_section(buckets["news"], lang)
    lines += build_survey_section(buckets["survey"], lang)
    lines += build_paper_section(buckets, lang)
    lines += build_dataset_section(buckets["dataset"], lang)
    lines += footer(lang, portal)
    return "\n".join(lines).rstrip() + "\n"


def export_json(catalog: dict) -> dict:
    items = [
        i
        for i in catalog.get("items", [])
        if i.get("status", "published") == "published" and i.get("verified_at")
    ]
    return {
        "meta": catalog.get("meta", {}),
        "updated_at": (catalog.get("meta") or {}).get("updated_at"),
        "items": items,
    }


def _wiki_list(entries: list[dict], lang: str = "zh") -> list[str]:
    return [format_resource_line(i, lang) for i in entries]


def build_wiki_models(buckets: dict[str, list[dict]]) -> str:
    tcm = buckets["model_tcm"]
    general = buckets["model_general"]
    hf = buckets["model_hf"]
    open_tcm = [e for e in tcm if is_open_weights(e)]
    paper_tcm = [e for e in tcm if not is_open_weights(e)]
    lines = [
        "# Models",
        "",
        "本页是 README [开源模型](../README.md#开源模型) 的展开版：先给选型原则，再给完整表。",
        "",
        "## 怎么选",
        "",
        "| 场景 | 优先看 |",
        "| --- | --- |",
        "| 本地推理 / 复现论文 | 开源权重 + 代码 + 配套数据 |",
        "| 中医问诊对话 | **MedChatZH**（论文 + 权重 + 代码 + 问诊数据） |",
        "| 舌诊 / 四诊 | 标签含 `multimodal` 的模型（如 ShizhenGPT、TongueVLM） |",
        "| 问诊工作流 | `agent` 或配套 GraphRAG 系统，而不是单模型 |",
        "| 当底座继续微调 | 同系列 Base / Instruct，以及通用中文医疗模型 |",
        "| 只做对照实验 | 通用中文医疗栏（华佗、孙思邈等） |",
        "",
        f"中医专用 {len(tcm)} · 其中开源权重 {len(open_tcm)} · 通用医疗 {len(general)} · HF 精选 {len(hf)}。",
        "",
        "## 开源权重",
        "",
    ]
    lines += model_table(open_tcm, "zh")
    lines += ["", "## 论文或产品向（无公开权重）", ""]
    lines += _wiki_list(paper_tcm) or ["（无）"]
    lines += ["", "## 通用中文医疗模型", ""]
    lines += _wiki_list(general)
    lines += ["", "## Hugging Face 精选", ""]
    for entry in hf:
        lines.append(format_dataset_line(entry, "zh"))
    lines += ["", "返回 [[Home]] · 分类法见 [[Taxonomy]]。", ""]
    return "\n".join(lines)


def build_wiki_datasets(buckets: dict[str, list[dict]]) -> str:
    datasets = buckets["dataset"]
    by_section: dict[str, list[dict]] = defaultdict(list)
    for entry in datasets:
        section = entry.get("section") or "其他"
        if section == HF_SECTION:
            continue
        by_section[section].append(entry)
    lines = [
        "# Datasets",
        "",
        "数据集按用途分栏，与 README [数据集](../README.md#数据集) 同源。评测基准的任务对照见 [[Benchmarks]]。",
        "",
    ]
    for section in DATASET_SECTION_ORDER_ZH:
        entries = by_section.get(section) or []
        if not entries:
            continue
        lines += [f"## {section}", ""]
        for entry in entries:
            blurb = entry.get("summary_zh") or ""
            line = format_dataset_line(entry, "zh")
            if blurb and blurb not in line:
                line = f"{line} — {blurb}"
            lines.append(line)
        lines.append("")
    extra = [s for s in by_section if s not in DATASET_SECTION_ORDER_ZH]
    for section in extra:
        lines += [f"## {section}", ""]
        for entry in by_section[section]:
            lines.append(format_dataset_line(entry, "zh"))
        lines.append("")
    lines += ["返回 [[Home]]。", ""]
    return "\n".join(lines)


def build_wiki_benchmarks(buckets: dict[str, list[dict]]) -> str:
    bench_ds = [
        e
        for e in buckets["dataset"]
        if (e.get("section") == "评测基准") or "benchmark" in tags_of(e)
    ]
    bench_papers = buckets["eval"]
    lines = [
        "# Benchmarks",
        "",
        "把「可下载的评测集」和「评测论文」分开，避免和模型论文混在一起。",
        "",
        "## 评测集",
        "",
    ]
    for entry in bench_ds:
        lines.append(format_dataset_line(entry, "zh"))
    lines += ["", "## 评测与评估论文", ""]
    lines += _wiki_list(bench_papers)
    lines += [
        "",
        "## 阅读提示",
        "",
        "- 名称相近不一定是同一套：例如存在多个 **TCM-Eval**。",
        "- 考试类（执业医师 / 考研）测的是知识回忆，不等于临床辨证能力。",
        "- 多模态基准（TCM-Ladder、舌象集）需要看输入模态是否与模型匹配。",
        "",
        "返回 [[Home]] · 模型见 [[Models]]。",
        "",
    ]
    return "\n".join(lines)


def write_wiki_generated(buckets: dict[str, list[dict]]) -> None:
    WIKI_DIR.mkdir(exist_ok=True)
    mapping = {
        "Models.md": build_wiki_models(buckets),
        "Datasets.md": build_wiki_datasets(buckets),
        "Benchmarks.md": build_wiki_benchmarks(buckets),
    }
    for name, text in mapping.items():
        (WIKI_DIR / name).write_text(text, encoding="utf-8")


def main() -> None:
    if not CATALOG_YML.exists():
        print(f"Missing {CATALOG_YML}", file=sys.stderr)
        sys.exit(1)
    catalog = yaml.safe_load(CATALOG_YML.read_text(encoding="utf-8"))
    i18n_en = load_i18n_en()
    missing = [
        i["id"]
        for i in catalog.get("items", [])
        if i.get("status", "published") == "published" and i["id"] not in i18n_en
    ]
    README_ZH.write_text(build_readme(catalog, "zh"), encoding="utf-8")
    README_EN.write_text(build_readme(catalog, "en", i18n_en), encoding="utf-8")
    payload = export_json(catalog)
    CATALOG_JSON.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    zh_items = catalog.get("items") or []
    write_wiki_generated(classify_items(zh_items))
    msg = (
        f"Wrote {README_ZH.relative_to(ROOT)}, {README_EN.relative_to(ROOT)}, "
        f"{CATALOG_JSON.relative_to(ROOT)}, and wiki/{{Models,Datasets,Benchmarks}}.md "
        f"({len(payload['items'])} items; i18n_en={len(i18n_en)})"
    )
    print(msg)
    if missing:
        print(
            f"WARNING: missing English i18n for {len(missing)} ids: {', '.join(missing[:12])}"
            + ("..." if len(missing) > 12 else ""),
            file=sys.stderr,
        )


if __name__ == "__main__":
    main()
