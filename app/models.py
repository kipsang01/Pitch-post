from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime
from flask_login import UserMixin
from . import login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    name  = db.Column(db.String(255), nullable=False)
    bio = db.Column(db.String(255))
    profile_pic = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True, nullable = False)
    username = db.Column(db.String(255),unique = True,nullable = False)
    password_hash = db.Column(db.String(255),nullable = False)
    date_joined  = db.Column(db.DateTime,nullable = False,default=datetime.utcnow())
    posts = db.relationship('Pitch', backref='author', lazy='dynamic')
    comments = db.relationship('Comment', backref='author', lazy='dynamic')
    
    
    def __repr__(self):
        return f'User {self.username}'
    
    def save_user(self):
        db.session.add(self)
        db.session.commit()
        
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)


class Pitch(db.Model):
    __tablename__ = 'pitches'
    id = db.Column(db.Integer,primary_key = True)
    category = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(255), nullable=False)
    date_posted  = db.Column(db.DateTime,nullable = False,default=datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),nullable = False)
    comments = db.relationship('Comment', backref='pitch', lazy='dynamic')
    
    
    
    def __repr__(self):
        return f'Pitch {self.category}{self.content}'
    
    
    def save_pitch(self):
        db.session.add(self)
        db.session.commit()
        
        
class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer,primary_key = True)
    content = db.Column( db.String(255))
    date_posted  = db.Column(db.DateTime,nullable = False,default=datetime.utcnow())
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'),nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),nullable = False)
    
    
    def __repr__(self):
        return f'Comment {self.category}{self.content}'