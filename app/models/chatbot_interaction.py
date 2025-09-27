from pydantic import BaseModel, Field
from datetime import datetime

class ChatbotInteraction(BaseModel):
    interaction_id: str = Field(..., alias="_id")
    session_id: str
    timestamp: datetime
    user_message: str
    bot_response: str
    sentiment: Optional[str] = None
    
    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "interaction_id": "interaction_001",
                "session_id": "session_001",
                "timestamp": "2024-01-01T10:00:00Z",
                "user_message": "I'm feeling anxious today",
                "bot_response": "I understand you're feeling anxious. Let's try some breathing exercises.",
                "sentiment": "negative"
            }
        }

class ChatbotInteractionCreate(BaseModel):
    session_id: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    user_message: str
    bot_response: str
    sentiment: Optional[str] = None