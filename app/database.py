from motor.motor_asyncio import AsyncIOMotorClient
from typing import Optional
import os

class Database:
    client: Optional[AsyncIOMotorClient] = None
    
db = Database()

async def get_database() -> AsyncIOMotorClient:
    return db.client

async def connect_to_mongo():
    """Create database connection"""
    db.client = AsyncIOMotorClient(os.getenv("MONGODB_URL", "mongodb+srv://chandureddy8325_db_user:chandu123@cluster0.f3hnlmm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"))
async def close_mongo_connection():
    """Close database connection"""
    db.client.close()

def get_collection(collection_name: str):
    """Get a collection from the database"""
    return db.client.mental_health_db[collection_name]