from fastapi import APIRouter, HTTPException
from typing import List
from ..models.therapy_module import TherapyModule, TherapyModuleCreate
from ..database import get_collection
from ..schemas.responses import StandardResponse
import uuid

router = APIRouter(prefix="/therapy-modules", tags=["therapy-modules"])

@router.post("/", response_model=StandardResponse)
async def create_therapy_module(module: TherapyModuleCreate):
    collection = get_collection("therapy_modules")
    module_dict = module.model_dump()
    module_dict["_id"] = f"module_{uuid.uuid4().hex[:8]}"
    
    result = await collection.insert_one(module_dict)
    if result.inserted_id:
        return StandardResponse(
            success=True,
            message="Therapy module created successfully",
            data={"module_id": module_dict["_id"]}
        )
    raise HTTPException(status_code=500, detail="Failed to create therapy module")

@router.get("/", response_model=List[TherapyModule])
async def list_therapy_modules():
    collection = get_collection("therapy_modules")
    modules = []
    async for module in collection.find():
        modules.append(TherapyModule(**module))
    return modules

@router.get("/{module_id}", response_model=TherapyModule)
async def get_therapy_module(module_id: str):
    collection = get_collection("therapy_modules")
    module = await collection.find_one({"_id": module_id})
    if module:
        return TherapyModule(**module)
    raise HTTPException(status_code=404, detail="Therapy module not found")