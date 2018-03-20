"""
Exercise #2: Primes
"""

from flask import Flask, render_template
import math

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("primes.html")


if __name__ == "__main__":
    app.run()
