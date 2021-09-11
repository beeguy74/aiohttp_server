from app.store.crm.models import ConnectInfo
import typing
import uuid
from app.crm.models import User
from typing import Optional

if typing.TYPE_CHECKING:
    from app.web.app import Application


class CrmAccessor:
    def __init__(self):
        self.app: Optional["Application"] = None

    #this called on signal of aiohttp app
    async def connect(self, app: "Application"):
        self.app = app

        # await db.set_bind(f"postgesql://{app.config.db_host}/{app.config.db_name}")
        # await db.gino.create_all()
        # await self._on_connect()
        
        print("connected to database")

    #this called on signal of aiohttp app
    async def _on_connect(self):
        await ConnectInfo.create()

    async def disconnect(self, app: "Application"):
        self.app = None
        # await db.pop_bind().close()
        print("disconnected from database")

    async def add_user(self, user: User):
        self.app.database['users'].append(user)

    async def list_users(self) ->list[User]:
        return self.app.database['users']

    async def get_user(self, id_: uuid.UUID) -> Optional[User]:
        for user in self.app.database["users"]:
            if user.id_ == id_:
                return user
        return None