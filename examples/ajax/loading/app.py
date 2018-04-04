"""
AJAX example
"""

from flask import Flask, request
import time
import hashlib

app = Flask(__name__)


@app.route("/get_pw", methods=["POST"])
def get_pw():
    pw = request.form.get("pw", "")
    time.sleep(1)  # wait one second with the response
    return hashlib.md5(pw.encode()).hexdigest()


@app.route("/")
def index():
    return app.send_static_file("loading.html")


if __name__ == "__main__":
    app.run()
