FROM python:3-alpine

COPY main.py .
COPY requirements.txt .
COPY tntvillage-release-dump ./tntvillage-release-dump
COPY templates ./templates

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["waitress-serve", "--host", "0.0.0.0", "--port", "5000", "main:app"]
