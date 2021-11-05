from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime
# from . import login_manager




class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    name  = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255),unique = True, nullable = False)
    username = db.Column(db.String(255),unique = True,nullable = False)
    password_hash = db.Column(db.String(255),nullable = False)
    date_joined  = db.Column(db.DateTime,nullable = False,default=datetime.utcnow())
    
    def __repr__(self):
        return f'User {self.username}'