from fastapi import FastAPI
from app.routers.v1 import example_2
from app.routers.v1 import example_router
from app.config import config

V1 = "/v1"

app = FastAPI()
app.include_router(example_router.example_router, prefix=V1)
app.include_router(example_2.example_router2, prefix=V1)

settings = config.Settings()


@app.get("/")
def hello_world():
    print("hello")
    print(settings.pg_username)
    return {"hello": "world"}


@app.get("/health")
def healthy():
    return {"health": 200}
