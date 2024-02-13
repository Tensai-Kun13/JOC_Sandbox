def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

# x = int(input("Input a number: "))
# y = int(input("Input another number to add to the first: "))
#
# print(f"The sum of your entered numbers is: {add(x, y)}")
#
# i = int(input("Input a number: "))
# j = int(input("Input another number to be multiplied with the first: "))
#
# print(f"The product of your 2 numbers is: {multiply(i, j)}")


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

def calculate_total(meal, tax_rate, tip_rate):
    return meal + (meal * tax_rate) + (meal * tip_rate)

def hey(number):
    return number ** 2

def there(n):
    if n < 0:
        return 0
    return 2 ** n

def are_we(repeat, phrase):
    for i in range(repeat):
        print(f"Are we {phrase} yet?", end = " ")
    print()

def main():
    print("4 is even:", is_even(4))
    print("5 is even:", is_even(5))
    print("Total should be $66.85:", calculate_total(53.48, .07, .18))
    print("hey(5)", hey(5) == 25)
    print("hey(0)", hey(0) == 0)
    print("hey(-3)", hey(-3) == 9)
    print("there(5)", there(5) == 32)
    print("there(0)", there(0) == 1)
    print("there(3)", there(3) == 8)
    print("there(-2)", there(-2) == 0)
    print("there(-6)", there(-6) == 0)
    are_we(2, "there")
    are_we(3, "50")
    are_we(1, "")
    are_we(0, "hey!")

main()