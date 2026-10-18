## Week 2 Homework: Notes CRUD API and Weekend Activity How Is AI Changing Cloud Computing

#### **Part 1** Week 2 Homework 1: Simple CRUD with FastAPI and SQLite

I have used:

- Github reporitory **https://github.com/warestack/cc** has been cloned and personal repository **https://github.com/the-coder-alchemist/advance-cloud-computing** has been created
- Pull commands are coming from **https://github.com/warestack/cc** and push commands go to **https://github.com/the-coder-alchemist/advance-cloud-computing** 
- `gitignore` file prepared and notes.db added
- `main.py` used for the main python file
- the homework is located inside `\class-2\week2-notes-crud`
- one `venv` is used for the overall module as it I have noticed in the past that it takes a lot of storage in my limited storage capacity on my machine to have separate .venv per week
- one `requirements.txt` has been created as I have limited storage capacity in my machine for one load for every week.


#### **Part 2** Week2 Weekend Activity:How Is AI Changing Cloud Computing

I have used:

- `cloud-and-ai.md` for the main document file for the week2 weekend activity assignment
- the homework is located inside `\class-2\week2-cloud-ai`
- read homework for [Weekend Activity: Cloud and AI](../week2-cloud-ai/cloud-and-ai.md)


#### Folder Structure


```text
class-2/
    week2-cloud-ai/
        cloud-and-ai.md
    week2-notes-crud
        main.py
        notes.db
        README.md
requirements.txt
.venv/
```



#### Part 1.1: Create a Virtual Environment

A **venv (virtual environment)** is an isolated Python environment created for a specific project. It allows each project to have its own libraries and package versions without affecting other Python projects on your computer.

1.1.a. Create a virtual environment:

```bash
python3 -m venv .venv
```

On Windows, use one of these if `python3` does not work:

```powershell
python -m venv .venv
py -m venv .venv
```

1.1.b. Activate the virtual environment.

On macOS/Linux:

```bash
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.venv\Scripts\Activate.ps1
```

When the environment is active, you should see `(.venv)` at the start of the terminal line.


#### Part 1.2: Create and install `requirements.txt`

1.2.a. Create a new file in VS Code called `requirements.txt` if it doesn't exist, dependent if you would like a `.venv` per week then this will be created on a per week folder basis, I have used one for the whole module:

```text
requirements.txt
```

1.2.b. Add these lines, more files can always be added:

```text
fastapi==0.141.1;
uvicorn==0.52.4;
```

1.2.c Save the file.

> `requirements.txt` is a list of packages needed by the project. It helps everyone install the same dependencies.

1.2.d. Install the packages:

```bash
python -m pip install -r requirements.txt
```

1.2.e. Check the installed packages:

```bash
python -m pip list
```

You should see `fastapi` and `uvicorn`.



#### Python code for `main.py`:

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pathlib import Path
import sqlite3

app = FastAPI()

DATABASE_PATH = Path(__file__).resolve().parent / "notes.db"


class NoteCreate(BaseModel):
    title: str
    text: str


class NoteUpdate(BaseModel):
    title: str | None = None
    text: str | None = None


