from pydantic import BaseModel, Field
from datetime import datetime

class FacialEmotion(BaseModel):
    emotion_id: str = Field(..., alias="_id")
    user_id: str
    timestamp: datetime
    detected_emotion: str
    confidence: float
    
    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "emotion_id": "emotion_001",
                "user_id": "user_001",
                "timestamp": "2024-01-01T10:00:00Z",
                "detected_emotion": "happy",
                "confidence": 0.85
            }
        }

class FacialEmotionCreate(BaseModel):
    user_id: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    detected_emotion: str
    confidence: float
