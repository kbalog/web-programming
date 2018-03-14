"""
Flask: Login
"""

import os
from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.debug = True
app.secret_key = 'some_secret'


def valid_login(username, password):
    """Checks if username-password combination is valid."""
    # user password data typically would be stored in a database
    USER_PASSWORDS = {
        "johndoe": "pbkdf2:sha1:1000$z65Imqow$3ffdcb44ff28b10f1b5a54752086010b92dd4e3f",  # pw: Joe123
        "maryjane": "pbkdf2:sha1:1000$lCyNVisB$628649fb210b5c831760da488f89559a160f4aef"  # pw" LoveDogs
    }
    # the generate a password hash use the line below:
    # generate_password_hash("rawPassword")
    if username in USER_PASSWORDS:
        return check_password_hash(USER_PASSWORDS[username], password)
    return False


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":  # if the form was submitted (otherwise we just display form)
        if valid_login(request.form["username"], request.form["password"]):
            session["username"] = request.form["username"]
            return redirect(url_for("index"))
        else:
            flash("Invalid username or password!")
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("username")
    return redirect(url_for("index"))


@app.route("/")
def index():
    return render_template("index.html", username=session.get("username", None))


if __name__ == "__main__":
    app.run()
