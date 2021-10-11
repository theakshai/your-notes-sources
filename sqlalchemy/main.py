from sqlalchemy import create_engine

##Engine is a starting point, Where it reference both a dialect and pool which together interpret DBAPI's module functions as well as db

engine = create_engine('sqlite+pysqlite:///./cookies.db',echo=True)
# Produce an engine object based on the url

connection = engine.connect()
# opens a connection to the database