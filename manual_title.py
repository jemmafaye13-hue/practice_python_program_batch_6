# Prog10. title() makes all first letter of each word in the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using title() function.

text = input("Enter text: ")
result = ""
new_word = True # Flag to capitalize the next letter

for char in text:
    if char == " ":
        result += " "
        new_word = True
    elif new_word:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
        new_word = False
    else:
        if 'A' <= char <= 'Z':
            result += chr(ord(char) + 32)
        else:
            result += char
        new_word = False

print("Title case:", result)