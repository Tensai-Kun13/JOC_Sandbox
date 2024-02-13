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
    # upperStr = string.upper()
    # remove_3rd_char = remove_ith_character(upperStr, 2)
    # remove_3rd_last = remove_ith_character(remove_3rd_char, -3)
    # reversed_final = remove_3rd_last[::-1]

    # Simpler solution
    string = string.upper()
    string = string[0:2] + string[3:-3] + string[-2:]

    return string

def count_e(strings):
    e_count = 0
    # Simpler solution
    for word in strings:
        e_count += word.upper().count("E")
    #     for letter in word:
    #         if letter == "e" or letter == "E":
    #             e_count += 1

    return e_count

def count_vowels(strings):
    vowel_count = 0
    for word in strings:
        upper = word.upper()
        for vowel in "AEIOU":
            vowel_count += upper.count(vowel)
        # for letter in word_upper:
        #     if letter == "A" or letter == "E" or letter == "I" or letter == "O" or letter == "U":
        #         vowel_count += 1

    return vowel_count


def main():
    print(mangle("hellothere"))
    print(mangle("42 degrees Celsius"))
    print(mangle("eeeeeee"))
    print(count_e(["hi", "hello", "EEK!"]))
    print(count_vowels(["hi", "hello", "OOF!"]))

main()