from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class User(BaseModel):
    user_id: str = Field(..., alias="_id")
    name: str
    email: str
    dob: datetime
    gender: str
    language_pref: str
    privacy_consent: bool
    created_at: datetime = Field(default_factory=datetime.utcnow)
    
    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "user_id": "user_001",
                "name": "John Doe",
                "email": "john@example.com",
                "dob": "1990-01-01T00:00:00Z",
                "gender": "male",
                "language_pref": "en",
                "privacy_consent": True
            }
        }

class UserCreate(BaseModel):
    name: str
    email: str
    dob: datetime
    gender: str
    language_pref: str = "en"
    privacy_consent: bool = True