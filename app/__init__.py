from flask import Flask



def create_app():
    app = Flask(__name__)
    
    #Registering blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint,url_prefix='/')
    
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/')
    
    return app