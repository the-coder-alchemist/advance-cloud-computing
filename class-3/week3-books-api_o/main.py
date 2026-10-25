from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
import schemas 
import models
from database import engine, get_db

# Create the database tables when the app starts.
# This uses the Book model from models.py.
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Books API is running"}


@app.get("/books", response_model=list[schemas.BookResponse])
def get_books(db: Session = Depends(get_db)):
    # Depends(get_db) asks FastAPI to open a database session for this request.
    # response_model tells FastAPI to return a list of BookResponse objects.
    # Read all books from the database.
    books = db.query(models.Book).all()
    return books


@app.get("/books/{book_id}", response_model=schemas.BookResponse)
def get_book(book_id: int, db: Session = Depends(get_db)):
    # Find one book by primary key.
    # .first() returns one Book object or None.
    book = db.query(models.Book).filter(models.Book.id == book_id).first()

    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")

    return book


@app.post("/books", response_model=schemas.BookResponse, status_code=201)
def create_book(book_data: schemas.BookCreate, db: Session = Depends(get_db)):
    # book_data has already been checked by Pydantic.
    # We can use dot notation because book_data is a BookCreate object.
    # The keys must match the JSON fields sent by the client.
    book = models.Book(
        title=book_data.title,
        author=book_data.author,
        year=book_data.year
    )

    try:
        # Add the new object to the session, then commit it to the database.
        db.add(book)
        db.commit()

        # Refresh loads database-generated values such as id.
        db.refresh(book)
        return book

    except IntegrityError:
        # If the unique book code is repeated, undo the failed transaction.
        db.rollback()
        raise HTTPException(status_code=409, detail="Book code already exists")