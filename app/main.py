from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from .database import Base, engine, get_db
from .schemas import UserRegister, UserLogin
from . import crud

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def health_check():
    return {"status": "OK"}

@app.post("/register")
def register(user: UserRegister, db: Session = Depends(get_db)):
    if user.password != user.password_repeat:
        raise HTTPException(status_code=400, detail="Passwords do not match")

    existing_user = crud.get_user_by_email(db, user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    crud.create_user(db, user.email, user.password)
    return {"status": "registered"}

@app.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    authenticated_user = crud.authenticate_user(db, user.email, user.password)
    if not authenticated_user:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    return {"status": "login successful"}
