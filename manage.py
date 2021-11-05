from app import create_app,db
from config import Config
from flask_script import Manager








app = create_app()

app.config['SECRET_KEY']= Config.SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI']=Config.DATABASE_URI


with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug = True)