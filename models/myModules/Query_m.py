import models.myModules.CRUD_db as CRUD_db
import json

def queryFormat(db_name, collection, index = 0):
    data = CRUD_db.getAll(db_name, collection)
    # "None" mean no data, "Error" mean something wrong
    if (data == "None" or data == "Error"):
        return data

    if(index >= len(data)):
        return "None"

    return json.loads(data[index])

def listeningTest(part = "Part I", index = 0):
    if (part == "Part I" or  part == "Part II" or part == "Part III" or part == "Part IV" ):
        return queryFormat("ListeningTest", part, index)
    else:
        return "Invalid part"

def readingTest(part = "Part V", index = 0):
    if (part == "Part V" or  part == "Part VI" or part == "Part VII"):
        return queryFormat("ReadingTest", part, index)
    else:
        return "Invalid part"

def shortStory(index = 0):
    return queryFormat("ShortStories", "Short Stories", index)

def topicVocab(topic, index = 0):
    return queryFormat("TopicVocab", topic, index)
