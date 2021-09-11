from app.web.config import setup_config
from app.web.middlewares import setup_middlewares
from app.store import setup_accessors
from app.store.crm.accessor import CrmAccessor
from typing import Optional
from aiohttp.web import Application as AiohttpApplication, run_app as aiohttp_run_app, View as AiohttpView, Request as AiohttpRequest
from aiohttp_apispec import setup_aiohttp_apispec
from attr import dataclass
from app.web.routes import setup_routes


class Application(AiohttpApplication):
    database: dict = {}
    crm_accessot: Optional[CrmAccessor] = None

class Request(AiohttpRequest):
    @property
    def app(self) -> Application:
        return super().app


class View(AiohttpView):
    @property
    def request(self) -> Request:
        return super().request

app = Application()

def run_app():
    setup_config(app)
    setup_routes(app)
    setup_aiohttp_apispec(app, title='CRM App', url='/docs/json', swagger_path='/docs')
    setup_middlewares(app)
    setup_accessors(app)
    aiohttp_run_app(app)
