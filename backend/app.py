from flask import Flask, jsonify
from api import blueprint as api
from api.models import db
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = '{dialect}://{user}:{password}@{uri}/{db}'.format(
    dialect=os.environ.get('DATABASE_DIALECT'),
    user=os.environ.get('POSTGRES_USER'),
    password=os.environ.get('POSTGRES_PASSWORD'),
    uri=os.environ.get('SQLALCHEMY_DATABASE_URI'),
    db=os.environ.get('POSTGRES_DB'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

app.config['RESTPLUS_VALIDATE'] = True

app.register_blueprint(api, url_prefix='/api')


def create_db():
    with app.app_context():
        db.create_all()

def drop_db():
    with app.app_context():
        db.drop_all()
