from fastapi import APIRouter, Depends

from ..database import UserInfoCrud
from ..exception.http import BadRequestException
from ..middleware.auth import get_current_user
from ..schema.base import Detail
from ..schema.user import User, UserCreate
from ..service.user import hash_password

user_router = APIRouter()


@user_router.post("", response_model=Detail, tags=["Auth", "User"])
async def create_user(data: UserCreate):
    if await UserInfoCrud.exists_by_username(data.user_name):
        raise BadRequestException("Username already exists")
    if await UserInfoCrud.exists_by_email(data.email):
        raise BadRequestException("Email already exists")
    data.password = hash_password(data.password)
    return {"detail": await UserInfoCrud.create(data.dict())}


@user_router.get("/me", response_model=User, tags=["User"])
async def read_current_user(user = Depends(get_current_user)):
    return user
