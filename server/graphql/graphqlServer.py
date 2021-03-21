#graphql python
import graphene
import json
#gestion de firebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

 #Connexion à la base de donnée
cred = credentials.Certificate("config/info802-ep-firestore-firebase-adminsdk-wprjd-dfb2fdaea4.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

baseProduct = db.collection("MarketPlace")


class Product(graphene.ObjectType):
    """ défini un produit graphql """
    id = graphene.ID()
    name = graphene.String()
    cost = graphene.Float()
    weight = graphene.Float()

    def __init__(self, bdObject):
        self.id = bdObject.id
        self.name = bdObject.get("name")
        self.cost = float(bdObject.get("cost"))
        self.weight = float(bdObject.get("weight"))

class Products(graphene.ObjectType):
    """défini une liste de produits """

    def __init__(self):
        self.products = []
        #on récupère la collection des Produits

        #on récupère tout les documents de la collection
        allProducts = baseProduct.stream()
        for product in allProducts:
            self.products.append(Product(product))

    def getProducts(self):
        return self.products


class Query(graphene.ObjectType):

    #type de retour
    products = graphene.List(Product)
    product_by_id = graphene.Field(Product, id=graphene.String())
    #produits = ListeProduit.getProducts()

    #test = graphene.String()
    def resolve_products(self, info):
        ListeProduit = Products()
        return ListeProduit.getProducts()

    def resolve_product_by_id(self, info, id):
        product = baseProduct.document(id).get()
        return Product(product)


schema = graphene.Schema(query = Query)
