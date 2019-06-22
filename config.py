import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_ECHO = True
    POSTS_PER_PAGE = 10
    SECRET_KEY = "9l\xbe(&\xf5\xe8`\x98@P\xb8\xf4\xa4\x807\xc5\x84\xf9\xcf~}\xa0+"


class ProdConfig(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:niblas69$@localhost:5432/flask_db"
    # SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
