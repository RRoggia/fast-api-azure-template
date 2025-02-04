from fastapi import APIRouter

example_router = APIRouter()

@example_router.get("/example/" )
def get_example():
    return [{"get": "example"}]
