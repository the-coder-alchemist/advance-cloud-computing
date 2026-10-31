## Week 4 Homework : Test Your Authentication API


#### What the Application Does & Python Version

* **What it does:** This application is a secure FastAPI-based authentication API. It allows users to register accounts with hashed passwords, log in to receive a JSON Web Token (JWT), and access a protected profile endpoint (`/profile/me`) using HTTP Bearer authentication.
* **Python Version:** Python 3.10 or higher is recommended.


#### Folder Structure:


```text
.venv
class-4/
    week4-auth-api_o/
        application.py
        database.py
        main.py
        models.py
        README.md
        schemas.py
        security.py
        tests/
            conftest.py
            test_api.py
        routers/
            __init__.py
            auth.py
            profile.py
requirement.txt
```

I have used:

- `main.py` used for the main python file
- the homework is located inside `\class-4\week4-auth-api_o`
- one `.venv` is used for the overall module as I have noticed in the past that it takes a lot of storage in my limited storage capacity on my machine to have separate .venv per week
- one `requirements.txt` has been created as I have limited storage capacity in my machine for one load for every week.



### Environment Setup, Installing Dependencies & Running the Test
Follow these steps to set up virtual environment and install the required packages:

1. **Create and activate a virtual environment:**
```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
```
   
2. **Install dependencies:**
```bash
python -m pip install -r requirements.txt
```

3. **Configuring the Secret Key (JWT_SECRET)**

The application requires a secure signing key to create and verify JSON Web Tokens. It must be at least 32 characters long.

Generate a secure secret key:

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

Set it as an environment variable in your terminal before running the app (replace our_generated_secret_here with your actual generated value):

On macOS/Linux:

```bash
export JWT_SECRET="paste-your-generated-value-here"
```

On Windows PowerShell:

```powershell
$env:JWT_SECRET = "paste-your-generated-value-here"
```

4. **Running the Server & Using Swagger UI**

Start the development server using Uvicorn:

```bash
uvicorn main:app --reload
```

Open your browser and navigate to: `http://127.0.0.1:8000/docs`

Register: Use POST /auth/register with a JSON body (username, email, password) to create a new user.

Log in: Use POST /auth/login with your credentials to receive an access_token.

Access Profile: Click the Authorize button in Swagger UI, paste your bearer token, and execute GET /profile/me to view your profile data.


5. **Running Tests & Results Summary**

The project includes unit tests using pytest and FastAPI TestClient.

Run the tests from the project root:

```bash
python -m pytest -q
```

Result Summary:

6 passed (Tests cover password hashing, successful login/profile access, token requirements, duplicate registration conflicts, bad password login prevention, and schema validation errors).

```bash
python -m pytest -v
```

Result Summary:

```text
collected 6 items      
tests/test_auth.py::test_password_hash PASSED                      [ 16%]
tests/test_auth.py::test_login_and_profile PASSED                  [ 33%]
tests/test_auth.py::test_profile_requires_token PASSED             [ 50%]
tests/test_auth.py::test_duplicate_registration PASSED             [ 66%]
tests/test_auth.py::test_wrong_password_login PASSED               [ 83%]
tests/test_auth.py::test_invalid_registration_data PASSED          [100%]
```

### Database Architecture

* `Normal Operation`: SQLite automatically stores user accounts locally in an auth.db file in the project root directory.

* `Testing Isolation`: Automated tests use an isolated, temporary SQLite database (tmp_path) managed by conftest.py so they never overwrite or modify the live development database auth.db.