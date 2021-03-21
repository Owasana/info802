from flask import render_template, flash, redirect
from forms import DevisForm, UserForm
from model.products import Products, Product
from model.users import User
from app import app

@app.route('/')
@app.route('/index')
def index():

    produits = Products.getProduits()
    return render_template('index.html', title='Home', produits=produits)

@app.route('/devis/<productid>', methods=['GET', 'POST'])
def devis(productid):
    produit = Products.getProduit(productid)

    form = DevisForm()
    if form.validate_on_submit():
        distance = form.distance.data
        produitAct = Product(produit)
        prix = produitAct.DevisTot(distance)
        return render_template('devis.html', produit = produit, prix = prix, form = form)

    return render_template('devis.html', produit = produit, form = form)


@app.route('/payment/<productid>/<livraison>', methods=['GET', 'POST'])
def payment(productid, livraison):
    produit = Products.getProduit(productid)
    produitAct = Product(produit)
    cout = produitAct.getCost()

    form = UserForm()
    if form.validate_on_submit():
        print(form)
        first_name = form.first_name.data
        last_name = form.last_name.data
        birthday = form.birthday.data
        nationality = form.nationality.data
        country_of_residence = form.country_of_residence.data
        email = form.email.data
        cardNumber = form.cardNumber.data
        cardCvx = form.cardCvx.data
        cardExpirationDate = form.cardExpirationDate.data

        acheteur = User(first_name, last_name, birthday, nationality, country_of_residence, email, cardNumber, cardCvx, cardExpirationDate)
        res = acheteur.pay(cout, livraison)

        return render_template('payment.html', produit = produit, form = form, livraison = livraison, cout = cout, res = res)

    return render_template('payment.html', produit = produit, livraison = livraison, cout = cout, form = form)
