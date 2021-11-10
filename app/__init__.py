from flask import Flask
import os
from config import  DevConfig, config_options
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_login import LoginManager
from flask_mail import Mail
from flask_uploads import UploadSet,configure_uploads,IMAGES

db = SQLAlchemy()

mail = Mail()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

photos = UploadSet('photos',IMAGES)


def create_app():
    app = Flask(__name__)
    
    #app.config.from_object(config_options[config_name])
    # config_options[config_name].init_app(app)
    
    app.config['SECRET_KEY']= os.environ.get('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI']= DevConfig.DATABASE_URI
    app.config['UPLOADED_PHOTOS_DEST'] = 'app/static/images'

    
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    

    
    #initializing database
    db.init_app(app)
    
    mail.init_app(app)
    
    login_manager.init_app(app)
    
    migrate = Migrate(app,db)
    configure_uploads(app,photos)
     
    
    #Registering blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint,url_prefix='/')
    
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/')
    
    return app