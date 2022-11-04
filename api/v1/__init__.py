from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .router import *

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(question_router, prefix="/question")
app.include_router(school_router, prefix="/school")
app.include_router(specialized_router, prefix="/specialized")
app.include_router(area_router, prefix="/area")
app.include_router(branch_router, prefix="/branch")
app.include_router(unit_router, prefix="/unit")
app.include_router(auth_router, prefix="/auth")
app.include_router(user_router, prefix="/user")
