from passlib.context import CryptContext

from jose import jwt
from src.core.config import settings

from jose import JWTError

from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from src.models.user import User
from src.core.database import get_db

from datetime import datetime
from datetime import timedelta

from fastapi.security import HTTPAuthorizationCredentials
from fastapi.security import HTTPBearer

pwd = CryptContext(
    schemes=["pbkdf2_sha256"],
    deprecated="auto"
)


def hash_password(password):
    return pwd.hash(password)

def verify_password(plain, hashed):
    return pwd.verify(plain, hashed)

def create_token(data):

    payload = data.copy()

    payload["exp"] = (
        datetime.utcnow()
        + timedelta(hours=24)
    )

    return jwt.encode(
        payload,
        settings.JWT_SECRET,
        algorithm="HS256"
    )

def decode_token(token: str):

    try:
        return jwt.decode(
            token,
            settings.JWT_SECRET,
            algorithms=["HS256"]
        )

    except JWTError:
        return None
    
security = HTTPBearer()

def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):
    token = credentials.credentials

    payload = decode_token(token)

    if not payload:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    email = payload.get("sub")

    user = (
        db.query(User)
        .filter(User.email == email)
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="User not found"
        )

    return user