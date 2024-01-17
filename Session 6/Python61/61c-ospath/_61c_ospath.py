import os

# Check if the 'log.txt' file exists
if os.path.exists('log.txt'):
    # Open the file in append mode
    with open('log.txt', 'a') as writeFile:
        toLog = input("What do you want to write to the log? ")
        writeFile.write("\n" + toLog)
else:
    # 'log.txt' does not exist, open it in write mode
    with open('log.txt', 'w') as writeFile:
        toLog = input("What do you want to write to the log? ")
        writeFile.write(toLog)
