class Config(object):
    pass

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUB = True