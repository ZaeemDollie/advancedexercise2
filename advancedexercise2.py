# -------------------------------------------
# Advanced Python Challenge: Exercise 02 Operators and Conditionals
# -------------------------------------------

# Overview:
# This exercise challenges your understanding of Python operators, conditionals, and input handling.
# Complete each section with the required logic, using good variable names and adding comments where necessary.

# -------------------------------------------
# Question 1: Multi-Step Arithmetic Operations
# -------------------------------------------

# Task:
# Use compound arithmetic operators to modify values of a, b, and c.
# Then calculate the square root of the sum of their squares.
# Tip: Use the math module.

import math

# Start with some base values
a = 5
b = 10
c = 7

# TODO: Add 3 to a using +=
a += 3
print(a)
# TODO: Multiply b by 2 using *=
b *= 2
print(b)
# TODO: Modulo c by 4 using %=
c %= 4
print(c)
# TODO: Calculate the square root of (a^2 + b^2 + c^2)
print(math.sqrt(a**2 +b**2 + c**2))
# TODO: Print the final result rounded to 2 decimal places
print(result :=round(math.sqrt(a**2 +b**2 + c**2), 2))


# -------------------------------------------
# Question 2: Complex Conditional Evaluation
# -------------------------------------------

# Task:
# Ask the user to input three integers (x, y, z).
# Then evaluate and print whether:
# - x is even
# - y is positive
# - z is between 10 and 50
# Use logical operators to combine the conditions.

# Tip: Use and/or to join conditions.

# TODO: Input x, y, z
x = int(input("Enter x: "))
y = int(input("Enter y: "))
z = int(input("Enter z: "))

# TODO: Create conditions:
#   is_even = True if x is even
#   is_positive = True if y > 0
#   is_in_range = True if z between 10 and 50
if x % 2 == 0:
    is_even = True
else:
    is_even = False
if y > 0:
    is_positive = True
else:
    is_positive = False
if 10 <= z <= 50:
    is_in_range = True
else:
    is_in_range = False
# TODO: Create final_condition = is_even and is_positive and is_in_range
if is_even and is_positive and is_in_range:
    final_condition = True
else:
    final_condition = False

# TODO: Print final_condition
print(final_condition)

# -------------------------------------------
# Question 3: Grading with Adjustments
# -------------------------------------------

# Task:
# Ask the user for their base score, then apply:
# - bonus points (+5)
# - late penalty (-10)
# Final score must not exceed 100 or drop below 0.
# Then assign a grade.

# Tip: Use min() and max() to constrain the score.

# TODO: Input score from user
score = int(input("Enter your base score: "))
# TODO: Apply adjustments
score += 5  # bonus points
score -= 10  # late penalty
# TODO: Clamp score between 0 and 100
score = max(0, min(score, 100))
# TODO: Use if-elif-else to determine grade and print it
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'


# -------------------------------------------
# Question 4: Advanced Calculator
# -------------------------------------------

# Task:
# Ask the user to input two numbers and an operation (+, -, *, /, %, **).
# Handle division/modulus by zero with error checking.
# Perform the operation and print the result.

# Tip: Use try-except and elif branches for each operation.

# TODO: Input num1, num2
input_num1 = int(input("Enter first number: "))
input_num2 = int(input("Enter second number: "))
# TODO: Input operation
operation = input("Enter operation (+, -, *, /, %, **): ")
# TODO: Match operation using if-elif
if operation == '+':
    result = input_num1 + input_num2
elif operation == '-':
    result = input_num1 - input_num2
elif operation == '*':
    result = input_num1 * input_num2
elif operation == '/':
    # TODO: Handle division by zero with try-except
    try:
        result = input_num1 / input_num2
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        result = None
elif operation == '%':
    # TODO: Handle modulus by zero with try-except
    try:
        result = input_num1 % input_num2
    except ZeroDivisionError:
        print("Error: Modulus by zero is not allowed.")
        result = None
elif operation == '**':
    result = input_num1 ** input_num2
else:
    print("Invalid operation.")
    result = None

# TODO: Print result
result = result if result is not None else "No result due to error."
print(f"Result: {result}")