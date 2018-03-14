"""
Exercise #2: Form handling

@author: Krisztian Balog
"""

from flask import Flask, url_for, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("form.html")


@app.route("/register", methods=["POST"])
def reg():
    return render_template("reg.html",
                           name=request.form["name"],
                           email=request.form["email"])


if __name__ == "__main__":
    app.run()
