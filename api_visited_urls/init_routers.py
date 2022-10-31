from api_visited_urls.routers.links import create_links_router
from api_visited_urls.routers.domains import create_domains_router
from api_visited_urls.services.links import links_service
from api_visited_urls.services.domains import domains_service


def init_routers(app, db_cache):
    links_router = create_links_router(links_service, db_cache)
    domains_router = create_domains_router(domains_service, db_cache)
    app.include_router(links_router)
    app.include_router(domains_router)
