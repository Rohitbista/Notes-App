from fastapi import FastAPI, HTTPException
from models.note import Notes
from db import save_to_db, delete_from_db, update_in_db, print_from_db, get_one_from_db

app = FastAPI()

db = {}

@app.get("/")
def root():
    return {"message":"this is a new project"}

@app.get("/view_notes")
def see_all_notes():
    if print_from_db():
        return print_from_db()
    raise HTTPException(status_code=404, detail="Note App database is empty")

@app.post("/add_note")
def add_a_note(note: Notes):
    if get_one_from_db(note.id):
        print(get_one_from_db(note.id))
        raise HTTPException(status_code=404, detail="Note ID already exists")
    save_to_db(note)
    return get_one_from_db(note.id)

@app.delete("/delete_by_ID/{note_id}")
def delete_a_note(note_id: int):
    if get_one_from_db(note_id):
        delete_from_db(note_id)
        return {"message":f"Note with Note ID {note_id} has been successfully deleted"}
    raise HTTPException(status_code=404, detail="Note ID does not exist")

@app.put("/update_a_note/{note_id}")
def update_note(note_id: int, note: Notes):
    if get_one_from_db(note_id):
        return update_in_db(note_id, note).data
    raise HTTPException(status_code=404, detail="Note ID does not exist")






