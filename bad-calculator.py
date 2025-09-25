# Coding Principles Violated:
# DRY:
#   The code repeats itself a lot. Each operation has one function for the math
#   and another one just for input and printing, instead of reusing code.
#   Input handling is written out four separate times instead of being done once.
#
# Single Responsibility:
#   The functions are doing too many things at once. For example, add_numbers
#   both asks for input and does the math. The main function also takes care of
#   the menu, input, and running everything all in one place.
#
# Clean Code:
#   There’s no error handling at all, so dividing by zero will crash the program.
#   Variable names are not descriptive, comments are basically missing, and the
#   overall structure is messy and harder to follow.



def add(x, y):
    return x + y

def add_numbers():
    a = float(input("Enter first number for add: "))
    b = float(input("Enter second number for add: "))
    print("Result:", add(a, b))

def subtract(x, y):
    return x - y

def subtract_numbers():
    a = float(input("Enter first number for subtract: "))
    b = float(input("Enter second number for subtract: "))
    print("Result:", subtract(a, b))

def multiply(x, y):
    return x * y

def multiply_numbers():
    a = float(input("Enter first number for multiply: "))
    b = float(input("Enter second number for multiply: "))
    print("Result:", multiply(a, b))

def divide(x, y):
    return x / y   # no error handling for divide by zero

def divide_numbers():
    a = float(input("Enter first number for divide: "))
    b = float(input("Enter second number for divide: "))
    print("Result:", divide(a, b))

# main runs everything at once
def main():
    while True:
        print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Quit")
        choice = input("Enter choice: ")

        if choice == "1":
            add_numbers()
        elif choice == "2":
            subtract_numbers()
        elif choice == "3":
            multiply_numbers()
        elif choice == "4":
            divide_numbers()
        elif choice == "5":
            break
        else:
            print("wrong input")
    print("done")

main()