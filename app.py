from flask import Flask, jsonify
from flask_cors import CORS
from crawlers.advanceAmerica import AdvanceAmerica
from crawlers.crawlerManager import FullCrawl
from db import init_app
from config import Config

app = Flask(__name__)

app.config.from_object(Config)
CORS(app)
init_app(app)

@app.route('/')
def hello_world():
    FullCrawl.crawl()
    return "200"