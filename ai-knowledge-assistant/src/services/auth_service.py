from src.models.user import User
from src.core.database import SessionLocal
from src.core.security import (hash_password,create_token)
from src.core.security import verify_password
from fastapi import HTTPException
 
def register_user(data):

    db = SessionLocal()

    existing_user = (
        db.query(User)
        .filter(User.email == data.email)
        .first()
    )

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    user = User(
        email=data.email,
        password=hash_password(data.password)
    )

    db.add(user)

    db.commit()

    db.close()

    return {"message": "registered"}


def login_user(user):

    token = create_token(
        {
            "sub": user.email
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }

def authenticate_user(data):

    db = SessionLocal()

    user = (
        db.query(User)
        .filter(User.email == data.email)
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    if not verify_password(
        data.password,
        user.password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )
    
    db.close()

    return login_user(user)