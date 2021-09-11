from app.web.utils import json_response
from app.web.schemes import OkResponseSchema
from app.crm.schemes import ListUsersResponseSchema, UserAddSchema, UserGetRequestSchema, UserGetResponseSchema, UserSchema
import uuid

from app.crm.models import User
from app.web.app import View
from aiohttp_apispec import docs, request_schema, response_schema, querystring_schema
from aiohttp.web_exceptions import HTTPNotFound

class AddUserView(View):
    @docs(tags=['crm'], summary='Add new user', description='Add new user to database')
    @request_schema(UserAddSchema)
    @response_schema(OkResponseSchema, 200)
    async def post(self):
        data = self.request['data']
        user = User(id_=uuid.uuid4(), email=data['email'])
        await self.request.app.crm_accessot.add_user(user)
        print(self.request.app.database['users'])
        return json_response()

class ListUsersView(View):
    @docs(tags=['crm'], summary='List users', description='List of users in database')
    @response_schema(ListUsersResponseSchema, 200)
    async def get(self):
        users = await self.request.app.crm_accessot.list_users()
        raw_users = [{'email': user.email, 'id': str(user.id_)} for user in users]
        return json_response(data={'users': raw_users})

class GetUserView(View):
    @docs(tags=['crm'], summary='Get user', description='Get user by UUID from database')
    @querystring_schema(UserGetRequestSchema)
    @response_schema(UserGetResponseSchema , 200)
    async def get(self):
        user_id = self.request.query['id']
        user = await self.request.app.crm_accessot.get_user(uuid.UUID(user_id))
        if user:
            return json_response(data={'user': {'email': user.email, 'id': str(user.id_)}})
        else:
            raise HTTPNotFound
