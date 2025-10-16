import os

BASE_URL = "https://www.demoblaze.com"
DEFAULT_TIMEOUT = 10000
HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"
