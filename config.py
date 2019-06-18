class Config(object):
    SQLALCHEMY_ECHO = True
    POSTS_PER_PAGE = 10


class ProdConfig(Config):
    SECRET_KEY = "9l\xbe(&\xf5\xe8`\x98@P\xb8\xf4\xa4\x807\xc5\x84\xf9\xcf~}\xa0+"


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:niblas69$@localhost:5432/flask_db"
    # SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
    SECRET_KEY = "\x91\xef\xf9V\xa6f\xda\xad!\x95N\xd2\xee\x19\xf3\xc2\x82mm\x87\xa2\x00\x97\xdc"
