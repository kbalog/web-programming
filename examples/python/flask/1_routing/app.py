"""
Flask: Routing and URL building
"""
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Index Page"


@app.route("/info")
def hello():
    return "This is a static info page"


@app.route("/user/<username>")
def user(username):
    return "Showing the profile page for user {}".format(username)


@app.route("/package/<int:package_id>")
def package(package_id):
    return "Showing the details for package #{}".format(package_id)


if __name__ == "__main__":
    app.run()
