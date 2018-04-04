"""
Exercise #2: Inventory
"""

from flask import Flask, request
import json

app = Flask(__name__)


@app.route("/inventory")
def inventory():
    # the data is stored in this static dict for now, indexed by item_id
    ITEMS = {
        "001": {
            "name": "iPhone 5",
            "brand": "Apple",
            "size_x": 5,
            "size_y": 7,
            "size_z": 2,
            "price": 2000,
            "available": True
        },
        "123": {
            "name": "Test item",
            "brand": "CompanyX",
            "size_x": 11,
            "size_y": 22,
            "size_z": 33,
            "price": 1000,
            "available": False
        },
        "999": {
            "name": "Test item 2",
            "brand": "CompanyY",
            "size_x": 33,
            "size_y": 22,
            "size_z": 11,
            "price": 500,
            "available": True
        }
    }

    item_id = request.args.get("item_id", None)
    if item_id and len(item_id) == 3:
        if item_id in ITEMS:
            return json.dumps(ITEMS[item_id])

    return ""


@app.route("/")
def index():
    return app.send_static_file("exercise2.html")


if __name__ == "__main__":
    app.run()
