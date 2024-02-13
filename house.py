import turtle

turtle.shape("turtle")
turtle.color("blue")
turtle.pensize(3)
turtle.speed(3)

size = 100

def square(size):
    for i in range(4):
        turtle.forward(size)
        turtle.right(90)

def triangle(size):
    for i in range(3):
        turtle.forward(size)
        turtle.left(120)

def house(size):
    triangle(size)
    square(size)

house(size)

turtle.Screen().exitonclick()