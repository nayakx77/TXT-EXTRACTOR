import os
from os import getenv

API_ID = int(os.environ.get("API_ID", "20699247"))  # Replace "123456" with your actual api_id or use .env
API_HASH = os.environ.get("API_HASH", "a1271e4ecc86745a62d222b62be8ba96")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8217326333:AAFo5uh-24KzUu9RCo2HTHq6XXB1NTSAim8")

OWNER_ID = int(os.environ.get("OWNER_ID", "1543124151"))  # Your Telegram user ID
SUDO_USERS = list(map(int, os.environ.get("SUDO_USERS", "").split()))  # Space-separated user IDs

MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://ravinayak77:ravixnayak@cluster0.wnazpuf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")##your mongo url eg: withmongodb+srv://xxxxxxx:xxxxxxx@clusterX.xxxx.mongodb.net/?retryWrites=true&w=majority
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002133500528"))  # Telegram channel ID (with -100 prefix)

PREMIUM_LOGS = os.environ.get("PREMIUM_LOGS", "")  # Optional here you'll get all logs
