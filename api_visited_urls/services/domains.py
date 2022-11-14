from urllib.parse import urlparse


def get_domains_service(db_cache, beginning_time, end_time):
    domains = []
    keys = db_cache.scan_iter(match='*')
    beginning_time_bytes = bytes(beginning_time, encoding='UTF-8')
    end_time_bytes = bytes(end_time, encoding='UTF-8')
    keys_within_period = [
        key for key in keys if (
            key >= beginning_time_bytes) and (key <= end_time_bytes)]

    for key in keys_within_period:
        for db_link in db_cache.lrange(key, 0, -1):
            link = db_link.decode('UTF-8')
            hostname = urlparse(link).hostname
            domain = hostname if hostname else urlparse(
                f'//{link}').hostname
            if domain not in domains:
                domains.append(domain)
    return domains
