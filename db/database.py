import pymongo

class Database:
    def __init__(self, database, collection, dataset=None):
        connectionString = "localhost:27017"
        self.clusterConnection = pymongo.MongoClient(
            connectionString,
            # CASO OCORRA O ERRO [SSL_INVALID_CERTIFICATE]
            tlsAllowInvalidCertificates=True
        )
        self.db = self.clusterConnection[database]
        self.collection = self.db[collection]
        if dataset:
            self.dataset = dataset

    def resetDatabase(self):
        self.db.drop_collection(self.collection)
        self.collection.insert_many(self.dataset)

    def read(self):
        return self.collection.find({})

    def readOne(self,nome_sensor):
        return self.collection.find({"nomeSensor":nome_sensor})

    def update(self, nome_sensor, key, value):
        return self.collection.update_one(
            {"nomeSensor": nome_sensor},
            {
                "$set": {key: value},
            }
        )
