from app.web.mixins import AuthRequiredMixin
from aiohttp_apispec import docs, request_schema, response_schema, querystring_schema
from app.admin.schemes import AdminResponseSchema, AdminSchema
from aiohttp.web_response import json_response
from app.web.app import View
from aiohttp_session import new_session
from aiohttp.web_exceptions import HTTPForbidden, HTTPUnauthorized

class AdminLoginView(View):
    @docs(tags=['admin'], summary='login', description='Return auth cookie by email and password')
    @request_schema(AdminSchema)
    @response_schema(AdminResponseSchema, 200)
    async def post(self):
        email = self.data['email']
        password = self.data['password']
        admin = await self.store.admins.get_by_email(email)
        if not admin:
            raise HTTPForbidden
        if not admin.check_password(password):
            raise HTTPForbidden

        session = await new_session(self.request)
        raw_admin = AdminResponseSchema().dump(admin)
        session['admin'] = raw_admin
        return json_response(data={'admin': raw_admin})


class AdminCurrentView(AuthRequiredMixin, View):
    @docs(tags=['admin'], summary='Check auth cookie', description='Return admin email and id by cookie')
    @response_schema(AdminResponseSchema, 200)
    async def get(self):
        # if self.request.admin is None:
        #     raise HTTPUnauthorized
        return json_response(data={'admin': AdminResponseSchema().dump(self.request.admin)})

