from elasticsearch import Elasticsearch
from ..config import settings

_es = None

def get_es_client():
    global _es
    if _es is None:
        try:
            _es = Elasticsearch(settings.ES_URL)
        except Exception:
            _es = None
    return _es

import aioredis
from ..config import settings

_redis = None

async def get_redis():
    global _redis
    if _redis is None:
        try:
            _redis = await aioredis.create_redis_pool(settings.REDIS_URL, encoding="utf-8")
        except Exception:
            _redis = None
    return _redis
