import sqlite3, urllib, json

DB_FILE = "trivia.db"

def exec(cmd):
    """Executes a sqlite command"""
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    output = c.execute(cmd)
    db.commit()
    return output

def execmany(cmd, inputs):
    """Executes a sqlite command using ? placeholder"""
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    output = c.execute(cmd, inputs)
    db.commit()
    return output

#==========================================================
def build_db():
    command="CREATE TABLE IF NOT EXISTS user_tbl (id INT, username TEXT, password TEXT, name TEXT)"
    exec(command)

    command="CREATE TABLE IF NOT EXISTS todo_tbl (id INT, order INT, date TEXT, todo TEXT, color TEXT)"
    exec(command)

    command="CREATE TABLE IF NOT EXISTS stored_tbl (id INT)"
    exec(command)

    command="INSERT INTO stored_tbl VALUES(0);"
    exec(command);
