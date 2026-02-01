from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    ES_URL: str = "https://localhost:9200"
    ES_USER: str = "elastic"
    ES_PASS: str = "changeme"  # match ELASTIC_PASSWORD
    REDIS_URL: str = "redis://localhost:6379/0"
    DATABASE_URL: str = "postgresql://user:pass@localhost:5432/mentors_db"
    MENTOR_INDEX: str = "mentors"
    CACHE_TTL_SECONDS: int = 120
    LOCK_TTL_MS: int = 10000

    class Config:
        env_file = ".env"

settings = Settings()
