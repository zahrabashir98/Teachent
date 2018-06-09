from flask_wtf import Form
from wtforms.fields import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(Form):
    username = StringField('Username:', validators=[DataRequired()] )
    password = PasswordField('Password:', validators=[DataRequired()] )
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Submit')
