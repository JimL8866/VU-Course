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


class Shirt:
    def __init__(self, colour, name, length):
        self.colour = colour
        self.name = name
        self.length = length
        self.wear = False

    def put_on(self):
        print("put on a shirt")
        self.wear = True
    
    def take_off(self):
        print("take off your shirt")
        self.wear = False


my_shirt = Shirt("black", "monday", "medium")
my_shirt.put_on()
print(my_shirt.wear)
print(id(my_shirt))
my_shirt.colour = "green"
print(id(my_shirt))

child_shirt = Shirt("purple", "tuesday", "small")
child_shirt.take_off()
print(child_shirt.wear)
print(id(child_shirt))
child_shirt.colour = "red"
print(id(child_shirt))
