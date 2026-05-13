from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from typing import List


app = FastAPI()

Std=[]

class students(BaseModel):
    name:str
    roll_no:int
    marks:float
    
@app.post("/students")
def add_student(student: students):
    Std.append(student)
    return {
        "message": "Student added successfully"
    }
    

@app.get("/students")
def get_students():
    return Std


@app.get("/percent/{roll_no}")
def calculate_percent(roll_no: int):
    for s in Std:
        if s.roll_no == roll_no:
            percentage = (s.marks / 100) * 100
            return {
                "name": s.name,
                "roll_no": s.roll_no,
                "marks": s.marks,
                "percentage": percentage
            }
    raise HTTPException(status_code=404, detail="Student not found")



@app.get("/grades/{roll_no}")
def calculate_grade(roll_no: int):
    for s in Std:
        if s.roll_no == roll_no:
            if s.marks >= 90:
                grade = "A"
            elif s.marks >= 80:
                grade = "B"
            elif s.marks >= 70:
                grade = "C"
            elif s.marks >= 60:
                grade = "D"
            else:
                grade = "F"
            return {
                "name": s.name,
                "roll_no": s.roll_no,
                "marks": s.marks,
                "grade": grade
            }
    raise HTTPException(status_code=404, detail="Student not found")