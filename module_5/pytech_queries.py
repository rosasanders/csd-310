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

print(" -- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY -- \n")

doc = student_collection.find_one({"student_id": "1007"})
print(f'Student ID: {doc["student_id"]}')
print(f'First Name: {doc["first_name"]}')
print(f'Last Name: {doc["last_name"]}')
print("\n")