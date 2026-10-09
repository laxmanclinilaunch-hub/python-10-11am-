from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI(
    Title="FastAPI Application",
    description="This is a sample FastAPI application.",
    version="1.0.0"
)


class Student(BaseModel):
    name: str
    age: int
    email: str
    course: str


# temoprary data storage for students

students = {
    1: {
        "name": "John Doe",
        "age": 20,
        "email": "john.doe@example.com",
        "course": "Computer Science",
    },
    2: {
        "name": "Jane Smith",
        "age": 22,
        "email": "jane.smith@example.com",
        "course": "Data Science",
    },
}


@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI application!"}



# Get all students

@app.get("/students")
def get_students():
    return students




#Get single student access

@app.get("/students/{student_id}")
def get_student(student_id: int):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    return students[student_id]





# post method used to create new data


# Post - create student

@app.post("/students")
def create_students(student: Student):

    new_id=max(students.keys() ,default=0)+1

    students[new_id]=student.model_dump()

    return {
        "message": "Student created successfully",
        "student_id": new_id,
        "student_data": students[new_id]
    }




# PUT - update entire  student


@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    students[student_id] = student.model_dump()
    return {
        "message": "Student updated successfully",
        "student_id": student_id,
        "student_data": students[student_id]
    }




# Delete - delete student


@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    del students[student_id]
    return {"message": "Student deleted successfully", "student_id": student_id}