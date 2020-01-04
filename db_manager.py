import sqlite3
from db_builder import exec, execmany
import random

def formatFetch(results):
    '''def formatFetch(results): format results from fetchall into a list'''
    collection=[]
    for item in results:
        collection.append(str(item)[2:-3])
    return collection
def formatFetch2(results):
    '''def formatFetch(results): format results from fetchall into a list'''
    collection=[]
    for item in results:
        newitem=str(item)[2:-3]
        if newitem not in collection:
            collection.append(newitem)
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
        print(num)
        num+=1
        q="UPDATE stored_tbl SET id=? WHERE id=?"
        inputs=(num,num-1)
        execmany(q,inputs)
        return True
    return False

def additem(username,name,date,item,color):
    inputs = (username,)
    q="SELECT id FROM user_tbl WHERE username=?"
    id=execmany(q,inputs).fetchone()[0]
    q="SELECT maxorder FROM user_tbl WHERE username=?"
    maxorder=execmany(q,inputs).fetchone()[0] + 1
    maxorder+=1
    q="UPDATE user_tbl SET maxorder=? WHERE username=?"
    inputs=(maxorder,username)
    execmany(q,inputs)
    q="INSERT INTO todo_tbl VALUES(?,?,?,?,?,?)"
    inputs=(id,name,maxorder,date,item,color);
    inputs=(id,maxorder)
    execmany(q,inputs)

def getName(username):
    q="SELECT name FROM user_tbl WHERE username=?"
    inputs=(username,)
    data=execmany(q,inputs).fetchall()
    data=formatFetch(data)[0]
    return data
def getID(username):
    q="SELECT id FROM user_tbl WHERE username=?"
    inputs=(username,)
    data=execmany(q,inputs).fetchone()[0]
    return data

def getList(username):
    id=getID(username)
    q="SELECT listName FROM todo_tbl WHERE id=?"
    inputs=(id,)
    data=execmany(q,inputs).fetchall()
    data=formatFetch2(data)
    return data
