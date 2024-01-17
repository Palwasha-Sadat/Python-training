# Use the 'with' statement to open 'log.txt' in write ('w') mode
with open('log.txt', 'w') as log_file:
    # Take user input
    toLog = input("What do you want to write to the log? ")

    # Write the user input to the file
    log_file.write(toLog)
    
# The 'with' block is exited, and the file is automatically closed
