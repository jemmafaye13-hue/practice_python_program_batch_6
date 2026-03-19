# Prog04. isupper() check if all characters of the string is on upper case. Create a program that do the same functionality without using isupper() function.

text = input("Enter text: ")
is_all_upper = True

for char in text:
    if 'a' <= char <= 'z':
        is_all_upper = False
        break

print("Is all upper?", is_all_upper)