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

def main():
    prompt = "Please enter a number (enter \"0\" when finished): "
    entry = input(prompt)
    responses = []

    while entry != "0":
        responses.append(int(entry))
        entry = input(prompt)

    print(sorted(responses))
    print(f"The total of all input numbers is: {sum(responses)}")
    print(f"The average of all input numbers is: {sum(responses) / len(responses)}")

main()
