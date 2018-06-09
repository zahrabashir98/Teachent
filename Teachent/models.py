from Teachent import db
from flask_login import UserMixin
from werkzeug.security import check_password_hash,generate_password_hash


class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer, nullable=False)
    konkoorRank = db.Column(db.Integer, nullable=False)
    madrak = db.Column(db.String(80), nullable=False)
    reshte = db.Column(db.String(80), nullable=False)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    name = db.Column(db.String(20), unique=False)
    surname = db.Column(db.String(20), unique=False)
    password = db.Column(db.String(30), unique=False, nullable=True)
    courses = db.Column(db.String(80), unique=False)
    university = db.Column(db.String(80), unique=False)
    number = db.Column(db.Integer, nullable=False)
    rank = db.Column(db.String(10), nullable=False)
    picLink = db.Column(db.String(100), nullable=False, unique=True)

    def __repr__(self):
        return "<User '{}'>".format(self.username)


class Student(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    #age = db.Column(db.Integer, nullable=False)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    #name = db.Column(db.String(20), unique=False)
    #surname = db.Column(db.String(20), unique=False)
    password_hash = db.Column(db.String)
    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)
    def check_password(self,password):
        return check_password_hash(self.password_hash,password)
    @staticmethod
    def get_by_username(username):
        return Student.query.filter_by(username=username).first()


    def __repr__(self):
        return "<User '{}'>".format(self.username)
