import redis
import time
from fastapi.testclient import TestClient
from api_visited_urls.server import app
from api_visited_urls.routers import services


client = TestClient(app)

r = redis.Redis(db=15)

FIXTURE1 = [
    "https://ya.ru",
    "https://ya.ru?q=123",
    "funbox.ru",
    "https://stackoverflow.com/questions/11828270/how-to-exit-the-vim-editor"
]

FIXTURE2 = [
    "https://www.google.com",
    "https://www.google.com/?q=456",
    "funbox.ru"
]

DOMAINS = ['ya.ru', 'funbox.ru', 'stackoverflow.com', 'www.google.com']


def test_app(monkeypatch):
    monkeypatch.setattr(
        services, 'r', r)

    beginning_time = time.time()
    response_post = client.post("/visited_links", json=FIXTURE1)
    for link in FIXTURE1:
        assert link in response_post.text

    client.post("/visited_links", json=FIXTURE2)

    end_time = time.time()
    response_get = client.get(
        f"/visited_domains?from_={beginning_time}&to_={end_time}")
    for domain in DOMAINS:
        assert domain in response_get.text
    r.flushdb()
    
