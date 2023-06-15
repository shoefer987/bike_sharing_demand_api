FROM python:3.10.6-buster

COPY requirements_prod.txt requirements.txt
COPY api api
COPY bikesharing bikesharing

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD uvicorn api.api:app --host 0.0.0.0 --port $PORT
