import uvicorn

from fastapi import FastAPI
from api_visited_urls.db import init_db
from api_visited_urls.init_routers import init_routers


app = FastAPI()

db_cache = init_db()

init_routers(app, db_cache)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
