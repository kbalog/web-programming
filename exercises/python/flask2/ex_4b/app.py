"""
Exercise #4b: Movie search
"""

from flask import Flask, render_template

app = Flask(__name__)

MOVIES = [
    {"title": "The Dark Knight",
     "year": 2008,
     "url": "http://www.imdb.com/title/tt0468569",
     "rating": 8.9},
    {"title": "The Shawshank Redemption",
     "year": 1994,
     "url": "http://www.imdb.com/title/tt0111161",
     "synopsis": "Two imprisoned men bond over a number of years, finding solace \
     and eventual redemption through acts of common decency.",
     "rating": 9.3},
    {"title": "Pulp Fiction",
     "year": 1994,
     "url": "http://www.imdb.com/title/tt0110912",
     "synopsis": "The lives of two mob hit men, a boxer, a gangster's wife, and a \
      pair of diner bandits intertwine in four tales of violence and redemption.",
     "rating": 8.9},
    {"title": "The Godfather",
     "year": 1972,
     "url": "http://www.imdb.com/title/tt0068646",
     "synopsis": "The aging patriarch of an organized crime dynasty transfers control \
     of his clandestine empire to his reluctant son.",
     "rating": 9.2},
    {"title": "Inception",
     "year": 2010,
     "url": "http://www.imdb.com/title/tt1375666",
     "synopsis": "A thief, who steals corporate secrets through use of dream-sharing \
     technology, is given the inverse task of planting an idea into the mind of a CEO.",
     "rating": 8.8},
]


@app.route("/")
def index():
    # TODO: add input handling and implement search functionality here
    return render_template("movies.html", movies=MOVIES)


if __name__ == "__main__":
    app.run()
