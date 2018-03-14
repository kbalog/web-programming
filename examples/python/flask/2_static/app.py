"""
Flask: Serving static files
"""

from flask import Flask, url_for

app = Flask(__name__)

HTML_FRAME_TOP = "<!DOCTYPE HTML>\n<html>\n<head>\n<title>My site</title>\n" \
                 "<link rel=\"stylesheet\" href=\"{css}\"/>\n</head>\n<body>\n"
HTML_FRAME_BOTTOM = "</body>\n</html>\n"


@app.route("/")
def index():
    # we replace the string {css} with the URL generated for the static "style.css" file
    html = HTML_FRAME_TOP.replace("{css}", url_for("static", filename="style.css"))
    html += "<h1>Hello world</h1>"
    html += HTML_FRAME_BOTTOM
    return html


if __name__ == "__main__":
    app.run()
