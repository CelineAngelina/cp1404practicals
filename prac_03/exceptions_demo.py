"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    There will be a ValueError when the input for numerator and denominator is not a valid integer.
2. When will a ZeroDivisionError occur?
    ZeroDivisionError occurs when the input of denominator is 0 (zero).
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    Yes, by using 'while' loop, so when the user enter 0, it will print an error message and prompt the user to enter a valid (non-zero) integer again.
"""

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
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
print("Finished.")