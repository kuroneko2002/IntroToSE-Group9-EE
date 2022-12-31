import models.myModules.CRUD_db as CRUD_db
import json

def archiveFormat(db_name, collection, data):
    backup = CRUD_db.getAll(db_name, collection)

    CRUD_db.deleteAll(db_name, collection)

    for obj in data:
        res = CRUD_db.insert_db(db_name, collection, obj)
        if (res == 'Error'):
            # backup data when adding process has something wrong!
            CRUD_db.deleteAll(db_name, collection)
            CRUD_db.backupData(db_name, collection, backup)
            return res
    
    return 'Succeed'


def archiveTest(type, part, data):
    if (type == "listening"):
        if (part == "Part I" or  part == "Part II" or part == "Part III" or part == "Part IV" ):
            return archiveFormat("ListeningTest", part, data)
        else:
            return "Invalid part"
        
    elif (type == "reading"):
        if (part == "Part V" or  part == "Part VI" or part == "Part VII"):
            return archiveFormat("ReadingTest", part, data)
        else:
            return "Invalid part"
        
    else:
        return 'Error'

def archiveShortStory(data):
    return archiveFormat("ShortStories", "Short Stories", data)
    
def archiveVocab(topic, data):
    return archiveFormat("TopicVocab", topic, data)
    