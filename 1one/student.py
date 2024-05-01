class Employee:
    def __init__(self, name, empid, department, designation, experience, basic_pay):
        self.name = name
        self.empid = empid
        self.department = department
        self.designation = designation
        self.experience = experience
        self.basic_pay = basic_pay

    def net_salary(self):
        da = 0.1 * self.basic_pay
        hra = 0.05 * self.basic_pay
        epf = 0.05 * self.basic_pay
        tax = 0.1 * self.basic_pay
        return self.basic_pay + da + hra - epf - tax

    def __str__(self):
        return f"Name: {self.name}, Emp ID: {self.empid}, Department: {self.department}, " \
               f"Designation: {self.designation}, Experience: {self.experience} years, " \
               f"Basic Pay: {self.basic_pay}, Net Salary: {self.net_salary()}"


def main():
    employees = []

    while True:
        print("\nEmployee Payroll Management System")
        print("1. Add Employee")
        print("2. Display Employee Details")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter employee name: ")
            empid = input("Enter employee ID: ")
            department = input("Enter department: ")
            designation = input("Enter designation: ")
            experience = float(input("Enter experience (in years): "))
            basic_pay = float(input("Enter basic pay: "))
            employee = Employee(name, empid, department, designation, experience, basic_pay)
            employees.append(employee)
            print("Employee added successfully.")
        elif choice == '2':
            if not employees:
                print("No employees to display.")
            else:
                for emp in employees:
                    print(emp)
        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
