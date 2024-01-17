toLog = input("What do you want to write to the log? ")

# Use a 'with' statement to open 'log.txt' in write ('w') mode
with open('log.txt', 'w') as writeFile:
    writeFile.write(toLog)
