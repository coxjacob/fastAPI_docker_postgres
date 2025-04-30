from http.client import HTTPException
from typing import Union

from fastapi import FastAPI

from app.db import get_db_connection
from app.student import Student, StudentCreate

from typing import List

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


@app.get("/students/", response_model=List[Student])
def get_all_students():
    students = []
    conn, cursor = get_db_connection()
    try:
        cursor.execute("SELECT * FROM Students;")
        rows = cursor.fetchall()
        for row in rows:
            students.append(Student(**row))
        cursor.close()
        print("Completed get_all_students")
    except Exception as e:
        conn.close()
        raise HTTPException(status_code=500, detail=str(e))
    
    conn.close()
    if students:
        return students
    raise HTTPException(status_code=400, detail="Student not found")


@app.delete("/student/{student_id}")
def delete_student(student_id: int):
    conn, cursor = get_db_connection()
    try:
        cursor.execute("DELETE FROM Students WHERE id = %s", (student_id,))
        conn.commit()
        cursor.close()
    except Exception as e:
        conn.close()
        raise HTTPException(status_code=500, detail=str(e))
    
    conn.close()
    return {"message": "Student deleted successfully"}