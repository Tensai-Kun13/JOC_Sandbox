# 1a
# i = 1
# while i < 6:
#     print(i)
#     i += 1

# 1b
# i = 2
# while i < 12:
#     print(i)
#     i += 3

# 1c
# i = -10
# while i < 1:
#     print(i, end=" ")
#     i += 2

# 1d
# i = 0
# while i < 4:
#     print("****")
#     i += 1

# 2
# text = "CSCI 150"
# i = 0
# while i < len(text):
#     print(text[i])
#     i += 1

# 3
# def sum(list):
#     total = 0
#     for item in list:
#         total += item
#     return total

def average_neg_evens(numbers):
    i = 0
    total = 0
    counter = 0
    while i < len(numbers):
        if numbers[i] < 0 and numbers[i] % 2 == 0:
            total += numbers[i]
            counter += 1
        i += 1
    return total / counter

def count_letter(strings, letter):
    i = 0
    letter = letter.upper()
    counter = 0
    while i < len(strings):
        tempString = strings[i].upper()
        counter += tempString.count(letter)
        i += 1
    return counter

def main():
    # prompt = "Please enter a number (enter \"0\" when finished): "
    # entry = input(prompt)
    # responses = []
    #
    # while entry != "0":
    #     responses.append(int(entry))
    #     entry = input(prompt)
    #
    # print(sorted(responses))
    # print(f"The total of all input numbers is: {sum(responses)}")
    # print(f"The average of all input numbers is: {sum(responses) / len(responses)}")

    # print(average_neg_evens([0, 1, 2, -2, -3, -4, 3, 4]))

    list = ["HELLO", "goodbye", "1234 Oooh!"]
    print(count_letter(list, "o"))

main()
