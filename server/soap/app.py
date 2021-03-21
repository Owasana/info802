import logging
logging.basicConfig(level=logging.DEBUG)

from spyne import Application, rpc, ServiceBase, \
    Integer, Unicode , Decimal
from spyne import Iterable
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
import decimal

class CalculLivraison(ServiceBase):
    @rpc(Decimal, Decimal, _returns=Decimal)
    def calcul_livraison(ctx, distance, poids):
        cout = decimal.Decimal('5') + (decimal.Decimal('0.01') * distance ) + (decimal.Decimal('0.5') * poids)
        return cout

application = Application([CalculLivraison],
    tns='info802.soap.ep',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

app = WsgiApplication(application)

if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    server = make_server('127.0.0.1', 8080, app)

    print("listening to http://127.0.0.1:8080")
    print("wsdl is at: http://localhost:8080/?wsdl")

    server.serve_forever()
