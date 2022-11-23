import json
from pymongo import MongoClient

try:
    CONNECTION_STRING = "mongodb+srv://matheushenry1:123@cluster0.jruob8s.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(CONNECTION_STRING)
    db = client.allDataCollection
    collection = db.allDataCollection

    with open('apartaments.json') as file:
        file_dataApartments = json.load(file)

    with open('casa.json') as file:
        file_dataCasa = json.load(file)

    with open('daltonGoncales.json') as file:
        file_dataDalton = json.load(file)

    if isinstance(file_dataApartments, list):
        collection.insert_many(file_dataApartments)
    else:
        collection.insert_one(file_dataApartments)

    if isinstance(file_dataCasa, list):
        collection.insert_many(file_dataCasa)
    else:
        collection.insert_one(file_dataCasa)

    if isinstance(file_dataDalton, list):
        collection.insert_many(file_dataDalton)
    else:
        collection.insert_one(file_dataDalton)

except:
    print('fail')

