#!/usr/bin/env python3

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "oss-macos.json"
README_FILE = ROOT / "README.md"

REQUIRED_FIELDS = {
    "name",
    "repo_url",
    "homepage",
    "description",
    "license",
    "category",
    "macos_native",
    "last_commit_verified",
    "oss_verified",
    "source_url",
    "status",
}
VALID_STATUSES = {"active", "maintenance", "archived"}
VALID_CATEGORIES = {
    "developer-tools",
    "productivity",
    "utilities",
    "media",
    "design",
    "security-privacy",
    "terminal-system",
    "notes-knowledge",
    "communication",
    "browsers",
}


def normalize_heading(title: str) -> str:
    cleaned = "".join(ch for ch in title if ch.isalnum() or ch.isspace() or ch in "-")
    cleaned = cleaned.replace("&", " ")
    return re.sub(r"[^a-z0-9]+", "-", cleaned.lower()).strip("-")


def load_data() -> list[dict]:
    data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
    assert isinstance(data, list) and data, "oss-macos.json must be a non-empty list"
    for i, entry in enumerate(data):
        missing = REQUIRED_FIELDS - entry.keys()
        assert not missing, f"entry {i} ({entry.get('name')}) missing {sorted(missing)}"
        assert entry["category"] in VALID_CATEGORIES, f"entry {i} bad category {entry['category']}"
        assert entry["status"] in VALID_STATUSES, f"entry {i} bad status {entry['status']}"
        assert isinstance(entry["oss_verified"], bool), f"entry {i} oss_verified not bool"
        assert isinstance(entry["last_commit_verified"], bool), f"entry {i} last_commit_verified not bool"
        assert isinstance(entry["macos_native"], bool), f"entry {i} macos_native not bool"
        assert entry["repo_url"].startswith("https://github.com/"), (
            f"entry {i} repo_url must be https://github.com/..."
        )
        if entry["homepage"]:
            assert entry["homepage"].startswith("https://"), f"entry {i} homepage must be https"
        if entry["oss_verified"]:
            assert entry["source_url"].startswith("https://"), (
                f"entry {i} verified entry needs https source_url"
            )
            assert entry["license"] != "unverified", (
                f"entry {i} verified entry must name a license"
            )
    names = [entry["name"] for entry in data]
    assert len(names) == len(set(names)), "duplicate names"
    return data


def validate_readme(data: list[dict]) -> None:
    readme_text = README_FILE.read_text(encoding="utf-8")
    match = re.search(r"A curated list of \*\*(\d+)\s+open-source macOS applications\*\*", readme_text)
    assert match, "README summary line is missing the total entry count"
    reported_total = int(match.group(1))
    assert reported_total == len(data), (
        f"README summary count ({reported_total}) does not match data file ({len(data)})"
    )

    toc_counts = {
        match.group(1): int(match.group(2))
        for match in re.finditer(
            r"^- \[[^\]]+\]\(#([^\)]+)\)\s+\((\d+)\)\s*$",
            readme_text,
            re.M,
        )
    }
    assert toc_counts, "README contents section counts were not found"

    heading_matches = list(re.finditer(r"^##\s+(.+)$", readme_text, re.M))
    actual_counts: dict[str, int] = {}
    for idx, heading_match in enumerate(heading_matches):
        title = heading_match.group(1).strip()
        if title in {"Notable exclusions", "Docs", "Contributing", "License"}:
            continue
        start = heading_match.end()
        end = heading_matches[idx + 1].start() if idx + 1 < len(heading_matches) else len(readme_text)
        section_text = readme_text[start:end]
        section_count = len(re.findall(r"^- \*\*\[", section_text, re.M))
        actual_counts[normalize_heading(title)] = section_count

    for slug, expected in toc_counts.items():
        assert slug in actual_counts, f"README section #{slug} missing a matching heading"
        assert actual_counts[slug] == expected, (
            f"README section #{slug} reports {expected} entries but has {actual_counts[slug]}"
        )


def main() -> None:
    data = load_data()
    validate_readme(data)
    print(f"OK: data/oss-macos.json: {len(data)} entries validated")
    print("OK: README.md: summary and category counts match the data file")


if __name__ == "__main__":
    main()
