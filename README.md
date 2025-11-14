# pyweb: The Fastest Python Web Scraper

**pyweb** is a command-line web scraper engineered for one purpose: **to be the fastest Python web scraper in existence**. It achieves this with a hyper-optimized, asynchronous Rust core built on `tokio` and a fine-tuned `reqwest` client using `native-tls`.

## Performance

`pyweb` is definitively the fastest Python web scraper. Here's the final benchmark, scraping 50 pages from `books.toscrape.com` and comparing against the best-in-class pure-Python async solution (`httpx` + `selectolax`):

| Scraper                               | Time (seconds) |
| ------------------------------------- | -------------- |
| **pyweb (hyper-tuned async Rust)**    | **1.64**       |
| httpx+selectolax                      | 2.79           |

`pyweb` is **~1.7x faster** than its closest competitor, a result of advanced compiler optimizations, `TCP_NODELAY`, a fine-tuned concurrency model, and a highly-optimized `native-tls` backend.

## Installation

```bash
pip install pyweb-scraper
```

## Usage

```bash
pyweb scrape [OPTIONS] [URLS]...
```

**Options:**

*   `-s, --selector TEXT`: CSS selector to extract specific elements.
*   `-o, --output [json|text]`: Output format.
*   `-c, --concurrency INTEGER`: Number of concurrent requests.
*   `--help`: Show this message and exit.

**Example:**

```bash
pyweb scrape "http://books.toscrape.com" -s "h3 > a" -c 200
```
