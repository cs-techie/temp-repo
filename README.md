
=======
# Mentor Search Backend

Short: Search infra for mentors using FastAPI + Elasticsearch + Redis

## Table of Contents

- [Mentor Search Backend](#mentor-search-backend)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Folder Structure](#folder-structure)
  - [Installation](#installation)
  - [Configuration](#configuration)
  - [Usage](#usage)
  - [API Endpoints](#api-endpoints)
    - [POST /search/mentors](#post-searchmentors)
  - [Testing](#testing)
  - [Contributing](#contributing)
  - [License](#license)
  - [Contact](#contact)
- [For questions or support, please contact the maintainers.](#for-questions-or-support-please-contact-the-maintainers)
- [Ashkan Added](#ashkan-added)
  - [run redis](#run-redis)
  - [run ellasticSearch](#run-ellasticsearch)
  - [run fastapi app](#run-fastapi-app)
  - [if you still get error because there is no mentor field add it with curl command in console](#if-you-still-get-error-because-there-is-no-mentor-field-add-it-with-curl-command-in-console)

## Overview

This project provides a backend service for searching mentors using FastAPI, Elasticsearch for indexing and searching, and Redis for caching. It allows users to search for mentors based on various criteria.

## Folder Structure

- `app/`: Main application code
  - `api/`: API endpoints
  - `services/`: Business logic services
  - `utils/`: Utility functions and clients
  - `models.py`: Database models
  - `schemas.py`: Pydantic schemas
  - `config.py`: Configuration settings
  - `database.py`: Database connection
- `scripts/`: Utility scripts for setup and maintenance
- `tests/`: Unit and integration tests
- `main.py`: FastAPI application entry point
- `requirements.txt`: Python dependencies
- `docker-compose.yml`: Docker services configuration
- `README.md`: This file

## Installation

1. Clone the repository:
   ```bash
   git clone <repo_url>
   cd mentor_search_backend
   ```

2. Start the required services using Docker Compose:
   ```bash
   docker-compose up -d
   ```

3. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the reindexing script to populate Elasticsearch:
   ```bash
   python scripts/reindex.py
   ```

## Configuration

Configure the following environment variables in a `.env` file:

- `DATABASE_URL`: URL for the database connection
- `ES_URL`: URL for Elasticsearch
- `REDIS_URL`: URL for Redis

You can also modify `app/config.py` for additional configuration settings.

## Usage

To run the application in development mode:

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`.

## API Endpoints

### POST /search/mentors

Search for mentors based on criteria.

**Request Body:** See `app/schemas.py` for the expected schema.

**Example Request:**
```json
{
  "query": "python",
  "location": "remote"
}
```

**Response:**
```json
{
  "mentors": [
    {
      "id": 1,
      "name": "John Doe",
      "skills": ["Python", "Django"]
    }
  ]
}
```

## Testing

Run the tests using pytest:

```bash
pytest
```

## Contributing

Please read the contributing guidelines before making contributions.

## License

This project is licensed under the MIT License.

## Contact

For questions or support, please contact the maintainers.
=======


# Ashkan Added

## run redis
```bash
docker run -p 6379:6379 redis
```

## run ellasticSearch
```bash
docker run -d --name elasticsearch -e "discovery.type=single-node" -e "ELASTIC_PASSWORD=changeme" -p 9200:9200 docker.elastic.co/elasticsearch/elasticsearch:8.14.0
```

## run fastapi app
```bash
uvicorn main:app --reload
```

## if you still get error because there is no mentor field add it with curl command in console
```bash
curl -k -u elastic:changeme -X PUT "https://localhost:9200/mentors" -H 'Content-Type: application/json' -d'
{
  "mappings": {
    "properties": {
      "name": { "type": "text" },
      "bio": { "type": "text" },
      "skills": { "type": "keyword" },
      "location": { "properties": { "city": { "type": "keyword" } } },
      "experience_years": { "type": "integer" },
      "rating": { "type": "float" }
    }
  }
}
'
```