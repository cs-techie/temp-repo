import json
from elasticsearch import helpers
from ..utils.es_client import get_es_client
from ..config import settings

es = get_es_client()

MENTOR_MAPPING = {
  "mappings": {
    "properties": {
      "mentor_id": {"type": "keyword"},
      "name": {"type": "text", "fields": {"raw": {"type": "keyword"}}},
      "bio": {"type": "text"},
      "skills": {"type": "text", "fields": {"raw": {"type": "keyword"}}},
      "experience_years": {"type": "integer"},
      "rating": {"type": "float"},
      "location": {"properties": {"city": {"type": "keyword"}, "country": {"type": "keyword"}}},
      "availability": {"type": "nested", "properties": {"slot_id": {"type": "keyword"}, "date": {"type": "date"}, "start": {"type": "keyword"}, "end": {"type": "keyword"}, "is_booked": {"type": "boolean"}}},
      "created_at": {"type": "date"},
      "updated_at": {"type": "date"}
    }
  }
}

def create_index_if_not_exists(index_name: str = None):
    name = index_name or settings.MENTOR_INDEX
    if not es.indices.exists(index=name):
        es.indices.create(index=name, body=MENTOR_MAPPING)

def bulk_index(docs_iterable):
    helpers.bulk(es, docs_iterable)

def index_single(doc: dict):
    es.index(index=settings.MENTOR_INDEX, id=doc.get("mentor_id"), body=doc)

def update_availability(mentor_id: str, availability: list):
    es.update(index=settings.MENTOR_INDEX, id=mentor_id, body={"doc": {"availability": availability}})
