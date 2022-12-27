import CRUD_db
import json

def queryFormat(db_name, collection, index = 0):
    data = CRUD_db.getAll(db_name, collection)
    if (data == 'Error'):
        return data

    return json.loads(data[index])

def listeningTest(part = "Part I", index = 0):
    return queryFormat("ListeningTest", part, index)

def readingTest(part = "Part V", index = 0):
    return queryFormat("ReadingTest", part, index)

def shortStory(index = 0):
    return queryFormat("ShortStories", "Short Stories", index)

def TopicVocab(topic, index = 0):
    return queryFormat("TopicVocab", topic, index)
