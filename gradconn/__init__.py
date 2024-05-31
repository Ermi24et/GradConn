from flask import Flask
from pymongo import MongoClient

app = Flask(__name__, template_folder='./templates', static_folder='./static')
app.secret_key = "super secret key"

client = MongoClient('localhost', 27017)

db = client.flask_db
gradconn = db.gradconn
user_db = db.user_db
employer_db = db.employer_db
job_db = db.job_db

from gradconn import routes