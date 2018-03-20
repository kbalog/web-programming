"""
Exercise #2: Primes
"""

from flask import Flask, render_template
import math

app = Flask(__name__)


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


@app.route("/")
def index():
    # we pass a list, which tells for each number (index+1) whether it is a prime
    nums = [is_prime(i) for i in range(1, 21)]
    return render_template("primes.html", numbers=nums)


if __name__ == "__main__":
    app.run()
