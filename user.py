import base64
import bcrypt

#class to represent a user, this will be used to create a new user and by default will contain a empty task list represented as dictionary

class User:
    def __init__(self, username, password):
        self.username = username.casefold()
        self.password = get_hashed_password_string(password)
        self.task_list = dict()
    
def get_hashed_password_string(password):
    hashed_pw_bytes = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()) #hash the password
    encoded_hashed_pw = base64.b64encode(hashed_pw_bytes) #encode the hashed password
    return encoded_hashed_pw.decode('utf-8') #return the encoded hashed password as a string to enable easy storage in a json file