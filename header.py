text = "Hello, World!"
char = "~"

def header(surround, text):
    print(surround * (len(text) + 4))
    print(surround, text, surround)
    print(surround * (len(text) + 4))

header("*", "Hello, World!")
header("!", "Python Rocks")
header("+", "Coders 4 EVER")