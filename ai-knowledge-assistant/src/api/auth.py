from fastapi import APIRouter

from src.schemas.auth import (RegisterRequest)

from src.services.auth_service import (register_user)

router = APIRouter()

@router.post("/register")
async def register(data: RegisterRequest):
    return register_user(data)

