#!/usr/local/bin/python3
import os, csv, json
from datetime import datetime
from flask import Flask, request, render_template

INPUT_PATH = os.path.join("tntvillage-release-dump", "tntvillage-release-dump.csv")
CSV_SEPARATOR = ","
HEADER = [ "DATA", "HASH", "TOPIC", "POST", "AUTORE", "TITOLO", "DESCRIZIONE", "DIMENSIONE", "CATEGORIA" ]
TABLE_HEADER = [ "DATA", "CATEGORIA", "TITOLO", "DESCRIZIONE", "AUTORE", "DIMENSIONE", "HASH" ]
CATEGORIE = {
    1: "Film TV e programmi",
    2: "Musica",
    3: "E Books",
    4: "Film",
    6: "Linux",
    7: "Anime",
    8: "Cartoni",
    9: "Macintosh",
    10: "Windows Software",
    11: "Pc Game",
    12: "Playstation",
    13: "Students Releases",
    14: "Documentari",
    21: "Video Musicali",
    22: "Sport",
    23: "Teatro",
    24: "Wrestling",
    25: "Varie",
    26: "Xbox",
    27: "Immagini sfondi",
    28: "Altri Giochi",
    29: "Serie TV",
    30: "Fumetteria",
    31: "Trash",
    32: "Nintendo",
    34: "A Book",
    35: "Podcast",
    36: "Edicola",
    37: "Mobile"
}
MAGNET_STR = '<button onclick=\"location.href=\'magnet:?xt=urn:btih:{}\'\" class="btn btn-danger">m</button>'

def handle_content(content: str):
    return { x: content[idx] for idx, x in enumerate(HEADER) }
    
def search_keyword(content, keyword: str, category=0):
    results = [ x for x in content if keyword.lower() in x['TITOLO'].lower()]
    if category == 0:
        return results
    return [ x for x in results if category == x['CATEGORIA']]

def get_last_torrents(content, page=1, amt=50):
    tmp = sorted(content, key=lambda x:x['DATA'], reverse=True)
    tmp_length = len(content)
    
    offset = amt * page
    start_from = offset - amt
    start_from = 0 if start_from < 0 else start_from
    end_with = start_from + amt
    end_with = tmp_length if end_with > tmp_length else end_with
    return tmp[start_from:end_with]

def load_content(input_path=INPUT_PATH):
    with open(input_path, "r", encoding="utf-8") as in_file:
        csv_iterator = csv.reader(in_file, quotechar='"', delimiter=',', quoting=csv.QUOTE_NONNUMERIC, skipinitialspace=True)
        next(csv_iterator)
        return [ handle_content(x) for x in csv_iterator ]

def sizeof_fmt(num, suffix="B"):
    for unit in ("", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"):
        if abs(num) < 1024.0:
            return f"{num:3.1f}{unit}{suffix}"
        num /= 1024.0
    return f"{num:.1f}Yi{suffix}"

def parse_values(result):
    tmp = result.copy()
    tmp['DATA'] = datetime.strptime(tmp['DATA'], "%Y-%m-%dT%H:%M:%S").strftime("%d/%m/%Y")
    tmp['CATEGORIA'] = CATEGORIE[int(tmp['CATEGORIA'])]
    tmp['HASH'] = MAGNET_STR.format(tmp['HASH'])
    tmp['DIMENSIONE'] = sizeof_fmt(tmp['DIMENSIONE'])
    return tmp

def format_results(results, headers=HEADER):
    print(len(results))
    contents = [parse_values(x) for x in results]
    return [[result[header] for header in headers] for result in contents]

def get_args(args):
    keywords = args.get("keywords") or ""
    category = args.get("category") or 0
    page = args.get("page") or 1
    return keywords, category, page

content = load_content()
app = Flask(__name__)

@app.route('/api/header')
def route_api_header():
    return json.dumps(HEADER)

@app.route('/api')
def route_api():
    keywords, category, page = get_args(request.args)
    results = search_keyword(content, keywords, int(category))
    results = get_last_torrents(results, page=int(page))
    return json.dumps(results)

@app.route('/')
def route_main():
    keywords, category, page = get_args(request.args)
    results = search_keyword(content, keywords, int(category))
    results = get_last_torrents(results, page=int(page))
    results = format_results(results, headers=TABLE_HEADER)
    return render_template("index.html", headers=TABLE_HEADER, content=results, categories=CATEGORIE.items(), page=page)  

if __name__ == '__main__':
    app.run()
