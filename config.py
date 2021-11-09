class Config():
    SECRET_KEY = 'my secret key'
    DATABASE_URI = 'postgresql+psycopg2://moringa:czar@localhost/pitch'
    UPLOADED_PHOTOS_DEST ='app/static/images'


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:czar@localhost/pitch_test'
class DevConfig(Config):
    DATABASE_URI = 'postgresql+psycopg2://moringa:czar@localhost/pitch'
    DEBUG = True
    
class ProdConfig(Config):
    pass

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}