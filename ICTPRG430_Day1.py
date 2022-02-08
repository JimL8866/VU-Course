# from turtle import Turtle, Screen
# from random import randint



# window = Screen()
# window.bgcolor("white")

# tim = Turtle()
# tim.color("red")
# tim.shape("turtle")
# tim.penup()
# tim.goto(0, 50)
# tim.pendown()

# jim = Turtle("turtle")
# jim.color("green")
# jim.penup()
# jim.goto(0, 100)
# jim.pendown()

# julie = Turtle("turtle")
# julie.color("black")
# julie.penup()
# julie.goto(0, 150)
# julie.pendown()

# alex = Turtle("turtle")
# alex.color("purple")
# alex.penup()
# alex.goto(0, 200)
# alex.pendown()


# for movement in range(100):
#     jim.forward(randint(1,5))
#     julie.forward(randint(1,5))
#     tim.forward(randint(1,5))
#     alex.forward(randint(1,5))



# window.exitonclick()


# class Shirt:
#     def __init__(self, colour, name, length):
#         self.colour = colour
#         self.name = name
#         self.length = length
#         self.wear = False

#     def put_on(self):
#         print("put on a shirt")
#         self.wear = True
    
#     def take_off(self):
#         print("take off your shirt")
#         self.wear = False


# my_shirt = Shirt("black", "monday", "medium")
# my_shirt.put_on()
# print(my_shirt.wear)
# print(id(my_shirt))
# my_shirt.colour = "green"
# print(id(my_shirt))

# child_shirt = Shirt("purple", "tuesday", "small")
# child_shirt.take_off()
# print(child_shirt.wear)
# print(id(child_shirt))
# child_shirt.colour = "red"
# print(id(child_shirt))

# list is mutable
# my_list = [1, 2, 3, 4]
# print(id(my_list))

# my_list.append(5)
# print(id(my_list))

# my_num_list = [1, 2, 3, 4]
# print(my_num_list)
# print(id(my_num_list))
# my_num_list_1 = my_num_list
# print(id(my_num_list_1))
# my_num_list.append(10)
# print(my_num_list)
# print(id(my_num_list))
# print(id(my_num_list_1))

# # string is unmutable so has to create a new object
# my_string = "hello"
# print(id(my_string))
# my_string = "hello" + "world"
# print(my_string)
# print(id(my_string))

################################################################################################
class Car:
    def __init__(self, speed, colour) -> None:
        self.speed = speed
        self.colour = colour

honda = Car(150, "red")
toyota = Car(220,"blue")
bmw = Car(250, "yellow")

print(honda.speed)
print(toyota.speed)
print(bmw.speed)

honda.speed = 1000
print(honda.speed)


class Students:
    def __init__(self, *args, **kwargs) -> None:
        print(args, kwargs)


jim = Students("Jim", 25, "Chinese", shirt= "blue")
alex = Students("Alex", 30 , "American", shirt="red")
julie = Students("Julie", 28, "Australian", shirt="purple")
