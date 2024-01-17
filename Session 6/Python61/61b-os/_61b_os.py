import os

# Prompt the user to enter the name of the folder they want to create
dirName = input("Enter the name of the folder you want to create: ")

# Check if the directory already exists
if not os.path.exists(dirName):
    # Create the directory
    os.mkdir(dirName)
    print(f"Directory '{dirName}' created.")
else:
    print(f"Directory '{dirName}' already exists.")

# Exercise
# Print the current working directory
print("Current directory:", os.getcwd())

# Change the directory to 'C:/Users'
os.chdir('C:/Users/palwa/Documents/')

# Print the new current working directory
print("New current directory:", os.getcwd())

# Uncomment the following lines to create a directory and remove it.
# os.makedirs('Arab')  # Create a directory and any necessary parent directories.
# os.makedirs('Arab/Sub-dir')  # Create directories with multiple levels of hierarchy.
# os.removedirs('Arab')  # Remove the directory 'Arab' and its parent directories if empty.
# print(os.listdir())  # Print the list of files and directories in the current directory.
