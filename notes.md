
## Useful commands
* type nul > filename.txt
* pip install virtualenv
* Window activate venv
    * .venv\Scripts\activate
* FastAPI
    ```
    pip install "fastapi[standard]"
    # uvicorn main:app --reload
    # uvicorn main:app --host 0.0.0.0 --port 8006
    # uvicorn main:app --port 5000 #before moving main to app folder
    uvicorn app.main:app --port 5000 #after moving main to app folder
    ```

* Git Setup

    ```
    echo "# fastAPI_docker_postgres" >> README.md
    git init
    git add README.md
    git commit -m "first commit"
    git branch -M main
    git remote add origin https://github.com/coxjacob/fastAPI_docker_postgres.git
    git push -u origin main
    ```

* Other useful git commands
    ```
    git reset --soft Head~1
    git status *
    ```
* Install
    ```
    pip install pytest
    pytest

    pytest -c app/tests/pytest.ini
    ```
* Requirements
    ```
    pip freeze
    pip freeze > requirments.txt
    pip install -r requirements.txt
    ```

* Add Table
    ```
    CREATE TABLE IF NOT EXISTS Students (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL
    );
    ```

* Docker Start
    ```
    docker compose up
    ```

## Useful references
* [Manual FastAIP](https://fastapi.tiangolo.com/deployment/manually/#server-machine-and-server-program)
* [Validation errors](https://docs.pydantic.dev/2.11/errors/validation_errors/#missing)