def get_connection():
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def create_table():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            text TEXT NOT NULL
        )
        """
    )
    connection.commit()
    connection.close()


create_table()


@app.get("/")
def home():
    return {"message": "Notes API is running"}


@app.get("/notes")
def get_notes():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM notes ORDER BY id")
    rows = cursor.fetchall()
    connection.close()
    return [dict(row) for row in rows]


@app.get("/notes/{note_id}")
def get_note(note_id: int):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM notes WHERE id = ?", (note_id,))
    row = cursor.fetchone()
    connection.close()

    if row is None:
        raise HTTPException(status_code=404, detail="Note not found")

    return dict(row)


@app.post("/notes", status_code=201)
def create_note(note: NoteCreate):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO notes (title, text) VALUES (?, ?)",
        (note.title, note.text)
    )
    connection.commit()
    note_id = cursor.lastrowid
    connection.close()
    return {"id": note_id, "title": note.title, "text": note.text}


@app.patch("/notes/{note_id}")
def update_note(note_id: int, note: NoteUpdate):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM notes WHERE id = ?", (note_id,))
    existing = cursor.fetchone()

    if existing is None:
        connection.close()
        raise HTTPException(status_code=404, detail="Note not found")

    new_title = note.title if note.title is not None else existing["title"]
    new_text = note.text if note.text is not None else existing["text"]

    cursor.execute(
        "UPDATE notes SET title = ?, text = ? WHERE id = ?",
        (new_title, new_text, note_id)
    )
    connection.commit()
    connection.close()

    return {"id": note_id, "title": new_title, "text": new_text}


@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM notes WHERE id = ?", (note_id,))
    existing = cursor.fetchone()

    if existing is None:
        connection.close()
        raise HTTPException(status_code=404, detail="Note not found")

    cursor.execute("DELETE FROM notes WHERE id = ?", (note_id,))
    connection.commit()
    connection.close()

    return {"message": "Note deleted"}
```



#### Part 1.3:Run the **API** and test ech endpoint.

1.3.a Run the app:

```bash
uvicorn main:app --reload
```

1.3.b. Open FastAPI docs:

```text
http://127.0.0.1:8000/docs
```

The server starts at `http://127.0.0.1:8000`. Interactive docs are at
`http://127.0.0.1:8000/docs`. The app creates `notes.db` on
startup, so notes persist between server restarts. 



1.3.c Expand `POST /notes` in `/docs`, click **Try it out**, replace the example request body with the JSON below, and click **Execute**:

```json
{
  "title": "First note",
  "text": "This note is stored in SQLite."
}
```

The response should have status **201** and include the created note's `id`. Record that ID; use it in all following requests. The app creates `notes.db` beside `main.py` on startup, and notes persist between server restarts.

1.3.d. Open in the browser:

```text
http://127.0.0.1:8000/notes
```

You should see your note.

1.3.e. In `/docs`, expand `GET /notes/{note_id}`, click **Try it out**, enter the ID returned by `POST`, and click **Execute**. Expect `200` and that note.

1.3.f. Test `PATCH /notes/{note_id}` with the same ID and this JSON body:

```json
{"title": "Updated first note"}
```

Expect `200`. The title changes and the text stays the same. Repeat using your own note content and update only the `text` field.

1.3.g. Stop the server with `Ctrl + C`, restart it, and read the note again. Its changes should still be present.

1.3.h. Test `DELETE /notes/{note_id}` with the same ID. Expect `200` and `{"message":"Note deleted"}`. Read that ID again; expect `404` and `{"detail":"Note not found"}`.

1.3.i. Choose an ID that is absent from `GET /notes`, such as `9999`. Send `PATCH /notes/9999` with `{"title":"Missing note test"}`, then `DELETE /notes/9999`; both should return `404`. Send `POST /notes` with `{"title":"Incomplete note"}` and no text; expect `422`, meaning the request body did not match the required model.


1.3.j. Stop the server with once all task is completed

`Ctrl + C`.



#### Guided example endpoints


| Action | HTTP method and path | Successful response |
| --- | --- | --- |
| Create | `POST /notes` | `201` and the new note |
| Read all | `GET /notes` | `200` and a list of notes |
| Read one | `GET /notes/{note_id}` | `200` and one note |
| Update selected fields | `PATCH /notes/{note_id}` | `200` and the updated note |
| Delete | `DELETE /notes/{note_id}` | `200` and a confirmation |

**Status codes:** `200` means OK, `201` means Created, `404` means Not Found, and `422` means the request failed validation.


## Test summary

I ran the server and tested each endpoint. The tests below were sent with against `http://127.0.0.1:8000`; the same requests can be made with **Try it out** in `/docs`. The note used was ID `1`, and the ID `9999` was
used for the missing-note tests because it does not exist in `GET /notes`.


| # | Test | Request | Observed status | Observed response |
| --- | --- | --- | --- | --- |
| 1 | Create a note | `POST /notes` with `{"title": "Shopping list", "text": "Milk, eggs, bread."}` | **201** | `{"id":1,"title":"Shopping list","text":"Milk, eggs, bread."}` |
| 2 | Read all notes | `GET /notes` | **200** | `[{"id":1,"title":"Shopping list","text":"Milk, eggs, bread."}]` |
| 3 | Read the note | `GET /notes/1` | **200** | `{"id":1,"title":"Shopping list","text":"Milk, eggs, bread."}` |
| 4 | Update one field (title) | `PATCH /notes/1` with `{"title": "Weekly shopping list"}` | **200** | `{"id":1,"title":"Weekly shopping list","text":"Milk, eggs, bread."}` |
| 5 | Update one field (text) | `PATCH /notes/1` with `{"text": "Milk, eggs, bread, coffee."}` | **200** | `{"id":1,"title":"Weekly shopping list","text":"Milk, eggs, bread, coffee."}` |
| 6 | Persistence after restart | Stop the server, restart it, then `GET /notes/1` | **200** | `{"id":1,"title":"Weekly shopping list","text":"Milk, eggs, bread, coffee."}` |
| 7 | Delete the note | `DELETE /notes/1` | **200** | `{"message":"Note deleted"}` |
| 8 | Read the deleted note | `GET /notes/1` | **404** | `{"detail":"Note not found"}` |
| 9 | Update a missing note | `PATCH /notes/9999` with `{"title": "Missing note test"}` | **404** | `{"detail":"Note not found"}` |
| 10 | Delete a missing note | `DELETE /notes/9999` | **404** | `{"detail":"Note not found"}` |
| 11 | Invalid create (no `text`) | `POST /notes` with `{"title": "Incomplete note"}` | **422** | `{"detail":[{"type":"missing","loc":["body","text"],"msg":"Field required", ...}]}` |

### Summary of results

- **Creating a note** returned `201` with the new note, including its
  database-assigned `id`.
- **Reading it** returned `200`, both from the list endpoint (`GET /notes`)
  and the single-note endpoint (`GET /notes/1`).
- **Updating one field** returned `200`. When only `title` was sent, the
  `text` stayed the same; when only `text` was sent, the new title was kept.
  This confirms `PATCH` performs a partial update.
- **Persistence:** after stopping and restarting the server, the updated note
  was still present, so the data is stored in SQLite and not in memory.
- **Deleting it** returned `200` with `{"message":"Note deleted"}`. Reading
  the same ID afterwards returned `404`, and `GET /notes` returned an empty
  list `[]`.
- **Requesting a missing note** returned `404` with
  `{"detail":"Note not found"}`. `PATCH` and `DELETE` on a missing ID (`9999`)
  also returned `404`.
- **Validation:** a `POST` with the required `text` field missing returned
  `422`, because the body did not match the `NoteCreate` model.

All five endpoints behaved as specified in the assignment, and every item in
the submission checklist is satisfied.

## Submission checklist

- [x] `GET /notes` returns notes
- [x] `GET /notes/{note_id}` returns one note
- [x] `POST /notes` creates a note
- [x] `PATCH /notes/{note_id}` updates a note
- [x] `DELETE /notes/{note_id}` deletes a note
- [x] missing notes return a `404` error