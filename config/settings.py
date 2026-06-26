import os
from dotenv import load_dotenv

# Load .env file FIRST before reading any variables
load_dotenv()

# The base URL of the API we are testing
BASE_URL = os.getenv("BASE_URL", "https://reqres.in/api")

# How many seconds to wait for a response before giving up
TIMEOUT = 10

# Read API key - loaded from .env file
API_KEY = os.getenv("REQRES_API_KEY", "")

# Common headers sent with every request
HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "x-api-key": API_KEY
}
