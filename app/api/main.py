from fastapi import APIRouter, HTTPException
from typing import Any

from ..schemas import SearchRequest
from ..utils.helpers import get_es_client, get_redis
from ..config import settings
import json, hashlib

router = APIRouter()

@router.get("/health")
async def health():
    return {"status": "ok"}

def fingerprint(obj: dict) -> str:
    normalized = json.dumps(obj, sort_keys=True, separators=(',', ':'))
    return 'search:' + hashlib.sha256(normalized.encode()).hexdigest()

@router.post('/search/mentors')
async def search_mentors(body: SearchRequest):
    if body.size > 50:
        raise HTTPException(status_code=400, detail='size must be <= 50')

    es = get_es_client()
    redis = await get_redis()

    es_query = {'bool': {'must': [], 'filter': []}}
    if body.q:
        es_query['bool']['must'].append({
            'multi_match': {'query': body.q, 'fields': ['name^3', 'bio', 'skills', 'location.city']}
        })
    if body.skills:
        es_query['bool']['filter'].append({'terms': {'skills.raw': body.skills}})
    if body.city:
        es_query['bool']['filter'].append({'term': {'location.city': body.city}})
    if body.min_experience is not None:
        es_query['bool']['filter'].append({'range': {'experience_years': {'gte': body.min_experience}}})
    if body.min_rating is not None:
        es_query['bool']['filter'].append({'range': {'rating': {'gte': body.min_rating}}})

    body_dict = {'query': es_query, 'from': (body.page - 1) * body.size, 'size': body.size}
    if body.sort_by:
        if ':' in body.sort_by:
            field, order = body.sort_by.split(':')
            body_dict['sort'] = [{field: {'order': order}}]

    key = fingerprint(body_dict)
    cached = await redis.get(key)
    if cached:
        return json.loads(cached)

    res = es.search(index=settings.MENTOR_INDEX, body=body_dict)
    hits = [{**hit.get('_source', {}), '_score': hit.get('_score'), '_id': hit.get('_id')} for hit in res['hits']['hits']]
    out = {'total': res['hits']['total']['value'], 'page': body.page, 'size': body.size, 'results': hits}
    await redis.set(key, json.dumps(out))
    await redis.expire(key, settings.CACHE_TTL_SECONDS)
    return out
