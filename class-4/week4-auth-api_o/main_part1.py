from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, Field

app = FastAPI()


# This schema describes the data accepted by /register-preview.
# A schema is a Python class that says which fields the request body must contain.
class UserRegister(BaseModel):
    # Field adds validation rules.
    # Here, username must be between 3 and 50 characters.
    username: str = Field(min_length=3, max_length=50)

    # EmailStr checks that the value looks like an email address.
    # This needs the email-validator package.
    email: EmailStr

    # password must be at least 6 characters.
    password: str = Field(min_length=6)


@app.post("/register-preview")
def register_preview(user: UserRegister):
    # If we reach this point, validation has passed.
    # FastAPI has already converted the JSON body into a UserRegister object.
    # Do not return the password in the response.
    return {
        "username": user.username,
        "email": user.email,
        "message": "Validation passed"
    }