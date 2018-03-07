# Python HTTP exercises

## Exercise #0: Test HTTP server

Launch the [example Python HTTP server](../../../examples/python/http/server.py) and test it by making a request to it both from a browser and using curl.


## Exercise #1: POST requests

Extend the HTTP server to be able to handle POST requests.
Test it by making a post request using curl.


## Exercise #2: Form handling

Make a HTML form with some input fields and set its action such that it is submitted to your Python HTTP server (using GET). Your server should output all input variables that are included in the request.

  - Use [urllib.parse](https://docs.python.org/3/library/urllib.parse.html) to extract input variables from the URL


## Exercise #3: Form handling (POST)

Extend the previous exercise such that the form is submitted using POST.
