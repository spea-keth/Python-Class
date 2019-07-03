#unordered but changeable
#key: value
person_data = dict()
student = {"name" : "John Doe",
           "age": 12,
           "gender": "Male"}
print(student)

#Accessing items in a dictionary
print(student.get("age"))
print(student["age"])

#Adding key pairs
student['year'] = 1899
print(student['year'])

#Assignment:
    #1. Looping a dictionary
    #2. Finding dictionary length