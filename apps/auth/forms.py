from flask_wtf import FlaskForm
from wtforms import SubmitField

class LoginForm(FlaskForm):
    
    submit = SubmitField("로그인")
