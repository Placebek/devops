from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from .database import Base, engine, SessionLocal
from .models import Student

app = FastAPI()


origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  
    allow_credentials=True,
    allow_methods=["*"],    
    allow_headers=["*"],
)


# создаем таблицы
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "Student API работает!"}

@app.post("/students/")
def create_student(name: str, age: int, email: str, db: Session = Depends(get_db)):
    student = Student(name=name, age=age, email=email)
    db.add(student)
    db.commit()
    db.refresh(student)
    return student

@app.get("/students/")
def get_students(db: Session = Depends(get_db)):
    return db.query(Student).all()
