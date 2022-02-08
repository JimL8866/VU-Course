from turtle import Turtle, Screen
from random import randint



window = Screen()
window.bgcolor("white")

tim = Turtle()
tim.color("red")
tim.shape("turtle")
tim.penup()
tim.goto(0, 50)
tim.pendown()

jim = Turtle("turtle")
jim.color("green")
jim.penup()
jim.goto(0, 100)
jim.pendown()

julie = Turtle("turtle")
julie.color("black")
julie.penup()
julie.goto(0, 150)
julie.pendown()

alex = Turtle("turtle")
alex.color("purple")
alex.penup()
alex.goto(0, 200)
alex.pendown()


for movement in range(100):
    jim.forward(randint(1,5))
    julie.forward(randint(1,5))
    tim.forward(randint(1,5))
    alex.forward(randint(1,5))



window.exitonclick()