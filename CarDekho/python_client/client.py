import requests


endpoints = "http://127.0.0.1:8000/car/list"    # endpoints or url both are same...


getresponse = requests.get(endpoints)

print(getresponse.json())