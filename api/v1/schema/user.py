from pydantic import BaseModel


class UserCreate(BaseModel):
    user_name: str
    email: str
    password: str
    description: str | None


class User(BaseModel):
    user_name: str
    email: str
    description: str | None
