from flask_wtf import FlaskForm
from wtforms import ValidationError
from wtforms.validators import DataRequired, Email, EqualTo, Required,Length
from ..models import User
from wtforms import StringField, PasswordField, BooleanField, SubmitField


class RegForm(FlaskForm):
    username = StringField('Enter Your Username', validators=[Required(), Length(min=4, max=20)])
    email = StringField('Email Address', validators=[Required(),Email()])
    password = PasswordField('Password',validators = [Required(), EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords',validators = [Required()])
    submit = SubmitField('Sign Up')

    def validate_email(self, data_field):

        if User.query.filter_by(email=data_field.data).first():
            raise ValidationError("There is an Account with that Email")

    def validate_username(self, data_field):
        if User.query.filter_by(username=data_field.data).first():
            raise ValidationError('That Username is taken')


class LoginForm(FlaskForm):
    email = StringField("Your Email Address", validators=[
                         DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember me")
    submit = SubmitField("Sign In")
