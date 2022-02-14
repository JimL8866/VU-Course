# class Employee:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# class Salary(Employee):
#     def __init__(self, rate, hour, *args):
#         self.rate = rate
#         self.hour = hour
#         super().__init__(*args)
#
#
# def total_salary(arg):
#     total = arg.rate * arg.hour
#     print(f"{arg.name}'s total salary is {total}. His gae is {arg.age}")
#
#
# alex_salary = Salary(40, 100, "alex", 30)
#
# total_salary(alex_salary)


# Polymorphism example

##############################################################################

# class Employee:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# class Salary:
#     def __init__(self, rate, hour, name, age):
#         self.rate = rate
#         self.hour = hour
#         self.employee = Employee(name, age)

#     def total_salary(self):
#         total = self.rate * self.hour
#         print(f"{self.employee.name}'s total salary is {total}. His gae is {self.employee.age}")


# alex_salary = Salary(50, 300, "alex", 30)

# alex_salary.total_salary()


# Composition example

##############################################################################


# class Employee:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# class Salary:
#     def __init__(self, rate, hour, employee):
#         self.rate = rate
#         self.hour = hour
#         self.employee = employee
#
#     def total_salary(self):
#         total = self.rate * self.hour
#         print(f"{self.employee.name}'s total salary is {total}. His gae is {self.employee.age}")
#
#
# alex = Employee("alex", 30)
#
# alex_salary = Salary(40, 352, alex)
#
# alex_salary.total_salary()
#
# # Aggregation example

##############################################################################

class BaseClass:
    def __init__(self):
        self.x = 10


class BaseClass2:
    def __init__(self, y):
        self.y = y

    def display(self):
        print(self.y.x)


obj1 = BaseClass()
obj2 = BaseClass2(obj1)
obj2.display()
