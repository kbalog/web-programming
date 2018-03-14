"""
Exercise #2: Shopping cart
"""

from flask import Flask, render_template, request, redirect, url_for, flash, abort, session

app = Flask(__name__)
app.debug = True  # only for development!
app.secret_key = "any random string"


class ShoppingCart:
    """Class representing a shopping cart."""

    def __init__(self, contents=dict()):
        """Initializes a shopping cart with content (if provided)."""
        self.__cart = contents

    def add(self, product_id, qt):
        """Adds a product to the shopping cart or increases its quantity if it's already there."""
        self.__cart[product_id] = self.__cart.get(product_id, 0) + qt

    def remove(self, product_id):
        """Removes a product from the shopping cart."""
        self.__cart.pop(product_id)

    def contains(self, product_id):
        """Checks if the cart contains a given product."""
        return product_id in self.__cart

    def contents(self):
        """Returns the contents of the cart as a dict."""
        return self.__cart


@app.route("/")
def index():
    # TODO show cart contents
    return render_template("page.html", cart=dict())


@app.route("/add", methods=["POST"])
def add():
    # TODO add product to cart
    return redirect(url_for("index"))


@app.route("/remove", methods=["GET"])
def remove():
    # TODO remove product from cart
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run()
