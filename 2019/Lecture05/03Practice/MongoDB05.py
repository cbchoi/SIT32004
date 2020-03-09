import pymongo

conn = pymongo.MongoClient('localhost', 27017)
db = conn.get_database('mongo_test')
collection = db.get_collection('customer')

collection.delete_one({'name':'cbchoi1'})

results = collection.find()
[print(result) for result in results]