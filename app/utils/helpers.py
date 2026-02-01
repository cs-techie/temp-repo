from elasticsearch import Elasticsearch
from ..config import settings

_es = None

def get_es_client() -> Elasticsearch:
    return Elasticsearch(
        settings.ES_URL,  # "https://localhost:9200"
        basic_auth=(settings.ES_USER, settings.ES_PASS),
        verify_certs=False  # for local testing only
    )

import aioredis
from ..config import settings

_redis = None

async def get_redis():
    global _redis
    if _redis is None:
        _redis = await aioredis.create_redis_pool(settings.REDIS_URL, encoding="utf-8")
    return _redis
