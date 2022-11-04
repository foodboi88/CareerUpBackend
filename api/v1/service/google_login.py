from os import getenv

from authlib.integrations.starlette_client import OAuth, OAuthError
from fastapi import Request
from starlette.config import Config

oauth = OAuth(
    Config(environ={
        "GOOGLE_CLIENT_ID": getenv("GOOGLE_CLIENT_ID"),
        "GOOGLE_CLIENT_SECRET": getenv("GOOGLE_CLIENT_SECRET"),
    })
)

oauth.register(
    name="google",
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
    client_kwargs={"scope": "openid email profile"},
)

async def authorize_redirect(request: Request, url: str):
    return await oauth.google.authorize_redirect(request, url)

async def parse_id_token(request: Request) -> dict:
    return dict(await oauth.google.parse_id_token(request, await oauth.google.authorize_access_token(request)))
