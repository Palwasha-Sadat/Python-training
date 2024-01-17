# Open a file 'writeFile' in write ('w') mode
writeFile = open('output.txt', 'w')

# Text to write to the file
toLog = "This is some text to write to the file."

# Write the text to the file
writeFile.write(toLog)

# Close the file to save changes and release system resources
writeFile.close()
