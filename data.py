import requests
parameters = {
    "amount": 11,
    "type": "boolean",
    "difficulty": "medium",
    "category": 18,
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
question_data = response.json()["results"]
