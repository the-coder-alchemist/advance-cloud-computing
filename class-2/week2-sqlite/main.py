from fastapi import FastAPI
from pathlib import Path
import sqlite3

app = FastAPI()

<<<<<<< HEAD
# Find the database beside main.py, regardless of the terminal folder.
DATABASE_PATH = Path(__file__).resolve().parent / "university.db"


def get_connection():
    # Open a connection to the SQLite database file.
    # row_factory lets us access columns by name.
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
=======

# Check where you are connecting! Ask yourself: "Which one is my database?"
# The students table lives in university.db, created in Part 1 by setup_students.sql.
# Careful: sqlite3.connect() silently CREATES an empty file if this path does not
# exist, so a wrong filename shows up later as "no such table", not "file not found".
DB_PATH = Path(__file__).parent / "university.db"


def get_connection():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row

>>>>>>> 72091c3d6075ca30e9dedb1199ed0d45e9b502c8
    return connection


@app.get("/")
def home():
    return {"message": "University API is running"}


@app.get("/students")
def get_students():
    connection = get_connection()
<<<<<<< HEAD
    try:
        cursor = connection.cursor()

        # Read all rows from the students table in ID order.
        cursor.execute("SELECT * FROM students ORDER BY id")
        rows = cursor.fetchall()
    finally:
        # Close the connection even if the query fails.
        connection.close()

    # Convert each row into a dictionary
    students = []

    for row in rows:
        students.append(dict(row))

    return students
=======

    try:
        cursor = connection.cursor()
        cursor.execute("select * from students")
        students = cursor.fetchall()

    finally:
        connection.close()

    return students
>>>>>>> 72091c3d6075ca30e9dedb1199ed0d45e9b502c8
