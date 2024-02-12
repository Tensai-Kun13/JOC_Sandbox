import turtle

turtle.color("blue")
turtle.pensize(3)
size = 75

def triangle(size):
    for i in range(3):
        turtle.forward(size)
        turtle.left(120)

def square(size):
    for i in range(4):
        turtle.forward(size)
        turtle.left(90)

def back(len):
    turtle.penup()
    turtle.backward(len)
    turtle.pendown()

triangle(75)
back(75)
triangle(50)
back(150)
triangle(120)

back(100)
square(50)
back(150)
square(75)