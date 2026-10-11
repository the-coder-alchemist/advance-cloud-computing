# Import FastAPI, the framework we use to build the API.
from fastapi import FastAPI

# Import the movies router from routers/movies.py.
from routers import movies

# Create the FastAPI application object.
# Uvicorn will run this object.
app = FastAPI()

# Connect all routes from movies.py under the /movies URL prefix.
app.include_router(movies.router, prefix="/movies")

# This endpoint runs when the browser opens http://127.0.0.1:8000/
@app.get("/")
def home():
    # Returning a dictionary sends JSON back to the browser.
    return {"message": "Hello world!"}


# This endpoint runs when the browser opens http://127.0.0.1:8000/hello
@app.get("/hello")
def hello():
    return {"message": "world!"}