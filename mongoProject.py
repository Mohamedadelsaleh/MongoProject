from http import client
import pymongo

client = pymongo.MongoClient('mongodb+srv://adel-khouly:adel-khouly9499@clusterofmongoprogect.xy8ec.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
print(client.list_database_names())

db=client['mongoProject']

print(db.list_collection_names())

collection=db.randomData

randomDataDocument = {
    "Name" : "Mohamed El-Yamany", 
    "Age" : 24, 
    "Faculty" : "Computer Science", 
    "City" : "Giza"
}


data1= db.randomData.insert_one(randomDataDocument).inserted_id
print(data1)