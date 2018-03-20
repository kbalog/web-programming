"""
Exercise #3: Cash machine
"""

from flask import Flask, render_template, request
import math

app = Flask(__name__)
app.debug = True

# available values
VALUES = [1, 5, 10, 20, 50, 100, 500]


@app.route("/")
def index():
    return render_template("cashmachine.html")


def used_to_pay(amount):
    """Return the bills/coins used as a list of (value, count) tuples."""
    used = []
    a = amount
    for v in sorted(VALUES, reverse=True):
        c = math.floor(a / v)
        a %= v
        if c > 0:
            used.append((v, c))
    return used


@app.route("/pay")
def pay():
    # read amount
    amount = int(request.args.get("amount", 0))
    return render_template("cashmachine.html", amount=amount, used=used_to_pay(amount))


if __name__ == "__main__":
    app.run()
