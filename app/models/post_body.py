from pydantic import BaseModel


class PostBody(BaseModel):
    id: int
    name: str
    optional: str | None = None
