from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.database import connect_to_mongo, close_mongo_connection
from app.routers import users, sessions, therapy_modules, wearable_data
from app.utils.seed_data import seed_database

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    await connect_to_mongo()
    await seed_database()  # Seed dummy data
    yield
    # Shutdown
    await close_mongo_connection()

app = FastAPI(
    title="Mental Health Therapy API",
    description="A comprehensive API for mental health therapy sessions with wearable integration",
    version="1.0.0",
    lifespan=lifespan
)

# Include routers
app.include_router(users.router)
app.include_router(sessions.router)
app.include_router(therapy_modules.router)
app.include_router(wearable_data.router)

@app.get("/")
async def root():
    return {"message": "Mental Health Therapy API", "version": "1.0.0"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}