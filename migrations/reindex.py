"""
Simple reindex script: reads mentors from DB and bulk indexes.
Run: python migrations/reindex.py
"""
from app.database import SessionLocal
from app.models import Mentor
from app.services.ml_service import create_index_if_not_exists, bulk_index

def transform(m: Mentor):
    return {
        "_index": "mentors",
        "_id": str(m.id),
        "_source": {
            "mentor_id": str(m.id),
            "name": m.name,
            "bio": m.bio,
            "skills": m.skills.split(",") if m.skills else [],
            "experience_years": m.exp_years,
            "rating": m.rating,
            "location": {"city": m.city, "country": m.country},
            "availability": m.availability or [],
            "created_at": m.created_at,
            "updated_at": m.updated_at,
        }
    }

def main():
    create_index_if_not_exists()
    db = SessionLocal()
    try:
        mentors = db.query(Mentor).all()
        actions = [transform(m) for m in mentors]
        if actions:
            bulk_index(actions)
            print(f"Indexed {len(actions)} mentors")
        else:
            print("No mentors found in DB")
    finally:
        db.close()

if __name__ == "__main__":
    main()
