def listeningTest(model_res):
    if (model_res == "None"):
        return {
            "err_msg": "No data"
        }
    if (model_res == "Error"):
        return {
            "err_msg": "Error"
        }
    if (model_res == "Invalid part"):
        return {
            "err_msg": "Wrong part"
        }

    # have data
    return {
        "err_msg": "None",
        "data": model_res
    }

def readingTest(model_res):
    if (model_res == "None"):
        return {
            "err_msg": "No data"
        }
    if (model_res == "Error"):
        return {
            "err_msg": "Error"
        }
    if (model_res == "Invalid part"):
        return {
            "err_msg": "Wrong part"
        }
        
    # have data
    return {
        "err_msg": "None",
        "data": model_res
    }

def shortStory(model_res):
    if (model_res == "None"):
        return {
            "err_msg": "No data"
        }
    if (model_res == "Error"):
        return {
            "err_msg": "Error"
        }

    # have data
    return {
        "err_msg": "None",
        "data": model_res
    }

def topicVocab(model_res):
    if (model_res == "None"):
        return {
            "err_msg": "No data"
        }
    if (model_res == "Error"):
        return {
            "err_msg": "Error"
        }

    # have data
    return {
        "err_msg": "None",
        "data": model_res
    }