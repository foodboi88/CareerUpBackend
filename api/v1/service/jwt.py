from datetime import datetime, timedelta
from os import getenv, urandom

from jose import JWTError, jwt

SECRET_KEY = getenv("JWT_SECRET_KEY", urandom(32))
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_HOURS = 24

def create_token(data: dict, type: str) -> str:
    return jwt.encode(
        {
            **data,
            "type": type,
            "exp": datetime.utcnow() + timedelta(hours=ACCESS_TOKEN_EXPIRE_HOURS),
        },
        key=SECRET_KEY,
        algorithm=ALGORITHM
    )

def decode_token(token: str) -> dict:
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
