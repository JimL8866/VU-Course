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

###################################################################

# class MyList:
#     def __init__(self, mylist):
#         self.mylist = mylist

#     def display(self):
#         return self.mylist

#     def display_item(self):
#         for item in self.mylist:
#             print(item)


# my_list = MyList([1, 2, 3, 4])
# print(my_list.display())
# my_list.display_item()


# class MyDict:
    
#     def __init__(self, **kwargs):
#         self.mydictionary = kwargs

#     def display(self):
#         return self.mydictionary

#     def display_item(self):
#         for (i, v) in self.mydictionary.items():
#             print(i, v)


# my_dictionary = MyDict(name="jim", age="35", mobile="0430")
# print(my_dictionary.display())
# my_dictionary.display_item()

############################################################################
# import random
# random.randint(1,10)

# print(random.randint.__doc__)

##################################################
class Book:
    """
     A class to represent a book.
     
     Attributes
    ----------
    title : str
        The title of the book
    author : str
        The author of the book
    
    Methods
    -------
    display():
        Prints the book's title and author.
    """
    
    def __init__(self, title, author):
        """
         Constructs all the necessary attributes for the book object.

        Args:
            self (undefined): instance/object of the Book class
            title (undefined): instance variable named "title"
            author (undefined): instance variable named "author"

        """
        self.title = title
        self.author = author

    def display(self):
        """
        instance method used to display two instance variables: "title", "author".
        
        """
        print(f"This book is called {self.title}.")
        print(f"The author of this book is {self.author}")


book = Book("Welcome to Australia", "JL")
book.display()