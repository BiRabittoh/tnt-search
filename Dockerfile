FROM tiangolo/meinheld-gunicorn-flask:python3.9-alpine3.13

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY main.py /app/main.py
COPY tntvillage-release-dump /app/tntvillage-release-dump
COPY templates /app/templates

ENV APP_MODULE=main:app
