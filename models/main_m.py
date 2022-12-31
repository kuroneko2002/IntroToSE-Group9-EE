import models.myModules.Login_m as Login_m
import models.myModules.Query_m as Query_m
import models.myModules.Archive_m as Archive_m

def loginGroup(type, data):
    if (type == 'Login'):
        return Login_m.login({
            "user": data.user, 
            "password": data.password
            })
    elif (type == 'Signup'):
        return Login_m.signUp({
            "user": data.user,
            "password": data.password,
            "name": data.name,
            "DoB": data.DoB,
            "email": data.email
        })
    elif (type == 'Logout'):
        return Login_m.logout({
            "user": data.user
        })
    else:
        return 'Wrong type name'

def queryGroup(type, data):
    if (type == 'Listening'):
        return Query_m.listeningTest(data.part, data.index)

    elif (type == 'Reading'):
        return Query_m.readingTest(data.part, data.index)

    elif (type == 'Story'):
        return Query_m.shortStory(data.index)

    elif (type == 'Topic'):
        return Query_m.topicVocab(data.topic, data.index)

    else:
        return 'Wrong type name'

def archiveGroup(type, data):
    if (type == 'Test'):
        return Archive_m.archiveTest(data.type, data.part, data.data)

    elif (type == 'Story'):
        return Archive_m.archiveShortStory(data.data)

    elif (type == 'Topic'):
        return Archive_m.archiveVocab(data.topic, data.data)

    else:
        return 'Wrong type name'