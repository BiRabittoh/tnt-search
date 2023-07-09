# TNTVillage Search Tool

## Instructions

### Bare metal
```
python -m venv venv
source venv\bin\activate
pip install --upgrade pip
pip install -r requirements.txt
waitress-serve --host 127.0.0.1 --port 5000 main:app
```

### Docker
```
docker build -t tnt-search .
docker run -d -p 5000:5000 tnt-search
```
