Prog02. removeprefix() remove the characters at the beginning of the string that matches the function parameter. Create a program that do the same functionality without using removeprefix() function.

text = input("Enter text: ")
prefix = input("Enter prefix to remove: ")

# Check if the text starts with the prefix characters
if text[:len(prefix)] == prefix:
    print("Output:", text[len(prefix):])
else:
    print("Output:", text)