from fastapi import FastAPI 
# import models 
import students
from database import engine 
# import user_controller 
import s_user_controller 
from fastapi.middleware.cors import CORSMiddleware

# Create tables in MySQL automatically if they don't exist 
# models.Base.metadata.create_all(bind=engine) 
students.Base.metadata.create_all(bind=engine) 

app = FastAPI(title="FastAPI MySQL Object-Oriented Clean") 

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
         "https://fastapi-student-management-1.onrender.com"
    ],
    allow_credentials=True, 
    allow_methods=["*"],
    allow_headers=["*"],
)


# Register the controller routes 

# app.include_router(user_controller.router) 
app.include_router(s_user_controller.router) 


@app.get("/")
def home():
    return {"message": "FastAPI MySQL is working"}