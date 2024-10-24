# app/utils/dependencies.py
import datetime

import pytz
from fastapi import HTTPException, Security, Depends
from fastapi.security.api_key import APIKeyHeader
from sqlalchemy.orm import Session

from app.api_key import get_api_key as fetch_api_key
from app.database import get_db

API_KEY = "your_api_key"
api_key_header = APIKeyHeader(name="X-API-Key")


async def get_api_key(api_key: str = Security(api_key_header), db: Session = Depends(get_db)):
    db_api_key = fetch_api_key(db, api_key)  # Fetch the API key from the database
    # timezone = pytz.timezone("Your/Timezone")  # Replace with your timezone
    now = datetime.datetime.now(datetime.timezone.utc)
    # Check if the API key is valid, active, and not expired
    if not db_api_key or not db_api_key.is_active or db_api_key.expires_at < datetime.datetime.now():
        raise HTTPException(
            status_code=403, detail="Could not validate API key"
        )
    return db_api_key
