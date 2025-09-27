from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class Session(BaseModel):
    session_id: str = Field(..., alias="_id")
    user_id: str
    start_time: datetime
    end_time: Optional[datetime] = None
    mood_summary: Optional[str] = None
    conversation_log: Optional[str] = None
    
    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "session_id": "session_001",
                "user_id": "user_001",
                "start_time": "2024-01-01T10:00:00Z",
                "end_time": "2024-01-01T11:00:00Z",
                "mood_summary": "User reported feeling anxious but showed improvement",
                "conversation_log": "User discussed work stress..."
            }
        }

class SessionCreate(BaseModel):
    user_id: str
    start_time: datetime = Field(default_factory=datetime.utcnow)
    mood_summary: Optional[str] = None
    conversation_log: Optional[str] = None