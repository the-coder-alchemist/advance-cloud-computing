from fastapi import FastAPI

import models
from database import engine
from routers import auth, profile

# Create the users table if it does not exist.
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# All auth routes start with /auth.
app.include_router(auth.router, prefix="/auth")
app.include_router(profile.router, prefix="/profile")

@app.get("/")
def home():
    return {"message": "Week 4 auth API is running"}