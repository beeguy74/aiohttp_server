from app.admin.models import Admin
import json

from aiohttp_session import get_session
from marshmallow.fields import Email
from app.web.utils import error_json_response
import typing
from aiohttp.web_exceptions import HTTPException, HTTPForbidden, HTTPUnauthorized, HTTPUnprocessableEntity
from aiohttp.web_middlewares import middleware
from aiohttp_apispec import validation_middleware

if typing.TYPE_CHECKING:
    from app.web.app import Application, Request

#Add "admin" to the request from the cookie
@middleware
async def auth_middleware(request: "Request", handler):
    session = await get_session(request)
    if request.cookies.get('AIOHTTP_SESSION') and not session.get('admin'): #invalid cookie
        raise HTTPForbidden
    if session.get('admin'):
        request.admin = Admin(
            id=session['admin']['id'],
            email=session['admin']['email'],
        )
    else:
        request.admin = None
    return await handler(request)

@middleware
async def error_handling_middleware(request: "Request", handler):
    try:
        print("try in midleware")
        response = await handler(request)
        return response
    except HTTPUnprocessableEntity as e:
        return error_json_response(http_status=400, status='bad request', message=e.reason, data=json.loads(e.text))
    except HTTPException as e:
        return error_json_response(http_status=e.status, status='error', message=str(e))
    except Exception as e:
        return error_json_response(http_status=500, status='internal server error', message=str(e))


def setup_middlewares(app: "Application"):
    app.middlewares.append(auth_middleware)
    app.middlewares.append(error_handling_middleware)
    app.middlewares.append(validation_middleware)

