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
    command="CREATE TABLE IF NOT EXISTS user_tbl (id INT, username TEXT, password TEXT, Name)"
    exec(command)

    command="CREATE TABLE IF NOT EXISTS todo_tbl (id INT, date TEXT, todo TEXT, color TEXT)"
    exec(command)
