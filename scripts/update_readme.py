"""
Regenerates the "Live Stats" block in README.md by querying the GitHub REST API.

Run by .github/workflows/update-readme.yml on a daily schedule and on every push,
so the README reflects real numbers instead of static text. Uses only the
standard library + requests, and writes back only the block between the
START/END markers so nothing else in the README is touched.
"""

from __future__ import annotations

import os
import re
import sys
from datetime import datetime, timezone

import requests

USERNAME = "Sunilsoftwarengineer"
README_PATH = "README.md"
START_MARKER = "<!-- LIVE-STATS:START -->"
END_MARKER = "<!-- LIVE-STATS:END -->"
API_ROOT = "https://api.github.com"


def _headers() -> dict:
    token = os.environ.get("GITHUB_TOKEN")
    headers = {"Accept": "application/vnd.github+json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers


def fetch_repos() -> list[dict]:
    repos, page = [], 1
    while True:
        resp = requests.get(
            f"{API_ROOT}/users/{USERNAME}/repos",
            params={"per_page": 100, "page": page, "type": "owner"},
            headers=_headers(),
            timeout=15,
        )
        resp.raise_for_status()
        batch = resp.json()
        if not batch:
            break
        repos.extend(batch)
        page += 1
    return repos


def summarize(repos: list[dict]) -> dict:
    total_stars = sum(r.get("stargazers_count", 0) for r in repos)
    total_forks = sum(r.get("forks_count", 0) for r in repos)

    languages: dict[str, int] = {}
    for r in repos:
        lang = r.get("language")
        if lang:
            languages[lang] = languages.get(lang, 0) + 1
    top_language = max(languages, key=languages.get) if languages else "N/A"

    return {
        "public_repos": len(repos),
        "total_stars": total_stars,
        "total_forks": total_forks,
        "top_language": top_language,
    }


def render_block(stats: dict) -> str:
    updated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    return (
        f"{START_MARKER}\n"
        "| Metric | Value |\n"
        "|---|---|\n"
        f"| Public repos | {stats['public_repos']} |\n"
        f"| Total stars earned | {stats['total_stars']} |\n"
        f"| Total forks | {stats['total_forks']} |\n"
        f"| Most-used language | {stats['top_language']} |\n\n"
        f"<sub>Auto-updated {updated} by `scripts/update_readme.py`</sub>\n"
        f"{END_MARKER}"
    )


def update_readme(new_block: str) -> bool:
    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    pattern = re.compile(
        re.escape(START_MARKER) + r".*?" + re.escape(END_MARKER), re.DOTALL
    )
    if not pattern.search(content):
        print("Markers not found in README.md — nothing to update.", file=sys.stderr)
        return False

    updated_content = pattern.sub(new_block, content)
    if updated_content == content:
        return False

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(updated_content)
    return True


def main() -> None:
    repos = fetch_repos()
    stats = summarize(repos)
    block = render_block(stats)
    changed = update_readme(block)
    print("README updated." if changed else "No changes needed.")


if __name__ == "__main__":
    main()
