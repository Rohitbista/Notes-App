from pydantic import BaseModel

class Notes(BaseModel):
    id: int
    topic: str
    content: str

class NoteCreate(BaseModel):    # Without requiring note id creating new note
    topic: str
    content: str

class NoteUpdate(BaseModel):
    topic: str
    content: str
