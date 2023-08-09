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
```

* Debug:
```
flask --app main run --port 1111 --debug
```
* Production: 
```
pip install waitress
waitress-serve --host 127.0.0.1 --port 1111 main:app
```

### Docker
Simply run:
```
docker-compose up --detach --build
```
