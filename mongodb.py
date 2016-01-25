from pymongo import MongoClient
client = MongoClient()
db = client.test
# cursor = db.restaurants.find()
# cursor = db.restaurants.find({"grades.grade": "B"})
# for document in cursor:
#     print(document)
# result = db.restaurants.update_many(
#     {"address.zipcode": "10016", "cuisine": "Other"},
#     {
#         "$set": {"cuisine": "Category To Be Determined"},
#         "$currentDate": {"lastModified": True}
#     }
# )
# print result.matched_count
# from datetime import datetime
# result = db.restaurants.insert_one(
#     {
#         "address": {
#             "street": "2 Avenue",
#             "zipcode": "10075",
#             "building": "1480",
#             "coord": [-73.9557413, 40.7720266]
#         },
#         "borough": "Manhattan",
#         "cuisine": "Italian",
#         "grades": [
#             {
#                 "date": datetime.strptime("2014-10-01", "%Y-%m-%d"),
#                 "grade": "A",
#                 "score": 11
#             },
#             {
#                 "date": datetime.strptime("2014-01-16", "%Y-%m-%d"),
#                 "grade": "B",
#                 "score": 17
#             }
#         ],
#         "nickname":"yifeir",
#         "name": "Vella",
#         "restaurant_id": "41704620"
#     }
# )
cursor = db.restaurants.find({"nickname": {'$regex': 'fei'}})
for document in cursor:
	print document