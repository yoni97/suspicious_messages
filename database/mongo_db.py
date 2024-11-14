from pymongo import MongoClient

# MongoDB setup
client = MongoClient('mongodb://mongodb:27017/')
db = client['suspicious_emails']
collection = db['messages_all']