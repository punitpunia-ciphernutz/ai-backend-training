from fastapi import APIRouter

from src.schemas.auth import (
    RegisterRequest,
    LoginRequest
)

from src.services.auth_service import (
    register_user,
    authenticate_user
)

router = APIRouter()

@router.post("/register")
async def register(data: RegisterRequest):
    return register_user(data)

@router.post("/login")
async def login(
    data: LoginRequest
):
    return authenticate_user(data)