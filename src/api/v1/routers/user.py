from fastapi import APIRouter

from src.core.models import User
from src.core.schemas import UserRead


router = APIRouter()

@router.get(path="/ping")
async def ping():
    return {"message" : "OK"}

@router.post(
    path="/create",
    response_model=UserRead
)
async def create(
    user: User,
):
    return {"message" : "OK"}