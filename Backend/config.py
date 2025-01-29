import os
from decouple import config

# add the file path folder to the database
BASE_DIR = os.path.dirname(os.path.realpath(__file__))

class Config:

    SECRET_KEY = config('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = config('SQLALCHEMY_TRACK_MODIFICATIONS', cast=bool)

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, 'open.db')
    DEBUG = True
    SQLALCHEMY_ECHO = True


class ProdConfig(Config):
    #Production config
    pass

class TestConfig(Config):
    #Test configuration
        SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"
        SQLALCHEMY_ECHO = False
        TESTING=True
