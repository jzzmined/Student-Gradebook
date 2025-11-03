gradebook = {"Andrea": 85,"Erich": 95, "Miguel": 75,"Jasmine": 90,"Chase": 89}

print("---STUDENT GRADEBOOK SYSTEM---")

print("Student Gradebook: ")
for student, grade in gradebook.items():
    print(f"{student} -> {grade}")

print("\n")

search_name = input("Search for Student: ")
if search_name in gradebook:
    print(f"{search_name}'s grade is: {gradebook[search_name]}")
else:
    print("Student not found.")
print("\n")

update_name = input("Enter student name to update grade: ")

if update_name in gradebook:
    old_grade = gradebook[update_name]
    new_grade = int(input(f"Enter new grade for {update_name}: "))
    print(f"Updating grade: {update_name} -> {old_grade} to {new_grade}")
    gradebook[update_name] = new_grade
else:
    print("Student not found.")

print("\n")

print("Updated Gradebook: ")
for student, grade in gradebook.items():
    print(f"{student} -> {grade}")

print("\n")

top_student = None
highest_grade = -1

for student, grade in gradebook.items():
    if grade > highest_grade:
        highest_grade = grade
        top_student = student

print(f"Top Student: {top_student} with grade of {highest_grade}")
