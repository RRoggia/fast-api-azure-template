from fastapi import APIRouter
from app.models.post_body import PostBody

example_router = APIRouter()


@example_router.get("/example/")
def get_example():
    return [{"get": "example"}]


@example_router.post("/example/", response_model=PostBody, status_code=201)
def post_example(post_body: PostBody):
    return post_body
