import sqlite3
import time

conn = sqlite3.connect("note-app.db")
cur = conn.cursor()

#creating a table
cur.execute("""
            CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            mood TEXT NOT NULL)
            """)
conn.commit()


def search_note():
     keyword = input("\n🔍 Enter keyword to search in title: ").strip()
     cur.execute("SELECT * FROM notes WHERE title LIKE ?", (f"%{keyword}%",))
     rows = cur.fetchall()

     if rows:
        print("\n📌 Matching notes:")
        for row in rows:
            print(f"ID: {row[0]}, Title: {row[1]}, Mood: {row[3]}")
     else:
        print("❌ No matching notes found.")
     time.sleep(4)
     return rows, keyword

def delete_by_id():
    try:
        id_to_delete = int(input("Entere ID to delete: "))
        cur.execute("DELETE FROM notes WHERE id = ?", (id_to_delete))
        conn.commit()
        print("note deleted")
    except ValueError:
        print("Error, enter valid number.")

def delete_all_by_keyword():
    rows, keyword = search_note()
    if rows:
        confirm = input(f"Do your really want to delete all notes of this keyword {keyword}?(Yes/No)").lower()
        if confirm == "yes":
            cur.execute("DELETE FROM notes WHERE title LIKE ?", (f"%{keyword}%",))
            conn.commit()
        else:
            print("cancelled.")
    else:
        print("No notes to delete.")

def update_note():
    try:
        update_id = int(input("📝 Enter ID of the note to update: "))
        new_title = input("Enter new title: ")
        new_content = input("Enter new content: ")
        new_mood = input("Enter your mood: ")

        cur.execute("""
                    UPDATE notes SET title = ?, content = ?, mood = ? 
                    WHERE id = ?
                    """,(new_title, new_content, new_mood, update_id))
        conn.commit()
    except ValueError:
        print("Enter valid input.")

def add_note():
    title = input("🆕 Title: ")
    content = input("Content: ")
    mood = input("Mood: ")
    cur.execute("INSERT INTO notes (title,content,mood) VALUES (?,?,?)", (title,content,mood))
    conn.commit()
    print("Note added")


while True:
    print("\n")
    print("*"*40)
    print("📒 NOTES APP MENU")
    print("1. Add a new note")
    print("2. Search notes")
    print("3. Delete a note by ID")
    print("4. Delete all notes by keyword")
    print("5. Update a note")
    print("6. Show all notes")
    print("7. Exit")
    print("*"* 40)

    try:
        choice = int(input("\nEnter your choice: "))
        
    except ValueError:
        print("invalid input, try again.")
        continue
    if choice == 1:
        add_note()
    elif choice == 2:
        search_note()
    elif choice == 3:
        delete_by_id()
    elif choice == 4:
        delete_all_by_keyword()
    elif choice == 5:
        update_note()
    elif choice == 6:
        cur.execute("SELECT * FROM notes")
        rows = cur.fetchall()
        for row in rows:
            print("\n",row)
            time.sleep(.5)
    elif choice == 7:
        print("\n👋 Exiting... Goodbye!\n")
        break
    else:
        print("\n❌ Invalid option. Try again.\n")


conn.close()