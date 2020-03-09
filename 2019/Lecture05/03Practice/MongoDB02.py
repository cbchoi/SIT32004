import pymongo

conn = pymongo.MongoClient('localhost', 27017)
db = conn.get_database('mongo_test')
collection = db.get_collection('customer')

collection.insert_one({"name":"cbchoi", "category":1, "region":'Daejeon'})

results = collection.find()

[print(result) for result in results]