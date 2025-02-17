from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging
from app.routers.v1 import example_2
from app.routers.v1 import example_router
from app.config import config
import httpx

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


@app.get("/rescomp")
def res_comp():
    return {"answer": "from comp"}


@app.get("/reqcomp")
def req_comp():
    print(">>>>>>>>>>>>>>>>>>>>")
    print(settings.comp_api_url)
    client = httpx.Client()
    response = client.get(f"{settings.comp_api_url}/rescomp")
    return response.json()


@app.get("/health")
def healthy():
    return {"health": 200}
