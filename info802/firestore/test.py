import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("info802-ep-firestore-firebase-adminsdk-wprjd-dfb2fdaea4.json")
firebase_admin.initialize_app(cred)

db = firestore.client()


doc = db.collection("CollectionName").document("DocTest")

doc.set({"Name":"Jean"})
