import pymongo

url = "mongodb+srv://admin:admin@cluster0.bvwh7.mongodb.net/pytech?retryWrites=true&w=majority"
client = pymongo.MongoClient(url)

db = client.pytech

student_collection = db.get_collection("students")

bob = {
    "student_id": "1007",
    "first_name": "Bob",
    "last_name": "Thisteacheristerrible"
}

bob_student_id = student_collection.insert_one(bob).inserted_id

mary = {
    "student_id": "1008",
    "first_name": "Mary",
    "last_name": "Pleasegivebetterinstructions"
}

mary_student_id = student_collection.insert_one(mary).inserted_id

ben = {
    "student_id": "1009",
    "first_name": "Ben",
    "last_name": "Dover"
}

ben_student_id = student_collection.insert_one(ben).inserted_id

student_collection.insert_one(bob)
student_collection.insert_one(mary)
student_collection.insert_one(ben)

print(" -- INSERT STATEMENTS --")
print(f'Inserted student record {bob.get("first_name")} {bob.get("last_name")} into the students collection with document_id {bob_student_id}')
print(f'Inserted student record {mary.get("first_name")} {mary.get("last_name")} into the students collection with document_id {mary_student_id}')
print(f'Inserted student record {ben.get("first_name")} {ben.get("last_name")} into the students collection with document_id {ben_student_id}')
