from pydantic import BaseModel
from typing import List, Optional

class AvailabilitySlot(BaseModel):
    slot_id: str
    date: str
    start: str
    end: str
    is_booked: bool = False

class MentorOut(BaseModel):
    mentor_id: str
    name: str
    bio: Optional[str]
    skills: List[str]
    experience_years: int
    rating: float
    city: Optional[str]
    country: Optional[str]
    availability: List[AvailabilitySlot]

class SearchRequest(BaseModel):
    q: Optional[str] = ""
    skills: Optional[List[str]] = []
    city: Optional[str] = None
    min_experience: Optional[int] = None
    min_rating: Optional[float] = None
    page: int = 1
    size: int = 10
    sort_by: Optional[str] = None
