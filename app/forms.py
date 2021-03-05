from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    username = StringField(label='Username', validators=[DataRequired(
        message='This field can\'t be empty'), Length(min=1, message='enter '
                                                                     'username'
                                                                     '')])
    password = PasswordField(label='password', validators=[DataRequired(
        message='This field '
                                                              'can\'t be '
                                                              'empty'),
                                         Length(min=5, message='minimum 5 '
                                                               'characters')])
    remember_me = BooleanField(label='remember_me')
    submit = SubmitField('Sign In')
