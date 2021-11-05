from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
def create_app():
    app = Flask(__name__)
    


    
    #initializing database
    db.init_app(app)
    migrate = Migrate(app,db)
    
    #Registering blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint,url_prefix='/')
    
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/')
    
    return app