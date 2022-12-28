import CRUD_db
import json

def login(user):
    try:
        data = CRUD_db.get("Account", "Account", "name", user.user)
        if (data == "None"):
            return 'Invalid username'

        data = json.loads(data[0])
        if (data.password != user.password):
            return "Invalid password"

        # check already login?
        if (data.status == "Online"):
            return "Already login"

        # Login confirmed
        data = CRUD_db.update_db("Account", "Account", "name", user.user, "status", 'Online')
        return 'Succeed'
    except:
        return 'Error'

def signUp(user):
    try:
        data = CRUD_db.get("Account", "Account", "name", user.user)
        if (data == None):
            CRUD_db.insert_db("Account", "Account",user)
            return 'Succeed'

        return 'Invalid user'
    except:
        return 'Error'

def logout(user):
    try:
        # Logout confirmed
        data = CRUD_db.update_db("Account", "Account", "name", user.user, "status", 'Offline')
        if (data == "Succeed"):
            return data

        return 'Error'
    except:
        return 'Error'