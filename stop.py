# draw a stop sign

import turtle

turtle.shape("turtle")
turtle.color("red")
turtle.pensize(3)
turtle.speed(3)

def rectangle(width, length):
    for i in range(4):
        if i % 2 == 0:
            turtle.forward(width)
        else:
            turtle.forward(length)

        turtle.right(90)

def octagon(length):
    for i in range(8):
        turtle.forward(length)
        turtle.left(45)

def stop(length):
    octagon(length)
    turtle.penup()
    turtle.forward(length * 3/8)
    turtle.pendown()
    rectangle(length / 5, length * 2)

stop(100)

turtle.Screen().exitonclick()