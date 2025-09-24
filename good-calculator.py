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
  
