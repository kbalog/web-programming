"""
Flask: Using sessions
"""

from flask import Flask, render_template, redirect, url_for, session

app = Flask(__name__)
app.debug = True
app.secret_key = "any random string"


@app.route("/")
def index():
    counter = session.get("counter", 0)
    return render_template("page.html", counter=counter)


@app.route("/inc")
def inc():
    counter = session.get("counter", 0)
    session["counter"] = counter + 1
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run()
