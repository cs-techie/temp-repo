#!/usr/bin/env python3
"""
Seed database with sample mentors.
Run: python migrations/seed_data.py
"""
from app.database import SessionLocal
from app.models import Mentor
from datetime import datetime

def main():
    db = SessionLocal()
    try:
        # Sample mentors data
        mentors = [
            {
                "name": "Sarah Mitchell",
                "bio": "Experienced corporate lawyer with 12 years in mergers and acquisitions",
                "skills": "Corporate Law, M&A, Contract Negotiation, Securities Law",
                "exp_years": 12,
                "rating": 4.9,
                "city": "New York",
                "country": "USA",
                "availability": [
                    {"slot_id": "slot1", "date": "2024-01-15", "start": "10:00", "end": "11:00", "is_booked": False},
                    {"slot_id": "slot2", "date": "2024-01-16", "start": "14:00", "end": "15:00", "is_booked": False}
                ]
            },
            {
                "name": "Michael Chen",
                "bio": "Criminal defense attorney specializing in white-collar crime cases",
                "skills": "Criminal Law, White-Collar Crime, Trial Advocacy, Legal Ethics",
                "exp_years": 15,
                "rating": 4.8,
                "city": "Los Angeles",
                "country": "USA",
                "availability": [
                    {"slot_id": "slot3", "date": "2024-01-17", "start": "09:00", "end": "10:00", "is_booked": False}
                ]
            },
            {
                "name": "Emily Rodriguez",
                "bio": "Family law specialist focusing on divorce and child custody matters",
                "skills": "Family Law, Divorce, Child Custody, Mediation, Domestic Relations",
                "exp_years": 10,
                "rating": 4.7,
                "city": "Chicago",
                "country": "USA",
                "availability": [
                    {"slot_id": "slot4", "date": "2024-01-18", "start": "11:00", "end": "12:00", "is_booked": False},
                    {"slot_id": "slot5", "date": "2024-01-19", "start": "15:00", "end": "16:00", "is_booked": False}
                ]
            },
            {
                "name": "David Wilson",
                "bio": "Full-stack developer with focus on scalable applications",
                "skills": "Java, Spring Boot, Angular, PostgreSQL",
                "exp_years": 9,
                "rating": 4.6,
                "city": "Berlin",
                "country": "Germany",
                "availability": [
                    {"slot_id": "slot6", "date": "2024-01-20", "start": "13:00", "end": "14:00", "is_booked": False}
                ]
            },
            {
                "name": "Eva Brown",
                "bio": "Mobile app developer for iOS and Android platforms",
                "skills": "Swift, Kotlin, React Native, Firebase",
                "exp_years": 5,
                "rating": 4.5,
                "city": "Sydney",
                "country": "Australia",
                "availability": [
                    {"slot_id": "slot7", "date": "2024-01-21", "start": "10:00", "end": "11:00", "is_booked": False},
                    {"slot_id": "slot8", "date": "2024-01-22", "start": "16:00", "end": "17:00", "is_booked": False}
                ]
            }
        ]

        for mentor_data in mentors:
            mentor = Mentor(**mentor_data)
            db.add(mentor)

        db.commit()
        print(f"Inserted {len(mentors)} sample mentors")

    except Exception as e:
        db.rollback()
        print(f"Error seeding data: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    main()
