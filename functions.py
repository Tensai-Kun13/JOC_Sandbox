def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

x = int(input("Input a number: "))
y = int(input("Input another number to add to the first: "))

print(f"The sum of your entered numbers is: {add(x, y)}")

i = int(input("Input a number: "))
j = int(input("Input another number to be multiplied with the first: "))

print(f"The product of your 2 numbers is: {multiply(i, j)}")