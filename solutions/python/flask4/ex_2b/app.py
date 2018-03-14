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

    def set(self, product_id, qt):
        """Sets a product quantity."""
        self.__cart[product_id] = qt

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
    cart = ShoppingCart(session.get("cart", dict()))
    return render_template("page.html", cart=cart.contents())


@app.route("/add", methods=["POST"])
def add():
    product_id = request.form.get("product_id", None)
    qt = int(request.form.get("qt", 0))

    if product_id and qt:
        cart = ShoppingCart(session.get("cart", dict()))
        cart.add(product_id, qt)
        session["cart"] = cart.contents()
        flash("Product added to cart")
    else:
        abort(400)

    return redirect(url_for("index"))


@app.route("/remove", methods=["GET"])
def remove():
    product_id = request.args.get("product_id", None)
    if product_id:
        cart = ShoppingCart(session.get("cart", dict()))
        if cart.contains(product_id):
            cart.remove(product_id)
            session["cart"] = cart.contents()
            flash("Product removed cart")
        else:  # trying to remove a product which is not in the cart
            abort(400)
    else:
        abort(400)
    return redirect(url_for("index"))


@app.route("/mod", methods=["POST"])
def mod():
    product_id = request.form.get("product_id", None)
    qt = int(request.form.get("qt", 0))

    if product_id and qt:
        cart = ShoppingCart(session.get("cart", dict()))
        cart.set(product_id, qt)
        session["cart"] = cart.contents()
        flash("Quantity modified")
    else:
        abort(400)

    return redirect(url_for("index"))


@app.errorhandler(400)
def bad_request(error):
    return render_template("400.html"), 400


if __name__ == "__main__":
    app.run()
