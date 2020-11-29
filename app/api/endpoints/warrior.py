import redis

from fastapi import APIRouter, Depends

from app.config import get_settings, Settings
from app.config import redis_class_conn_uri

from app.worker.tasks import change_stance

redis_class = redis.Redis.from_url(redis_class_conn_uri)

router = APIRouter()


@router.get("/warrior/{name}")
async def warrior(name: str, settings: Settings = Depends(get_settings)):
    for i in range(5):
        change_stance.apply_async((name, settings.fight_stance[i]), countdown=i*settings.round_length_in_seconds)
    return True


@router.get("/stance/{name}")
async def stance(name: str):
    return redis_class.get(name)
