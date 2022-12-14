import pika
from aio_pika import connect_robust
from elasticsearch import Elasticsearch
from pydantic import BaseSettings, Field
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .logger import logger


class Settings(BaseSettings):
    debug: bool = bool(Field(env="DEBUG"))
    password_key: str = Field(env="PASSWORD_ENCRYPTION_KEY")
    db_name: str = Field(env="DB_NAME")
    db_user: str = Field(env="DB_USER")
    db_password: str = Field(env="DB_PASSWORD")
    db_host: str = Field(env="DB_HOST")
    elasticsearch_host: str = Field(env="ELASTICSEARCH_HOST")
    rabbitmq_host: str = Field(env="RABBITMQ_HOST")

    @property
    def db_string(self) -> str:
        return f"postgresql://{self.db_user}:{self.db_password}@{self.db_host}:5432/{self.db_name}"

    @property
    def elasticsearch_string(self) -> str:
        return f"http://{self.elasticsearch_host}:9200"

    class Config:
        env_file = ".env"


settings = Settings()


# DB session and connection
class DBSession:
    """
    Handles base db configuration and session access in repos \n
    `get_session` method returns session for performing db operations
    """

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


# Elasticsearch configuration
class ESClient:
    """
    Class for initiating Elasticsearch client \n
    `search` - returns data from given index (available with detailed searching) \n
    `index` - add data in dict form to given index
    """

    _es = Elasticsearch(settings.elasticsearch_string)

    def search(self, search_data: dict, index: str) -> list:
        result = self._es.search(index=index, body={"query": {"match": search_data}})
        return result["hits"]["hits"]  # Get nested ES search response

    def index(self, body: dict, index: str):
        self._es.index(index=index, document=body)


# RabbitMQ configuration
class RabbitMQClient:
    """Class configured for communicating and handling rabbitmq queue"""
    def __init__(self, queue_name: str):
        self.queue_name = queue_name
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=settings.rabbitmq_host)
        )
        self.channel = self.connection.channel()
        self.queue = self.channel.queue_declare(queue=self.queue_name)
        self.callback_queue = self.queue.method.queue

    async def consume(self, loop, process_data=lambda x: print(x)):
        """Setup message listener with the current running loop"""
        connection = await connect_robust(
            host=settings.rabbitmq_host, port=5672, loop=loop
        )
        channel = await connection.channel()
        queue = await channel.declare_queue(self.queue_name)
        await queue.consume(process_data, no_ack=False)
        logger.info("Established pika async listener")
        return connection
