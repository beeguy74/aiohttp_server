from app.admin.schemes import AdminResponseSchema, AdminSchema
from aiohttp.web_response import json_response
from app.web.app import View
from aiohttp_session import new_session
from aiohttp_apispec import json_schema
from aiohttp.web_exceptions import HTTPForbidden


class AdminLoginView(View):
    @json_schema(AdminSchema)
    async def post(self):
        email = self.data['email']
        password = self.data['password']
        admin = await self.store.admins.get_by_email(email)
        if not admin:
            raise HTTPForbidden
        if not admin.check_password(password):
            raise HTTPForbidden

        session = await new_session(self.request)
        session['admin'] = email

        return {'admin': AdminResponseSchema().dump(admin)}


class AdminCurrentView(View):
    async def get(self):
        raise NotImplementedError
