class Car:
    driver = "Tom"

    def __init__(self, speed):
        self.speed = speed

    def display(self):
        print(f"The car speed is {self.speed}")


car1 = Car(100)
car2 = Car(120)
car1.display()
car2.display()
print(car1.driver)
print(car2.driver)

################################################################################
class Driver:
    demerit = 12
    def __init__(self):
        pass



name = Driver()
print(Driver.demerit)
print(name.demerit)
print(id(Driver.demerit))
print(id(name.demerit))
name.demerit = 9
print(name.demerit, Driver.demerit)
print(id(name.demerit), id(Driver.demerit))