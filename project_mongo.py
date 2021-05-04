from pymongo import MongoClient
mc=MongoClient("localhost:27017")
db=mc.project
d={"_id":2231,"pname":'Pendrive',"cost":1250}
db.product.insert_one(d)
mc.close()
