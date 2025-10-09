from sqlalchemy import Column, Integer, String, JSON, Float, DateTime
from .database import Base
import datetime

class Mentor(Base):
    __tablename__ = "mentors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    bio = Column(String)
    skills = Column(String)  # comma-separated for demo; normalize in prod
    exp_years = Column(Integer, default=0)
    rating = Column(Float, default=0.0)
    city = Column(String)
    country = Column(String)
    availability = Column(JSON, default=[])  # list of slot dicts
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
