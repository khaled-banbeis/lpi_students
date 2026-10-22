from sqlalchemy import create_engine 
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import sessionmaker 


SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/training_new" 
# SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://training_8cn2_user:D4JUFWusk4GVGqMXLDVMSZWFz2TEFybU@dpg-dbbfh061egvs73fsa060-a.oregon-postgres.render.com/training_8cn2"
engine = create_engine(SQLALCHEMY_DATABASE_URL) 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) 
Base = declarative_base() 

def get_db(): 
    db = SessionLocal() 
    try: 
        yield db 
    finally: 
        db.close() 
