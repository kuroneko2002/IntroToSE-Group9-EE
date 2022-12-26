import CRUD_db
import json

def login(user):
    try:
        data = CRUD_db.get("Account", "Account", "name", user.username)
        if (data == None):
            return 'Invalid username'

        data = json.loads(data[0])
        if (data.password != user.password):
            return "Invalid password"

        return 'Valid'
    except:
        return 'Error'

def signIn(user):
    try:
        data = CRUD_db.get("Account", "Account", "name", user.username)
        if (data == None):
            CRUD_db.insert_db("Account", "Account",user)
            return 'Succeed'

        return 'Invalid'
    except:
        return 'Error'

def logout(user):
    try:
        # update account.status
        data = CRUD_db.update_db("Account", "Account", "name", user.username, "status", False)
        if (data == "Succeed"):
            return data

        return 'Error'
    except:
        return 'Error'