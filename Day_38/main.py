import os
import requests
from datetime import datetime

from requests.api import head

APP_ID =  os.environ['Nutritionx_APP_ID']
API_Key = os.environ['Nutritionx_APP_Key']

exercises = input("What exercise have done today? ")

nutritionx_url = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_url = os.environ["Sheet_endpoint"]

today = datetime.now().strftime("%d/%m/%Y")
now = datetime.now().strftime("%X")

nutritionx_param = {
    'query': exercises,
    'gender': 'male',
    'weight_kg': 140,
    'height_cm': 182,
    'age': 30
}

nutritionx_headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_Key
}

nutritionx_request = requests.post(url=nutritionx_url, json=nutritionx_param, headers=nutritionx_headers)
nutritionx_result = nutritionx_request.json()

sheety_header = {
    "Authorization": os.environ['Sheet_Auth']
}

for exercise in nutritionx_result['exercises']:
    sheet_param = {
        'workout': {
            'date': today,
            'time': now,
            'exercise': exercise['name'].title(),
            'duration': exercise['duration_min'],
            'calories': exercise['nf_calories']
        }
    }

    sheety_request = requests.post(url=sheety_url, json=sheet_param, headers=sheety_header)
    print(sheety_request.text)