from Teachent import db
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash


class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=False)
    surName = db.Column(db.String(20), unique=False)
    age = db.Column(db.Integer, nullable=False)
    identificationId = db.Column(db.Integer, nullable=False, unique=True)
    address = db.Column(db.String(200), nullable=False)
    gender = db.Column(db.String(), nullable=False)
    mariddalState = db.Column(db.String(), nullable=False)
    major = db.Column(db.String(), nullable=False)
    education = db.Column(db.String(), nullable=False)
    rank = db.Column(db.Integer, nullable=False)
    teachingExperience = db.Column(db.String(30), nullable=False)
    username = db.Column(db.String(80), nullable=False)
    password_hash = db.Column(db.String)
    email = db.Column(db.String(120), nullable=False)

    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @staticmethod
    def get_by_username(username):
        return Teacher.query.filter_by(username=username).first()

    def __repr__(self):
        return "<User '{}'>".format(self.username)


class Student(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=False)
    surName = db.Column(db.String(20), unique=False)
    age = db.Column(db.Integer, nullable=False)
    identificationId = db.Column(db.Integer, nullable=False, unique=True)
    address = db.Column(db.String(200), nullable=False)
    gender = db.Column(db.String(), nullable=False)
    username = db.Column(db.String(80), nullable=False)
    password_hash = db.Column(db.String)
    email = db.Column(db.String(120), nullable=False)

    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @staticmethod
    def get_by_username(username):
        return Student.query.filter_by(username=username).first()

    def __repr__(self):
        return "<User '{}'>".format(self.username)
