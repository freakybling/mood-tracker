from flask import Flask,jsonify,request
import sqlite3

app = Flask(__name__)
DB = "notes.db"

def connect_db():
    return sqlite3.connect(DB)

#home page
@app.route('/')
def home():
    return jsonify("Welcome to my webapp.")


#Get all notes:
@app.route('/notes/get', methods = ['GET'])
def get_notes():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
                CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                mood TEXT NOT NULL)
                """)
    cur.execute("SELECT * FROM notes")
    rows = cur.fetchall()
    conn.close()

    notes= []
    for row in rows:
        notes.append({
            "id": row[0],
            "title": row[1],
            "content": row[2],
            "mood": row[3]
        })
    return jsonify(notes)


#Post note:
@app.route('/notes', methods = ['POST'])
def add_note():
    data = request.get_json()
    title = data.get("title")
    content = data.get("content")
    mood = data.get("mood")

    if not title or not content or not mood:
        return jsonify({"error": "all feilds are empty."}), 400
    
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO notes (title, content, mood) VALUES (?,?,?)", (title,content,mood))
    conn.commit()
    conn.close()

    return jsonify({"message": f"Note Added {title}"}), 201


#search note with keyword
@app.route('/notes/search', methods = ['GET'])
def search():
    keyword = request.args.get('keyword', "")
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM notes WHERE title LIKE ?", (f"%{keyword}%",))
    rows = cur.fetchall()
    conn.close()
    
    if not rows:
        return jsonify({"message": "No match found..."}), 404
    
    notes = []
    for row in rows:
        notes.append({
            "id": row[0],
            "title": row[1],
            "content": row[2],
            "mood": f"{row[3]}\n"
        })
    return jsonify(notes)


#update note:
@app.route('/notes/update/<int:id>', methods=['PUT'])
def update(id):
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')
    mood = data.get('mood')

    
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM notes WHERE id = ?", (id,))
    if not cur.fetchone():
        conn.close()
        return jsonify({"error": "Note not found"}), 404

    cur.execute("UPDATE notes SET title = ?, content =?, mood =? WHERE id=?", (title,content,mood,id))
    conn.commit()
    conn.close()
    
    return jsonify({"message":"Note update."})


#deleting a note:
@app.route('/notes/delete/<int:id>', methods=["DELETE"])
def delete(id):
    con = connect_db()
    cur = con.cursor()
    cur.execute("SELECT * FROM notes WHERE id =?", (id,))
    if not id:
        con.close()
        return jsonify({"message":"ID do not exists."}), 404
    cur.execute("DELETE FROM notes WHERE id =?",(id,))
    con.commit()
    con.close()
    return jsonify({"message": "The note is Deleted..."})




if __name__ == '__main__':
    app.run(debug=False)