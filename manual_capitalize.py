# Prog09. capitalize() makes the first letter of the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using capitalize() function.

text = input("Enter text: ")
if len(text) > 0:
    first_char = text[0]
    # Make first char upper if needed
    if 'a' <= first_char <= 'z':
        first_char = chr(ord(first_char) - 32)

    # Make rest of the string lower
    rest = ""
    for char in text[1:]:
        if 'A' <= char <= 'Z':
            rest += chr(ord(char) + 32)
        else:
            rest += char
    print("Result:", first_char + rest)