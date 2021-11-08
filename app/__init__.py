from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_login import LoginManager
from flask_uploads import UploadSet,configure_uploads,IMAGES

db = SQLAlchemy()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
photos = UploadSet('photos',IMAGES)


def create_app():
    app = Flask(__name__)
    
    app.config['SECRET_KEY']= Config.SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI']=Config.DATABASE_URI
    app.config['UPLOADED_PHOTOS_DEST'] = Config.UPLOADED_PHOTOS_DEST
    

    
    #initializing database
    db.init_app(app)
    login_manager.init_app(app)
    migrate = Migrate(app,db)
    configure_uploads(app,photos)
     
    
    #Registering blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint,url_prefix='/')
    
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/')
    
    return app