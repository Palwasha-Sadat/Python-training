import os

# Check if the 'log.old' file exists
if os.path.exists('log.old'):
    # If the file exists, delete it
    os.remove('log.old')
    print("The log_old file has been removed.")
else:
    # If the file doesn't exist, print a message indicating that there was no 'log.old' file to remove
    print("There was no log_old file to remove.")
