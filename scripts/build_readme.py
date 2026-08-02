#!/usr/bin/env python3
"""Build README.md and data/catalog.json from data/catalog.yml."""

from __future__ import annotations

import json
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
README = ROOT / "README.md"

SITE_ZH = "https://tyang816.github.io/zh/"
SITE_EN = "https://tyang816.github.io/"
DEFAULT_PORTAL = "https://tyang816.github.io/projects/tcm/"
PORTAL_ZH = "https://tyang816.github.io/zh/projects/tcm/"

DATASET_SECTION_ORDER = [
    "公开资料整理",
    "原始书籍 / 预训练语料",
    "评测基准",
    "考试数据集",
    "指令/对话数据集",
    "知识图谱",
    "Hugging Face 开源模型（精选）",
]


def link_md(label: str, url: str) -> str:
    return f"[[{label}]({url})]"


def format_links(links: dict | None) -> str:
    if not links:
        return ""
    parts = [link_md(key, url) for key, url in links.items() if url]
    return (" " + " ".join(parts)) if parts else ""


def format_resource_line(entry: dict) -> str:
    bits = ["-"]
    if entry.get("venue"):
        bits.append(f"[*{entry['venue']}*]")
    bits.append(f"**{entry['name']}**")
    if entry.get("summary_zh"):
        bits.append(entry["summary_zh"])
    orgs = entry.get("orgs") or []
    if orgs:
        bits.append(f"[{'，'.join(orgs)}]")
    return " ".join(bits) + format_links(entry.get("links"))


def format_news_line(entry: dict) -> str:
    date = entry.get("date") or str(entry.get("year", ""))
    line = f"- [{date}] {entry.get('summary_zh', '')}"
    links = entry.get("links") or {}
    if links.get("链接"):
        line += f" {link_md('链接', links['链接'])}"
    elif links:
        line += format_links(links)
    return line


def build_site_links_block(portal: str) -> list[str]:
    return [
        f"**相关链接**：[项目页]({portal}) · [中文]({PORTAL_ZH}) · "
        f"[作者中文主页]({SITE_ZH}) · [Author site (EN)]({SITE_EN})",
        "",
        f"> 项目页支持标签筛选与搜索，数据与本 README 同源（`data/catalog.yml`）。",
    ]


def build_readme(catalog: dict) -> str:
    meta = catalog.get("meta") or {}
    portal = meta.get("portal_url", DEFAULT_PORTAL)
    lines = [
        "# 🔥 开源中文医疗大模型",
        "",
        "![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-green)  "
        "[![Awesome](https://awesome.re/badge.svg)](https://awesome.re) "
        "![Stars](https://img.shields.io/github/stars/tyang816/Awesome-TCM-LLM?color=yellow)  "
        "![Forks](https://img.shields.io/github/forks/tyang816/Awesome-TCM-LLM?color=blue&label=Fork)",
        "",
        "本仓库收集了开源中文医疗大模型（中医/西医）相关的资源，包括新闻、论文、模型、数据集等，欢迎大家贡献更多资源。",
        "",
        "This repository curates open resources for Traditional Chinese Medicine (and related Chinese medical) LLMs — papers, models, benchmarks, datasets, and news.",
        "",
        *build_site_links_block(portal),
        "",
        "## 📰 新闻",
    ]

    news = [
        i
        for i in catalog["items"]
        if i.get("type") == "news" and i.get("status", "published") == "published"
    ]
    news.sort(key=lambda x: x.get("date", ""), reverse=True)
    lines.extend(format_news_line(i) for i in news)

    lines += ["", "## 📚 资源"]
    resources = [
        i
        for i in catalog["items"]
        if i.get("type") == "resource" and i.get("status", "published") == "published"
    ]
    by_year: dict[int, list] = defaultdict(list)
    for entry in resources:
        by_year[int(entry.get("year") or 0)].append(entry)
    for year in sorted(by_year.keys(), reverse=True):
        if year == 0:
            continue
        lines += ["", f"### {year}"]
        lines.extend(format_resource_line(i) for i in by_year[year])

    lines += ["", "## 📚 数据集"]
    datasets = [
        i
        for i in catalog["items"]
        if i.get("type") in ("dataset", "model_hf")
        and i.get("status", "published") == "published"
    ]
    by_section: dict[str, list] = defaultdict(list)
    for entry in datasets:
        by_section[entry.get("section") or "其他"].append(entry)

    seen = set()
    for section in DATASET_SECTION_ORDER:
        if section not in by_section:
            continue
        seen.add(section)
        lines += ["", f"### {section}"]
        for entry in by_section[section]:
            title = entry.get("title_zh") or entry["name"]
            lines.append(f"- {title}{format_links(entry.get('links'))}")

    for section, entries in by_section.items():
        if section in seen:
            continue
        lines += ["", f"### {section}"]
        for entry in entries:
            title = entry.get("title_zh") or entry["name"]
            lines.append(f"- {title}{format_links(entry.get('links'))}")

    lines.append("")
    return "\n".join(lines)


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


def main() -> None:
    if not CATALOG_YML.exists():
        print(f"Missing {CATALOG_YML}", file=sys.stderr)
        sys.exit(1)
    catalog = yaml.safe_load(CATALOG_YML.read_text(encoding="utf-8"))
    README.write_text(build_readme(catalog), encoding="utf-8")
    payload = export_json(catalog)
    CATALOG_JSON.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(
        f"Wrote {README.relative_to(ROOT)} and {CATALOG_JSON.relative_to(ROOT)} "
        f"({len(payload['items'])} items)"
    )


if __name__ == "__main__":
    main()
