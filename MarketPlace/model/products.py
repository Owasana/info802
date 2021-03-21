from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

import zeep


#GRAPH QL :
_transport = RequestsHTTPTransport(
    url='https://info802-ep-ql.azurewebsites.net/graphql',
    use_json=True,
)

client = Client(
    transport =_transport,
    fetch_schema_from_transport=True,
)

#SOAP :
clientSOAP = zeep.Client('https://info802-ep-soap-server.azurewebsites.net/?wsdl')
#clientSOAP = zeep.Client('http://localhost:8080/?wsdl')


class Product:

    def __init__(self, values):
        self.id = values["id"]
        self.name = values["name"]
        self.cost = values["cost"]
        self.weight = values["weight"]

    def DevisTot(self, distance):
        return clientSOAP.service.calcul_livraison(distance, self.weight)

    def getCost(self):
        return self.cost

class Products:

    @staticmethod
    def getProduits():
        queryProduits = gql("""
        {
            products{
                id
                name
                cost
                weight
            }
        }
        """)
        return client.execute(queryProduits)['products']

    @staticmethod
    def getProduit(productid):
        queryProduitById = gql("""
         {
            productById(id: \"""" + productid + """\") {
                id
                name
                cost
                weight
         }
        }""")
        return client.execute(queryProduitById)['productById']
