#!/usr/bin/env python3
"""
Update and validate K-12 English Knowledge Base materials.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DATA_DIR = ROOT / "data"

def validate_data():
    topics_file = DATA_DIR / "grammar_topics.json"
    cards_file = DATA_DIR / "cards_samples.json"

    if not topics_file.exists() or not cards_file.exists():
        print("Error: Missing core data files in data/", file=sys.stderr)
        return False

    try:
        topics = json.loads(topics_file.read_text(encoding="utf-8"))
        cards = json.loads(cards_file.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"JSON validation failed: {e}", file=sys.stderr)
        return False

    all_ids = set()
    total_points = 0
    for ch in topics.get("chapters", []):
        for p in ch.get("points", []):
            pid = p.get("id")
            if pid in all_ids:
                print(f"Warning: Duplicate topic ID {pid}", file=sys.stderr)
            all_ids.add(pid)
            total_points += 1

    print(f"Validation successful: {len(topics.get('chapters', []))} chapters, {total_points} topics, {len(cards)} mnemonic cards.")
    return True

def import_cards(file_path: str):
    p = Path(file_path)
    if not p.exists():
        print(f"File not found: {file_path}", file=sys.stderr)
        return False

    new_data = json.loads(p.read_text(encoding="utf-8"))
    cards_file = DATA_DIR / "cards_samples.json"
    existing = json.loads(cards_file.read_text(encoding="utf-8")) if cards_file.exists() else []

    existing_ids = {c.get("id") for c in existing}
    added = 0
    for item in new_data:
        if item.get("id") not in existing_ids:
            existing.append(item)
            added += 1

    cards_file.write_text(json.dumps(existing, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Successfully imported {added} new cards. Total: {len(existing)}")
    return True

def main():
    parser = argparse.ArgumentParser(description="English Knowledge Base Maintenance Tool")
    parser.add_argument("--validate", action="store_true", help="Validate JSON integrity")
    parser.add_argument("--import-cards", type=str, help="Import new cards from a JSON file")

    args = parser.parse_args()

    if args.validate:
        sys.exit(0 if validate_data() else 1)
    elif args.import_cards:
        sys.exit(0 if import_cards(args.import_cards) else 1)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
