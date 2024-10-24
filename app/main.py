# app/main.py

from fastapi import FastAPI,Depends

from app.models import Base
from app.routes import items
from app.database import engine
from app.api_key import create_api_key
from sqlalchemy.orm import Session
from app.database import get_db

app = FastAPI()

app.include_router(items.router)


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.post("/api-keys/")
def generate_api_key(owner: str, db: Session = Depends(get_db)):
    api_key = create_api_key(db=db, owner=owner)
    return {"api_key": api_key.key, "expires_at": api_key.expires_at}

Base.metadata.create_all(bind=engine)