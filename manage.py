from app import create_app,db
from config import Config
from flask_script import Manager








app = create_app('production')


with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run()