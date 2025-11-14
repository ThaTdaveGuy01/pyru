# pyweb: The Fastest Python Web Scraper

**pyweb** is a command-line web scraper built for one thing: **speed**. It uses a true asynchronous Rust core, built on `tokio` and `hyper`, to achieve unrivaled performance.

## Performance

`pyweb` is the fastest Python web scraper. Here's how it compares to the best-in-class pure-Python async solution (`httpx` + `selectolax`) when scraping 50 pages from `books.toscrape.com`:

| Scraper               | Time (seconds) |
| --------------------- | -------------- |
| **pyweb (async Rust)**| **1.49**       |
| httpx+selectolax      | 2.99           |

`pyweb` is **~2x faster** than its closest competitor, demonstrating the raw power of a purpose-built, asynchronous Rust core.

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
*   `--help`: Show this message and exit.

**Example:**

```bash
pyweb scrape "http://books.toscrape.com" -s "h3 > a"
```
