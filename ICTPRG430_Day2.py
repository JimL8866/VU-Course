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
