import sqlite3
from db_builder import exec, execmany
import random

def formatFetch(results):
    '''def formatFetch(results): format results from fetchall into a list'''
    collection=[]
    for item in results:
         if str(item) not in collection:
            collection.append(str(item)[2:-3])
    return collection

def userValid(username, password):
    q = "SELECT username FROM user_tbl;"
    data = exec(q)
    for uName in data:
        if uName[0] == username:
            q = "SELECT password from user_tbl WHERE username=?"
            inputs = (username,)
            data = execmany(q, inputs)
            for passW in data:
                if (passW[0] == password):
                    return True
    return False

def addUser(name,username, password):
    inputs = (username,)
    data = execmany(q, inputs).fetchone()
    if (data is None):
        q = "INSERT INTO user_tbl VALUES(?, ?, ?, ?)"
        command = "SELECT flag from flags_tbl where country=?"
        inputs = (name, username, password)
        execmany(q, inputs)
        return True
    return False
