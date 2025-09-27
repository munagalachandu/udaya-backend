from fastapi import APIRouter, HTTPException
from typing import List
from ..models.session import Session, SessionCreate
from ..database import get_collection
from ..schemas.responses import StandardResponse

import uuid

router = APIRouter(prefix="/sessions", tags=["sessions"])

@router.post("/", response_model=StandardResponse)
async def create_session(session: SessionCreate):
    collection = get_collection("sessions")
    session_dict = session.model_dump()
    session_dict["_id"] = f"session_{uuid.uuid4().hex[:8]}"
    
    result = await collection.insert_one(session_dict)
    if result.inserted_id:
        return StandardResponse(
            success=True,
            message="Session created successfully",
            data={"session_id": session_dict["_id"]}
        )
    raise HTTPException(status_code=500, detail="Failed to create session")

@router.get("/user/{user_id}", response_model=List[Session])
async def get_user_sessions(user_id: str):
    collection = get_collection("sessions")
    sessions = []
    async for session in collection.find({"user_id": user_id}):
        sessions.append(Session(**session))
    return sessions

@router.put("/{session_id}/end")
async def end_session(session_id: str):
    from datetime import datetime
    collection = get_collection("sessions")
    result = await collection.update_one(
        {"_id": session_id},
        {"$set": {"end_time": datetime.utcnow()}}
    )
    if result.modified_count:
        return StandardResponse(success=True, message="Session ended successfully")
    raise HTTPException(status_code=404, detail="Session not found")