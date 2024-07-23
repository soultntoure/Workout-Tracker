import requests
from datetime import datetime

APP_ID = "be9f1dbc"
API_KEY = "81dde624f8246c81da547a510c9079ca"
SHEETY_USERNAME = "c929226d8eb7321e53d3e1d38d9cc363"
SHEETY_BEARER_TOKEN = 'awetlopingkjrc,f'

EXCERCISE_ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'
SHEET_ENDPOINT = f'https://api.sheety.co/{SHEETY_USERNAME}/workoutsTracking/workouts'

WEIGHT_KG = 73.7
HEIGHT_CM = 179
AGE = 18

excecise_query = input("Tell me which excercises you did: ")

excersice_params = {
    "query": excecise_query,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

response = requests.post(url=EXCERCISE_ENDPOINT, json=excersice_params, headers=headers)
result = response.json()



today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheety_params = {
        "workout":{
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {SHEETY_BEARER_TOKEN}'
}


sheet_response = requests.post(url=SHEET_ENDPOINT, json=sheety_params, headers=headers)
print(sheet_response.text)


