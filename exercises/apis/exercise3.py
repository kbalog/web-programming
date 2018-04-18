"""
Exercise #3: Photos from Flickr
"""

from flask import Flask, render_template
import requests  # note that this is not the same requests as flask.requests

app = Flask(__name__)


@app.route("/")
def index():
    url = "http://api.flickr.com/services/feeds/photos_public.gne"

    # TODO complete the request parameters
    # see https://www.flickr.com/services/feeds/docs/photos_public/
    params = {
    }

    # this makes a request and parses the JSON response into data
    data = requests.get(url, params=params).json()
    # TODO extract the first 5 photos from the data and pass them to the template
    # TODO complete exercise3.html
    return render_template("exercise3.html", photos=[])


if __name__ == "__main__":
    app.run()
