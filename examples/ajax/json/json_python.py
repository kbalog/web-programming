"""
Using JSON from Python
"""

import json

data = {
    "name": "John Smith",
    "age": 32,
    "married": True,
    "interests": [1, 2, 3],
    "other": {
        "city": "Stavanger",
        "postcode": 4041
    }
}

# encode
j = json.dumps(data)
print(j)

# pretty printing
#print(json.dumps(data, sort_keys=True, indent=4))

# decode
data2 = json.loads(j)
print(data2)
