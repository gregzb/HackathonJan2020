from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import session
import random
import os
import random
import db_builder
import db_manager
app = Flask(__name__)
app.secret_key = os.urandom(32)
images = ["altitude", "beach", "calmocean", "fireworks", "forest", "hotel", "italy", "minecraft", "mountain", "nomansky", "skyline", "sunrise", "timessquare", "treasurebottle", "winter"]

coolors = [['#5668d', '#28090', '#0a896', '#2c39a', '#f0f3bd']
,['#ffffff', '#0171f', '#03459', '#07ea7', '#0a8e8']
,['#d8e2dc', '#ffe5d9', '#ffcad4', '#f4acb7', '#9d8189']
,['#fe938c', '#e6b89c', '#ead2ac', '#9cafb7', '#4281a4']
,['#5bc0eb', '#fde74c', '#9bc53d', '#e55934', '#fa7921']
,['#ed6a5a', '#f4f1bb', '#9bc1bc', '#5ca4a9', '#e6ebe0']
,['#ef476f', '#ffd166', '#6d6a0', '#118ab2', '#73b4c']
,['#b132b', '#1c2541', '#3a506b', '#5bc0be', '#6fffe9']
,['#03049', '#d62828', '#f77f0', '#fcbf49', '#eae2b7']
,['#bce784', '#5dd39e', '#348aa7', '#525174', '#513b56']
,['#000', '#14213d', '#fca311', '#e5e5e5', '#ffffff']
,['#11627', '#fdfffc', '#2ec4b6', '#e71d36', '#ff9f1c']
,['#9c89b8', '#f0a6ca', '#efc3e6', '#f0e6ef', '#b8bedd']
,['#f2d7ee', '#d3bcc0', '#a5668b', '#69306d', '#e103d']
,['#114b5f', '#28090', '#e4fde1', '#456990', '#f45b69']
,['#22223b', '#4a4e69', '#9a8c98', '#c9ada7', '#f2e9e4']
,['#dcdcdd', '#c5c3c6', '#46494c', '#4c5c68', '#1985a1']
,['#ff9f1c', '#ffbf69', '#ffffff', '#cbf3f0', '#2ec4b6']
,['#3d5a80', '#98c1d9', '#e0fbfc', '#ee6c4d', '#293241']
,['#114b5f', '#1a936f', '#88d498', '#c6dabf', '#f3e9d2']
,['#11627', '#f71735', '#41ead4', '#fdfffc', '#ff9f1c']
,['#7bdff2', '#b2f7ef', '#eff7f6', '#f7d6e0', '#f2b5d4']
,['#e63946', '#f1faee', '#a8dadc', '#457b9d', '#1d3557']
,['#ffcdb2', '#ffb4a2', '#e5989b', '#b5838d', '#6d6875']
,['#264653', '#2a9d8f', '#e9c46a', '#f4a261', '#e76f51']
,['#50514f', '#f25f5c', '#ffe066', '#247ba0', '#70c1b3']
,['#1a535c', '#4ecdc4', '#f7fff7', '#ff6b6b', '#ffe66d']
,['#2b2d42', '#8d99ae', '#edf2f4', '#ef233c', '#d9429']
,['#ffffff', '#84dcc6', '#a5ffd6', '#ffa69e', '#ff686b']
,['#247ba0', '#70c1b3', '#b2dbbf', '#f3ffbd', '#ff1654']]

quotes = ["Perfection is not attainable, but if we chase perfection we can catch excellence.",
"Everything you've ever wanted is on the other side of fear.",
"There are two ways of spreading light: to be the candle or the mirror that reflects it.",
"It is never too late to be what you might have been.",
"The roots of education are bitter, but the fruit is sweet.",
"To be the best, you must be able to handle the worst.",
"The key to immortality is first living a life worth remembering.",
"You must be the change you wish to see in the world.",
"Keep your face always toward the sunshine - and shadows will fall behind you.",
"To succeed in life, you need two things: ignorance and confidence.",
"Mastering others is strength. Mastering yourself is true power.",
"Change your life today.",
"If you obey all the rules, you miss all the fun.",
"Wanting to be someone else is a waste of the person you are.",
"No one can make you feel inferior without your consent.",
"Be not afraid of going slowly, be afraid only of standing still."]

@app.route("/")
@app.route("/index")
def index():
    db_builder.build_db()
    if 'username' in session and 'password' in session:
        session['name'] = db_manager.getName(session['username'])
        listList=db_manager.getList(session['username'])
        colors = random.choice(coolors)
        return render_template("todo.html", session = session, motivational_quote = "Well done is better than well said.", lists=listList,coolors = colors, image = random.choice(images))
    return render_template('login.html', errorMessage = "", image = random.choice(images))

@app.route("/login", methods=["POST"])
def login():
    session['username'] = request.form["username"]          # assign username key in session to inputted username
    session['password'] = request.form["password"]          # assign password key in session to inputted password
    if (session):
        username = session['username']
        password = session['password']
        if (db_manager.userValid(username, password)):
            return redirect(url_for("index"))
        return render_template('login.html', errorMessage = "Invalid Credentials", image = random.choice(images))
    else:
        return render_template('login.html',errorMessage = "", image = random.choice(images))

@app.route("/register", methods=["GET"])
def register_get():
    return render_template('register.html', errorMessage = "", image = random.choice(images))

@app.route("/register", methods=["POST"])
def register():
    if(request.form['sub1'] == 'Log In'):
        return redirect(url_for("index"))
    else:
        session['username'] = request.form["username"]          # assign username key in session to inputted username
        session['password'] = request.form["password1"]          # assign password key in session to inputted password1
        session['password2'] = request.form["password2"]          # assign password key in session to inputted password2
        session['name'] = request.form["name"]
        if (session):
            name = session['name']
            username = session['username']
            password1 = session['password']
            password2 = session['password2']
            if password1 == '' or password2 == '':
                return render_template('register.html', errorMessage = 'Password cannot be blank', image = random.choice(images))
            if (password1 == password2):
                if (db_manager.addUser(name , username, password1)):
                    return render_template('login.html')
                return render_template('register.html',
                    errorMessage = "Username already taken")
            return render_template('register.html',
                errorMessage = "Passwords do not match. Please try again.", image = random.choice(images))
        return render_template('register.html', errorMessage = "", image = random.choice(images))

    #add user checks if account exists (returns false). If DNE, enters into database, returns true

@app.route("/logout", methods=["GET"])
def logout():      # route logs out the user by getting rid of username and password in session
    if ('username' in session and 'password' in session):
        session.pop('username')
        session.pop('password')
        session.pop('name')
        if 'password2' in session:
            session.pop('password2')
        return redirect(url_for("index"))                # redirect to beginning
    return redirect(url_for("index"))                # redirect to beginning



if __name__ == "__main__":
    db_builder.build_db()
    app.debug = True
    app.run()
