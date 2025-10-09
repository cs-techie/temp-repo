from elasticsearch import Elasticsearch
from ..config import settings

_es = None

def get_es_client() -> Elasticsearch:
    global _es
    if _es is None:
        _es = Elasticsearch(settings.ES_URL)
    return _es
