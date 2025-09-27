from pydantic import BaseModel, Field
from datetime import datetime

class ClinicianExport(BaseModel):
    export_id: str = Field(..., alias="_id")
    user_id: str
    export_date: datetime
    exported_summary: str
    consent_status: str
    
    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "export_id": "export_001",
                "user_id": "user_001",
                "export_date": "2024-01-01T10:00:00Z",
                "exported_summary": "Patient showed 30% improvement in anxiety levels...",
                "consent_status": "granted"
            }
        }

class ClinicianExportCreate(BaseModel):
    user_id: str
    export_date: datetime = Field(default_factory=datetime.utcnow)
    exported_summary: str
    consent_status: str = "pending"
