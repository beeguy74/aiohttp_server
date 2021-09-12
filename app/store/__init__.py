from app.store.database.database import Database
from app.store.crm.accessor import CrmAccessor
import typing
from app.store.admin.accessor import AdminAccessor

if typing.TYPE_CHECKING:
    from app.web.app import Application

def setup_accessors(app: "Application"):
    app.crm_accessot = CrmAccessor()
    app.on_startup.append(app.crm_accessot.connect)
    app.on_cleanup.append(app.crm_accessot.disconnect)

class Store:
    def __init__(self, app: "Application"):
        # from app.store.quiz.accessor import QuizAccessor
        # self.quizzes = QuizAccessor(app)
        self.admins = AdminAccessor(app)


def setup_store(app: "Application"):
    app.database = Database()
    app.store = Store(app)