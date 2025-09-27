from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class WearableData(BaseModel):
    data_id: str = Field(..., alias="_id")
    user_id: str
    timestamp: datetime
    heart_rate: Optional[float] = None
    hrv: Optional[float] = None  # Heart Rate Variability
    spo2: Optional[float] = None  # Blood Oxygen
    device_type: str
    
    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "data_id": "data_001",
                "user_id": "user_001",
                "timestamp": "2024-01-01T10:00:00Z",
                "heart_rate": 72.5,
                "hrv": 45.2,
                "spo2": 98.5,
                "device_type": "smartwatch"
            }
        }

class WearableDataCreate(BaseModel):
    user_id: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    heart_rate: Optional[float] = None
    hrv: Optional[float] = None
    spo2: Optional[float] = None
    device_type: str