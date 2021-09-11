from app.web.utils import check_basic_auth, json_response
from app.web.schemes import OkResponseSchema
from app.crm.schemes import ListUsersResponseSchema, UserAddSchema, UserGetRequestSchema, UserGetResponseSchema, UserSchema
import uuid

from aiohttp_apispec import docs, request_schema, response_schema, querystring_schema
from app.crm.models import User
from app.web.app import View
from aiohttp.web_exceptions import HTTPForbidden, HTTPNotFound, HTTPUnauthorized

class AddUserView(View):
    @docs(tags=['crm'], summary='Add new user', description='Add new user to database')
    @request_schema(UserAddSchema)#input data
    @response_schema(OkResponseSchema, 200)#output data
    async def post(self):
        data = self.request['data']
        user = User(id_=uuid.uuid4(), email=data['email'])
        await self.request.app.crm_accessot.add_user(user)
        print(self.request.app.database['users'])
        return json_response()

class ListUsersView(View):
    @docs(tags=['crm'], summary='List users', description='List of users in database')
    @response_schema(ListUsersResponseSchema, 200)#output data
    async def get(self):
        if not self.request.headers.get('Authorization'):
            raise HTTPUnauthorized
        if not check_basic_auth(self.request.headers['Authorization'], username=self.request.app.config.username, 
                                password=self.request.app.config.password):
            raise HTTPForbidden
        users = await self.request.app.crm_accessot.list_users()
        raw_users = [UserSchema().dump(user) for user in users]
        return json_response(data={'users': raw_users})

class GetUserView(View):
    @docs(tags=['crm'], summary='Get user', description='Get user by UUID from database')
    @querystring_schema(UserGetRequestSchema)
    @response_schema(UserGetResponseSchema , 200)#output data
    async def get(self):
        if not self.request.headers.get('Authorization'):
            raise HTTPUnauthorized
        if not check_basic_auth(self.request.headers['Authorization'], username=self.request.app.config.username, 
                                password=self.request.app.config.password):
            raise HTTPForbidden
        user_id = self.request.query['id']
        user = await self.request.app.crm_accessot.get_user(uuid.UUID(user_id))
        if user:
            return json_response(data={'user': UserSchema().dump(user)})
        else:
            raise HTTPNotFound
