# Server Side Programming exercises (Python, Flask), Part I.

Documentation: [Flask quickstart](http://flask.pocoo.org/docs/0.12/quickstart/#quickstart)

## Exercise #0: Test Flask Application

Launch the [minimalistic Flask application](../../../examples/python/flask/flask_1) and test it by making a request to it both from a browser (http://localhost:5000).


## Exercise #1: Post code lookup service

Create a flask application that can look up location names based on the post code.  Store the locations in a dictionary, e.g.,
```
postcodes = {
    "0001": "Oslo",
    "4036": "Stavanger",
    "4041": "Hafrsfjord",
    "7491": "Trondheim",
    "9019": "Tromsø"
}
```

If the user goes to the index page, return the text "Postcode lookup service. Example usage: /postcode/4041", where the example link should be generated automatically (using `url_for()`) and should be a link (`<a href>...</a>`)
![Exercise1/1](images/exercise1_1.png)

If the post code exists, return the text "Post code {postcode} is {city}"
![Exercise1/2](images/exercise1_2.png)

Otherwise return "Unknown post code ({postcode})"
![Exercise1/3](images/exercise1_3.png)
