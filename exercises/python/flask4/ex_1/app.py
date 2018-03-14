"""
Exercise #1: Remembering user details
"""

from flask import Flask, render_template, request, redirect, url_for, flash, make_response
import datetime

app = Flask(__name__)
app.debug = True  # only for development!
app.secret_key = "any random string"


@app.route("/")
def index():
    # TODO: get name and email from cookies
    return render_template("page.html", name="", email="")


@app.route("/save", methods=["POST"])
def save():
    name = None
    email = None
    if "name" in request.form:
        name = request.form["name"]
    else:
        flash("Name is missing", "error")
    if "email" in request.form:
        email = request.form["email"]
    else:
        flash("Email is missing", "error")

    if name and email:
        # TODO: save name and email in cookies with expiry 60 days into the future
        flash("User details remembered", "success")

    return redirect(url_for("index"))


@app.route("/forget")
def forget():
    # TODO: delete name and email cookies
    flash("User details forgotten", "success")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run()
