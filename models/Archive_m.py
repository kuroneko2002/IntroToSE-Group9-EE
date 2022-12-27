import CRUD_db
import json

def archiveFormat(db_name, collection, file):
    try:
        f = open(file)
        data = json.load(f)
    except:
        return 'Error'

    # CRUD_db.deleteAll(db_name, collection)
     
    for obj in data:
        res = CRUD_db.insert_db(db_name, collection, obj)
        if (res == 'Error'): 
            return res
    
    return 'Succeed'


def archiveTest(type, part, file):
    if (type == "listening"):
        return archiveFormat("ListeningTest", part, file)
        
    elif (type == "reading"):
        return archiveFormat("ReadingTest", part, file)
        
    else:
        return 'Error'

def archiveShortStory(file):
    return archiveFormat("ShortStories", "Short Stories", file)
    
def archiveVocab(topic, file):
    return archiveFormat("TopicVocab", topic, file)
    