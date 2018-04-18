"""
Exercise #3: Photos from Flickr
"""

from flask import Flask, render_template
import requests  # note that this is not the same requests as flask.requests

app = Flask(__name__)


@app.route("/")
def index():
    url = "http://api.flickr.com/services/feeds/photos_public.gne"

    params = {
        "nojsoncallback": 1,
        "tags": "stavanger",
        "tagmode": "any",
        "format": "json"
    }

    data = requests.get(url, params=params).json()
    return render_template("exercise3.html", photos=data["items"][:5])


if __name__ == "__main__":
    app.run()
