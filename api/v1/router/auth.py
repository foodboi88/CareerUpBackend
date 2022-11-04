from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from ..database import UserInfoCrud
from ..exception.http import BadRequestException
from ..schema.base import Token
from ..service.jwt import create_token
from ..service.user import verify_password

auth_router = APIRouter()


@auth_router.post("/token", response_model=Token, tags=["Auth"])
async def login(data: OAuth2PasswordRequestForm = Depends()):
    user = await UserInfoCrud.find_by_username(data.username)
    if user is None or not verify_password(data.password, user.password):
        raise BadRequestException("Invalid username or password")
    return {
        "access_token": create_token({"id": user.id}, "access"),
        "token_type": "bearer",
    }
