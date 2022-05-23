import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth
import os

GENDER = "M"
WEIGHT_KG = 92.2
HEIGHT_CM = 185
AGE = 32

APP_ID = "8bb7b5d2"
API_KEY = "20e5ede1ed35e74d0b8f8a4e2d70ee58"

# BEARER_TOKEN = "Bearer iojawdioj123!"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/5d63f146dcb5025f5e5e26ffd7aabde5/myWorkouts/workouts"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

################### Start of Step 4 Solution ######################

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    # sheet_response = requests.post(url=sheety_endpoint, json=sheet_inputs)
    #
    # print(sheet_response.text)

    bearer_headers = {
        "Authorization": "Bearer iojawdioj123!"
    }
    sheet_response = requests.post(
        url=sheety_endpoint,
        json=sheet_inputs,
        headers=bearer_headers
    )
    print(sheet_response.text)