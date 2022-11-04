from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from ..database import UserInfoCrud
from ..database.base import Crud
from ..exception.http import CredentialException, NotFoundException
from ..service.jwt import JWTError, decode_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")


async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = decode_token(token)
        if payload["type"] != "access":
            raise CredentialException()
        user = await UserInfoCrud.find_by_id(payload.get("id"))
        if user is None:
            raise CredentialException()
        return user
    except JWTError:
        raise CredentialException()


def require_existed(crud: Crud):
    async def func(obj = Depends(crud.find_by_id)):
        if obj is None:
            raise NotFoundException()
        return obj
    return func
