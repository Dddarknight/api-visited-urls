import time
import redis
from fastapi import APIRouter
from fastapi.responses import ORJSONResponse
from api_visited_urls.routers.utils import get_domains_for_period


router = APIRouter()

r = redis.Redis(db=1)


@router.post("/visited_links", response_class=ORJSONResponse)
async def collect_links(links: list):
    current_time = time.time()
    try:
        for link in links:
            r.lpush(current_time, link)
        return ORJSONResponse({'links': links, 'status': 'ok'})
    except Exception as e:
        return ORJSONResponse({'status': e})


@router.get("/visited_domains", response_class=ORJSONResponse)
async def get_domains(from_, to_):
    try:
        domains = get_domains_for_period(r, from_, to_)
        return ORJSONResponse({'domains': domains, 'status': 'ok'})
    except Exception as e:
        return ORJSONResponse({'status': e})
