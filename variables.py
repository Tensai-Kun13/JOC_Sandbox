import turtle

turtle.color("blue")
turtle.pensize(3)
size = 75

def back(len):
    turtle.penup()
    turtle.backward(len)
    turtle.pendown()

# forward helper function
def move(len):
    back(-1 * len)

# def triangle(size):
#     for i in range(3):
#         turtle.forward(size)
#         turtle.left(120)
#
# def square(size):
#     for i in range(4):
#         turtle.forward(size)
#         turtle.left(90)

def polygon(numSides, size):
    angle = 360 / numSides
    for i in range(numSides):
        turtle.forward(size)
        turtle.left(angle)

def spiral (len, angle):
    for i in range(len, 5, -5):
        turtle.forward(i)
        turtle.right(angle)

# polygon(3, 75)
# back(75)
# polygon(3, 50)
# back(150)
# polygon(3, 120)
#
# back(100)
# polygon(4, 50)
# back(125)
# polygon(4, 75)

# for n in range(3, 10):
#     move(50) # forward
#     polygon(n, 100 / n)
#     back(50)
#     turtle.right(360 / 7)

spiral(75, 45)
move(150)
turtle.color("red")
spiral(100, 90)