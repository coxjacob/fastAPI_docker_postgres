
## Useful commands
* type nul > filename.txt
* pip install virtualenv
* Window activate venv
    * .venv\Scripts\activate
* FastAPI
    * pip install "fastapi[standard]"
    * uvicorn main:app --reload
    * uvicorn main:app --host 0.0.0.0 --port 8006
    * uvicorn main:app --port 5000

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




## Useful references
* [Manual FastAIP](https://fastapi.tiangolo.com/deployment/manually/#server-machine-and-server-program)