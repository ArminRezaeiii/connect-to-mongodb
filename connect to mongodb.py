
from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017/")


db = client["mydatabase"]
users_collection = db["users"]


user = {"name": "Ali", "email": "ali@example.com", "age": 25}
insert_result = users_collection.insert_one(user)
print("User inserted with _id:", insert_result.inserted_id)


print("\nAll users:")
for u in users_collection.find():
    print(u)


update_result = users_collection.update_one(
    {"name": "Ali"},
    {"$set": {"age": 26}}
)
print("\nUpdated documents:", update_result.modified_count)


user_found = users_collection.find_one({"name": "Ali"})
print("\nUser found:", user_found)


delete_result = users_collection.delete_one({"name": "Ali"})
print("\nDeleted documents:", delete_result.deleted_count)


client.close()
