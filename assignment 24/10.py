class Employee:
    def __init__(self, empid, name, salary):
        self.empid = empid
        self.name = name
        self.salary = salary

    def input_details(self):
        self.empid = int(input("Enter Employee ID: "))
        self.name = input("Enter Name: ")
        self.salary = float(input("Enter Salary: "))

    def display(self):
        print(f"ID: {self.empid}, Name: {self.name}, Salary: {self.salary}")

emp1 = Employee(0, "", 0.0)
emp1.input_details()
emp1.display()
