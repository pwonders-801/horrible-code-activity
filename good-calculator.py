"""
Calculator Program - Good Version
Coding Principles Demonstrated:
1. KISS
2. DRY
3. Single responsibility
"""

#Simple calculator class with basic arithmetic operations.
class Calculator:

  #Returns the sum of x and y.
  def add(self, x, y):
    return x + y

  #Returns the difference of x and y.
  def subtract(self, x, y):
    return x - y

  #Returns the product of x and y.
  def multiply(self, x, y):
    return x * y

  #Returns the quotient of x and y. Handles divide by zero error.
  def divide(self x, y):
    if y == 0:
      raise ValueError("You cannot divide by 0.")
    return x / y

#Handles user input and calculator execution
def main(): 
  calc = Calculator()

#KISS: Use a straightforward loop with clear user prompts.
while True:
  try:
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))
    operator = input("Options:\n+ for addition\n- for subtraction\n* for multiplication\n"
                      "/ for division\nexit to quit\nEnter a command: ")
    
    if operator == "exit":
      print("You have exited the program.")
      break

    #DRY: Avoid repeating logic by mapping the operators to functions.
    operations = {
      "+": calc.add,
      "-": calc.subtract,
      "*": calc.multiply,
      "/": calc.divide
    }

    #Handles function calls and output. Handles any errors caused by upsupported input.
    if operator in operations:
      result = operations[operator](x, y)
      print(f"Result: {result}\n")
    else:
      print("Invalid operator.\n")
      
  except ValueError as e:
    print(f"Error: {e}\n")


if __name__ == "__main__":
  main()
