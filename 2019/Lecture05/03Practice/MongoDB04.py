import pymongo

conn = pymongo.MongoClient('localhost', 27017)
db = conn.get_database('mongo_test')
collection = db.get_collection('customer')

collection.replace_one({'name':'cbchoi1'}, {'name':'cbchoi1', 'category':2, 'region':'Daejeon'})

results = collection.find()
[print(result) for result in results]