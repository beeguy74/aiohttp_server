from app.store.crm.models import ConnectInfo
import typing
import uuid
from app.crm.models import User
from typing import Optional
from app.store.crm.gino import db

if typing.TYPE_CHECKING:
    from app.web.app import Application



class CrmAccessor:
    def __init__(self):
        self.app: Optional["Application"] = None

    #this called on signal of aiohttp app
    async def connect(self, app: "Application"):
        self.app = app

        try:
            self.app.databaseN['users']
        except KeyError:
            self.app.databaseN['users'] = []

        await db.set_bind(f"postgresql://{app.config.db_host}/{app.config.db_name}")
        await db.gino.create_all()
        await self._on_connect()
        
        print("connected to databaseN")

    #this called on signal of aiohttp app
    async def _on_connect(self):
        await ConnectInfo.create()

    async def disconnect(self, app: "Application"):
        self.app = None
        await db.pop_bind().close()
        print("disconnected from databaseN")

    async def add_user(self, user: User):
        self.app.databaseN['users'].append(user)

    async def list_users(self) ->list[User]:
        return self.app.databaseN['users']

    async def get_user(self, id_: uuid.UUID) -> Optional[User]:
        for user in self.app.databaseN["users"]:
            if user.id_ == id_:
                return user
        return None