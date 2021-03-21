import mangopay
from mangopay.resources import User, NaturalUser
from mangopay.utils import Address

mangopay.client_id='info802-ep'
mangopay.apikey='MZ3zAhEH5nbYg8RPH6ekOZQdsAYqQJTvghh8fJkamzJtZnvEXu'

from mangopay.api import APIRequest

handler = APIRequest(sandbox=True)



natural_user = NaturalUser(first_name='Victor',
                           last_name='Hugo',
                           birthday=1300186358,
                           nationality='FR',
                           country_of_residence='FR',
                           email='victor@hugo.com',
                           )

natural_user.save() # save the new user

print(natural_user.get_pk()) # retrieve the primary key
