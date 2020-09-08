from flask import g, current_app
from pymongo import MongoClient

def teardown_db(error=None):
    database = g.pop('db', None)
    if database:
        database.client.close()

def get_db():
    if 'db' not in g:
        host = current_app.config['DATABASE_HOST']
        port = current_app.config['DATABASE_SERVICE']
        client = MongoClient(host, port)
        g.db = client[current_app.config['DATABASE_NAME']]
    return g.db

def init_app(app):
    app.teardown_appcontext(teardown_db)