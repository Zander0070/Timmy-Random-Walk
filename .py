import turtle
import random
from turtle import Screen

dark_colors = [
    "black",
    "darkblue",
    "darkgreen",
    "darkred",
    "darkmagenta",
    "darkcyan",
    "indigo",
    "maroon",
    "navy",
    "purple",
    "brown",
    "slateblue",
    "seagreen",
    "darkslategray",
    "darkolivegreen",
    "midnightblue",
    "firebrick",
    "saddlebrown",
    "darkgoldenrod",
    "darkviolet"
]


Random_angles = [90,180,270]

tutle = turtle.Turtle()
tutle.shape("turtle")
tutle.color("green")



def Moveforward():
    forwardMovement = random.randint(-75,75)
    tutle.forward(forwardMovement)
def Rotate(Sides):
    #total = 360 / Sides
    leftMovement = random.randint(0,2)
    tutle.left(Random_angles[leftMovement])
    #tutle.speed(1000)
sides = 2

RandomMoveSet = random.randint(50,100)
tutle.speed(5000)
tutle.pensize(width=20)
for I in range (RandomMoveSet):
    #sides = sides + 1
        Moveforward()
        Rotate(sides)
        randomColour = random.randint(0,15)
        tutle.color(dark_colors[randomColour])



My_screen = Screen()
My_screen.listen()

My_screen.onkey(Moveforward,"w")
My_screen.onkey(Rotate,"a")



Screen().exitonclick()
