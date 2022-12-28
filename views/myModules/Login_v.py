def login(model_res):
    if (model_res == "Succeed"):
        return {
            "err_msg": "None"
        }
    if (model_res == "Error"):
        return {
            "err_msg": "Error occur! Please re-enter account!"
        }
    if (model_res == "Invalid username"):
        return {
            "err_msg": "Wrong username! Please re-enter account!"
        }
    if (model_res == "Invalid password"):
        return {
            "err_msg": "Wrong password! Please re-enter password!"
        }
    if (model_res == "Already login"):
        return {
            "err_msg": "User is already login!"
        }

def signUp(model_res):
    if (model_res == "Succeed"):
        return {
            "err_msg": "None"
        }
    if (model_res == "Error"):
        return {
            "err_msg": "Error occur! Please re-enter account!"
        }
    if (model_res == "Invalid user"):
        return {
            "err_msg": "Username is used! Please choose another username!"
        }

def logout(model_res):
    if (model_res == "Succeed"):
        return {
            "err_msg": "None"
        }
    if (model_res == "Error"):
        return {
            "err_msg": "Error occur! Please re-enter account!"
        }