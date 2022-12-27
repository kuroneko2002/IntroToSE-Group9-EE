import pymongo

password='group9'
#connect to cluster in MongoDB
connection_string = f'mongodb+srv://group9:{password}@cluster0.yorkz9p.mongodb.net/?retryWrites=true&w=majority'

def getAll(db_name, col_name):
    try:
        client= pymongo.MongoClient(connection_string)

        #connect to Account Database
        db=client[db_name]

        #connect to Account Collection in Account Database
        account_coll=db[col_name]

        #get data
        data=account_coll.find()
        if(data):
            return data
        return "None"
    except:
        return 'Error'

def get(db_name, col_name, key, key_value):
    try:
        client= pymongo.MongoClient(connection_string)

        #connect to Account Database
        db=client[db_name]

        #connect to Account Collection in Account Database
        account_coll=db[col_name]

        #update data
        query = {key: key_value}
        data = account_coll.find(query)
        return data

    except:
        return 'Error'

def insert_db(db_name, col_name, data):
    try:
        client= pymongo.MongoClient(connection_string)

        #connect to Account Database
        db=client[db_name]

        #connect to Account Collection in Account Database
        account_coll=db[col_name]

        #insert data
        x = account_coll.insert_one(data)
        return x.insert_id

    except:
        return 'Error'

def update_db(db_name, col_name, key, key_value, update_key, update_value):
    try:
        client= pymongo.MongoClient(connection_string)

        #connect to Account Database
        db=client[db_name]

        #connect to Account Collection in Account Database
        account_coll=db[col_name]

        #update data
        query = {key: key_value}
        newvalues = {"$set": {update_key: update_value}}
        account_coll.update_one(query, newvalues)
        return 'Succeed'

    except:
        return 'Error'

def delete(db_name, col_name, key, value):
    try:
        client= pymongo.MongoClient(connection_string)

        #connect to Account Database
        db=client[db_name]

        #connect to Account Collection in Account Database
        account_coll=db[col_name]

        #delete data
        query = {key: value}
        account_coll.delete_one(query)
        return 'Succeed'

    except:
        return 'Error'

def deleteAll(db_name, col_name):
    try:
        client= pymongo.MongoClient(connection_string)

        #connect to Account Database
        db=client[db_name]

        #connect to Account Collection in Account Database
        account_coll=db[col_name]

        #delete data
        x=account_coll.delete_many({})
        return x.deleted_count
    except:
        return 'Error'

def getSize(db_name, col_name):
    try:
        client= pymongo.MongoClient(connection_string)

        #connect to Account Database
        db=client[db_name]

        #connect to Account Collection in Account Database
        account_coll=db[col_name]

        return len(account_coll)
        
    except:
        return 'Error'