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
    return number * number

def there(n):
    if n >= 0:
        return pow(2, n)
    else:
        return 0

def are_we(repeat, phrase):
    print(f"Are we {phrase} yet? " * repeat)

def main():
    are_we(2, "there")
    are_we(3, "50")
    are_we(1, "")
    are_we(0, "hey!")

main()