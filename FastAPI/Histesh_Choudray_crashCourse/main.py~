''' Just a simple api to create,get,post,delete courses.I used uvicorn to excecute'''

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()
fakedb = []

class Course(BaseModel):
	id: int
	name: str
	price: float
	is_earlyBird: Optional[bool] = None
#Root
@app.get('/')
def read_root():
	return {"greetings": "Hello, Akshai"}

#Getting all courses
@app.get("/courses")
def get_course():
	return fakedb

#Getting course with the course_id
@app.get("/courses/{course_id}")
def get_a_course(course_id: int):
	course  = course_id - 1
	return fakedb[course]

#Posting a course
@app.post("/courses")
def add_course(course: Course):
	fakedb.append(course.dict())
	return fakedb[-1]

#Deleting a course
@app.delete("/courses/{course_id}")
def delete_course(course_id: int):
	fakedb.pop(course_id-1)
	return {"task": "deletion successfull"}
