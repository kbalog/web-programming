"""
AJAX Zipcode example
"""

from flask import Flask, request

app = Flask(__name__)


@app.route("/getplace", methods=["GET"])
def getplace():
    POSTCODES = {
        "0107": "Oslo",
        "0506": "Oslo",
        "4090": "Hafrsfjord",
        "4033": "Stavanger",
        "4014": "Stavanger",
        "4050": "Sola",
        "4056": "Tananger"
    }
    postcode = request.args.get("postcode", None)
    # look up corresponding place or return empty string
    if postcode and (postcode in POSTCODES):
        return POSTCODES[postcode]
    return ""


@app.route("/")
def index():
    return app.send_static_file("zipcode2.html")


if __name__ == "__main__":
    app.run()
