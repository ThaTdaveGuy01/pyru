# Codex Task Directive — Universal Website Scraper Builder (Astral uv Edition, v1.5)
# Last Updated: 2025-10-31T00:00:00Z
# Author: Codex Autonomous Build Agent

---

## Objective
Develop a **Python 3.14+ universal website scraper** that clones and serves any website fully offline.  
All links and assets MUST be rewritten for local use.  
Packaging, tooling, and validation MUST rely solely on the **Astral ecosystem**: `uv`, `ruff`, `black`, `ty`, and `pytest`.

---

## Deliverables
1. ✅ `uv`-managed project scaffold at `/srv/projects/www/scraper`.  
2. ✅ CLI executable: `uv run scraper`.  
3. ✅ Complete static mirror under `mirror/` with integrity report.  
4. ✅ Verified self-test of scraping + serving.  
5. ✅ One Git commit and tag `v1.5.0`.

---

## Tooling and Packaging (Astral Only)

| Purpose | Tool | Requirement |
|:--|:--|:--|
| Package Manager | `uv` | Required (no pip / Poetry) |
| Formatter | `black` | Enforced PEP 8 style |
| Linter | `ruff` | Strict CI mode |
| Type Checker | `ty` | Mandatory |
| Tests | `pytest` | Required for E2E |
| Tasks | `uv run` aliases | No Makefile |
| Lock File | `uv.lock` | Deterministic builds |

Setup example:
```bash
uv init scraper && cd scraper
uv add aiohttp playwright beautifulsoup4 selectolax lxml tenacity typer rich tldextract cssutils orjson
uv run playwright install --with-deps
CLI Interface
bash
Copy code
uv run scraper --url https://target.tld \
  --depth 3 --output ./mirror --dynamic true \
  --concurrency 64 --rate 8/s --timeout 30 \
  --ignore-robots false --delay 0.25 \
  --include '+=*.target.tld/*' --exclude '-=/cdn/*' \
  --max-bytes 2GiB --max-files 25000 \
  --resume true --serve false --bind 127.0.0.1:8000 \
  --auth 'cookie:NAME=VALUE' --header 'X-Token:…' \
  --wait 'dom:idle,net:idle,ms:2500'
Architecture
graphql
Copy code
src/scraper/
  ├── __init__.py
  ├── cli.py        # Typer CLI
  ├── core.py       # crawl orchestration, BFS frontier
  ├── fetcher.py    # aiohttp + Playwright fetch/rate-limit
  ├── rewrite.py    # URL normalization and rewriting
  ├── store.py      # content-addressed blob store
  ├── server.py     # local preview HTTP server
  ├── verify.py     # integrity walker + report
  └── utils.py      # logging / robots / heuristics
Dependency Policy
Baseline libraries (installed via uv add):

Package	Purpose	Version
aiohttp	Async HTTP fetch	≥ 3.10 < 4
playwright	Dynamic page rendering	≥ 1.47 < 2
beautifulsoup4	HTML parsing	≥ 4.12 < 5
selectolax	Fast HTML traversal	≥ 0.3.24
lxml	HTML/XML parser	≥ 5 < 6
tenacity	Retries + back-off	≥ 8.5 < 9
typer	CLI framework	≥ 0.12 < 1
rich	Logging UI	≥ 13.8 < 14
tldextract	Domain scope	≥ 5 < 6
cssutils	CSS rewriting	≥ 2.9 < 3
orjson	Fast JSON	≥ 3.10 < 4

Flexibility clause:
If a demonstrably superior or more maintained alternative arises (e.g. httpx for aiohttp, pyppeteer for playwright, parsel for selectolax), substitution is ALLOWED provided it:

Offers equivalent or better async performance.

Preserves full offline mirroring functionality.

Maintains API compatibility or includes a clear adapter layer.

Updates pyproject.toml and uv.lock deterministically.

Otherwise, remain on the baseline stack above.

Core Behaviors
Crawler

Prefers aiohttp; switches to Playwright when JS/CSR needed.

BFS frontier with per-host concurrency, depth limits, include/exclude rules.

Resumable runs via metadata; respects robots.txt (default true).

Dynamic Mode

Playwright headless Chromium w/ auth, cookies, headers.

Wait modes: dom:idle, net:idle, ms:<delay>.

Bounded infinite-scroll loop (height/nodes/time).

Rewriting Rules
Target	Action
HTML	Rewrite href/src → relative paths.
CSS	Rewrite url() and @import.
JS	Conservative literal rewrites (no semantics change).
Headers	Strip CSP, SRI, crossorigin, referrerpolicy.
Assets	Inline ≤ 8 KiB as data: URIs.
SPA	Snapshot resolved DOM routes.

Normalization: .html extensions, _q_<hash> for queries, Unicode NFKC filenames.

Storage Layout
php-template
Copy code
mirror/
  ├── assets/<algo>/<prefix>/<hash>.<ext>
  ├── pages/.../index.html
  ├── metadata.json
  └── integrity.json
SHA-256 content addressed, hard-link de-duplication, timing + link maps.

Robustness and Performance
Retries + jitter (tenacity).

Per-origin rate-limit & back-off.

DNS/TLS/connect/read timeouts.

Skip unsupported schemes.

Safe filenames + path length guard.

≥ 64 concurrent fetches, ≥ 99 % resolved links, ≥ 25 % dedup savings.

Verification
Walk mirror → verify all refs resolve.

Launch --serve → self-crawl (200/304).

Emit integrity.json with totals + stats.

Security and Compliance
Default respect for robots.txt (override --ignore-robots).

Never execute mirrored JS offline.

Remove service workers + manifests.

Redact cookies / headers in logs.

Legal use only.

uv Run Aliases
Alias	Command
fmt	black . && ruff check .
lint	ruff check .
type	ty check src
test	pytest -q
e2e	Scrape https://example.com, serve, verify, exit 0

Success Criteria
✅ Offline mirror served via http://localhost:1337.
✅ No broken links.
✅ Deterministic re-runs.
✅ Passes all Astral CI aliases.
✅ Tagged v1.5.0.

Vault Secrets Automation
Secrets resolved from /srv/vault.

Loaders: 05-vault-loader.zsh, 10-secrets.zsh.

Never commit plaintext credentials.

Reference Vault paths only.
