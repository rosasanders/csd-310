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
    
student_collection.update_one({"student_id": "1007"}, {"$set": {"last_name": "Smith"}})

doc = student_collection.find_one({"student_id": "1007"})

print(f" -- DISPLAYING STUDENT DOCUMENT 1007 -- \n\n" +
      f"Student ID: {doc['student_id']} \n" +
      f"First Name: {doc['first_name']} \n" +
      f"Last Name: {doc['last_name']} \n")
