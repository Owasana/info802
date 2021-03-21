from decimal import *

import mangopay
import requests
import urllib

##Réglage MongoPay
mangopay.client_id = 'info802-ep'
mangopay.apikey='MZ3zAhEH5nbYg8RPH6ekOZQdsAYqQJTvghh8fJkamzJtZnvEXu'

from mangopay.api import APIRequest
from mangopay.resources import *
from mangopay.utils import Address


##Vendeur Défini :
#vendor_user = NaturalUser(first_name = 'Lily',
#                          last_name = 'Lala',
#                          birthday = 1300186358,
#                          nationality='FR',
#                          country_of_residence='FR',
#                          email='Lily@lala.com', )

#vendor_user.save()

#vendor_user_wallet = Wallet(owners = [vendor_user],
#                    description='L\'argent des abonnés',
#                    currency='EUR',
#                    tag='wall user 1')

#vendor_user_wallet.save()

vendor_user = NaturalUser.get(104339777)
wallet_vendor = vendor_user.wallets[0]

class User:

    def __init__(self, first_name, last_name, birthday, nationality, country_of_residence, email, cardNumber, cardCvx, cardExpirationDate):

        ##On enregistre l'utilisateur
        self.mangopay_user = NaturalUser(
                        first_name=first_name,
                        last_name=last_name,
                        birthday=int(birthday.strftime('%s')),
                        nationality=nationality,
                        country_of_residence=country_of_residence,
                        email=email)
        self.mangopay_user.save()

        ##On enregistre la carte de l'utilisateur
        card_registration = CardRegistration(user=self.mangopay_user, currency = 'EUR')
        card_registration.save()

        card_url = card_registration.card_registration_url
        res = requests.post(card_url, data = {
            'cardNumber': cardNumber,
            'cardCvx': cardCvx,
            'cardExpirationDate' : cardExpirationDate,
            'accessKeyRef': card_registration.access_key,
            'data': card_registration.preregistration_data
        })

        card_registration.registration_data = res.text
        card_registration.save()

        self.card_user = card_registration.card


    def pay(self, product_price, delivery):

        pricetot = (Decimal(product_price) + Decimal(delivery))
        direct_pay_in = DirectPayIn(author=self.mangopay_user,
                                    debited_funds=Money(amount=pricetot * 100, currency ='EUR'),
                                    fees=Money(amount = 0, currency='EUR'),
                                    credited_wallet_id=wallet_vendor,
                                    card_id=self.card_user,
                                    secure_mode="DEFAULT",
                                    secure_mode_return_url="https://www.ulule.com/")
        direct_pay_in.save()

        return "Payement fait , coût total : " + str(pricetot)
