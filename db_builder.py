import sqlite3, urllib, json

DB_FILE = "todo.db"

def exec(cmd):
    """Executes a sqlite command"""
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    output = c.execute(cmd)
    db.commit()
    return output

def execmany(cmd, inputs):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    output = c.execute(cmd, inputs)
    db.commit()
    return output

#==========================================================
def build_db():
    command="CREATE TABLE IF NOT EXISTS user_tbl (id INT, username TEXT, password TEXT, name TEXT,maxorder INT)"
    exec(command)

    command="CREATE TABLE IF NOT EXISTS todo_tbl (id INT, listName TEXT, ordernum INT, date TEXT, todo TEXT, color TEXT)"
    exec(command)

    command="CREATE TABLE IF NOT EXISTS stored_tbl (id INT)"
    exec(command)

    command="INSERT INTO stored_tbl VALUES(0);"
    exec(command)
