import os
from supabase import create_client
from dotenv import load_dotenv
from models.note import Notes

load_dotenv()

supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")

supabase = create_client(supabase_url, supabase_key)

def save_to_db(note: Notes):
    print(note.id, "    ", note.topic, "    ", note.content)
    response = supabase.table("notes_app_database").insert({"id":note.id, "topic":note.topic, "content":note.content}).execute()
    return response

def delete_from_db(note_id: int):
    response = supabase.table("notes_app_database").delete().eq("id", note_id).execute()
    return response

def update_in_db(note_id: int, note: Notes):
    response = supabase.table("notes_app_database").update({"topic":note.topic, "content":note.content}).eq("id", note_id).execute()
    return response

def print_from_db():
    response = supabase.table("notes_app_database").select("*").execute()
    return response.data

def get_one_from_db(note_id:int):
    response = supabase.table("notes_app_database").select("*").eq("id", note_id).execute()
    if response.data:
        return response.data[0]
    return None



