#!/usr/bin/env python3
"""Validate catalog structure, localization coverage, and generated metadata."""

from __future__ import annotations

import json
import sys
from collections import Counter
from datetime import date
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "data" / "catalog.yml"
SCHEMA = ROOT / "data" / "catalog.schema.json"
I18N_EN = ROOT / "data" / "i18n_en.yml"

ALLOWED_SECTIONS = {
    "公开资料整理",
    "原始书籍 / 预训练语料",
    "评测基准",
    "考试数据集",
    "指令/对话数据集",
    "知识图谱",
    "Hugging Face 开源模型（精选）",
    "语料/指令",
}


def main() -> int:
    catalog = yaml.safe_load(CATALOG.read_text(encoding="utf-8"))
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    i18n = yaml.safe_load(I18N_EN.read_text(encoding="utf-8")) or {}
    errors: list[str] = []

    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    for error in sorted(validator.iter_errors(catalog), key=lambda e: list(e.path)):
        path = ".".join(str(part) for part in error.absolute_path) or "catalog"
        errors.append(f"{path}: {error.message}")

    items = catalog.get("items") or []
    ids = [item.get("id") for item in items]
    for item_id, count in Counter(ids).items():
        if count > 1:
            errors.append(f"duplicate id: {item_id} ({count} entries)")

    item_ids = set(ids)
    missing_i18n = sorted(
        item["id"] for item in items
        if item.get("status", "published") == "published" and item.get("id") not in i18n
    )
    orphan_i18n = sorted(set(i18n) - item_ids)
    if missing_i18n:
        errors.append("missing English localization: " + ", ".join(missing_i18n))
    if orphan_i18n:
        errors.append("orphan English localization: " + ", ".join(orphan_i18n))

    for item in items:
        section = item.get("section")
        if section and section not in ALLOWED_SECTIONS:
            errors.append(f"{item.get('id')}: unsupported section {section!r}")
        verified = item.get("verified_at")
        if verified:
            try:
                if date.fromisoformat(str(verified)) > date.today():
                    errors.append(f"{item.get('id')}: verified_at is in the future")
            except ValueError:
                pass  # The schema reports the malformed date.

    published_dates = [
        str(item["verified_at"])
        for item in items
        if item.get("status", "published") == "published" and item.get("verified_at")
    ]
    expected_updated = max(published_dates, default=None)
    actual_updated = str((catalog.get("meta") or {}).get("updated_at") or "")
    if expected_updated and actual_updated != expected_updated:
        errors.append(
            f"meta.updated_at is {actual_updated!r}; expected latest verified_at {expected_updated!r}"
        )

    if errors:
        print("Catalog validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"Catalog validation passed: {len(items)} items, {len(i18n)} localizations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
