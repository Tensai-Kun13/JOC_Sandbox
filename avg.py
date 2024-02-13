# Output the average of 10 numbers input by the user

total = 0

for i in range(10):
    total += int(input("Please input a number. "))

avg = total / 10
print(f"The average of the numbers you input is {avg}")