from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired

class SignupForm(Form):
    name = StringField('name', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])

class LoginForm(Form):
    name = StringField('name', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])


    