import math

def add(num1, num2):
   return num1 + num2

def subtract(num1, num2):
   return num1 - num2

def multiply(num1, num2):
   return num1 * num2

def divide(num1, num2):
   return num1 / num2

def sqrt(num1):
   return math.sqrt(num1)

def absolute(num1):
   return abs(num1)

def main():
   operation = input('What do you want to do?(+, -, *, sqrt, abs,  or /): ')
   if operation != '+' and operation != '-' and operation != '*' and operation != '/' and operation != 'sqrt' and operation != 'abs': 
      print('Your request is invalid')
   else:
      if operation == 'abs':
         num1 = float(input('Enter a number: '))
         print(abs(num1))
      else:
       if operation == "sqrt":
         num1 = float(input('Enter a number: '))
         print(sqrt(num1))
       else:
        num1 = float(input('Enter First Number: '))
        num2 = float(input('Enter Second Number: '))
        if operation == '+':
         print(add(num1, num2))
        elif operation == '-':
         print(subtract(num1, num2))
        elif operation == '*':
         print(multiply(num1, num2))
        elif operation == '/':
         print(divide(num1, num2))
        elif operation == "sqrt":
         print(sqrt(num1))
main()
