from app.database import get_collection
from datetime import datetime, timedelta
import uuid

async def seed_database():
    """Seed the database with dummy data"""
    
    # Seed Users
    users_collection = get_collection("users")
    if await users_collection.count_documents({}) == 0:
        dummy_users = [
            {
                "_id": "user_001",
                "name": "Alice Johnson",
                "email": "alice@example.com",
                "dob": datetime(1992, 5, 15),
                "gender": "female",
                "language_pref": "en",
                "privacy_consent": True,
                "created_at": datetime.utcnow()
            },
            {
                "_id": "user_002",
                "name": "Bob Smith",
                "email": "bob@example.com",
                "dob": datetime(1988, 8, 22),
                "gender": "male",
                "language_pref": "en",
                "privacy_consent": True,
                "created_at": datetime.utcnow()
            },
            {
                "_id": "user_003",
                "name": "Carol Davis",
                "email": "carol@example.com",
                "dob": datetime(1995, 12, 3),
                "gender": "female",
                "language_pref": "es",
                "privacy_consent": True,
                "created_at": datetime.utcnow()
            }
        ]
        await users_collection.insert_many(dummy_users)
        print("Seeded users")
    
    # Seed Therapy Modules
    modules_collection = get_collection("therapy_modules")
    if await modules_collection.count_documents({}) == 0:
        dummy_modules = [
            {
                "_id": "module_001",
                "name": "Anxiety Management",
                "type": "CBT",
                "description": "Learn cognitive behavioral techniques to manage anxiety"
            },
            {
                "_id": "module_002",
                "name": "Mindfulness Meditation",
                "type": "Mindfulness",
                "description": "Practice mindfulness and meditation for mental well-being"
            },
            {
                "_id": "module_003",
                "name": "Sleep Hygiene",
                "type": "Behavioral",
                "description": "Improve sleep quality through behavioral changes"
            },
            {
                "_id": "module_004",
                "name": "Stress Reduction",
                "type": "CBT",
                "description": "Techniques to identify and reduce stress triggers"
            }
        ]
        await modules_collection.insert_many(dummy_modules)
        print("Seeded therapy modules")
    
    # Seed Sessions
    sessions_collection = get_collection("sessions")
    if await sessions_collection.count_documents({}) == 0:
        base_time = datetime.utcnow() - timedelta(days=7)
        dummy_sessions = [
            {
                "_id": "session_001",
                "user_id": "user_001",
                "start_time": base_time,
                "end_time": base_time + timedelta(minutes=45),
                "mood_summary": "User reported feeling anxious about work presentation",
                "conversation_log": "Discussed breathing techniques and positive self-talk"
            },
            {
                "_id": "session_002",
                "user_id": "user_001",
                "start_time": base_time + timedelta(days=1),
                "end_time": base_time + timedelta(days=1, minutes=50),
                "mood_summary": "Improved mood, less anxiety reported",
                "conversation_log": "Practiced mindfulness exercises, user felt more centered"
            },
            {
                "_id": "session_003",
                "user_id": "user_002",
                "start_time": base_time + timedelta(days=2),
                "end_time": base_time + timedelta(days=2, minutes=40),
                "mood_summary": "User struggling with sleep issues",
                "conversation_log": "Discussed sleep hygiene and relaxation techniques"
            }
        ]
        await sessions_collection.insert_many(dummy_sessions)
        print("Seeded sessions")
    
    # Seed Wearable Data
    wearable_collection = get_collection("wearable_data")
    if await wearable_collection.count_documents({}) == 0:
        dummy_wearable_data = []
        users = ["user_001", "user_002", "user_003"]
        
        for i in range(50):  # Generate 50 data points
            timestamp = datetime.utcnow() - timedelta(hours=i)
            dummy_wearable_data.append({
                "_id": f"data_{uuid.uuid4().hex[:8]}",
                "user_id": users[i % 3],
                "timestamp": timestamp,
                "heart_rate": 70 + (i % 30),
                "hrv": 40 + (i % 20),
                "spo2": 95 + (i % 5),
                "device_type": "smartwatch" if i % 2 == 0 else "fitness_tracker"
            })
        
        await wearable_collection.insert_many(dummy_wearable_data)
        print("Seeded wearable data")
    
    # Seed Facial Emotions
    emotions_collection = get_collection("facial_emotions")
    if await emotions_collection.count_documents({}) == 0:
        emotions = ["happy", "sad", "neutral", "anxious", "calm"]
        dummy_emotions = []
        
        for i in range(30):
            timestamp = datetime.utcnow() - timedelta(hours=i*2)
            dummy_emotions.append({
                "_id": f"emotion_{uuid.uuid4().hex[:8]}",
                "user_id": users[i % 3],
                "timestamp": timestamp,
                "detected_emotion": emotions[i % len(emotions)],
                "confidence": 0.6 + (i % 4) * 0.1
            })
        
        await emotions_collection.insert_many(dummy_emotions)
        print("Seeded facial emotions")
    
    # Seed User Module Progress
    progress_collection = get_collection("user_module_progress")
    if await progress_collection.count_documents({}) == 0:
        modules = ["module_001", "module_002", "module_003", "module_004"]
        dummy_progress = []
        
        for user in users:
            for i, module in enumerate(modules):
                dummy_progress.append({
                    "_id": f"progress_{uuid.uuid4().hex[:8]}",
                    "user_id": user,
                    "module_id": module,
                    "completion_percent": min(100, (i + 1) * 25 + (hash(user) % 20)),
                    "last_accessed": datetime.utcnow() - timedelta(days=i)
                })
        
        await progress_collection.insert_many(dummy_progress)
        print("Seeded user module progress")
    
    print("Database seeding completed!")