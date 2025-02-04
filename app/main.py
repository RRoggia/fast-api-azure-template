from fastapi import FastAPI
from app.routers.v1 import example_2
from app.routers.v1 import example_router

V1 = "/v1"

app = FastAPI()
app.include_router(example_router.example_router, prefix=V1)
app.include_router(example_2.example_router2, prefix=V1)


@app.get("/")
def hello_world():
    print("hello")
    return {"hello": "world"}


@app.get("/health")
def healthy():
    return {"health": 200}
