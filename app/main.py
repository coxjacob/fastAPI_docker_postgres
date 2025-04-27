from http.client import HTTPException
from typing import Union

from fastapi import FastAPI

from app.db import get_db_connection
from app.student import Student, StudentCreate

app = FastAPI(title="University API")


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/status")
async def status():
    return {"message":"OK"}

@app.post("/student/", response_model=Student)
def create_student(student: StudentCreate):
    conn, cursor = get_db_connection()
    try:
        cursor.execute("INSERT INTO Students (first_name, last_name) VALUES (%s, %s) RETURNING *",
                       (student.first_name, student.last_name))
        # cursor.execute(f"INSERT INTO STUDENTS (first_name, last_name) " +
        #                f"VALUES {student.first_name}, {student.last_name}"
        #                )
        new_student = cursor.fetchone()
        conn.commit()
        cursor.close()
    except Exception as e: 
        conn.close()
        raise HTTPException(status_code=500, detail=str(e))
    
    conn.close()
    if new_student:
        # ** deconstructs new_student for Student Object
        return Student(**new_student)
    
    raise HTTPException(status_code=400, detail="Error creating student")