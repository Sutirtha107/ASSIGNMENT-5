StudentMarks = {
    "Alice" : 85,
    "Rohit" : 90,
    "Rahul" : 87
}

name = input("Enter the student's name: ")

if name in StudentMarks:
    print(f"{name}'s marks: {StudentMarks[name]}")

else: 
    print("Student not found.")
