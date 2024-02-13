def pyramid(char, number):
    for i in range(number):
        print(char * (i + 1))

pyramid("x", 10)