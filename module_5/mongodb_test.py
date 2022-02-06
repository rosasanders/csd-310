import pymongo

url = "mongodb+srv://admin:admin@cluster0.bvwh7.mongodb.net/pytech?retryWrites=true&w=majority"
client = pymongo.MongoClient(url)

db = client.pytech

collection = db.list_collection_names()
print(" -- Pytech Collection List --")
print(collection)
print("\n End of program, press any key to exit...")