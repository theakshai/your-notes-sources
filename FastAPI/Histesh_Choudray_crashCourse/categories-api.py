from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

categoriesapp = FastAPI()

class Categories(BaseModel):
		name: str
		icon: str

@categoriesapp.get('/categories')
def getName():
	return{"date":"time"}


# @categoriesAPI.post('/categories/')
# def writeName(userName):
# 	return 'hello'