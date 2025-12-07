from fastapi import APIRouter

from src.api import async_session
from src.core.models import User
from src.core.schemas import UserRead


router = APIRouter()

@router.get(path='/ping')
async def ping():
    return {'message' : 'OK'}

@router.post(
    path='/login',
)
async def login(
    db: async_session,
):
    return {'message' : 'OK'}

@router.post(
    path='/registration',
)
async def registration(
    db: async_session
):
    return {'message' : 'OK'}