# TNTVillage Search Tool

## Instructions

First, make sure to clone everything correctly:
```
git clone https://github.com/BiRabittoh/tnt-search
cd tnt-search
git submodule init
git submodule update
```

### Bare metal
```
python3 -m venv venv
source venv\bin\activate
pip install --upgrade pip
pip install -r requirements.txt
waitress-serve --host 127.0.0.1 --port 5000 main:app
```

### Docker

Either use Docker CLI:
```
docker build -t tnt-search .
docker run -d --name tnt-search --restart unless-stopped -p 5000:5000 tnt-search
```

Or, better, `docker-compose`:
```
docker-compose up -d
```
