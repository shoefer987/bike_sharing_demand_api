from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def default():
    return 'API Working'

@app.get('/base_predict')
def base_predict(date_hour , is_weekend , is_holiday):
    params = [date_hour , is_weekend , is_holiday]
    return params
