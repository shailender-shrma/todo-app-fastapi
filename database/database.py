from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
url = os.environ.get("URL")
password = os.environ.get("PASSWORD")

uri = MongoClient(f"{url}")

db = uri.todo_db

collection_name = db["todo_collection"]
