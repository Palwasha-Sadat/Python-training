import sys  # Import the sys module to use it later (not used in this specific code).

# Assuming 'c:\log.txt' is the path to your log file
log_path = r"c:\log.txt"  # Define the path to the log file using a raw string (r prefix).

try:
    with open(log_path, "r") as log:  # Attempt to open the log file in read mode using a 'with' statement.
        print(log.read())  # Read and print the contents of the log file.
except FileNotFoundError:  # Handle the FileNotFoundError exception if the file is not found.
    print(f"Log file '{log_path}' not found.")  # Print an error message when the file is not found.
except Exception as e:  # Handle any other exceptions that may occur and capture the exception details.
    print(f"An error occurred: {e}")  # Print an error message with details if any other exception occurs.
