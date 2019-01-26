from flask import Flask, jsonify
import os
import sys
from api import blueprint as api
from api.models import db


def setup_config(testing=False):
        app = Flask(__name__)

        app.config['SQLALCHEMY_DATABASE_URI'] = '{dialect}://{user}:{password}@{uri}/{db}'.format(
        dialect=os.environ.get('DATABASE_DIALECT'),
        user=os.environ.get('POSTGRES_USER'),
        password=os.environ.get('POSTGRES_PASSWORD'),
        uri=os.environ.get('SQLALCHEMY_DATABASE_URI'+(testing and '_TESTING' or '')),
        db=os.environ.get('POSTGRES_DB'))
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
        db.init_app(app)

        app.config['RESTPLUS_VALIDATE'] = True
        app.config['ENV'] = os.environ.get('ENV')
        app.config['TESTING'] = testing

        app.register_blueprint(api, url_prefix='/api')

        print(sys.path, '')

        return app


# Set TESTING env var before starting app, the setup_config fn should handle all other
# testing related setup 
# This code isn't called when testing as just the fns which are needed are imported
app = setup_config(testing=os.environ.get('TESTING') or False) # short-circuit None to False so env var doesn't need to be set

def create_db():
    with app.app_context():
        db.create_all()

def drop_db():
    with app.app_context():
        db.drop_all()
