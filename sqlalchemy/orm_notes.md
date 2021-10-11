<!-- **What is a orm?**

ORM(Object Relational Mapper): presents a method of associating user-defined python class with database tables and the instance of those classes(objects) with the row of that tables.

**What is called as unit_of_work**


```python

	from sqlalchemy import create_engine
	engine = create_engine(databse_url)

```

- The return value of the *create_engine* is an instance of *Engine* which represents the core interface of the database.
- The returned engine will not actually connected to the database yet. That will happen only when it tries to perform some tasks on the database.

**Declare a Mapping**

The actual configuration process starts by describing the database tables we will be dealing with and then by defining our own classes which will be mapped to those tables. These two tasks are performed by *declarative extension*

```python

	from sqlalchemy import create_engine
	engine = create_engine(databse_url)

	Base = declarative_base()
```

**What is declarative base class?**
Classes mapped using the declarative system are defined in terms of base calss Which have a log of classes and tables relative to that base.

```python

	
class User(Base):
	__tablename__ = 'users'

	id = Column(Integer, primary_key=True)
	name = Column(String)
	fullname = Column(String)
	nickname = Column(String)

```
- A class using a declarative need minimum atleast a tablename and a column -->

**The Session**
-----

- The session is the way *sqlalchemyORM* interacts with the database.

- It wraps a database connection via an engine, and provides an identity map for objects that you load via the session/associate with the session.It also wraps a transaction and that transaction will be open until the session is committed or rolled back.

	- **What is a identity-map?**
		It is a cache-like data structure that contains a unique list of objects determined by the object's table and primary key.

- **Creating a Session ?**

 sqlalchemy have a class called *Session Maker* to ensure that the sessions can be created with the same parameters for the entire application. It does that by creating a *Session* class that has been configured as per arguments passed to the sessionmaker factory.

```python

	from sqlalchemy import create_engine
	from sqlalchemy.orm import sessionmaker

	SQLURL = 'sqlite+pysqlite:///:memory:'
	engine = create_engine(SQLURL)

	Session = sessionmaker(bind=engine) #Define a Session class with the bind configuration 

	session = Session() #Creates a session for out use from the Session class

```
 Session will wait for our instructions to make a first connection with the database.

```py

	from datetime import datetime
	from sqlalchemy import (Table, Column, Integer, Numeric,String, DateTime,ForeignKey)
	from sqlalchemy.ext.declarative import declarative_base
	from sqlalchemy.orm import relationship, backref

	Base = declarative_base()
	
	class Cookie(Base):
 		__tablename__ = 'cookies'
 		cookie_id = Column(Integer(), primary_key=True)
 		cookie_name = Column(String(50), index=True)
		cookie_recipe_url = Column(String(255))
		cookie_sku = Column(String(55))
		 quantity = Column(Integer())
		 unit_cost = Column(Numeric(12, 2))
	
	def __repr__(self):
 		return "Cookie(cookie_name='{self.cookie_name}', " \
						"cookie_recipe_url='{self.cookie_recipe_url}', " \
						"cookie_sku='{self.cookie_sku}', " \
						"quantity={self.quantity}, " \
						"unit_cost={self.unit_cost})".format(self=self)
   class User(Base):
 		__tablename__ = 'users'
 		user_id = Column(Integer(), primary_key=True)
 
 ```

**session.flush()**:
 
  A flush is like a commit 
