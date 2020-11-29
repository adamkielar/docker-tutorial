import redis

from .worker import celery
from app.config import redis_class_conn_uri

redis_class = redis.Redis.from_url(redis_class_conn_uri)


@celery.task
def change_stance(name, stance):
    redis_class.set(name, stance)
    return stance
