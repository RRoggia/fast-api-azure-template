from pydantic import BaseModel


class PostBody(BaseModel):
    id: int
    name: str
    address: str
    optional: str | None = None
