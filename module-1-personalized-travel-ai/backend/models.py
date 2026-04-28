from pydantic import BaseModel
from typing import List, Optional

class Person(BaseModel):
    age: int
    gender: str

class TravelRequest(BaseModel):
    session_id: str

    people: List[Person]

    start_location: str

    # Destination flow
    destination_known: bool
    destination: Optional[str] = None   # single or comma-separated

    # Preferences
    budget: str
    budget_style: Optional[str] = None  # saver / balanced / comfort
    mood: str
    interests: str

    # Optional personalization
    experiences: Optional[str] = ""
    suggestions: Optional[str] = ""

    # Safety & pace
    walking_tolerance: Optional[str] = None  # low / medium / high
    crowd_preference: Optional[str] = None   # avoid / neutral / ok

    # Mode
    travel_time: str       # now / later
    persona: str           # guide / friend / emergency
    language: str          # english / tamil / hindi
