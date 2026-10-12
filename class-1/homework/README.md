### Week 1 Homework 1: University API Exercise


#### Goal

API support these endpoints:


- `GET /` returns a welcome page with API information.
- `GET /students` returns all students.
- `GET /students/{student_id}` returns one student by ID.
- If the student does not exist, `404` JSON error is returned.

I have used:

- `main.py`
- a `routers` folders
- `routers/students.py`
- `APIRouter`
- the homework is located inside `\class-1\homework`
- `uvicorn main:app --reload`
- one `venv` is used for the overall module as it I have noticed in the past that it takes a lot of storage in my limited storage capacity on my machine
- one `requirements.txt` has been created as I have limited storage capacity in my machine to one load for every week.


#### Folder Structure


```text
class-1/
    homework/
        main.py
        routers/
            __init__.py
            students.py
requirements.txt
.venv/
```

#### Python code for `main.py`:

```python
from fastapi import FastAPI

from routers import students

app = FastAPI()

app.include_router(students.router, prefix="/students")


@app.get("/")
def home():
    return {
        "name": "University API",
        "version": "1.0.0",
        "description": "A simple API to fetch university student data.",
        "endpoints": {
            "root": "GET /",
            "all_students": "GET /students",
            "student_by_id": "GET /students/s1"
        }
    }
```


#### Python code for `students.py`:

```python
from fastapi import APIRouter, HTTPException

router = APIRouter()

students = {
    "s1": {
        "name": "John Smith",
        "student_id": "S12345",
        "major": "Computer Science",
        "year": 2
    },
    "s2": {
        "name": "Maria Garcia",
        "student_id": "S54321",
        "major": "Mathematics",
        "year": 3
    },
    "s3": {
        "name": "Ali Khan",
        "student_id": "S77777",
        "major": "Data Science",
        "year": 1
    }
}


@router.get("/")
def get_students():
    return students


@router.get("/{student_id}")
def get_student(student_id: str):
    student = students.get(student_id)

    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    return student
```

#### Root Endpoint result

Root endpoint returns:

```json
{
  "name": "University API",
  "version": "1.0.0",
  "description": "A simple API to fetch university student data.",
  "endpoints": {
    "root": "GET /",
    "all_students": "GET /students",
    "student_by_id": "GET /students/s1"
  }
}
```


#### Required Tests

Run the server:

```bash
uvicorn main:app --reload
```

The list route uses `@router.get("/")` with the prefix `/students`, so its full path is `/students/`. Visiting `/students` automatically redirects to `/students/`.

Open these URLs in your browser:

```text
http://127.0.0.1:8000/
http://127.0.0.1:8000/students/
http://127.0.0.1:8000/students/s1
http://127.0.0.1:8000/students/s10
```

The final URL should return a `404` error with:

```json
{"detail":"Student not found"}
```

Also check student `s2`:

```text
http://127.0.0.1:8000/students/s2
```






## What the API Does

| Method | Endpoint               | Description                                              |
| ------ | ---------------------- | -------------------------------------------------------- |
| GET    | `/`                    | Welcome page with API information                        |
| GET    | `/students/`           | Returns all students                                     |
| GET    | `/students/{student_id}` | Returns one student by ID (e.g. `s1`)                  |

If the requested student does not exist, the API returns a `404` JSON error:

```json
{"detail": "Student not found"}
```

> **Note:** The `{student_id}` in the URL is the dictionary key (`s1`, `s2`, `s3`), not the university registration number. For example, `/students/s1` returns John Smith (registration number `S12345`), while `/students/S12345` returns `404`.


## URLs to Test

Open these in your browser:

| URL                                  | Expected result                                |
| ------------------------------------ | ---------------------------------------------- |
| <http://127.0.0.1:8000/>             | Welcome message with API name, version, and endpoints |
| <http://127.0.0.1:8000/students/>    | All three students                             |
| <http://127.0.0.1:8000/students/s1>  | John Smith                                     |
| <http://127.0.0.1:8000/students/s2>  | Maria Garcia                                   |
| <http://127.0.0.1:8000/students/s10> | `404` with `{"detail":"Student not found"}`    |

Visiting `/students` (without the trailing slash) automatically redirects to `/students/`.



## Example Responses

**`GET /`**

```json
{
  "name": "University API",
  "version": "1.0.0",
  "description": "A simple API to fetch university student data.",
  "endpoints": {
    "root": "GET /",
    "all_students": "GET /students",
    "student_by_id": "GET /students/s1"
  }
}
```

**`GET /students/s1`**

```json
{
  "name": "John Smith",
  "student_id": "S12345",
  "major": "Computer Science",
  "year": 2
}
```

**`GET /students/s10`** (status `404`)

```json
{
  "detail": "Student not found"
}
```

### How `/{student_id}` Works

In `routers/students.py`, the route `@router.get("/{student_id}")` is a *path parameter*. Whatever text appears in that part of the URL is passed to the function as the `student_id` argument. The function looks that value up in the `students` dictionary. If a match is found, the student is returned as JSON; if not, an `HTTPException` with status code `404` is raised.

Because the router is included in `main.py` with `prefix="/students"`, every route in `students.py` is automatically placed under `/students`.

## Sample Data

| Key  | Name         | Registration No. | Major            | Year |
| ---- | ------------ | ---------------- | ---------------- | ---- |
| `s1` | John Smith   | S12345           | Computer Science | 2    |
| `s2` | Maria Garcia | S54321           | Mathematics      | 3    |
| `s3` | Ali Khan     | S77777           | Data Science     | 1    |


#### Submission Checklist

Before you finish, make sure:

- Your virtual environment works.
- Your `requirements.txt` contains `fastapi` and `uvicorn`.
- `GET /` works in the browser.
- `GET /students` works in the browser.
- `GET /students/s1` works in the browser.
- `GET /students/s10` returns a `404` JSON error.
- You can explain what `/{student_id}` does.