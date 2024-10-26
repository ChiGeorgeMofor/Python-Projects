# Define student dictionaries
lloyd = {  
    "name": "Lloyd", 
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],  
    "tests": [75.0, 90.0] 
}  
          
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}

tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

# Function to calculate average of a list of numbers
def average(numbers):
    return sum(numbers) / len(numbers)

# Function to get the average for a student
def get_average(student):
    homework_avg = average(student["homework"])
    quizzes_avg = average(student["quizzes"])
    tests_avg = average(student["tests"])
    return 0.1 * homework_avg + 0.3 * quizzes_avg + 0.6 * tests_avg

# Function to get the class average
def get_class_average(class_list):
    results = []
    for student in class_list:
        student_avg = get_average(student)
        results.append(student_avg)
    return average(results)

# List of students
students = [lloyd, alice, tyler]

# Printing average for each student and the class average
for student in students:
    print(f"{student['name']}'s average: {get_average(student):.2f}")

print(f"Class average: {get_class_average(students):.2f}")
