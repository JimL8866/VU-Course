# class Car:
#     driver = "Tom"

#     def __init__(self, speed):
#         self.speed = speed

#     def display(self):
#         print(f"The car speed is {self.speed}")


# car1 = Car(100)
# car2 = Car(120)
# car1.display()
# car2.display()
# print(car1.driver)
# print(car2.driver)

################################################################################
# class Driver:
#     demerit = 12
#     def __init__(self):
#         pass



# name = Driver()
# print(Driver.demerit)
# print(name.demerit)
# print(id(Driver.demerit))
# print(id(name.demerit))
# name.demerit = 9
# print(name.demerit, Driver.demerit)
# print(id(name.demerit), id(Driver.demerit))


#########################################################
# class Computer:
#     def __init__(self, name, value):
#         self.name = name
#         self.__value = value

#     def get_value(self):
#         print(self.__value)


# my_computer = Computer("Lenovo", 1000)
# # print(my_computer.__value)

# print(my_computer._Computer__value)

# my_computer.get_value()

#################################################
# class Phone:
#     def __init__(self, name, brand):
#         self.name = name
#         self.__brand = None

#     def set_value(self):
#         self.__brand = "iphone"

#     def get_value(self):
#         return self.__brand


# my_phone = Phone("Jim's phone", "iphone")
# my_phone.set_value()
# print(my_phone.get_value())


##################################################

class Appliance:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour

    def func(self):
        print(f"{self.name} can cooking meals")


class Microwave(Appliance):
    def __init__(self, value, weight):
        super().__init__("LG", "1000")
        self.value = value
        self.weight = weight

    def func(self):
        Appliance.func(self)
        print(f"{self.name} can make meals hot")


my_fridge = Microwave("500", "100KG")
my_fridge.func()
print(my_fridge.name)
print(my_fridge.colour)