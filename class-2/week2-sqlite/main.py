from fastapi import FastAPI
from pathlib import Path
import sqlite3

app = FastAPI()

# Find the database beside main.py, regardless of the terminal folder.
DATABASE_PATH = Path(__file__).resolve().parent / "university.db"


def get_connection():
    # Open a connection to the SQLite database file.
    # row_factory lets us access columns by name.
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection


@app.get("/")
def home():
    return {"message": "University API is running"}


@app.get("/students")
def get_students():
    connection = get_connection()
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