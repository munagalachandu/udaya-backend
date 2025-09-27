from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
from datetime import datetime
from ..models.wearable_data import WearableData, WearableDataCreate
from ..database import get_collection
from ..schemas.responses import StandardResponse
import uuid

router = APIRouter(prefix="/wearable-data", tags=["wearable-data"])

@router.post("/", response_model=StandardResponse)
async def create_wearable_data(data: WearableDataCreate):
    collection = get_collection("wearable_data")
    data_dict = data.model_dump()
    data_dict["_id"] = f"data_{uuid.uuid4().hex[:8]}"
    
    result = await collection.insert_one(data_dict)
    if result.inserted_id:
        return StandardResponse(
            success=True,
            message="Wearable data created successfully",
            data={"data_id": data_dict["_id"]}
        )
    raise HTTPException(status_code=500, detail="Failed to create wearable data")

@router.get("/user/{user_id}", response_model=List[WearableData])
async def get_user_wearable_data(
    user_id: str,
    start_date: Optional[datetime] = Query(None),
    end_date: Optional[datetime] = Query(None)
):
    collection = get_collection("wearable_data")
    query = {"user_id": user_id}
    
    if start_date or end_date:
        query["timestamp"] = {}
        if start_date:
            query["timestamp"]["$gte"] = start_date
        if end_date:
            query["timestamp"]["$lte"] = end_date
    
    data_points = []
    async for data in collection.find(query).sort("timestamp", -1):
        data_points.append(WearableData(**data))
    return data_points