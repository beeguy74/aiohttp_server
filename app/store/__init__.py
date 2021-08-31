from app.store.crm.accessor import CrmAccessor
import typing

if typing.TYPE_CHECKING:
    from app.web.app import Application

def setup_accessors(app: "Application"):
    app.crm_accessot = CrmAccessor()
    app.on_startup.append(app.crm_accessot.connect)
    app.on_cleanup.append(app.crm_accessot.disconnect)