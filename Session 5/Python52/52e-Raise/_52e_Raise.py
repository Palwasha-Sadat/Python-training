# Prompt the user to enter two numbers for division and handle potential exceptions.

a = float(input("Enter a number: "))  # Prompt the user to enter the first number and convert it to a floating-point number.
b = float(input("Enter a number to divide by: "))  # Prompt the user to enter the second number for division.

try:
    result = a / b  # Attempt to perform the division operation.
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")  # Raise a custom ZeroDivisionError if the denominator is zero.
    print(f"The answer is {result}.")  # Display the result of the division.
except ZeroDivisionError as e:
    print(f"Error: {e}")  # Handle a ZeroDivisionError and display a custom error message.
except ValueError:
    print("Error: Please enter valid numeric values.")  # Handle a ValueError if the user doesn't enter valid numeric values.
except:
    print("An unexpected error occurred.")  # Handle any other unexpected errors.
else:
    print("You successfully used the division feature in Python")  # If no exceptions occurred, display a success message.
finally:
    print("Thank you for playing.")  # This block always executes, providing a closing message.
