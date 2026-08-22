import requests

response = requests.post('http://127.0.0.1:5000/analyze', json={
    "scenario": "Flood in Assam, 3 districts affected, 50000 displaced",
    "disaster_type": "Flood"
})

print(response.json())
