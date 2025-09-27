from pydantic import BaseModel, Field
from typing import Optional

class TherapyModule(BaseModel):
    module_id: str = Field(..., alias="_id")
    name: str
    type: str  # CBT, mindfulness, etc.
    description: str
    
    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "module_id": "module_001",
                "name": "Anxiety Management",
                "type": "CBT",
                "description": "Learn techniques to manage anxiety through cognitive behavioral therapy"
            }
        }

class TherapyModuleCreate(BaseModel):
    name: str
    type: str
    description: str