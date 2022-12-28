def archiveTest(model_res):
    if (model_res == "Succeed"):
        return {
            "err_msg": "None"
        }
    if (model_res == "Error"):
        return {
            "err_msg": "Error occur! Please re-input file!"
        }
    if (model_res == "Invalid part"):
        return {
            "err_msg": "Some parts is belong to wrong test! Please check input file!"
        }
    

def archiveShortStory(model_res):
    if (model_res == "Succeed"):
        return {
            "err_msg": "None"
        }
    if (model_res == "Error"):
        return {
            "err_msg": "Error occur! Please re-input file!"
        }

def archiveVocab(model_res):
    if (model_res == "Succeed"):
        return {
            "err_msg": "None"
        }
    if (model_res == "Error"):
        return {
            "err_msg": "Error occur! Please re-input file!"
        }