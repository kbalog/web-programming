"""
Flask: Form handling
"""

from flask import Flask, url_for, redirect, request

app = Flask(__name__)

HTML_FRAME_TOP = "<!DOCTYPE HTML>\n<html>\n<head>\n<title>Flask form example</title>\n</head>\n<body>\n"
HTML_FRAME_BOTTOM = "</body>\n</html>\n"


@app.route("/")
def index():
    # redirect to form
    return redirect(url_for("static", filename="form.html"))


@app.route("/sendform", methods=["POST"])
def sendform():
    html = HTML_FRAME_TOP.replace("{css}", url_for("static", filename="style.css"))
    html += "Name: " + request.form["name"] \
            + "<br />" \
            + "Email: " + request.form["email"]
    html += HTML_FRAME_BOTTOM
    return html


if __name__ == "__main__":
    app.run()
