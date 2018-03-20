"""
Exercise #4b: Movie search
"""

from flask import Flask, render_template, request

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


def match(movie, keywords, year_from, year_to):
    """Checks if a movie matches a given keywords and time period"""
    for k in keywords:  # the movie must contain all keywords
        movietext = " ".join([movie.get("title", ""), movie.get("synopsis", "")])
        if k not in movietext.lower():  # search in title and synopsis lowercased
            return False

    if year_from:  # if from year is provided
        if movie["year"] < int(year_from):
            return False

    if year_to:  # if to year is provided
        if movie["year"] > int(year_to):
            return False

    return True


@app.route("/")
def index():
    # get parameters from URL
    query = request.args.get("query", "")
    year_from = request.args.get("year_from", None)
    year_to = request.args.get("year_to", None)
    keywords = query.lower().split() if query else []

    matches = []  # holds the list of matching movies
    for movie in MOVIES:
        if match(movie, keywords, year_from, year_to):
            matches.append(movie)

    return render_template("movies.html", movies=matches, query=query, year_from=year_from, year_to=year_to)


if __name__ == "__main__":
    app.run()
