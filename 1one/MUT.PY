class Student:
    def __init__(self, regno, name, cgpa):
        self.regno = regno
        self.name = name
        self.cgpa = cgpa

    def get_regno(self):
        return self.regno

    def set_regno(self, regno):
        self.regno = regno

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_cgpa(self):
        return self.cgpa

    def set_cgpa(self, cgpa):
        self.cgpa = cgpa

    def generate_report(self):
        report = f"Registration Number: {self.regno}\nName: {self.name}\nCGPA: {self.cgpa}"
        return report


# Creating two Student objects
student1 = Student("001", "John Doe", 3.8)
student2 = Student("002", "Jane Smith", 3.9)

# Displaying reports
print("Student 1 Report:")
print(student1.generate_report())
print("\nStudent 2 Report:")
print(student2.generate_report())
