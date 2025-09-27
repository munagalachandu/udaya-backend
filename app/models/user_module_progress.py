from pydantic import BaseModel, Field
from datetime import datetime

class UserModuleProgress(BaseModel):
    progress_id: str = Field(..., alias="_id")
    user_id: str
    module_id: str
    completion_percent: float
    last_accessed: datetime
    
    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "progress_id": "progress_001",
                "user_id": "user_001",
                "module_id": "module_001",
                "completion_percent": 75.5,
                "last_accessed": "2024-01-01T10:00:00Z"
            }
        }

class UserModuleProgressCreate(BaseModel):
    user_id: str
    module_id: str
    completion_percent: float = 0.0
    last_accessed: datetime = Field(default_factory=datetime.utcnow)