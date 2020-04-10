reg = {2200004:['SIT23005', "SIT22010", "SIT32004"],
       2200002:['SIT23004', "SIT22011", "SIT32005"],
       2200003:['SIT23004', "SIT22012", "SIT32006"]
}


'''
I     D| COURSE
--------
2200004| SIT23005
--------
2200004| SIT22010
--------
2200004| SIT32004
'''

print(reg[2200004])


import pymongo

conn = pymongo.MongoClient('localhost', 27017)
db = conn.get_database('mongo_test')
collection = db.get_collection('customer')

# INSERT INTO CUSTOMER(name, category, region) VALUES( "cbchoi", 1, "Daejeon")
#collection.insert_one({"name":"rchoi", "category":1, "region":'Daejeon'})

#collection.replace_one({'name':'cbchoi'}, {'name':'cbchoi1', 'category':2})

#results = collection.find({"name":"cbchoi"}) # SELECT * from CUSTOMER
results = collection.find() # SELECT * from CUSTOMER

[print(result) for result in results]





