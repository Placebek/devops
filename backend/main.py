from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
import models
import database

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)
# --- Создание таблиц при запуске ---
@app.on_event("startup")
def startup():
    models.Base.metadata.create_all(bind=database.engine)

# --- Подключение к БД ---
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- Эндпойнты ---
@app.get("/")
def root():
    return {"message": "API работает 🚀"}

@app.get("/library")
def get_library(db: Session = Depends(get_db)):
    library = db.query(models.Library).all()
    return library

@app.post("/library")
def create_library(name: str, author: str, db: Session = Depends(get_db)):
    library = models.Library(name=name, author=author)
    db.add(library)
    db.commit()
    db.refresh(library)
    return library
