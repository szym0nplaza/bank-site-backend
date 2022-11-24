from pydantic import BaseSettings, Field
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
    debug: bool = bool(Field(env="DEBUG"))
    password_key: str = Field(env="PASSWORD_ENCRYPTION_KEY")
    db_name: str = Field(env="DB_NAME")
    db_user: str = Field(env="DB_USER")
    db_password: str = Field(env="DB_PASSWORD")

    @property
    def db_string(self) -> str:
        return (
            f"postgresql://{self.db_user}:{self.db_password}@localhost:5432/{self.db_name}"
        )

    class Config:
        env_file = ".env"


settings = Settings()


class DBSession:
    _session = sessionmaker(bind=create_engine(settings.db_string))
    base = declarative_base()

    @classmethod
    def get_session(cls) -> _session:
        session = cls._session()
        try:
            return session
        except:
            session.rollback()
        finally:
            session.close()