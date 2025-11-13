# PyWeb Scraper

A hyper modern Python web scraper using FastAPI, Requests, and BeautifulSoup.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/afadesigns/pyweb.git
   ```
2. Navigate to the project directory:
   ```bash
   cd pyweb
   ```
3. Create a virtual environment:
   ```bash
   uv venv
   ```
4. Activate the virtual environment:
   ```bash
   source .venv/bin/activate
   ```
5. Install the dependencies:
   ```bash
   uv pip install -r requirements.txt
   ```

## Usage

1. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```
2. Open your browser and navigate to `http://127.0.0.1:8000`.
3. To scrape a website, use the `/scrape` endpoint with a `url` query parameter:
   `http://127.0.0.1:8000/scrape?url=https://www.google.com`
