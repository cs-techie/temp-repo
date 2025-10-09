# Mentor Search Backend

Short: Search infra for mentors using FastAPI + Elasticsearch + Redis

## Installation
1. docker-compose up -d
2. pip install -r requirements.txt
3. configure .env (DATABASE_URL, ES_URL, REDIS_URL)
4. python scripts/reindex.py

## Run
uvicorn main:app --reload

## API
POST /search/mentors
Body: See app/schemas.py

## Testing
pytest
