from app.web.logger import setup_logging
from app.web.config import Config, setup_config
from app.web.middlewares import setup_middlewares
from app.store import setup_accessors
from app.store.crm.accessor import CrmAccessor
from typing import Optional
from aiohttp.web import Application as AiohttpApplication, run_app as aiohttp_run_app, View as AiohttpView, Request as AiohttpRequest
from aiohttp_apispec import setup_aiohttp_apispec
from attr import dataclass
from app.web.routes import setup_routes
from aiohttp_session import setup as session_setup
from aiohttp_session.cookie_storage import EncryptedCookieStorage
from app.store import setup_store, Store
from app.admin.models import Admin

class Application(AiohttpApplication):
    config: Optional[Config] = None
    databaseN: dict = {}
    crm_accessot: Optional[CrmAccessor] = None
    store: Optional[Store] = None

class Request(AiohttpRequest):
    admin: Optional[Admin] = None

    @property
    def app(self) -> Application:
        return super().app


class View(AiohttpView):
    @property
    def request(self) -> Request:
        return super().request

    @property
    def store(self) -> Store:
        return self.request.app.store

    @property
    def data(self) -> dict:
        return self.request.get("data", {})

app = Application()

# application setup
def run_app():
    setup_logging(app)
    setup_config(app)#read config from yaml
    session_setup(app, storage=EncryptedCookieStorage(secret_key=app.config.session.key))
    setup_aiohttp_apispec(app, title='CRM App', url='/docs/json', swagger_path='/docs')#data validationa and setup swagger on 0.0.0.0:8080/docs
    setup_routes(app)#tunes app's routes and connects with "views"
    setup_middlewares(app)#another validation and error management
    setup_store(app)
    setup_accessors(app)#works with databases in memory, but we can add sql and something
    aiohttp_run_app(app)#start app
