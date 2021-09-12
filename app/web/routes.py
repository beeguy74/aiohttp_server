from aiohttp.web_app import Application
from app.crm.routes import setup_routes as crm_setup_routes
from app.admin.routes import setup_routes as admin_setup_routes

def setup_routes(app: Application):
    crm_setup_routes(app)
    admin_setup_routes(app)