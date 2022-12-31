import views.myModules.Login_v as Login_v
import views.myModules.Query_v as Query_v
import views.myModules.Archive_v as Archive_v

def loginGroup(type, model_res):
    if (type == 'Login'):
        return Login_v.login(model_res)

    elif (type == 'Signup'):
        return Login_v.signUp(model_res)

    elif (type == 'Logout'):
        return Login_v.logout(model_res)

    else:
        return {'err_msg' : 'Wrong type name'}

def queryGroup(type, model_res):
    if (type == 'Listening'):
        return Query_v.listeningTest(model_res)

    elif (type == 'Reading'):
        return Query_v.readingTest(model_res)

    elif (type == 'Story'):
        return Query_v.shortStory(model_res)

    elif (type == 'Topic'):
        return Query_v.topicVocab(model_res)

    else:
        return {'err_msg' : 'Wrong type name'}

def archiveGroup(type, model_res):
    if (type == 'Test'):
        return Archive_v.archiveTest(model_res)

    elif (type == 'Story'):
        return Archive_v.archiveShortStory(model_res)

    elif (type == 'Topic'):
        return Archive_v.archiveVocab(model_res)

    else:
        return {'err_msg' : 'Wrong type name'}