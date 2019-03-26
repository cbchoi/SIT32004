import pymongo

conn = pymongo.MongoClient('localhost', 27017)

db = conn.get_database('db_ams')
collection = db.log

results = collection.find()

for result in results:
	print(result)