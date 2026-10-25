## Week 3 Homework 1 Books API


I have used:

- `main.py` used for the main python file
- one database file called `books.db` and table `books` was created 
- the homework is located inside `\class-3\week3-books-api_o`
- one `.venv` is used for the overall module as I have noticed in the past that it takes a lot of storage in my limited storage capacity on my machine to have separate .venv per week
- one `requirements.txt` has been created as I have limited storage capacity in my machine for one load for every week.
- validation rules applied for `title` having at least 2 characters, `author` having at least 2 characters and `year` is greater than or equal to 1900


#### Folder Structure


```text
class-3/
    week3-books-api_o/
        database.py
        main.py
        models.py
        README.md
        schemas.py
    week3-sqlalchemy-api_o/
        application.py
        database.py
        main.py
        models.py
        read_courses.py
        rules.py
        README.md
        schemas.py
        seed.py
        tests/
            conftest.py
            test_rules.py
            test_api.py
requirement.txt
.venv/
```


#### Quick Comparison Table between SQLAlchemy model vs Pydantic schema

| Feature | SQLAlchemy Model (`models.py`) | Pydantic Schema (`schemas.py`) |
| :--- | :--- | :--- |
| **Primary Job** | Database storage & table structure | Request validation & API response shape |
| **Library** | `sqlalchemy` | `pydantic` |
| **Validation Rules** | Database constraints (`nullable=False`, `unique=True`) | Python-level rules (`min_length=2`, `ge=1900`) |
| **Feature** | SQLAlchemy Model (`Book`) | Pydantic Schema (`BookCreate/BookResponse`) |
| **Where it happens** | Inside the database engine, when saving data | In Python memory, before touching the database | 
| **When it runs** | When executing `db.commit()` | During the incoming HTTP request |


#### Test Result

1. Post request result status **201** and included the created book's `id` for the below json

```json
{
  "title": "Clean Code",
  "author": "Robert Martin",
  "year": 2008
}
```

2. Post request result status **422** because of validation rules that has been applies

```json
{
  "title": "A",
  "author": "B",
  "year": 1800
}
```

3. GET request for books and books/{book_id} resulted in `200` and the book information

4. Get request for non existing book resulted in `404` error message


#### Submission checklist

- [x] The app starts without errors
- [x] SQLAlchemy creates the `books` table
- [x] valid books can be inserted
- [x] invalid data is rejected
- [x] all routes were tested in Postman
- [x] missing book return a `404` error


## **Part 2** Week 3: Weekend Activity Courses API

I have used:

- `README.md` for the main document file for the week 3  weekend activity assignment
- the homework is located inside `\class-3\week3-sqlalchemy-api_o`
- link for homework for [Week 3: Weekend Activity](../week3-sqlalchemy-api_o/README.md)