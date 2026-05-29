import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "200"))

DEVS = list(map(int, os.getenv("DEVS", "1793916962").split()))

API_ID = int(os.getenv("API_ID", "30395855"))

API_HASH = os.getenv("API_HASH", "1c30da83b5287120b7f73246c39fd8a9")

BOT_TOKEN = os.getenv("BOT_TOKEN", "8829445598:AAE4YV1EkIZgNbpgX5tbTicILgFjQCgQgs4")

OWNER_ID = int(os.getenv("OWNER_ID", "1793916962"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1003985982211").split()))

RMBG_API = os.getenv("RMBG_API", "JNXT9FWy39r4KxwjUcdyi3KM")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://ikyubottel:ikyy6@cluster0.olr1ho0.mongodb.net/?appName=Cluster0")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1003985982211"))
