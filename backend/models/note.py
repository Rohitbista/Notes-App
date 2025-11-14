from pydantic import BaseModel

class Notes(BaseModel):
    id: int
    topic: str
    content: str
