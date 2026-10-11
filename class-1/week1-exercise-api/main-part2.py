from fastapi import FastAPI

# Import the movies router from routers/movies.py.
from routers import movies

app = FastAPI()

# Connect all routes from movies.py under the /movies URL prefix.
app.include_router(movies.router, prefix="/movies")

@app.get("/")
def home():
    return {"message": "Hello from my exercise API"}


@app.get("/hello")
def hello():
    return {"message": "world!"}


@app.get("/about")
def about():
    return {
        "name": "Week 1 Exercise API",
        "version": "1.0.0",
        "author": "Mei"}
