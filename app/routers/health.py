from fastapi import APIRouter
from fastapi.responses import JSONResponse


router = APIRouter()


@router.get("/health")
async def get_health():
    return JSONResponse({
        "status": "ok"
    })
