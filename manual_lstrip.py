Prog01. lstrip() remove the space characters at the beginning of the string. Create a program that do the same functionality without using lstrip() function.

text = input("Enter text: ")
start_index = 0

# Find the first index that is not a space
for i in range(len(text)):
    if text[i] != " ":
        start_index = i
        break

# Slice from that index to the end
print("Output:", text[start_index:])