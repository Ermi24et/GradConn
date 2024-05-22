from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = "super secret key"

client = MongoClient('localhost', 27017)

db = client.flask_db
gradconn = db.gradconn

from gradconn import routes