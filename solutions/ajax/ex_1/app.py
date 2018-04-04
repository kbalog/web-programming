"""
Exercise #1: Checking username
"""

from flask import Flask, request

app = Flask(__name__)


@app.route("/check_username")
def check_username():
    # this list contains the usernames taken
    USERNAMES = ["johnsmith", "maryjane", "johndoe", "smith"]

    name = request.args.get("username", None)
    if name:
        if len(name) < 3:
            return "Username is too short"
        elif not name.isalnum():  # check if it contains alphanumerical characters only
            return "Username may only contain letters or digits"
        elif name in USERNAMES:  # check if username is taken
            return "Username already taken"
    return ""


@app.route("/")
def index():
    return app.send_static_file("exercise1.html")


if __name__ == "__main__":
    app.run()
