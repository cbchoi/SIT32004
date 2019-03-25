import pymongo

conn = pymongo.MongoClient('localhost', 27017)
db = conn.get_database('mongo_test')
collection = db.get_collection('customer')
