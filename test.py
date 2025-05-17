import requests
import json

# Define the API URL
url = 'http://127.0.0.1:5000/predict'

# Create your input data as a Python dictionary (with all required fields)
input_data = {
    "Age": 60,
    "Diabetes": 0,
    "BloodPressureProblems": 0,
    "AnyTransplants": 0,
    "AnyChronicDiseases": 0,
    "Height": 180,
    "Weight": 73,
    "KnownAllergies": 0,
    "HistoryOfCancerInFamily": 0,
    "NumberOfMajorSurgeries": 3
}

# Convert to JSON
headers = {'Content-Type': 'application/json'}
response = requests.post(url, data=json.dumps(input_data), headers=headers)

# Print the prediction result
print(response.json())
