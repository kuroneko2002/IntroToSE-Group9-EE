import pymongo

password='group9'
#connect to cluster in MongoDB
connection_string = f'mongodb+srv://group9:{password}@cluster0.yorkz9p.mongodb.net/?retryWrites=true&w=majority'
client= pymongo.MongoClient(connection_string)

# #connect to Account Database
# db=client["Account"]

# #connect to Account Collection in Account Database
# account_coll=db["Account"]

# #get data
# data=account_coll.find()