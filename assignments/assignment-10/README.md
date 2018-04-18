# Assignment 10 - Booking admin

## Task

Your task is to develop an admin back-end for the booking site using a combination of technologies (Flask, MySQL, Bootstrap).

There are no starter files provided for this assignment.
You need to use Flask with templating, Bootstrap, and MySQL for implementing the functionality below. It is allowed to use any external Python package/module and Bootstrap component, plugin, or add-on.  A list of resources can be found at the bottom of the task description.

  * Login
    - All the functionality described below should be available only to logged in admin users. Login is based on a username and password combination.
    - There is no need to implement front-end functionality for adding new admin users. But you need to add a test user to your database dump that we can use for testing, username: "test" password: "dat310A9". You need to store passwords in a secure way in the database (i.e., no raw password strings). See [password salting](http://flask.pocoo.org/snippets/54/).
  * Property management
    - The user needs to be able to list, add, delete, and edit properties.
    - On the property edit/add form, check that
        - Property name is not empty
        - ...
        - Photo is provided
    - If an error appears, then show an alert and remember the form values already filled in.
    - Note that it is part of the task to be able to modify property photos. New products can only uploaded if a photo is provided.
  * Booking management
    - The admin user can list all the bookings that have been made.
    - Upon clicking on an booking, show the booking details, with a link to the booked property's page.
    - Your database should contain at least 20 bookings (You can generate "fake bookings" with a script.)
  * Statistics
    - Provide a plot which shows the number of orders over time. I.e., for each day, show the number of orders that were registered on that day.
    - Provide a list of the "most popular properties", i.e., products that have been booked the most. Show the property ID, name, and the total order number of bookings for that property.
  * General
    - When listing properties or bookings, show at most 10 items on a page and let the user paginate between pages.
    - All forms and alert/success messages must also be styled using Bootstrap.

It is up to you how you organize this functionality on the admin user interface (i.e., what menu points you have, etc.).
*Some example screenshots will be made available later, but these do not need to be strictly followed.*

Commit and push files to GitHub. You also need to submit a dump of your database in a single `database.sql` file.  Executing this file should create all the tables that are needed for your application and should insert property and order data.


## Resources

  * A dump of MySQL table structures can be found in [tables.sql](tables.sql) (meant for those that didn't do Assignment 8).
  * A login example can be found [under the flask examples](/examples/python/flask/9_login).
  * A file upload example can be found [under the flask examples](/examples/python/flask/8_file_upload). See also the [Flask documentation](http://flask.pocoo.org/docs/0.12/patterns/fileuploads/).
  * For plotting, you may use a JavaScript library, e.g., [D3.js](https://d3js.org/), [Chart.js](http://www.chartjs.org/), [CanvasJS](http://canvasjs.com/), or [one of these libraries](https://www.sitepoint.com/15-best-javascript-charting-libraries/).
    - Some specific examples using [D3.js](http://bl.ocks.org/d3noob/8952219), [Chart.js](http://www.chartjs.org/docs/#line-chart-introduction), or [CanvasJS](http://canvasjs.com/html5-javascript-line-chart/).
