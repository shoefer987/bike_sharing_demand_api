from fastapi import FastAPI
import requests

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
        'hourly': ['temperature_2m', 'relativehumidity_2m', 'apparent_temperature','windspeed_10m','precipitation'],
        'forecast_days' : 1,
        'start_date' : date,
        'end_date' : date
    }

    #https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m,relativehumidity_2m,apparent_temperature,precipitation,windspeed_10m&forecast_days=1&start_date=2023-06-15&end_date=2023-06-15

    weather_data = requests.get(url, params=params_weather).json()

    return {'Xpred' : weather_data['hourly']}
