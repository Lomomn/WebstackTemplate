from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from api import blueprint as api
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = '{dialect}://{user}:{password}@{uri}/{db}'.format(
    dialect=os.environ.get('DATABASE_DIALECT'),
    user=os.environ.get('POSTGRES_USER'),
    password=os.environ.get('POSTGRES_PASSWORD'),
    uri=os.environ.get('SQLALCHEMY_DATABASE_URI'),
    db=os.environ.get('POSTGRES_DB'))
db = SQLAlchemy(app)

app.register_blueprint(api, url_prefix='/api')

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
