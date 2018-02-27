""" JSON write
Make a dictionary from the following keys and values, and write that dictionary into a JSON file:
"""

import json

my_dict = dict(zip(tuple([1, 2, 3, 4, 5]), tuple(["I", "love", "python", "very", "much"])))
with open("6b.json", "w") as f:
    json.dump(my_dict, f, indent=2)
