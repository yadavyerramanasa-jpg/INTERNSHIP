from pymongo import MongoClient
from dotenv import load_dotenv
import certifi
import os

# Load Environment Variables
load_dotenv()

# MongoDB Connection String
MONGO_URI = os.getenv("MONGO_URI")

if not MONGO_URI:
    raise Exception("❌ MONGO_URI not found in .env file")

# Connect MongoDB Atlas
client = MongoClient(
    MONGO_URI,
    tls=True,
    tlsCAFile=certifi.where()
)

# Test Connection
try:
    client.admin.command("ping")
    print("✅ MongoDB Connected Successfully!")
except Exception as e:
    print("❌ MongoDB Connection Failed!")
    print(e)

# Database
db = client["AuraStyleDB"]

# Collection
products = db["products"]