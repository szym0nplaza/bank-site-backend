from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    password_key: str = Field(env="PASSWORD_ENCRYPTION_KEY")

    class Config:
        env_file = ".env"


settings = Settings()