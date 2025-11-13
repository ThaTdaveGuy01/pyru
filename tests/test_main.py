import pytest
from httpx import AsyncClient, ASGITransport
from main import app

@pytest.mark.asyncio
async def test_root():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the PyWeb Scraper API"}

@pytest.mark.asyncio
async def test_scrape_get():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.get("/scrape?url=https://example.com")
    assert response.status_code == 200
    assert "data" in response.json()
    assert "links" in response.json()["data"]

@pytest.mark.asyncio
async def test_scrape_post():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.post("/scrape", json={"url": "https://example.com", "selector": "h1"})
    assert response.status_code == 200
    assert "data" in response.json()
    assert "elements" in response.json()["data"]
    assert response.json()["data"]["elements"] == ["Example Domain"]
