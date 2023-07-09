FROM python:3-alpine

COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["waitress-serve", "--host", "127.0.0.1", "--port", "5000", "main:app"]
