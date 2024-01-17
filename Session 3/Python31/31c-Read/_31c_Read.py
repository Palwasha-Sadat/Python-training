# Open the file 'jackets.txt' in read ('r') mode
workFile = open('jackets.txt', 'r')

# Read the first line of the file and store it in a variable
workFileFirstLine = workFile.readline()
# Print the first line
print(workFileFirstLine)

# Read the second line of the file and store it in a variable
workFileSecondLine = workFile.readline()
# Print the second line
print(workFileSecondLine)

# Close the file when you're done with it
workFile.close()
