"""
Exercise #1: Listing movies
"""

from flask import Flask, render_template, g
import mysql.connector

app = Flask(__name__)

# Application config
app.config["DATABASE_USER"] = "root"
app.config["DATABASE_PASSWORD"] = "root"
app.config["DATABASE_DB"] = "dat310"
app.config["DATABASE_HOST"] = "localhost"
app.debug = True  # only for development!


def get_db():
    if not hasattr(g, "_database"):
        g._database = mysql.connector.connect(host=app.config["DATABASE_HOST"], user=app.config["DATABASE_USER"],
                                       password=app.config["DATABASE_PASSWORD"], database=app.config["DATABASE_DB"])
    return g._database


@app.teardown_appcontext
def teardown_db(error):
    """Closes the database at the end of the request."""
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route("/")
def index():
    db = get_db()
    cur = db.cursor()
    try:
        movies = []  # holds the data that we will return
        sql = "SELECT imdb_id, title, year, rating, synopsis FROM movies"
        cur.execute(sql)
        for (imdb_id, title, year, rating, synopsis) in cur:
            movies.append({
                "imdb_id" : imdb_id,
                "title": title,
                "year": year,
                "rating": rating,
                "synopsis": synopsis
            })
        return render_template("movies.html", movies=movies)
    except mysql.connector.Error as err:
        return render_template("error.html", msg="Error querying data")
    finally:
        cur.close()


if __name__ == "__main__":
    app.run()
