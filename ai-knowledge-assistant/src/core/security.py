from passlib.context import CryptContext

from jose import jwt
from src.core.config import settings

pwd = CryptContext(
    schemes=["pbkdf2_sha256"],
    deprecated="auto"
)


def hash_password(password):
    return pwd.hash(password)

def verify_password(plain, hashed):
    return pwd.verify(plain, hashed)

def create_token(data):
    return jwt.encode(
        data,
        settings.JWT_SECRET,
        algorithm="HS256"
    )
