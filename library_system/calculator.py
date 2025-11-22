"""
Create a custom Python module named calculator.py that contains functions for basic arithmetic operations 
(addition, subtraction, multiplication, division).
Create functions add, subtract, multiply, and divide in the calculator.py module.
Import the calculator module into a separate Python script main.py 
and use its functions to perform arithmetic operations on numbers like 5 and 3.
"""

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b