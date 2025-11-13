import requests
from bs4 import BeautifulSoup

async def scrape_website(url: str):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        soup = BeautifulSoup(response.content, "html.parser")
        # Replace this with your actual scraping logic
        # For example, to get all the links on a page:
        links = [a["href"] for a in soup.find_all("a", href=True)]
        return {"url": url, "links": links}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
