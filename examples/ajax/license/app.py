"""
AJAX License example
"""

from flask import Flask, request

app = Flask(__name__)


@app.route("/check_license", methods=["POST"])
def check_license():
    VALID_LICENSES = {
        "Smith": "ABC-123",
        "John Smith": "CDE-999",
        "Mary": "PPP-111"
    }
    name = request.form.get("name", None)
    license = request.form.get("license", None)
    # check if name and license match
    if name and license:
        if VALID_LICENSES.get(name, None) == license:
            return "<img src='/static/images/yes.png' /> Valid license key"
        else:
            return "<img src='/static/images/no.png' /> Invalid license key for {}".format(name)
    return ""


@app.route("/")
def index():
    return app.send_static_file("license.html")


if __name__ == "__main__":
    app.run()
