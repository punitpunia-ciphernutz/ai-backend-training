from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    GEMINI_API_KEY: str
    JWT_SECRET: str
    DATABASE_URL: str
    REDIS_URL: str

    class Config:
        env_file = ".env"

settings = Settings()