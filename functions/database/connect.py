# from pymongo import MongoClient
# import json

# with open("configs_account.json", "r") as json_file:
#     data = json.load(json_file)

# mongo_db_uri = data["database_value"]

# client = MongoClient(mongo_db_uri)
# db = client.get_database()

# def connect_to_database():
#     try:
#         client.server_info()
#         print("Connected to the database")
#     except Exception as e:
#         print(f"Error connecting to the database: {e}")

# class Hotmails:
#     def __init__(self, collection):
#         self.collection = collection

#     def insert_one(self, document):
#         return self.collection.insert_one(document)

# hotmails_collection = db.hotmails
# hotmails_model = Hotmails(hotmails_collection)