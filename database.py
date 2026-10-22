from sqlalchemy import create_engine 
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import sessionmaker 


# SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/training_new" 
SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://firstdb_90ty_user:y8fwXHaEOdf6IvXwYlUoHL7rKoBvEwge@dpg-dbcskq0473hc73a48kdg-a.oregon-postgres.render.com/firstdb_90ty"
engine = create_engine(SQLALCHEMY_DATABASE_URL) 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) 
Base = declarative_base() 

def get_db(): 
    db = SessionLocal() 
    try: 
        yield db 
    finally: 
        db.close() 
