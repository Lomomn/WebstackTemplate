from flask import Flask, jsonify
import os
import sys
from src.api import blueprint as api
from src.api.models import db


def get_database_uri_string(testing=False):
        '''Returns uri string for use with `sqlalchemy_utils.database_exists` tests'''
        return '{dialect}://{user}:{password}@{uri}/{db}'.format(
                dialect=os.environ.get('DATABASE_DIALECT'),
                user=os.environ.get('POSTGRES_USER'),
                password=os.environ.get('POSTGRES_PASSWORD'),
                uri=os.environ.get(testing and 'SQLALCHEMY_DATABASE_URI_TESTING' or 'SQLALCHEMY_DATABASE_URI'),
                db=os.environ.get('POSTGRES_DB'))


def create_db(app):
        with app.app_context():
                db.create_all()


def drop_db(app):
        with app.app_context():
                db.drop_all()


def setup_config(testing=False):
        app = Flask(__name__)

        app.config['SQLALCHEMY_DATABASE_URI'] = get_database_uri_string(testing)
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

        db.init_app(app)

        app.config['RESTPLUS_VALIDATE'] = True
        app.config['ENV'] = os.environ.get('ENV')
        app.config['TESTING'] = testing

        app.register_blueprint(api, url_prefix='/api')

        # Creates the tables if they don't exist
        create_db(app)


        return app


# Set TESTING env var before starting app, the setup_config fn should handle all other
# testing related setup 
# This code isn't called when testing as just the fns which are needed are imported
app = setup_config(testing=os.environ.get('TESTING') or False) # short-circuit None to False so env var doesn't need to be set