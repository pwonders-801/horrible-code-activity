"""
Calculator Program - Good Version
Coding Principles Demonstrated:
1. KISS
2. DRY
3. Single responsibility
"""
class Calculator:
  def add(self, x, y):
    return x + y
  def subtract(self, x, y):
    return x - y
  def multiply(self, x, y):
    return x * y
  def divide(self x, y):
    if y == 0:
      raise ValueError("You cannot divide by 0.")
    return x / y
    
def main(): 
  calc = Calculator()

while True:
  try:
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))
    operator = input("Options:\n+ for addition\n- for subtraction\n* for multiplication\n"
                      "/ for division\nexit to quit\nEnter a command: ")
    if operator == "exit":
      print("You have exited the program.")
      break

    operations = {
      "+": calc.add,
      "-": calc.subtract,
      "*": calc.multiply,
      "/": calc.divide
    }

    if operator in operations:
      result = operations[operator](x, y)
      print(f"Result: {result}\n")
    else:
      print("Invalid operator.\n")
  except ValueError as e:
    print(f"Error: {e}\n")


if __name__ == "__main__":
  main()
