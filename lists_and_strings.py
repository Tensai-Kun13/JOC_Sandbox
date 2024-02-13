def list_mean(list):
    sum = 0
    for number in list:
        sum += number
    return sum / len(list)

def average():
    numbers = []
    for i in range(20):
        numbers.append(int(input("Please input a number: ")))

    print(f"The average (mean) of your list of numbers is: {list_mean(numbers)}")

def remove_ith_character(string, i):
    # Base case: if index is 0,
    # return string with first character removed
    if i == 0:
        return string[1:]

    temp_string = string
    if i < 0:
        temp_string = string[::-1]
        i *= -1
        i -= 1

    # Recursive case: return first character
    # concatenated with result of calling function
    # on string with index incremented by 1
    return temp_string[len(temp_string) * -1] + remove_ith_character(temp_string[1:], i - 1)

def mangle(string):
    upperStr = string.upper()
    remove_3rd_char = remove_ith_character(upperStr, 2)
    remove_3rd_last = remove_ith_character(remove_3rd_char, -3)
    reversed_final = remove_3rd_last[::-1]


    return reversed_final

def main():
    print(mangle("hellothere"))
    print(mangle("42 degrees Celsius"))
    print(mangle("eeeeeee"))

    # print(remove_ith_character("hellothere", -3))

main()