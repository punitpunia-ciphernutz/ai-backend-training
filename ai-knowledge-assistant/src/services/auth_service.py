from src.models.user import User
from src.core.database import SessionLocal
from src.core.security import (hash_password,create_token)
 
def register_user(data):

    db = SessionLocal()

    user = User(
        email=data.email,
        password=hash_password(data.password)
    )

    db.add(user)

    db.commit()

    return {"message": "registered"}


def login_user(user):

    token = create_token(
        {
            "sub": user.email
        }
    )

    return {
        "access_token": token
    }