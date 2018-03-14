# Server Side Programming exercises (Python, Flask), Part III.

  * [MySQL Connector/Python](https://dev.mysql.com/doc/connector-python/en/)
  * [Flask QuickStart](http://flask.pocoo.org/docs/0.12/quickstart/)
  * [Jinja Templates](http://jinja.pocoo.org/docs/2.9/templates/)


## Exercise #0: Set up MySQL

  * Install MySQL on your local machine.
    - https://dev.mysql.com/downloads/mysql/
    - If you prefer to use a MySQL client, see e.g., [MySQL Workbench](https://dev.mysql.com/downloads/workbench/).
  * Create a MySQL database called `dat310`.
  * Create a table called `movies` with the following structure:
    - `imdb_id VARCHAR(20)` we'll use the IMDB movie IDs as a unique identifier and PRIMARY KEY
    - `title VARCHAR(40)`
    - `year INT`
    - `rating DOUBLE`
    - `synopsis TEXT`
  * Add some movies to the table.
  * You may create the table and add data using the [movies.sql](movies.sql) script.
  * Install MySQL Connector/Python
    - on the command line: `conda install mysql-connector-python`


## Exercise #1: Listing movies

Update [exercise 1 from the last lecture](../../../../solutions/python/flask2/ex_1) such that movies are loaded from the MySQL database.

Specifically,

  * Remove the `MOVIES` const; this data will need to be loaded from the database.
  * Make a connection to the database (make sure the DB and the movies table have been created).
  * Make a `SELECT` query that returns all movies from the table.
  * Notice that are not storing the IMDB URLs in the database. You'll need to generate the links to the IMDB movie pages from the `imdb_id` field. Do that in the `movies.html` template file (i.e., not in `app.py`).

The output should look exactly as before:
![Exercise1](images/exercise1.png)


## Exercise #2: Movie details

Generate a separate "details" page for each movie.

  * Remove the links to the IMDB profile page from the movie listing. Instead, make the title of the movie a link to `/movie/<movie_id>`, where `movie_id` refers to the `id` field in the `movies` table.
  * Make a `layout.html` file that contain a common header and footer. The movie listing and movie details pages should extend `layout.html`.

![Exercise2/1](images/exercise2_1.png)
![Exercise2/2](images/exercise2_2.png)
