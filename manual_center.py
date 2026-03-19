# Prog07. center() add space characters at the beginning and at the end of the string to print the string at the center. Create a program that do the same functionality without using center() function.

text = input("Enter text: ")
total_len = int(input("Enter total length: "))

while len(text) < total_len:
    text = " " + text  # Add to front
    if len(text) < total_len:
        text = text + " "  # Add to back

print(f"'{text}'")
