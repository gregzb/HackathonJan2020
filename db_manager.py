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
    q = "SELECT * FROM user_tbl WHERE username=?"
    inputs = (username,)
    data = execmany(q, inputs).fetchone()
    if (data is None):
        q = "INSERT INTO user_tbl VALUES(?, ?, ?, ?, 0)"
        command = "SELECT id from stored_tbl;"
        num=exec(command).fetchone()[0]
        inputs = (num,username, password, name)
        execmany(q, inputs)
        num+=1
        q="INSERT INTO stored_tbl VALUES(?)"
        inputs=(num,)
        execmany(q,inputs)
        return True
    return False

def additem(username,password, date,item,color):
    inputs = (username,)
    q="SELECT id FROM user_tbl WHERE username=?"
    id=execmany(q,inputs).fetchone()[0]
    q="SELECT maxorder FROM user_tbl WHERE username=?"
    maxorder=execmany(q,inputs).fetchone()[0] + 1
    maxorder+=1
    q="UPDATE user_tbl SET maxorder=? WHERE username=?"
    inputs=(maxorder,username)
    q="INSERT INTO todo_tbl VALUES(?,?,?,?,?)"
    inputs(id,maxorder)
