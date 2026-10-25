## **Week 3** Weekend activity Courses API


I have used:

- `main.py` used for the main python file
- the homework is located inside `\class-3\week3-sqlalchemy-api_o`
- one `.venv` is used for the overall module as I have noticed in the past that it takes a lot of storage in my limited storage capacity on my machine to have separate .venv per week
- one `requirements.txt` has been created as I have limited storage capacity in my machine for one load for every week.


#### Folder Structure:

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
```

#### The pytest command and a short summary of passed or failed tests.

Pytest Command & Test Summary:

1. Test One

```bash
python -m pytest tests/test_rules.py -q
```
result 
`3 passed`

2. Test 2: Temporarily change < to <= in rules.py, rerun, and inspect the failing boundary case.

result
`2 passed, 1 failed`


3. Test 3

```bash
python -m pytest tests/test_api.py -q
```

result 
`8 passed`
successful creation/retrieval, duplicates (409), invalid input (422), missing records (404), isolation and persistence across application instances


4. Test 4

```bash
python -m pytest -q
```

result 
`11 passed`

11 passed: three unit cases and 8 API tests with no failures 


5. Test 5 

```bash
python -m pytest -v

```
result 
`11 passed`

```text

collected 11 items  
tests/test_api.py::test_create_and_retrieve PASSED                     [  9%]
tests/test_api.py::test_duplicate_does_not_add_row PASSED              [ 18%]
tests/test_api.py::test_invalid_input_does_not_add_row PASSED          [ 27%]
tests/test_api.py::test_missing_course PASSED                          [ 36%]
tests/test_api.py::test_starts_empty PASSED                            [ 45%]
tests/test_api.py::test_data_survives_new_application PASSED           [ 54%]
tests/test_api.py::test_missing_title PASSED                           [ 63%]
tests/test_api.py::test_create_after_duplicate PASSED                  [ 72%]
tests/test_rules.py::test_enrolment_boundary[-1-True] PASSED           [ 81%]
tests/test_rules.py::test_enrolment_boundary[0-False] PASSED           [ 90%]
tests/test_rules.py::test_enrolment_boundary[1-False] PASSED           [100%]

============================= warnings summary ================================
..\..\.venv\Lib\site-packages\fastapi\testclient.py:1
venv\Lib\site-packages\fastapi\testclient.py:1: StarletteDeprecationWarning: Using `httpx` with `starlette.testclient` is deprecated; install `httpx2` instead.
    from starlette.testclient import TestClient as TestClient  # noqa

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
====================== 11 passed, 1 warning in 0.78s ================================
```


#### Difference between direct unit cases and API tests


| Feature | Direct Unit Cases (`test_rules.py`) | API Integration Tests (`test_api.py`) |
| :--- | :--- | :--- |
| **What is being tested** | A single standalone Python function (`enrolment_is_open`) containing business logic. | The full FastAPI application, including routing, validation, database sessions, and responses. |
| **Focus** | Checks specific logic boundaries (e.g., before, exactly at, and after a timestamp). | Checks HTTP status codes (`201`, `404`, `409`, `422`), JSON response structures, and database persistence. |
| **Summary** | Verify that a specific piece of isolated logic/rules works correctly on its own | verify that all parts of the web application work together correctly when an HTTP request comes in from a client |


####  Tests start with fresh data and do not depend on their execution order

`conftest` starts the test with fresh data. Every time a test function runs, pytest provides a built-in `tmp_path` fixture that creates a brand-new, empty temporary database. The `app_factory` fixture spins up a fresh FastAPI app and overrides the database dependency (`get_db`) to point exclusively to that temporary database.


## **Part 1** Week 3: Homework 1: Books API

I have used:

- `README.md` for the main document file for the week 3 weekend activity assignment
- the homework is located inside `\class-3\week3-books-api_o`
- link for homework for [Week 3: Homework](../week3-books-api_o/README.md)