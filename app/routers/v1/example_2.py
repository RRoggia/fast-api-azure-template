from fastapi import APIRouter

example_router2 = APIRouter()


@example_router2.get("/example2/")
def get_example():
    return [{"get": "example"}]
