CREATE TABLE books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    year INTEGER NOT NULL
);

INSERT INTO books (title, author, year)
VALUES ('Atomic Habits', 'James Clear', 2018);
INSERT INTO books (title, author, year)
VALUES ('The Untethered Soul', 'Michael Singer', 2007);
INSERT INTO books (title, author, year)
VALUES ('The Power of Now', 'Echhart Tolle', 1997);