# app/routes/items.py

from fastapi import APIRouter, Depends
from app.utils.dependencies import get_api_key

router = APIRouter()

@router.get("/items/")
def read_items(api_key: str = Depends(get_api_key)):
    return [{"name": "Item 1"}, {"name": "Item 2"}]
