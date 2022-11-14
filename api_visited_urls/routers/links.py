from fastapi import APIRouter
from fastapi.responses import ORJSONResponse


def create_links_router(get_links_service, db_cache):
    router = APIRouter()

    @router.post("/visited_links", response_class=ORJSONResponse)
    async def collect_links(links: list):
        try:
            get_links_service(links, db_cache)
            return ORJSONResponse({'links': links, 'status': 'ok'})
        except Exception as e:
            return ORJSONResponse({'status': str(e)})

    return router
