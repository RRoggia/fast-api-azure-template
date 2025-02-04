from fastapi import FastAPI
from app.routers.v1.example_2 import example_router2
from app.routers.v1.example_router import example_router

app = FastAPI()
app.include_router(example_router, prefix="/v1")
app.include_router(example_router2, prefix="/v1")


@app.get("/")
def hello_world():
    print("hello")
    return {"hello": "world"}


@app.get("/health")
def healthy():
    return {"health": 200}
