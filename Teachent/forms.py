from flask_wtf import Form
from wtforms.fields import StringField, PasswordField, BooleanField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo, \
    url, ValidationError, NumberRange
from Teachent.models import Student


class LoginForm(Form):
    username = StringField('', validators=[DataRequired()])
    password = PasswordField('', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Submit')


class StudentSignupForm(Form):
    name = StringField('Name', validators=[DataRequired()])
    surName = StringField('SurName', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired(), NumberRange(min=9, max=99)])
    identificationId = IntegerField('IdentId', validators=[DataRequired(), Length(3, 10)])
    address = StringField('Address', validators=[DataRequired(), Length(1, 200)])
    gender = SelectField(u'Gender', choices=[('زن'), ('مرد')])

    # female=BooleanField('Female',)
    # male=BooleanField('Male')

    username = StringField('Username',
                           validators=[
                               DataRequired(), Length(3, 80),
                               Regexp('^[A-Za-z0-9_]{3,}$',
                                      message='Usernames consist of numbers, letters,'
                                              'and underscores.')])
    password = PasswordField('Password',
                             validators=[
                                 DataRequired(),
                                 EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('Confirm password', validators=[DataRequired()])
    email = StringField('Email',
                        validators=[DataRequired(), Length(1, 120), Email()])

    def validate_email(self, email_field):
        if Student.query.filter_by(email=email_field.data).first():
            raise ValidationError('There already is a user with this email address.')

    def validate_username(self, username_field):
        if Student.query.filter_by(username=username_field.data).first():
            raise ValidationError('This username is already taken.')


class TeacherSignupForm(Form):
    name = StringField('Name', validators=[DataRequired()])
    surName = StringField('SurName', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired(), NumberRange(min=9, max=99)])
    identificationId = IntegerField('IdentId', validators=[DataRequired(), Length(3, 10)])
    address = StringField('Address', validators=[DataRequired(), Length(1, 200)])
    gender = SelectField(u'Gender', choices=[('زن'), ('مرد')])
    mariddalState=SelectField(u'MariddalState',choices=[('مجرد'),('متاهل'),(' ')])
    major=StringField('Major',validators=[DataRequired()])
    education =StringField('Education',validators=[DataRequired()])
    rank=IntegerField('Rank',validators=[DataRequired(),Length(1,5)])
    teachingExperience=StringField('TeachingEx',validators=[DataRequired(),Length(0,30)])

    username = StringField('Username',
                           validators=[
                               DataRequired(), Length(3, 80),
                               Regexp('^[A-Za-z0-9_]{3,}$',
                                      message='Usernames consist of numbers, letters,'
                                              'and underscores.')])
    password = PasswordField('Password',
                             validators=[
                                 DataRequired(),
                                 EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('Confirm password', validators=[DataRequired()])
    email = StringField('Email',
                        validators=[DataRequired(), Length(1, 120), Email()])

    def validate_email(self, email_field):
        if Student.query.filter_by(email=email_field.data).first():
            raise ValidationError('There already is a user with this email address.')

    def validate_username(self, username_field):
        if Student.query.filter_by(username=username_field.data).first():
            raise ValidationError('This username is already taken.')
