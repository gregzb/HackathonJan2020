from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import session
import os
import db_builder
app = Flask(__name__)
app.secret_key = os.urandom(32)


@app.route("/index")
def index():
    return render_template("todo.html")

@app.route("/")
def firstLogin():
    if ('username' in session and 'password' in session):
        redirect(url_for("index"))
    return render_template('login.html',errorMessage = "")

@app.route("/login", methods=["POST"])
def login():
    #print(request.form)
    if(request.form['sub1'] == 'Register'):
        return render_template('register.html', errorMessage = "")
    else:
        session['username'] = request.form["username"]          # assign username key in session to inputted username
        session['password'] = request.form["password"]          # assign password key in session to inputted password
        if (session):
            username = session['username']
            password = session['password']
            validLogin = db_manager.userValid(username, password) #temp for testing
            if (not validLogin):
                return render_template('login.html', errorMessage = "Invalid Credentials")
            return redirect(url_for("home"))
        else:
            return render_template('login.html',errorMessage = "")


@app.route("/register", methods=["POST"])
def register():
    if(request.form['sub1'] == 'Log In'):
        return redirect(url_for("firstLogin"))
    else:
        session['username'] = request.form["username"]          # assign username key in session to inputted username
        session['password'] = request.form["password1"]          # assign password key in session to inputted password1
        session['password2'] = request.form["password2"]          # assign password key in session to inputted password2
        if (session):
            username = session['username']
            password1 = session['password']
            password2 = session['password2']
            if password1 == '' or password2 == '':
                return render_template('register.html', errorMessage = 'Password cannot be blank')
            if (password1 == password2):
                if (db_manager.addUser("poo",username, password1)):
                    return redirect(url_for("home"))
                return render_template('register.html',
                    errorMessage = "Username already taken")
            return render_template('register.html',
                errorMessage = "Passwords do not match. Please try again.")
        return render_template('register.html', errorMessage = "")

    #add user checks if account exists (returns false). If DNE, enters into database, returns true

@app.route("/logout", methods=["GET"])
def logout():      # route logs out the user by getting rid of username and password in session
    if ('username' in session and 'password' in session):
        session.pop('username')
        session.pop('password')
        if 'password2' in session:
            session.pop('password2')
        return redirect(url_for("firstLogin"))                # redirect to beginning
    return redirect(url_for("firstLogin"))                # redirect to beginning



if __name__ == "__main__":
    db_builder.build_db()
    app.debug = True
    app.run()
