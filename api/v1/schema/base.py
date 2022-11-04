from pydantic import BaseModel


class Detail(BaseModel):
    detail: str


class Token(BaseModel):
    access_token: str
    token_type: str
