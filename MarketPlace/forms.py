from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, DecimalField, SubmitField, PasswordField, DateField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class DevisForm(FlaskForm):
    distance = DecimalField('distance', validators=[DataRequired()])
    submit = SubmitField('Devis')

class UserForm(FlaskForm):
    first_name = StringField('first_name', validators=[DataRequired()])
    last_name = StringField('last_name', validators=[DataRequired()])
    birthday = DateField('birthday', validators=[DataRequired()], format='%d/%m/%Y')
    nationality = StringField('nationality', validators=[DataRequired()])
    country_of_residence = StringField('country_of_residence', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    cardNumber = StringField('cardNumber', validators=[DataRequired()])
    cardCvx = StringField('cardCvx', validators=[DataRequired()])
    cardExpirationDate= StringField('cardExpirationDate', validators=[DataRequired()])
    submit = SubmitField('Payement')
