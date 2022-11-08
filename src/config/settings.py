from pydantic import BaseSettings, Field
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
    password_key: str = Field(env="PASSWORD_ENCRYPTION_KEY")
    db_name: str = Field(env="DB_NAME")
    db_user: str = Field(env="DB_USER")
    db_password: str = Field(env="DB_PASSWORD")

    @property
    @classmethod
    def db_string(cls) -> str:
        return (
            f"postgresql://{cls.db_user}:{cls.db_password}@localhost:5432/{cls.db_name}"
        )

    class Config:
        env_file = ".env"


class DBSession:
    session = sessionmaker(bind=create_engine(Settings.db_string))
    base = declarative_base()

    @classmethod
    def get_session(cls):
        session = cls.session()
        try:
            return session
        except:
            session.rollback()
        finally:
            session.close()
