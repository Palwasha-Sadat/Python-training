# Ask the user to input their guess for the capital of Latvia
capitalGuess = input("What is the capital of Latvia? ")

# Initialize a variable to keep track of the number of guesses
numberOfGuesses = 1

# Start a while loop that continues until the user's guess is "Riga"
while capitalGuess != "Riga":
    numberOfGuesses = numberOfGuesses + 1

    # Check if the number of guesses is greater than 3
    if numberOfGuesses > 3:
        print("You guessed incorrectly three times. Game over.")
        break  # Exit the loop if the user exceeded 3 guesses

    capitalGuess = input("Guess again. ")

# If the user guessed correctly (within 3 tries), display a success message
