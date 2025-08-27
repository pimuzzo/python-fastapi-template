from fastapi import APIRouter, HTTPException
from app.models.user import User, UserCreate
from app.services.user_service import save_user, get_all_users

router = APIRouter()


@router.post("/", response_model=User)
async def create_user(user: UserCreate):
    return await save_user(user)


@router.get("/", response_model=list[User])
async def get_users():
    return await get_all_users()
