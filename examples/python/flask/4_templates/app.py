"""
Flask: Using templates
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/members")
def members():
    return render_template("members.html", users=["john", "liza", "mary"])

@app.route("/postcodes")
def postcodes():
    postcodes = {
        "4041": "Stavanger",
        "0136": "Oslo"
    }
    return render_template("postcodes.html", postcodes=postcodes)


if __name__ == "__main__":
    app.run()
