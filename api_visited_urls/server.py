import uvicorn

from fastapi import FastAPI
from api_visited_urls.routers import services


app = FastAPI()

app.include_router(services.router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
