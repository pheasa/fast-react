from pydantic import BaseModel

class Sample(BaseModel):
    id: int
    title: str
