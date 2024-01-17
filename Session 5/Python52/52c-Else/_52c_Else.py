# This code creates an infinite loop to repeatedly prompt the user for an order number.
while True:
    try:
        order = int(input("Enter the order to execute: "))  # Prompt the user to enter an order number and convert it to an integer.
    except ValueError:
        print("That's not a valid order number!")  # If the input is not a valid integer, this error message is displayed.
    else:
        print(f"Execute order {order}.")  # If the input is a valid integer, this message is displayed, indicating the order to execute.
    finally:
        print("Try to write a valid number")  # This message is always displayed, regardless of whether an exception occurred or not.
