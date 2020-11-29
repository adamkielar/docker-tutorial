from celery import Celery

from app.config import backend_conn_uri, broker_conn_uri

celery = Celery("hello", backend=backend_conn_uri, broker=broker_conn_uri)
