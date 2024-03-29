from fastapi import FastAPI
import requests
import json,csv
import random

from bikesharing.interface.main import predict

app = FastAPI()

@app.get('/')
def default():
    return 'API Working'

@app.get('/base_predict')
def base_predict(date):

    url = "https://api.open-meteo.com/v1/forecast"
    params_weather = {
        'latitude': 48.14,
        'longitude': 11.58,
        'hourly': ['temperature_2m', 'apparent_temperature','windspeed_10m','precipitation'],
        'forecast_days' : 1,
        'start_date' : date,
        'end_date' : date
    }

    #https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m,relativehumidity_2m,apparent_temperature,precipitation,windspeed_10m&forecast_days=1&start_date=2023-06-15&end_date=2023-06-15

    weather_data = requests.get(url, params=params_weather).json()

    pred = predict(weather_data['hourly'])

    return pred

@app.get('/polygons')
def ploygons():
    polygons = {}
    # load coordinates for districts from csv and sava them in a dict of Polygons
    with open('bikesharing/data/polygons.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            polygons[row['district']] = json.loads(row['coordinates'])

    return polygons
