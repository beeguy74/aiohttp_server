from aiohttp.web import Application as AiohttpApplication, run_app as aiohttp_run_app
from attr import dataclass
from app.web.routes import setup_routes


class Application(AiohttpApplication):
    dataclass: dict = {}

app = Application()

def run_app():
    setup_routes(app)
    aiohttp_run_app(app)
