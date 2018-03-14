"""
Flask: Using Cookies
"""

from flask import Flask, render_template, request, redirect, url_for, make_response

app = Flask(__name__)
app.debug = True


@app.route("/")
def index():
    counter = request.cookies.get("counter", 0)
    return render_template("page.html", counter=counter)


@app.route("/inc")
def inc():
    counter = request.cookies.get("counter", "0")
    response = make_response(redirect(url_for("index")))
    response.set_cookie("counter", str(int(counter) + 1))
    return response


if __name__ == "__main__":
    app.run()
