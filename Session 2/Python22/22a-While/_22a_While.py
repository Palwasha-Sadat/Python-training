# Ask the user to input their guess for the capital of Germany
capitalGuess = input("What is the capital of Germany? ")

# Initialize a variable to keep track of the number of guesses
numberOfGuesses = 1

# Start a while loop that continues until the user's guess is "Berlin"
while capitalGuess != "Berlin":
    # Increment the number of guesses by 1
    numberOfGuesses = numberOfGuesses + 1
    
    # Ask the user to guess again and store their new guess
    capitalGuess = input("Guess again.")

# When the user's guess is "Berlin," exit the loop

# Print a message to let the user know they guessed correctly and how many guesses it took
print("You guessed it. Berlin is the capital of Germany. It took you " + str(numberOfGuesses) + " guesses.")



############## Exersice ##################
"""
 You are developing a Python application for an online product distribution company.
You need the program to iterate through a list of products and escape when a target product ID is found. 
you can create a numberic lists from 0 to 9 and target product is 6
"""





