# This part of the code prompts the user to enter two numbers for division and handles potential exceptions.
while True:
    try:
        a = float(input("Enter a number: "))
        b = float(input("Enter a number to divide by:"))
        result = a / b
        print(f"The answer is {result}.")
        break  # This break statement will exit the loop after a successful division
    except ValueError:
        print("Error: Please enter valid numeric values.")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

