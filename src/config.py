from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APPLICATION_VERSION: str = "test"
    TEST_MODE: bool = False 
    DATABASE_URL: str = "unset" if TEST_MODE else None
    DATABASE_SCHEMA: str = "public"

    class Config:
        env_file = ".env"  

def get_settings():
    return Settings()
