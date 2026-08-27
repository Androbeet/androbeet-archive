#!/usr/bin/env python3
"""
Regenerates index.html from templates/index.template.html + data/articles.json.

Run manually:   python3 scripts/build.py
Runs automatically via .github/workflows/build.yml on every push that
touches data/articles.json.
"""
import json
import html
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "articles.json"
TEMPLATE = ROOT / "templates" / "index.template.html"
OUTPUT = ROOT / "index.html"


def card(article: dict) -> str:
    title = html.escape(article["title"])
    url = html.escape(article["url"])
    desc = html.escape(article.get("description", ""))
    tags = article.get("tags", [])
    paid = article.get("paid", False)

    tags_html = "\n".join(f'<span class="tag">{html.escape(t)}</span>' for t in tags)
    paid_html = '<span class="paid-badge">Paid — email for link</span>' if paid else ""

    return f"""          <div class="essay-card">
            <h3><a href="{url}">{title}</a></h3>
            <p>{desc}</p>
            <div class="tags">
{tags_html}
              {paid_html}
            </div>
            <a class="read" href="{url}">Read on Medium →</a>
          </div>"""


def main():
    articles = json.loads(DATA.read_text())
    cards_html = "\n".join(card(a) for a in articles)
    template = TEMPLATE.read_text()
    output = template.replace("{{ESSAYS}}", cards_html).replace(
        "{{COUNT}}", str(len(articles))
    )
    OUTPUT.write_text(output)
    print(f"Built index.html with {len(articles)} articles.")


if __name__ == "__main__":
    main()
