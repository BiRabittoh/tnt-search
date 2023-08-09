FROM tiangolo/meinheld-gunicorn-flask:python3.9-alpine3.13

WORKDIR /app

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY tntvillage-release-dump ./tntvillage-release-dump
COPY templates ./templates
COPY main.py ./main.py

ENV APP_MODULE=main:app
