
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
import db_builder
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("template.html")

if __name__ == "__main__":
    db_builder.build_db()
    app.debug = True
    app.run()
