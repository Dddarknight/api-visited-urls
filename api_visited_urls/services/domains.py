from urllib.parse import urlparse


def domains_service(db_cache, beginning_time, end_time):
    domains = []
    keys = db_cache.scan_iter(match='*')
    b_beginning_time = bytes(beginning_time, encoding='UTF-8')
    b_end_time = bytes(end_time, encoding='UTF-8')
    keys_within_period = [
        key for key in keys if (
            key >= b_beginning_time) and (key <= b_end_time)]

    for key in keys_within_period:
        for link in db_cache.lrange(key, 0, -1):
            link_str = link.decode('UTF-8')
            hostname = urlparse(link_str).hostname
            domain = hostname if hostname else urlparse(
                f'//{link_str}').hostname
            if domain not in domains:
                domains.append(domain)
    return domains