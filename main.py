from fastapi import FastAPI
from scraper import scrape_website

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to the PyWeb Scraper API"}

@app.get("/scrape")
async def scrape(url: str):
    data = await scrape_website(url)
    return {"data": data}
