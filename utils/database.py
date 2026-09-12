from pymongo import MongoClient
from config import MONGOURL, DATABASE_NAME, COLLECTION_NAME

client = MongoClient(MONGOURL)
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]

