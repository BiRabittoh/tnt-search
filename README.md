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
Build image:
```
docker build -t tnt-search .
```

Then, either use Docker CLI:
```
docker run -d --name tnt-search --restart unless-stopped -p 5000:5000 tnt-search
```

Or, better, docker-compose (already set up for reverse-proxy only):
```
docker-compose up -d
```
