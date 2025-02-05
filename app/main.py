from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging
from app.routers.v1 import example_2
from app.routers.v1 import example_router
from app.config import config

V1 = "/v1"

settings = config.Settings()

app = FastAPI()
app.include_router(example_router.example_router, prefix=V1)
app.include_router(example_2.example_router2, prefix=V1)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors,
    allow_methods=["*"],
    allow_headers=["*"],
)

logger = logging.getLogger(__name__)


@app.get("/")
def hello_world():
    logger.info(">>>>>>>>>>>>> logging")

    print("hello")
    print(settings.pg_username)
    return {"hello": "world"}


@app.get("/health")
def healthy():
    return {"health": 200}
