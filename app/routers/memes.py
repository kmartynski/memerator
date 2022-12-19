from fastapi import APIRouter
from fastapi.responses import JSONResponse


router = APIRouter(
    prefix="/memes",
    tags=["memes"],
)
