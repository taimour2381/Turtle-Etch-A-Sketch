from turtle import Turtle, Screen
import random
tim = Turtle()
screen = Screen()


def turtle_forward():
    tim.forward(1)


def turtle_backward():
    tim.backward(1)


def turtle_turn_right():
    tim.right(1)


def turtle_turn_left():
    tim.left(1)


def turtle_color():
    clr = random.choice(["red", "yellow", "brown", "orange", "purple"])
    tim.color(clr)


def turtle_shape():
    shp = random.choice(["arrow", "turtle", "circle", "square", "triangle", "classic"])
    tim.shape(shp)


def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(fun=turtle_color, key="1")
screen.onkey(fun=turtle_shape, key="2")
screen.onkeypress(fun=turtle_forward, key="w")
screen.onkeypress(fun=turtle_backward, key="s")
screen.onkeypress(fun=turtle_turn_left, key="a")
screen.onkeypress(fun=turtle_turn_right, key="d")
screen.exitonclick()
