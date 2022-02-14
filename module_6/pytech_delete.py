import pymongo

url = "mongodb+srv://admin:admin@cluster0.bvwh7.mongodb.net/pytech?retryWrites=true&w=majority"
client = pymongo.MongoClient(url)

db = client.pytech

student_collection = db.get_collection("students")
students = student_collection.find({})

print("-- DISPLAYING STUDENT DOCUMENTS FROM find() QUERY -- \n")

for student in students:
    print(f'Student ID: {student["student_id"]}')
    print(f'First Name: {student["first_name"]}')
    print(f'Last Name: {student["last_name"]}')
    print("\n")


pam = {
    "student_id": "1010",
    "first_name": "pam",
    "last_name": "IStillDontUnderstand"
}

pam_student_id = student_collection.insert_one(pam).inserted_id

student_collection.insert_one(pam)

print(" -- INSERT STATEMENTS --")
print(f'Inserted student record {pam.get("first_name")} {pam.get("last_name")} into the students collection with document_id {pam_student_id}')

student_collection.delete_one(pam)

print("-- DISPLAYING STUDENT DOCUMENTS FROM find() QUERY -- \n")

for student in students:
    print(f'Student ID: {student["student_id"]}')
    print(f'First Name: {student["first_name"]}')
    print(f'Last Name: {student["last_name"]}')
    print("\n")
