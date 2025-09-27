from fastapi import APIRouter, HTTPException, status
from typing import List
from ..models.user import User, UserCreate
from ..database import get_collection
from ..schemas.responses import StandardResponse
import uuid

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=StandardResponse)
async def create_user(user: UserCreate):
    collection = get_collection("users")
    user_dict = user.model_dump()
    user_dict["_id"] = f"user_{uuid.uuid4().hex[:8]}"
    
    result = await collection.insert_one(user_dict)
    if result.inserted_id:
        return StandardResponse(
            success=True,
            message="User created successfully",
            data={"user_id": user_dict["_id"]}
        )
    raise HTTPException(status_code=500, detail="Failed to create user")

@router.get("/{user_id}", response_model=User)
async def get_user(user_id: str):
    collection = get_collection("users")
    user = await collection.find_one({"_id": user_id})
    if user:
        return User(**user)
    raise HTTPException(status_code=404, detail="User not found")

@router.get("/", response_model=List[User])
async def list_users():
    collection = get_collection("users")
    users = []
    async for user in collection.find():
        users.append(User(**user))
    return users