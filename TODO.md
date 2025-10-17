# TODO: Fix Internal Server Error by Making Redis and Elasticsearch Optional

## Steps:
- [x] Edit app/utils/helpers.py: Wrap get_redis() in try-except to return None on connection failure.
- [x] Edit app/api/main.py: Modify search_mentors to skip caching operations if redis is None.
- [x] Restart Uvicorn server if necessary (but --reload should handle file changes automatically).
- [x] Edit app/utils/helpers.py: Wrap get_es_client() in try-except to return None on connection failure.
- [x] Edit app/api/main.py: Modify search_mentors to return empty results if es is None.
- [x] Edit app/api/main.py: Wrap Elasticsearch search in try-except to handle runtime connection errors.
- [x] Test the /search/mentors endpoint with a sample POST request to confirm 200 OK with empty results (no 500 error).
- [x] Thorough testing: Edge cases (size>50: 400 OK, empty query: 200 empty, pagination page=2: 200 empty, sorting: 200 empty), other routers (genai/ml empty, no errors), server stability.
