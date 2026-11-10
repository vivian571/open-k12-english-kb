#!/usr/bin/env python3
"""
Export K-12 English Cards to Anki TSV or Markdown format.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DATA_DIR = ROOT / "data"

def export_anki(output_file: str):
    cards_file = DATA_DIR / "cards_samples.json"
    if not cards_file.exists():
        print("cards_samples.json not found.", file=sys.stderr)
        return

    cards = json.loads(cards_file.read_text(encoding="utf-8"))
    lines = []
    for c in cards:
        front = f"<b>【{c.get('topic')}】</b><br>{c.get('question', '')}"
        back = (
            f"<b>生活隐喻：</b>{c.get('metaphor', '')}<br><br>"
            f"<b>速记口诀：</b>{c.get('formula', '')}<br><br>"
            f"<b>启发式引导：</b>{c.get('heuristic_hint', '')}"
        )
        lines.append(f"{front}\t{back}")

    out_p = Path(output_file)
    out_p.write_text("\n".join(lines), encoding="utf-8")
    print(f"Exported {len(lines)} cards to Anki TSV: {out_p}")

def export_md(output_file: str):
    cards_file = DATA_DIR / "cards_samples.json"
    if not cards_file.exists():
        print("cards_samples.json not found.", file=sys.stderr)
        return

    cards = json.loads(cards_file.read_text(encoding="utf-8"))
    md_lines = ["# 初中英语语法启发式思维卡片精选\n"]
    for c in cards:
        md_lines.append(f"## 📌 {c.get('topic')}\n")
        md_lines.append(f"- **生活化隐喻**：{c.get('metaphor')}")
        md_lines.append(f"- **避坑口诀**：`{c.get('formula')}`")
        md_lines.append(f"- **启发式引导**：{c.get('heuristic_hint')}\n")

    out_p = Path(output_file)
    out_p.write_text("\n".join(md_lines), encoding="utf-8")
    print(f"Exported {len(cards)} cards to Markdown: {out_p}")

def main():
    parser = argparse.ArgumentParser(description="Export cards to Anki or Markdown")
    parser.add_argument("--anki", type=str, help="Export to Anki TSV format file path")
    parser.add_argument("--md", type=str, help="Export to Markdown format file path")

    args = parser.parse_args()
    if args.anki:
        export_anki(args.anki)
    elif args.md:
        export_md(args.md)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
