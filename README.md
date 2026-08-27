# androbeet-archive

Sibling repo to `androbeet.github.io` (which stays as the Lexicon). Static HTML, but the essay list is now data-driven — you edit one JSON file, a GitHub Action rebuilds the page automatically.

## Deploy (first time only)

1. New repo on GitHub named `androbeet-archive`, public.
2. Upload everything in this folder to the `main` branch.
3. Settings → Pages → source: `main` / root.
4. Settings → Actions → General → Workflow permissions → set to **"Read and write permissions"** (required so the auto-rebuild can commit `index.html` back — one-time setting).
5. Live at `https://androbeet.github.io/androbeet-archive/`.

## Adding a new Medium article (the "admin" workflow)

Two ways:

**Easy way** — open `tools/add-article.html` in a browser (works locally or once deployed, at `.../androbeet-archive/tools/add-article.html`), fill in the title, URL, a one-line description in your own words, tags, and whether it's paywalled. Tap Generate, copy the output.

**Then, either way** — open `data/articles.json` in the GitHub app → Edit → paste the new entry inside the `[ ]` brackets, right after `[` or after any existing entry's `},` → commit. The GitHub Action rebuilds `index.html` automatically within about a minute — you never touch the HTML.

## Paid articles

Every entry has a `"paid": true/false` field. Set it to `true` for anything paywalled and a badge appears on that card. There's also a standing banner on the page: readers can email you and you send a friend link — update the wording in `templates/index.template.html` if you want to change it.

## SEO / discoverability, what's actually in here

- Real static HTML for every article card (not just JS-rendered — crawlers that don't execute JavaScript still see full content)
- Meta description, canonical URL, Open Graph + Twitter Card tags
- JSON-LD `Person` schema linking your Mail, YouTube, Instagram, and Medium
- `sitemap.xml` and `robots.txt`
- `llms.txt` — a plain-language summary file some AI crawlers are starting to read; low effort, no downside, not a guaranteed ranking effect

None of this is a shortcut around needing real content and real links over time — it just makes sure nothing here is *invisible* to search or AI systems that would otherwise find it. There's no reliable trick that substitutes for that.

## About the "hidden archive" idea

I didn't build a page that's invisible to visitors but readable by search engines — that's called **cloaking**, and it's explicitly against Google's spam policies. If it's ever detected, the penalty isn't "that page gets ignored" — it's manual action against the *whole domain*, which could pull your actual Lexicon and Archive out of search entirely. That's the opposite of what you're trying to do here, so I'd rather flag it than build it quietly.

If what you actually want is a private space for your own drafts and notes — that's completely fine, just make it a **private** GitHub repo (not part of this public site). It won't do anything for SEO, but it won't need to; it's just your own scratchpad, and nothing pretends otherwise to Google.

## Structure

```
data/articles.json          ← the source of truth, edit this to add articles
templates/index.template.html
scripts/build.py            ← regenerates index.html from the two files above
.github/workflows/build.yml ← runs build.py automatically on push
tools/add-article.html      ← generates a properly formatted JSON entry
index.html                  ← generated output, don't hand-edit (gets overwritten)
```

## Also still open

- Book section: add the real Amazon URL for *The Ledger We Never Signed* in `templates/index.template.html`
- Confirm `youtube.com/@androbeet`, `instagram.com/androbeet_`, and `medium.com/@androbeet` are the exact right handles
