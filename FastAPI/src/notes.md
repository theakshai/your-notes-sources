## Notes on FastAPI from the documentation
----


#### Type hints
The type hints is excellent future in python which will help with editors and tools to get some support. An in case of fastapi it helps to validate the data that being passed
and automatic request parsing. All the data validation are happening under the hood of pydantic modules


###
```python

from fastapi import FastAPI #Importing fastapi class from the fastapi module

#Instantiating the fastapi class with the object app

app = FastAPI()  

#Defining the path and tells the fastapi to handle the request that comes to the path using get operation. 

@app.get('/')  #Pathoperator decoration
async def root():  
	return {"Best Coder":"Akshai"}


#Path parameters

@app.get('/items/{itemid}')
async def read_item(itemid: int):
	return {"item id": itemid}


```
**Path order matters:**

*def user('/user/me')* should come before *def user('/user/{userid}')* otherwise it will through an error of uid is not found.

**Passing a Path as a function parameter:**
```python

	@app.get('path/{filepath:path}'):
		def read(filepath):
		return {"path": filepath}

```


**Predefined Values(Path):**

If we want the predefined values for the path parameters we can use *Enum*


#### Query Parameter:
----

**Query**: Query is a set of value pairs that goes after ? in a url separated by & characters.

```python

	@app.get('/items')
	def user(skip:int = 0, limit:int = 10):
		return 

```
Fastapi can regonize the difference between path parameter and query parameter. (Parameters other than path are query parameters).

#### Request Body:
----

It is a data sent by the client. Whereas, **reponse body** is the data sent from the sever to client as a response to the request.

**What is a model?**
- Models are the primary means of defining objects in *pydantic lib*
- Models are similar to types in strictly typed languages or an endpoint in an api.

```python

	from pydantic import BaseModel #Importing base model class 

	#creating a data model
	class Item (BaseModel):
		name : str 
		description: str 
		price: float 
		tax: float 

# declaring as a parameter is similar to path and query

@app.get('/items/')
def create_item(item:Item): #Declaring the type as the model type
	return{item}

```

