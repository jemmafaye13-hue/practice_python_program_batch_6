# Prog05. endswith() check if the string end part matches the function parameter. Create a program that do the same functionality without using endswith() function.

text = input("Enter text: ")
suffix = input("Enter suffix to check: ")

# Slice the end of the text based on suffix length
if text[-len(suffix):] == suffix:
    print("Result: True")
else:
    print("Result: False")