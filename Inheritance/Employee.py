class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

emp = Employee("Siddhi", 30000)

print("Name:", emp.name)
print("Salary:", emp.salary)