import time


def links_service(links, db_cache):
    current_time = time.time()
    for link in links:
        db_cache.lpush(current_time, link)
