from dotenv import load_dotenv
import os

load_dotenv()

MEMORYDB_HOST = os.getenv("MEMORYDB_HOST")
MEMORYDB_PORT = int(os.getenv("MEMORYDB_PORT"))
MEMORYDB_USER = os.getenv("MEMORYDB_USER")
MEMORYDB_PASSWORD = os.getenv("MEMORYDB_PASSWORD")
