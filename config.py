import os
BASEDIR = os.path.abspath(os.path.dirname(__file__))

class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # URI for SQLite database
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    'postgres+psycopg2://nate:5759@localhost:5432/dealership'
