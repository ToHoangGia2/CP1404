"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")


# When will a ValueError occur?
# ValueError occur when the entered number is not a number

# When will a ZeroDivisionError occur?
# ZeroDivisionError occur when the denominator number entered is 0

# Could you change the code to avoid the possibility of a ZeroDivisionError?
# you could add a while function to check if the user entered 0 and ask user to input again