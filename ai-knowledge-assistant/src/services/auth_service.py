from fastapi import HTTPException

from src.models.user import User
from src.core.database import SessionLocal
from src.core.security import (
    hash_password,
    create_token,
    verify_password
)
from src.core.logger import logger


def register_user(data):

    db = SessionLocal()

    existing_user = (
        db.query(User)
        .filter(User.email == data.email)
        .first()
    )

    if existing_user:

        logger.warning(
            {
                "event": "registration_failed",
                "email": data.email,
                "reason": "email_already_exists"
            }
        )

        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    user = User(
        email=data.email,
        password=hash_password(data.password)
    )

    try:

        db.add(user)

        db.commit()

        logger.info(
            {
                "event": "user_registered",
                "email": data.email
            }
        )

    except Exception as e:

        logger.exception(
            {
                "event": "registration_error",
                "email": data.email,
                "error": str(e)
            }
        )

        raise

    finally:

        db.close()

    return {
        "message": "registered"
    }


def login_user(user):

    token = create_token(
        {
            "sub": user.email
        }
    )

    logger.info(
        {
            "event": "user_login",
            "email": user.email
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }


def authenticate_user(data):

    db = SessionLocal()

    try:

        user = (
            db.query(User)
            .filter(User.email == data.email)
            .first()
        )

    except Exception as e:

        logger.exception(
            {
                "event": "login_error",
                "email": data.email,
                "error": str(e)
            }
        )

        raise

    if not user:

        logger.warning(
            {
                "event": "login_failed",
                "email": data.email,
                "reason": "user_not_found"
            }
        )

        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    if not verify_password(
        data.password,
        user.password
    ):

        logger.warning(
            {
                "event": "login_failed",
                "email": data.email,
                "reason": "invalid_credentials"
            }
        )

        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    db.close()

    return login_user(user)