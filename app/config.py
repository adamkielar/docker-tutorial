import logging
import os
from functools import lru_cache

from pydantic import BaseSettings

log = logging.getLogger(__name__)

redis_host: str = os.getenv("REDIS_HOST")
redis_port: str = os.getenv("REDIS_PORT")
redis_celery_db_index: str = os.getenv("REDIS_CELERY_DB_INDEX")
redis_class_db_index: str = os.getenv("REDIS_CLASS_DB_INDEX")

rabbitmq_host: str = os.getenv("RABBITMQ_HOST")
rabbitmq_username: str = os.getenv("RABBITMQ_DEFAULT_USER")
rabbitmq_password: str = os.getenv("RABBITMQ_DEFAULT_PASS")
rabbitmq_port: str = os.getenv("RABBITMQ_PORT")

broker_conn_uri = f"amqp://{rabbitmq_username}:{rabbitmq_password}@{rabbitmq_host}:{rabbitmq_port}//"
backend_conn_uri = f"redis://{redis_host}:{redis_port}/{redis_celery_db_index}"
redis_class_conn_uri = f"redis://{redis_host}:{redis_port}/{redis_class_db_index}"


class Settings(BaseSettings):
    environment: str = os.getenv("ENVIRONMENT", "dev")
    testing: bool = os.getenv("TESTING", 0)

    fight_stance = ["Battle Stance", "Defensive Stance", "Gladiator Stance", "Berserker Stance", "One Punch Man Stance"]
    round_length_in_seconds = 10


@lru_cache()
def get_settings() -> BaseSettings:
    log.info("Loading config settings from the environment")
    return Settings()
