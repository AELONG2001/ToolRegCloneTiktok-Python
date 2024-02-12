# from functions.database.connect import hotmails_model
# from functions.database.connect import connect_to_database

# def updateMail(username, is_get_again):
#     try:
#         connect_to_database()
#         if not is_get_again:
#             hotmails_model.collection.update_one(
#                 {'username': username},
#                 {'$set': {'isUsed': True}}
#             )
#         else:
#             hotmails_model.collection.update_one(
#                 {'username': username},
#                 {'$set': {'isUsed': False}}
#             )

#     except Exception as error:
#         print("Error reading data:", error)

