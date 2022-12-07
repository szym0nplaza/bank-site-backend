from pydantic import BaseSettings, Field
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from elasticsearch import Elasticsearch


class Settings(BaseSettings):
    debug: bool = bool(Field(env="DEBUG"))
    password_key: str = Field(env="PASSWORD_ENCRYPTION_KEY")
    db_name: str = Field(env="DB_NAME")
    db_user: str = Field(env="DB_USER")
    db_password: str = Field(env="DB_PASSWORD")
    db_host: str = Field(env="DB_HOST")
    elasticsearch_host: str = Field(env="ELASTICSEARCH_HOST")

    @property
    def db_string(self) -> str:
        return f"postgresql://{self.db_user}:{self.db_password}@{self.db_host}:5432/{self.db_name}"

    @property
    def elasticsearch_string(self) -> str:
        return f"http://{self.elasticsearch_host}:9200"

    class Config:
        env_file = ".env"


settings = Settings()


class DBSession:
    """Handles base db configuration and session access in repos"""

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


class ESClient:
    """Class for initiating Elasticsearch client"""

    _es = Elasticsearch(settings.elasticsearch_string)

    def search(self, search_data: dict, index: str) -> list:
        result = self._es.search(index=index, body={"query": {"match": search_data}})
        return result["hits"]["hits"] # Get nested ES search response

    def index(self, body: dict, index: str):
        self._es.index(index=index, document=body)