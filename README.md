# mood-tracker
A simple Flask-based API to create, read, update, search, and delete notes with mood tracking. Notes are stored in an SQLite database.

# 📝 MoodTracker CLI Notes App (exe)

This is a simple **command-line notes application** written in Python using `sqlite3`. It allows users to:

- Add notes with a title, content, and mood
- Search notes by keywords in the title
- Delete individual notes or all notes with a specific keyword
- Update existing notes
- View all notes in the database

## 📦 Features (exe)

- ✅ Local storage with SQLite
- ✅ Auto-incremented unique note ID
- ✅ Mood tracking
- ✅ Search, Update, and Delete functionality
- ✅ Simple CLI interface
- ✅ Lightweight and beginner-friendly

---

## 💻 How to Run (exe)

Make sure you have Python installed. Then:

download .exe file to make it run in your cmd.

---

# Notes Management Flask API

A simple Flask-based API to create, read, update, search, and delete notes with mood tracking. Notes are stored in an SQLite database.

---

## 📚 Features

* Add a new note with title, content, and mood
* View all notes
* Search notes by keyword in title
* Update an existing note by ID
* Delete a note by ID

---

## 🌐 Endpoints

### 1. `GET /`

**Description:** Welcome message with usage hint

---

### 2. `GET /notes/get`

**Description:** Fetch all notes

**Returns:**

```json
[
  {
    "id": 1,
    "title": "...",
    "content": "...",
    "mood": "..."
  },
  ...
]
```

---

### 3. `POST /notes`

**Description:** Add a new note

**Request Body:**

```json
{
  "title": "My Note",
  "content": "This is a note.",
  "mood": "Happy"
}
```

**Returns:**

```json
{
  "message": "Note Added My Note"
}
```

---

### 4. `GET /notes/search?keyword=your_keyword`

**Description:** Search notes by title keyword

**Returns:** Array of matching notes or message if not found.

---

### 5. `PUT /notes/update/<id>`

**Description:** Update a note by ID

**Request Body:**

```json
{
  "title": "Updated Title",
  "content": "Updated Content",
  "mood": "Excited"
}
```

---

### 6. `DELETE /notes/delete/<id>`

**Description:** Delete a note by ID

**Returns:**

```json
{
  "message": "The note is Deleted..."
}
```

---

## 🔧 Setup Instructions

1. Clone the repo or copy the code.
2. Make sure you have Flask and `requests` installed:

```bash
pip install flask requests
```

3. Run the app:

```bash
python app.py
```

4. Access it on `http://127.0.0.1:5000`

---

## 📊 Tech Stack

* Python
* Flask
* SQLite3
* Postman or `requests` for API testing

---

## 🚀 Future Improvements

* Add web frontend (HTML/CSS/JS)
* Add authentication (login/signup)
* Export notes as PDF or TXT

---