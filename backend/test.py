<<<<<<< HEAD
import requests

response = requests.post('http://127.0.0.1:5000/analyze', json={
    "scenario": "Flood in Assam, 3 districts affected, 50000 displaced",
    "disaster_type": "Flood"
})

print(response.json())
=======
import requests

response = requests.post('http://127.0.0.1:5000/analyze', json={
    "scenario": "Flood in Assam, 3 districts affected, 50000 displaced",
    "disaster_type": "Flood"
})

print(response.json())
>>>>>>> 9589ca86d52acbf1f3293bedbd7d4c11503eb453
