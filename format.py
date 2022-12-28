### login msg
{
    "group": "Login",
    "type": "Login",
    "data": {
        "user": "",         # username
        "password": "",     # password
    }
}

### sign up msg
{
    "group": "Login",
    "type": "Signup",
    "data": {
        "user": "",         # username
        "password": "",     # password
        "name": "",         # name
        "DoB": "",          # date of birth
        "email": ""         # email
    }
}
### logout msg
{
    "group": "Login",
    "type": "Logout",
    "data": {
        "user": "",         # username
    }
}
### query listening msg
{
    "group": "Query",
    "type": "Listening",
    "data": {
        "part": "",         # "Part I" or "Part II" or "Part III" or "Part IV"
        "index": ""         # 0...n -> the index of test in database you want to take
    }
}
### query reading msg
{
    "group": "Query",
    "type": "Reading",
    "data": {
        "part": "",         # "Part V" or "Part VI" or "Part VII"
        "index": ""         # 0...n -> the index of test in database you want to take
    }
}
### query short stroy msg
{
    "group": "Query",
    "type": "Story",
    "data": {
        "index": ""         # 0...n -> the index of test in database you want to take
    }
}
### query topic vocab msg
{
    "group": "Query",
    "type": "Topic",
    "data": {
        "topic": "",        # name of topic
        "index": ""         # 0...n -> the index of test in database you want to take
    }
}
### archive listen test msg
{
    "group": "Archive",
    "type": "Test",
    "data": {
        "type": "listening",
        "data": {
            # JSON string parse from input file
        } 
    }
}
### archive read test msg
{
    "group": "Archive",
    "type": "Test",
    "data": {
        "type": "reading",
        "data": {
            # JSON string parse from input file
        } 
    }
}
### archive short story msg
{
    "group": "Archive",
    "type": "Story",
    "data": {
        "data": {
            # JSON string parse from input file
        } 
    }
}
### archive topic vocab msg
{
    "group": "Archive",
    "type": "Topic",
    "data": {
        "data": {
            # JSON string parse from input file
        } 
    }
}
### Exit msg
{
    "group": "Exit",
    "type": "", # nothing
    "data": "" # nothing
}