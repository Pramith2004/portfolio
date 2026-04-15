# Student Data Manager

students = []

# Input data for 5 students
for i in range(5):
    print(f"\nEnter details for student {i+1}:")
    name = input("Name: ")
    marks = float(input("Marks: "))
    
    student = {
        "name": name,
        "marks": marks
    }
    
    students.append(student)

# Calculate class average
total_marks = sum(student["marks"] for student in students)
average = total_marks / len(students)

# Find topper
topper = max(students, key=lambda x: x["marks"])

# Function to assign grade
def assign_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"

# Add grades to each student
for student in students:
    student["grade"] = assign_grade(student["marks"])

# Display results
print("\n--- Student Report ---")
for student in students:
    print(f"Name: {student['name']}, Marks: {student['marks']}, Grade: {student['grade']}")

print(f"\nClass Average: {average:.2f}")
print(f"Topper: {topper['name']} with {topper['marks']} marks")