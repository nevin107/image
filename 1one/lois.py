# Define the lloyd, alice, and tyler dictionaries
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

# Create a list called students containing lloyd, alice, and tyler
students = [lloyd, alice, tyler]

# Function to calculate average
def average(numbers):
    total = sum(numbers)
    total = float(total)
    return total / len(numbers)

# Function to calculate weighted average
def get_average(student):
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])
    return 0.1 * homework + 0.3 * quizzes + 0.6 * tests

# Function to get letter grade
def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Function to calculate class average
def get_class_average(students):
    results = []
    for student in students:
        results.append(get_average(student))
    return average(results)

# Print each student's data
for student in students:
    print(student["name"])
    print("Homework:", student["homework"])
    print("Quizzes:", student["quizzes"])
    print("Tests:", student["tests"])

# Test get_letter_grade function
lloyd_grade = get_letter_grade(get_average(lloyd))
print("Lloyd's grade:", lloyd_grade)

# Print class average and class letter grade
class_avg = get_class_average(students)
class_letter_grade = get_letter_grade(class_avg)
print("Class average:", class_avg)
print("Class letter grade:", class_letter_grade)
