# app/crud.py

from sqlalchemy.orm import Session
from app.models import APIKey
from datetime import timedelta
import datetime
import secrets


def create_api_key(db: Session, owner: str, expiration_days: int = 30):
    api_key = secrets.token_hex(16)  # Generates a random API key
    expires_at = datetime.datetime.now(datetime.timezone.utc) + timedelta(days=expiration_days)

    db_api_key = APIKey(key=api_key, owner=owner, expires_at=expires_at)
    db.add(db_api_key)
    db.commit()
    db.refresh(db_api_key)

    return db_api_key


def get_api_key(db: Session, key: str):
    result = db.query(APIKey).filter(APIKey.key == key, APIKey.is_active.is_(True)).first()
    print(result)  # Debugging line
    return result


def deactivate_api_key(db: Session, key: str):
    db_api_key = db.query(APIKey).filter(APIKey.key == key).first()
    if db_api_key:
        db_api_key.is_active = False
        db.commit()
        return db_api_key
    return None
