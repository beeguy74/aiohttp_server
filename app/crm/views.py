import uuid
from app.crm.models import User
from app.web.app import View
from aiohttp.web_response import json_response

class AddUserView(View):
    async def post(self):
        data = await self.request.json()
        user = User(_id=uuid.uuid4(), email=data['email'])
        await self.request.app.crm_accessot.add_user(user)
        print(self.request.app.database['users'])
        return json_response(data={'status': 'ok'})
