import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_API_TOKEN = str(os.getenv("TELEGRAM_API_TOKEN"))
TELEGRAM_OWNER_ID = str(os.getenv("TELEGRAM_OWNER_ID"))

PG_USER = str(os.getenv("PG_USER"))
PG_PASSWORD = str(os.getenv("PG_PASSWORD"))
PG_DATABASE = str(os.getenv("PG_DB"))
PG_HOST = str(os.getenv("PG_HOST"))

admins = [
    23466746
]