from fastapi import APIRouter
from fastapi.responses import ORJSONResponse

def create_domains_router(domains_service, db_cache):
    router = APIRouter()

    @router.get("/visited_domains", response_class=ORJSONResponse)
    async def get_domains(from_, to_):
        try:
            domains = domains_service(db_cache, from_, to_)
            return ORJSONResponse({'domains': domains, 'status': 'ok'})
        except Exception as e:
            return ORJSONResponse({'status': e})

    return router
