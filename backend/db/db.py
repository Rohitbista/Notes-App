from supabase import create_client
from models.note import Notes
from config.settings import SUPABASE_KEY, SUPABASE_URL

supabase_key = SUPABASE_KEY
supabase_url = SUPABASE_URL

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



