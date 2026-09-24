class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, name, age, salary, department):
        super().__init__(name, age)  
        self.salary = salary
        self.department = department

emp = Employee("Siddhi", 20, 30000, "IT")
print(emp.name)
print(emp.age)
print(emp.salary)
print(emp.department)