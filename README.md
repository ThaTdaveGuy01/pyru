# PyWeb Scraper

A hyper modern Python web scraper CLI, designed for speed.

## Performance

`pyweb` is designed to be the fastest Python web scraper. It uses a combination of `aiohttp`, `selectolax`, and `uvloop` to achieve maximum performance.

In a benchmark scraping 1000 pages from a local web server, `pyweb` outperformed `Scrapy` by a significant margin:

| Scraper | Time (seconds) |
|---|---|
| **pyweb** | **0.14** |
| Scrapy | 113.86 |

*Benchmark details: Scraping 1000 identical pages from a local web server to isolate parsing and processing speed. The task was to extract 10 specific paragraph elements from each page.*

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/afadesigns/pyweb.git
   ```
2. Navigate to the project directory:
   ```bash
   cd pyweb
   ```
3. Install the project:
   ```bash
   pip install .
   ```

## Usage

### Basic Scraping (get all links)
```bash
pyweb scrape https://example.com
```

### Scraping Multiple URLs
```bash
pyweb scrape https://example.com https://google.com
```

### Scraping with a CSS Selector
```bash
pyweb scrape https://example.com --selector "h1"
```

### Changing Output Format
```bash
pyweb scrape https://example.com -s "h1" -o json
```
