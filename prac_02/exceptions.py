"""
CP1404/CP5632 - Practical
Exceptions
"""
# 1. When will a ValueError occur?
# When a value is entered that is not an integer.
# 2. When will a ZeroDivisionError occur?
# When trying to divide by zero, which is undefined.
# 3. Could you change the code to avoid the possibility of a ZeroDivisionError?

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Cannot divide by zero!")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
