from flask import Flask, request, jsonify
import json
import google_play_scraper 


app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return "Hello World"


@app.route("/gscrap", methods=['POST'])
def scrap():
    record = json.loads(request.data)
    print(record["x"])
    z = google_play_scraper.app(record["x"])
    return z
    
   