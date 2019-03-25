import pymongo

conn = pymongo.MongoClient('localhost', 27017)
db = conn.get_database('mongo_test')
collection = db.get_collection('customer')

#collection.insert_one({"name":"T.choi", "category":2, "region":'Pohang'})

results = collection.find({"region":'Pohang'})

[print(result) for result in results]