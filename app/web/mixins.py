from aiohttp.web_response import StreamResponse
from app.web.app import View
from aiohttp.web_exceptions import HTTPUnauthorized

# Add autorization to View
class AuthRequiredMixin(View):
    async def _iter(self) -> StreamResponse:#redefine original def _iter of Aiohttp class View
        if not self.request.admin:
            raise HTTPUnauthorized
        return await super(AuthRequiredMixin, self)._iter()

