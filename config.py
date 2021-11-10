import os, re

class Config():
    SECRET_KEY = 'secret key'
    DATABASE_URI = 'postgresql+psycopg2://moringa:czar@localhost/pitch'

    UPLOADED_PHOTOS_DEST ='app/static/images'


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:czar@localhost/pitch_test'
class DevConfig(Config):
    DATABASE_URI = 'postgresql+psycopg2://moringa:czar@localhost/pitch'
    DEBUG = True
    
class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    if SQLALCHEMY_DATABASE_URI .startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI  = SQLALCHEMY_DATABASE_URI .replace("postgres://", "postgresql://", 1)

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}