import mangopay
from mangopay.resources import User, NaturalUser
from mangopay.utils import Address

mangopay.client_id='info802-ep'
mangopay.apikey='MZ3zAhEH5nbYg8RPH6ekOZQdsAYqQJTvghh8fJkamzJtZnvEXu'

from mangopay.api import APIRequest

handler = APIRequest(sandbox=True)



natural_user = NaturalUser(first_name='Victor',
                           last_name='Hugo',
                           address=Address(address_line_1='AddressLine1', address_line_2='AddressLine2',
                               city='City', region='Region',
                               postal_code='11222', country='FR'),
                           birthday=1300186358,
                           nationality='FR',
                           country_of_residence='FR',
                           occupation='Writer',
                           income_range='6',
                           proof_of_identity=None,
                           proof_of_address=None,
                           person_type='NATURAL',
                           email='victor@hugo.com',
                           tag='custom tag')

natural_user.save() # save the new user

print(natural_user.get_pk()) # retrieve the primary key
