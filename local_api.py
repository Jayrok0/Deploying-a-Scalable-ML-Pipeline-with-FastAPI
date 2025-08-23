import json

import requests

# TODO: send a GET using the URL http://127.0.0.1:8000
r = requests.get("http://127.0.0.1:8000") # Your code here
# TODO: print the status code
print(f"Status code: {r.status_code}")
# TODO: print the welcome message
print(f"Result: {r.json()['message']}")



data = {
    "age": 37,
    "workclass": "Private",
    "fnlgt": 178356,
    "education": "HS-grad",
    "education_num": 10,
    "marital_status": "Married-civ-spouse",
    "occupation": "Prof-specialty",
    "relationship": "Husband",
    "race": "White",
    "sex": "Male",
    "capital_gain": 0,
    "capital_loss": 0,
    "hours_per_week": 40,
    "native_country": "United-States",
}

# TODO: send a POST using the data above
r = requests.post("http://127.0.0.1:8000/data/", json=data) # Your code here
# TODO: print the status code
print(f"Status code: {r.status_code}")
# TODO: print the result
print(f"Response Body: {r.json()}")
