from pymongo import MongoClient
from bson.objectid import ObjectId
from pprint import pprint

def connect_mongo2(): # Connexion à la base de données
    client = MongoClient("mongo2.iem", port=27017, username="gb232322", password="gb232322", authSource="gb232322", authMechanism="SCRAM-SHA-1")
    db = client.gb232322
    return client, db
