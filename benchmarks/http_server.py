import asyncio
from aiohttp import web
import os

ROOT = os.path.dirname(__file__)

async def handle(request):
    with open(os.path.join(ROOT, "test_page.html"), "r") as f:
        return web.Response(text=f.read(), content_type='text/html')

async def main():
    app = web.Application()
    app.router.add_get('/test_page.html', handle)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '127.0.0.1', 8000)
    await site.start()
    await asyncio.Future()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass