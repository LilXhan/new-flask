from pymongo import MongoClient

client = MongoClient('localhost', 27017)

# creamos la db

db = client['api_rick_and_morty']