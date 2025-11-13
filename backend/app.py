from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Notes(BaseModel):
    id: int
    topic: str
    content: str

db = {}

@app.get("/")
def root():
    return {"message":"this is a new project"}

@app.post("/add_note")
def add_a_note(note: Notes):
    db[note.id] = note
    return {"message":"successfully entered the note in the db"}

@app.delete("/delete_by_ID/{note_id}")
def delete_a_note(note_id: int):
    if note_id in db:
        del db[note_id]
        return "Note has been deleted"
    raise HTTPException(status_code=404, detail="Note ID does not exist")

@app.put("/update_a_note/{note_id}")
def update_note(note_id: int, note: Notes):
    if note_id in db:
        db[note_id] = note
        return "Note has been updated"
    raise HTTPException(status_code=404, detail="Note ID does not exist")





