import sqlite3
from datetime import datetime
from pathlib import Path


APP_NAME = "suca"

DB_PATH = Path.home() / f".{APP_NAME}" / "databases" / "notes.db"



def init_db():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS notes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        created_at TEXT NOT NULL,
        updated_at TEXT,
        title TEXT,
        content TEXT NOT NULL,
        tags TEXT
    )
    """)
    
    conn.commit()
    conn.close()


def create_note():
    title = input("Title: ")
    content = input("Content: ")
    tags = input("Tags (comma separated): ")
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute(
        """
        INSERT INTO notes (created_at, title, content, tags)
        VALUES (?, ?, ?, ?)
        """,
        (
            datetime.now().isoformat(),
            title,
            content,
            tags
        )
    )
    
    conn.commit()
    conn.close()
    
    print("Note created.")
    

def list_notes():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor
    
    cursor.execute("SELECT id, title, created_at FROM notes")
    
    notes = cursor.fetchall()
    
    conn.close()
    
    if not notes:
        print("No notes found.")
        return
    
    for note in notes:
        print(f"[{note[0]}] {note[1]} - {note[2]}")
        
def view_note():
    note_id = input("Note ID: ")
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute(
        "SELECT * FROM notes WHERE id = ?",
        (note_id,)
    )
    
    note = cursor.fetchone()
    
    conn.close()
    
    if note:
        print(f"\nTitle: {note[3]}")
        print(f"Created: {note[1]}")
        print(f"Tags: {note[5]}")
        print("\n" + note[4])
    else:
        print("Note not found.")
        

def delete_note():
    note_id = input("Note ID: ")
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute(
        "DELETE FROM notes WHERE id = ?",
        (note_id,)
    )
    
    conn.commit()
    conn.close()
    
    print("Note deleted.")


def notes_menu():
    while True:
        command = input("notes> ")
        
        if command == "add":
            create_note()
        elif command == "list":
            list_notes()
        elif command == "view":
            view_note()
        elif command == "delete":
            delete_note()
        elif command == "help":
            print("help")
            print("add")
            print("delete")
            print("list")
            print("view")
            print("exit")
        elif command == "exit":
            break
        else:
            print("type help for commands")