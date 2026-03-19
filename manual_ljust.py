# Prog06. ljust() add space characters at the end of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using ljust() function.

text = input("Enter text: ")
total_len = int(input("Enter total length: "))

# Keep adding spaces until the length is reached
while len(text) < total_len:
    text += " "

print(f"'{text}'")

