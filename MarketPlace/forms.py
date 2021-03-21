from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, DecimalField, SubmitField, PasswordField, DateField
from wtforms.validators import DataRequired
import datetime

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class DevisForm(FlaskForm):
    distance = DecimalField('Entrer la distance en km', validators=[DataRequired()])
    submit = SubmitField('Calculer le coût de livraison')

#Donnée de test :
#'cardNumber': '4970100000000154',
#'cardCvx': '123',
#'cardExpirationDate': '0128',
class UserForm(FlaskForm):
    first_name = StringField('Prénom', default='Toto', validators=[DataRequired()])
    last_name = StringField('Nom', default='ChèqueEnBois',  validators=[DataRequired()])
    birthday = DateField('Date d \'anniversaire', default=datetime.date(1985, 12, 1), validators=[DataRequired()], format='%Y/%m/%d')
    nationality = StringField('Nationnalitée', default='FR',  validators=[DataRequired()])
    country_of_residence = StringField('Pays', default='FR',  validators=[DataRequired()])
    email = StringField('Email', default='toto@chequeenbois.fr',  validators=[DataRequired()])
    cardNumber = StringField('Numéro de carte', default='4970100000000154',  validators=[DataRequired()])
    cardCvx = StringField('Cvx de la carte', default='123', validators=[DataRequired()])
    cardExpirationDate= StringField('Date d\'expiration', default='0128', validators=[DataRequired()])
    submit = SubmitField('Payer')
