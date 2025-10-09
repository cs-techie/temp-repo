#!/usr/bin/env python3
"""
Create database tables script.
Run: python migrations/create_tables.py
"""
from app.database import Base, engine
from sqlalchemy import text
import app.models  # Import models to register them with Base

def main():
    # Create tables using SQLAlchemy 2.0 style
    with engine.begin() as conn:
        Base.metadata.create_all(conn)
    print("Tables created successfully")

    # Verify tables exist
    with engine.connect() as conn:
        result = conn.execute(text("SELECT name FROM sqlite_master WHERE type='table';"))
        tables = result.fetchall()
        print(f"Tables in database: {[table[0] for table in tables]}")

if __name__ == "__main__":
    main()
