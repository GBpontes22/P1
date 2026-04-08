from database import concessionaria_collection
from bson import ObjectId

def create_concessionaria(concessionaria_dict):
    return concessionaria_collection.insert_one(concessionaria_dict)

def get_all_concessionarias():
    return list(concessionaria_collection.find())

def get_concessionaria_by_id(concessionaria_id):
    return concessionaria_collection.find_one({"_id": ObjectId(concessionaria_id)})

def update_concessionaria(concessionaria_id, concessionaria_dict):
    return concessionaria_collection.update_one(
        {"_id": ObjectId(concessionaria_id)},
        {"$set": concessionaria_dict}
    )

def delete_concessionaria(concessionaria_id):
    return concessionaria_collection.delete_one(
        {"_id": ObjectId(concessionaria_id)}
    )